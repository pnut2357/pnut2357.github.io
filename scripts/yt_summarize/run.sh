#!/usr/bin/env bash
# Convenience runner for the YouTube -> Jekyll summarizer.
# Used by launchd and for manual runs. Creates/uses a local venv.
#
# Usage:
#   GEMINI_API_KEY=... ./run.sh --channel --commit
#   GEMINI_API_KEY=... ./run.sh --backfill
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Load a local .env if present (so GEMINI_API_KEY can live outside the shell).
if [ -f ".env" ]; then
  set -a
  # shellcheck disable=SC1091
  . ./.env
  set +a
fi

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  ./.venv/bin/pip install --quiet --upgrade pip
  ./.venv/bin/pip install --quiet -r requirements.txt
fi

exec ./.venv/bin/python summarize.py "$@"
