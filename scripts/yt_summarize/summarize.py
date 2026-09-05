#!/usr/bin/env python3
"""YouTube -> Jekyll summarizer.

Fetches videos from a YouTube playlist or channel, pulls their transcripts,
summarizes them with a free OpenAI-compatible LLM (Groq by default), optionally
generates a hero illustration (Pollinations by default), and writes Jekyll posts
into the blog's `_posts` directory.

No provider used here requires a credit card, so the pipeline can never incur a
bill -- free limits simply rate-limit or refuse requests.

Usage:
    # Backfill the playlist defined in config.yml
    python summarize.py --backfill

    # Backfill a specific playlist/video URL
    python summarize.py --backfill "https://www.youtube.com/playlist?list=..."

    # Incremental run over the channel's latest uploads
    python summarize.py --channel

    # Process one or more explicit videos/URLs
    python summarize.py --video https://youtu.be/VIDEO_ID

Common flags:
    --limit N        Cap the number of videos processed this run.
    --dry-run        Do everything except write posts / update state.
    --commit         git add + commit newly created posts.
    --config PATH    Path to config.yml (defaults to alongside this script).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from slugify import slugify

SCRIPT_DIR = Path(__file__).resolve().parent
# Repo root is two levels up: <repo>/scripts/yt_summarize/summarize.py
REPO_ROOT = SCRIPT_DIR.parent.parent

YOUTUBE_VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


# ---------------------------------------------------------------------------
# Config / state helpers
# ---------------------------------------------------------------------------
def load_config(path: Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"processed": {}}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, OSError):
        return {"processed": {}}
    data.setdefault("processed", {})
    return data


def save_state(path: Path, state: dict[str, Any]) -> None:
    tmp = path.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    tmp.replace(path)


# ---------------------------------------------------------------------------
# Video discovery (yt-dlp)
# ---------------------------------------------------------------------------
# Extra yt-dlp options applied to every call: browser cookies (raise YouTube's
# caption rate limit) and a forced player_client (cookies otherwise select the
# broken "tv_downgraded" client -> "The page needs to be reloaded").
_YDL_EXTRA: dict[str, Any] = {}
# Proxy URL applied to both fetchers (routes caption requests through a
# different IP to bypass YouTube's per-IP caption rate limit).
_PROXY: str = ""


def configure_youtube_access(cfg: dict[str, Any]) -> None:
    global _YDL_EXTRA, _PROXY
    opts: dict[str, Any] = {}
    browser = (cfg.get("cookies_from_browser") or "").strip()
    cookie_file = (cfg.get("cookies_file") or "").strip()
    if browser:
        opts["cookiesfrombrowser"] = (browser,)
    if cookie_file:
        opts["cookiefile"] = cookie_file
    clients = (cfg.get("youtube_player_client") or "").strip()
    if clients:
        client_list = [c.strip() for c in clients.split(",") if c.strip()]
        opts["extractor_args"] = {"youtube": {"player_client": client_list}}
    _PROXY = (cfg.get("proxy") or "").strip()
    if _PROXY:
        opts["proxy"] = _PROXY
    _YDL_EXTRA = opts


def _ydl_opts(flat: bool) -> dict[str, Any]:
    opts: dict[str, Any] = {
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,
        "skip_download": True,
        **_YDL_EXTRA,
    }
    if flat:
        opts["extract_flat"] = "in_playlist"
    return opts


def extract_video_id(url_or_id: str) -> str | None:
    """Pull an 11-char YouTube video id out of a URL or raw id."""
    if YOUTUBE_VIDEO_ID_RE.match(url_or_id):
        return url_or_id
    patterns = [
        r"(?:v=|/shorts/|youtu\.be/|/embed/|/v/)([A-Za-z0-9_-]{11})",
    ]
    for pat in patterns:
        m = re.search(pat, url_or_id)
        if m:
            return m.group(1)
    return None


def list_video_ids(source_url: str, limit: int | None = None) -> list[str]:
    """Return video ids for a playlist or channel URL using a flat extraction."""
    import yt_dlp  # imported lazily so --help works without the dep

    ids: list[str] = []
    with yt_dlp.YoutubeDL(_ydl_opts(flat=True)) as ydl:
        info = ydl.extract_info(source_url, download=False)
    if not info:
        return ids

    entries = info.get("entries") or []
    for entry in entries:
        if not entry:
            continue
        # Channel pages can nest tabs (e.g. "Videos") as sub-playlists.
        if entry.get("_type") == "playlist" and entry.get("entries"):
            for sub in entry["entries"]:
                if sub and sub.get("id"):
                    ids.append(sub["id"])
        elif entry.get("id"):
            ids.append(entry["id"])

    # De-dupe while preserving order.
    seen: set[str] = set()
    deduped = [i for i in ids if not (i in seen or seen.add(i))]
    if limit is not None:
        deduped = deduped[:limit]
    return deduped


def get_video_metadata(video_id: str) -> dict[str, Any] | None:
    """Full (non-flat) metadata for a single video."""
    import yt_dlp

    url = f"https://www.youtube.com/watch?v={video_id}"
    with yt_dlp.YoutubeDL(_ydl_opts(flat=False)) as ydl:
        info = ydl.extract_info(url, download=False)
    if not info:
        return None
    return {
        "id": info.get("id", video_id),
        "title": info.get("title") or video_id,
        "channel": info.get("channel") or info.get("uploader") or "",
        "duration": info.get("duration") or 0,
        "view_count": info.get("view_count"),
        "upload_date": info.get("upload_date"),  # YYYYMMDD string
        "webpage_url": info.get("webpage_url", url),
    }


# ---------------------------------------------------------------------------
# Transcript fetching
# ---------------------------------------------------------------------------
def fetch_transcript(video_id: str, languages: list[str]) -> str | None:
    """Return transcript text.

    Primary method is yt-dlp (robust against the IP blocks that frequently hit
    youtube-transcript-api's direct timedtext requests). Falls back to
    youtube-transcript-api if yt-dlp yields nothing.
    """
    text = _fetch_transcript_ytdlp(video_id, languages)
    if text:
        return text
    return _fetch_transcript_api(video_id, languages)


def _fetch_transcript_ytdlp(video_id: str, languages: list[str]) -> str | None:
    """Fetch subtitles/auto-captions via yt-dlp and parse to plain text."""
    import glob
    import tempfile

    import yt_dlp

    langs = list(languages) or ["en"]
    url = f"https://www.youtube.com/watch?v={video_id}"
    with tempfile.TemporaryDirectory() as tmp:
        opts = {
            "quiet": True,
            "no_warnings": True,
            "ignoreerrors": True,
            "skip_download": True,
            "writesubtitles": True,
            "writeautomaticsub": True,
            "subtitleslangs": langs,
            "subtitlesformat": "json3",
            "outtmpl": os.path.join(tmp, "%(id)s.%(ext)s"),
            **_YDL_EXTRA,
        }
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                ydl.download([url])
        except Exception as exc:
            msg = str(exc)
            if "429" in msg or "Too Many Requests" in msg:
                print(
                    "  ! caption download rate-limited (HTTP 429). Let your IP "
                    "cool down and/or set cookies_from_browser in config.yml.",
                    file=sys.stderr,
                )
            else:
                print(f"  ! yt-dlp subtitle fetch failed: {exc}", file=sys.stderr)
            return None

        files = glob.glob(os.path.join(tmp, "*.json3"))
        # Prefer manual subtitle langs in the requested order; else any file.
        def _rank(path: str) -> int:
            name = os.path.basename(path)
            for i, lang in enumerate(langs):
                if f".{lang}." in name:
                    return i
            return len(langs)

        for path in sorted(files, key=_rank):
            text = _parse_json3(path)
            if text:
                return text
    return None


def _parse_json3(path: str) -> str | None:
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return None
    parts: list[str] = []
    for event in data.get("events", []) or []:
        for seg in event.get("segs", []) or []:
            piece = seg.get("utf8", "")
            if piece and piece != "\n":
                parts.append(piece)
    text = " ".join("".join(parts).split())
    return text or None


def _fetch_transcript_api(video_id: str, languages: list[str]) -> str | None:
    """Fallback: youtube-transcript-api (classic <=0.6.x or >=1.0 shapes)."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        return None

    segments = _fetch_segments(YouTubeTranscriptApi, video_id, languages)
    if not segments:
        return None

    parts: list[str] = []
    for seg in segments:
        text = seg.get("text") if isinstance(seg, dict) else getattr(seg, "text", "")
        if text:
            parts.append(text.replace("\n", " ").strip())
    joined = " ".join(p for p in parts if p)
    return joined or None


def _proxies_dict() -> dict[str, str] | None:
    if not _PROXY:
        return None
    return {"http": _PROXY, "https": _PROXY}


def _proxy_config():
    """Build a >=1.0 proxy config object, or None if unavailable/unset."""
    if not _PROXY:
        return None
    try:
        from youtube_transcript_api.proxies import GenericProxyConfig
    except Exception:
        return None
    return GenericProxyConfig(http_url=_PROXY, https_url=_PROXY)


def _fetch_segments(api, video_id: str, languages: list[str]) -> list[Any] | None:
    proxies = _proxies_dict()
    try:
        # Classic classmethod API (<= 0.6.x).
        if hasattr(api, "get_transcript"):
            try:
                if proxies:
                    return api.get_transcript(
                        video_id, languages=languages, proxies=proxies)
                return api.get_transcript(video_id, languages=languages)
            except Exception:
                # Fall back to listing and choosing whatever exists.
                listing = api.list_transcripts(video_id)
                for tr in listing:
                    try:
                        return tr.fetch()
                    except Exception:
                        continue
                return None
        # Instance-based API (>= 1.0).
        proxy_cfg = _proxy_config()
        inst = api(proxy_config=proxy_cfg) if proxy_cfg else api()
        fetched = inst.fetch(video_id, languages=languages)
        # FetchedTranscript is iterable of snippets in >=1.0.
        return list(fetched)
    except Exception as exc:  # TranscriptsDisabled, NoTranscriptFound, etc.
        print(f"  ! transcript unavailable for {video_id}: {exc}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Summarization (OpenAI-compatible; Groq free tier by default)
# ---------------------------------------------------------------------------
THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL | re.IGNORECASE)


def summarize(prompt_template: str, meta: dict[str, Any], transcript: str,
              model_name: str, base_url: str, api_key: str,
              reasoning_effort: str | None = None,
              reasoning_format: str | None = None,
              max_tokens: int | None = None) -> str:
    from openai import OpenAI

    client = OpenAI(base_url=base_url, api_key=api_key)
    prompt = prompt_template.format(
        title=meta["title"],
        channel=meta.get("channel", ""),
        publish_date=format_date(meta.get("upload_date")),
        url=meta.get("webpage_url", ""),
        transcript=transcript,
    )

    # Reasoning models (e.g. Qwen3) accept these Groq-specific params. Sending
    # them is optional; they are merged into the request body via extra_body.
    extra_body: dict[str, Any] = {}
    if reasoning_effort:
        extra_body["reasoning_effort"] = reasoning_effort
    if reasoning_format:
        extra_body["reasoning_format"] = reasoning_format

    resp = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a meticulous senior engineer who writes accurate, "
                    "detailed technical study notes."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
        # Reasoning models spend completion tokens on hidden reasoning; without
        # a generous cap the answer can be truncated to empty (finish=length).
        max_tokens=max_tokens,
        extra_body=extra_body or None,
    )
    choice = resp.choices[0] if resp.choices else None
    text = choice.message.content if choice else None
    if not text:
        finish = getattr(choice, "finish_reason", "?")
        raise RuntimeError(
            f"LLM returned empty content (finish_reason={finish}); "
            "try raising max_tokens or lowering reasoning_effort"
        )
    # Safety net: strip any leaked chain-of-thought from reasoning models.
    return THINK_RE.sub("", text).strip()


# ---------------------------------------------------------------------------
# Hero image generation
# ---------------------------------------------------------------------------
HERO_RE = re.compile(r"<!--\s*HERO\s*(.*?)-->", re.DOTALL | re.IGNORECASE)


def parse_hero(summary_md: str) -> tuple[str, dict[str, Any] | None]:
    """Extract the trailing HERO directive block from the summary.

    Returns (summary_without_block, hero_dict_or_None). hero_dict has keys
    `needed` (bool), `prompt` (str), `alt` (str).
    """
    m = HERO_RE.search(summary_md)
    if not m:
        return summary_md.strip(), None

    cleaned = (summary_md[: m.start()] + summary_md[m.end():]).strip()
    body = m.group(1)

    needed_m = re.search(r"needed\s*:\s*(true|false)", body, re.IGNORECASE)
    alt_m = re.search(r"alt\s*:\s*(.+)", body)
    # prompt: everything after 'prompt:' up to a line starting with 'alt:' or end.
    prompt_m = re.search(
        r"prompt\s*:\s*(.*?)(?:\n\s*alt\s*:|\Z)", body, re.DOTALL | re.IGNORECASE
    )

    hero = {
        "needed": bool(needed_m and needed_m.group(1).lower() == "true"),
        "prompt": (prompt_m.group(1).strip() if prompt_m else ""),
        "alt": (alt_m.group(1).strip() if alt_m else ""),
    }
    return cleaned, hero


def _detect_image_ext(data: bytes) -> str:
    """Return a file extension by sniffing image magic bytes."""
    if data[:3] == b"\xff\xd8\xff":
        return ".jpg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return ".png"
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return ".webp"
    return ".png"


def generate_hero_image(hero: dict[str, Any], out_stem: Path,
                        cfg: dict[str, Any]) -> Path | None:
    """Generate a hero image via the configured provider.

    `out_stem` is the destination path WITHOUT extension; the real extension is
    chosen by sniffing the returned bytes. Returns the saved Path or None.
    """
    provider = (cfg.get("image_provider") or "none").lower()
    prompt = hero.get("prompt", "").strip()
    if not prompt or provider == "none":
        return None

    width = int(cfg.get("image_width", 1280))
    height = int(cfg.get("image_height", 720))

    try:
        if provider == "pollinations":
            data = _image_pollinations(prompt, width, height)
        elif provider == "huggingface":
            data = _image_huggingface(prompt, cfg)
        else:
            print(f"  ! unknown image_provider: {provider}", file=sys.stderr)
            return None
    except Exception as exc:
        print(f"  ! image generation failed: {exc}", file=sys.stderr)
        return None

    if not data:
        return None
    out_path = out_stem.with_name(out_stem.name + _detect_image_ext(data))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(data)
    return out_path


def _image_pollinations(prompt: str, width: int, height: int) -> bytes | None:
    """Free, keyless image generation via pollinations.ai."""
    import requests

    encoded = urllib.parse.quote(prompt, safe="")
    url = (
        f"https://image.pollinations.ai/prompt/{encoded}"
        f"?width={width}&height={height}&nologo=true&model=flux"
    )
    resp = requests.get(url, timeout=120)
    resp.raise_for_status()
    if resp.content and resp.headers.get("content-type", "").startswith("image"):
        return resp.content
    return None


def _image_huggingface(prompt: str, cfg: dict[str, Any]) -> bytes | None:
    """Free-tier image generation via Hugging Face Inference API (needs token)."""
    import requests

    token = os.environ.get(cfg.get("hf_api_key_env", "HF_TOKEN"), "")
    if not token:
        print("  ! HF token not set; skipping image", file=sys.stderr)
        return None
    model = cfg.get("hf_image_model", "black-forest-labs/FLUX.1-schnell")
    resp = requests.post(
        f"https://api-inference.huggingface.co/models/{model}",
        headers={"Authorization": f"Bearer {token}"},
        json={"inputs": prompt},
        timeout=180,
    )
    resp.raise_for_status()
    if resp.content and resp.headers.get("content-type", "").startswith("image"):
        return resp.content
    return None


# ---------------------------------------------------------------------------
# Jekyll rendering
# ---------------------------------------------------------------------------
def format_date(upload_date: str | None) -> str:
    """YYYYMMDD -> YYYY-MM-DD; falls back to today."""
    if upload_date and re.match(r"^\d{8}$", upload_date):
        return f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:8]}"
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def first_paragraph(markdown: str, max_len: int = 200) -> str:
    """Use the TL;DR (or first non-heading paragraph) as the excerpt."""
    lines = markdown.splitlines()
    collecting = False
    buf: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.lower().startswith("## tl;dr"):
            collecting = True
            continue
        if collecting:
            if stripped.startswith("#"):
                break
            if stripped:
                buf.append(stripped)
            elif buf:
                break
    text = " ".join(buf).strip()
    if not text:
        for line in lines:
            s = line.strip()
            if s and not s.startswith("#"):
                text = s
                break
    if len(text) > max_len:
        text = text[: max_len - 1].rstrip() + "\u2026"
    return text


def build_post(meta: dict[str, Any], summary_md: str, transcript: str,
               cfg: dict[str, Any], hero_image_rel: str | None = None,
               hero_alt: str = "") -> str:
    date = format_date(meta.get("upload_date"))
    excerpt = first_paragraph(summary_md)
    front = {
        "title": meta["title"],
        "description": excerpt,
        "categories": list(cfg.get("categories", [])),
        "tags": list(cfg.get("default_tags", [])),
        "toc": True,
        "toc_sticky": True,
        "comments": True,
        "excerpt": excerpt,
        "source_url": meta.get("webpage_url", ""),
        "youtube_channel": meta.get("channel", ""),
        "video_published": date,
    }
    if hero_image_rel:
        header = {"image": hero_image_rel, "teaser": hero_image_rel}
        if hero_alt:
            header["caption"] = hero_alt
        front["header"] = header
    front_yaml = yaml.safe_dump(
        front, sort_keys=False, allow_unicode=True, default_flow_style=False
    ).strip()

    views = meta.get("view_count")
    views_str = f"{views:,}" if isinstance(views, int) else "N/A"

    parts = [
        "---",
        front_yaml,
        "---",
        "",
        f"> Summary of [{meta['title']}]({meta.get('webpage_url', '')})",
        f"> from **{meta.get('channel', 'YouTube')}** "
        f"\u00b7 Published {date} \u00b7 Views: {views_str}",
        "",
        "*This note was generated automatically from the video transcript.*",
        "",
        summary_md.strip(),
        "",
    ]

    if cfg.get("include_transcript") and transcript:
        parts += [
            "## Full Transcript",
            "",
            "<details>",
            "<summary>Click to expand the raw transcript</summary>",
            "",
            transcript.strip(),
            "",
            "</details>",
            "",
        ]
    return "\n".join(parts)


def _slug_for(meta: dict[str, Any]) -> str:
    return slugify(meta["title"], max_length=60, word_boundary=True) or meta["id"]


def post_path(meta: dict[str, Any], cfg: dict[str, Any]) -> Path:
    date = format_date(meta.get("upload_date"))
    prefix = cfg.get("filename_prefix", "bbg")
    out_dir = REPO_ROOT / cfg.get("output_dir", "_posts")
    return out_dir / f"{date}-{prefix}-{_slug_for(meta)}.md"


def image_paths(meta: dict[str, Any], cfg: dict[str, Any]) -> tuple[Path, str]:
    """Return (absolute stem path, site-root-relative stem URL), no extension.

    The concrete file extension is decided when the image bytes are known.
    """
    date = format_date(meta.get("upload_date"))
    prefix = cfg.get("filename_prefix", "bbg")
    rel_dir = cfg.get("image_dir", "assets/images/bbg").strip("/")
    stem = f"{date}-{prefix}-{_slug_for(meta)}"
    abs_stem = REPO_ROOT / rel_dir / stem
    site_url_stem = f"/{rel_dir}/{stem}"
    return abs_stem, site_url_stem


# ---------------------------------------------------------------------------
# git
# ---------------------------------------------------------------------------
def git_commit(paths: list[Path], assets: list[Path], state_path: Path) -> None:
    if not paths:
        return
    rel = [str(p.relative_to(REPO_ROOT)) for p in (*paths, *assets)]
    rel.append(str(state_path.relative_to(REPO_ROOT)))
    try:
        subprocess.run(["git", "-C", str(REPO_ROOT), "add", *rel], check=True)
        msg = f"Add {len(paths)} auto-generated YouTube summary post(s)"
        subprocess.run(
            ["git", "-C", str(REPO_ROOT), "commit", "-m", msg], check=True
        )
        print(f"Committed {len(paths)} post(s).")
    except subprocess.CalledProcessError as exc:
        print(f"git commit failed: {exc}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def resolve_sources(args: argparse.Namespace, cfg: dict[str, Any]) -> list[str]:
    """Return a list of video ids to consider based on CLI args."""
    ids: list[str] = []
    if args.video:
        for v in args.video:
            vid = extract_video_id(v)
            if vid:
                ids.append(vid)
            else:
                print(f"Could not parse video id from: {v}", file=sys.stderr)
        return ids

    if args.channel:
        handle = cfg.get("channel_handle", "").lstrip("@")
        url = f"https://www.youtube.com/@{handle}/videos"
        print(f"Listing uploads from {url} ...")
        return list_video_ids(url, limit=None)

    # Default: backfill
    playlist = (
        args.backfill
        if isinstance(args.backfill, str)
        else cfg.get("backfill_playlist_url")
    )
    if not playlist:
        print("No backfill playlist configured.", file=sys.stderr)
        return ids
    print(f"Listing videos from {playlist} ...")
    return list_video_ids(playlist, limit=None)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="YouTube -> Jekyll summarizer")
    parser.add_argument(
        "--backfill", nargs="?", const=True, default=None,
        help="Backfill a playlist (defaults to config playlist if no URL given)",
    )
    parser.add_argument(
        "--channel", action="store_true",
        help="Incremental run over the channel's latest uploads",
    )
    parser.add_argument(
        "--video", action="append",
        help="Explicit video URL or id (repeatable)",
    )
    parser.add_argument("--limit", type=int, default=None,
                        help="Max videos to process this run")
    parser.add_argument("--dry-run", action="store_true",
                        help="Do not write posts or update state")
    parser.add_argument("--commit", action="store_true",
                        help="git add + commit new posts")
    parser.add_argument("--no-proxy", action="store_true",
                        help="Ignore config 'proxy' for this run (e.g. when on a "
                             "phone hotspot with a clean IP)")
    parser.add_argument("--proxy", default=None,
                        help="Override config 'proxy' for this run "
                             "(e.g. socks5h://127.0.0.1:9050)")
    parser.add_argument("--config", default=str(SCRIPT_DIR / "config.yml"))
    args = parser.parse_args(argv)

    if not (args.backfill or args.channel or args.video):
        # Default action is a config-driven backfill.
        args.backfill = True

    cfg = load_config(Path(args.config))
    # CLI proxy overrides (do not persist to config.yml).
    if args.no_proxy:
        cfg["proxy"] = ""
    elif args.proxy is not None:
        cfg["proxy"] = args.proxy
    configure_youtube_access(cfg)
    state_path = SCRIPT_DIR / "state.json"
    state = load_state(state_path)
    processed: dict[str, Any] = state["processed"]

    # API key (text provider). Groq's free key needs no credit card.
    text_key_env = cfg.get("text_api_key_env", "GROQ_API_KEY")
    api_key = os.environ.get(text_key_env, "")
    if not api_key and not args.dry_run:
        print(
            f"ERROR: LLM API key not found. Set the {text_key_env} environment "
            "variable (free, no credit card, at https://console.groq.com/keys).",
            file=sys.stderr,
        )
        return 2

    prompt_template = (SCRIPT_DIR / "prompt.md").read_text(encoding="utf-8")
    languages = cfg.get("transcript_languages", ["en"])
    min_duration = int(cfg.get("min_duration_seconds", 0))
    run_cap = args.limit or int(cfg.get("max_videos_per_run", 25))

    candidate_ids = resolve_sources(args, cfg)
    new_ids = [v for v in candidate_ids if v not in processed]
    print(
        f"Found {len(candidate_ids)} video(s); "
        f"{len(new_ids)} new after filtering processed."
    )

    text_model = cfg.get("text_model", "openai/gpt-oss-120b")
    text_base_url = cfg.get("text_base_url", "https://api.groq.com/openai/v1")
    reasoning_effort = cfg.get("reasoning_effort") or None
    reasoning_format = cfg.get("reasoning_format") or None
    max_tokens = cfg.get("max_tokens") or None
    generate_images = bool(cfg.get("generate_images", False))
    delay = float(cfg.get("request_delay_seconds", 0) or 0)

    # Safety limits so a bad key/model or a YouTube IP block can't walk the
    # whole channel and hammer external services.
    max_attempts = int(cfg.get("max_attempts_per_run", max(run_cap * 5, 25)))
    fail_limit = int(cfg.get("consecutive_failure_limit", 5))

    written: list[Path] = []
    assets: list[Path] = []
    count = 0
    attempts = 0
    consecutive_failures = 0
    for vid in new_ids:
        if count >= run_cap:
            print(f"Reached run cap ({run_cap} posts); stopping.")
            break
        if attempts >= max_attempts:
            print(f"Reached attempt cap ({max_attempts}); stopping.")
            break
        if consecutive_failures >= fail_limit:
            print(
                f"Aborting after {consecutive_failures} consecutive failures "
                "(likely a YouTube IP block, or a bad model/API key)."
            )
            break

        # Throttle every iteration to be gentle on YouTube (avoids IP blocks).
        if delay and attempts > 0:
            time.sleep(delay)

        attempts += 1
        print(f"\n[post {count + 1} / attempt {attempts}] {vid} ...")
        meta = get_video_metadata(vid)
        if not meta:
            print("  ! could not fetch metadata; will retry next run")
            consecutive_failures += 1
            continue

        duration = meta.get("duration")
        if not duration:
            # Unknown/zero duration usually means a transient fetch failure or
            # IP block -- do NOT mark processed, so it can be retried later.
            print("  ! unknown duration; skipping without marking (will retry)")
            consecutive_failures += 1
            continue

        if min_duration and duration < min_duration:
            print(
                f"  - genuinely short ({duration}s < {min_duration}s); "
                "marking processed"
            )
            processed[vid] = {
                "title": meta["title"],
                "skipped": "too_short",
                "processed_at": datetime.now(timezone.utc).isoformat(),
            }
            consecutive_failures = 0  # valid determination, not a failure
            continue

        transcript = fetch_transcript(vid, languages)
        if not transcript:
            print("  ! no transcript; will retry next run")
            consecutive_failures += 1
            continue

        print(f"  - transcript: {len(transcript)} chars; summarizing ...")
        if args.dry_run:
            print(f"  - [dry-run] would write {post_path(meta, cfg).name}")
            consecutive_failures = 0
            count += 1
            continue

        try:
            raw_summary = summarize(
                prompt_template, meta, transcript,
                text_model, text_base_url, api_key,
                reasoning_effort, reasoning_format, max_tokens,
            )
        except Exception as exc:
            print(f"  ! summarization failed: {exc}", file=sys.stderr)
            consecutive_failures += 1
            continue

        summary_md, hero = parse_hero(raw_summary)

        hero_url: str | None = None
        hero_alt = ""
        if generate_images and hero and hero.get("needed"):
            img_stem, url_stem = image_paths(meta, cfg)
            print(f"  - generating hero image via {cfg.get('image_provider')} ...")
            saved = generate_hero_image(hero, img_stem, cfg)
            if saved:
                hero_url = url_stem + saved.suffix
                hero_alt = hero.get("alt", "")
                assets.append(saved)
                print(f"  + wrote {saved.relative_to(REPO_ROOT)}")

        out = post_path(meta, cfg)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            build_post(meta, summary_md, transcript, cfg, hero_url, hero_alt),
            encoding="utf-8",
        )
        print(f"  + wrote {out.relative_to(REPO_ROOT)}")
        written.append(out)

        processed[vid] = {
            "title": meta["title"],
            "date": format_date(meta.get("upload_date")),
            "post_path": str(out.relative_to(REPO_ROOT)),
            "processed_at": datetime.now(timezone.utc).isoformat(),
        }
        save_state(state_path, state)
        count += 1
        consecutive_failures = 0

    if not args.dry_run:
        save_state(state_path, state)

    print(f"\nDone. Wrote {len(written)} new post(s), {len(assets)} image(s).")
    if args.commit and written and not args.dry_run:
        git_commit(written, assets, state_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
