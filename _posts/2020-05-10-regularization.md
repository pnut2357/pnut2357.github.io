---
title: Regularization
description: Regularization
categories:
  - machine-learning-project
tags:
toc: true
toc_sticky: true
comments: true
excerpt: |
  sdsd/sdsd
# header:
#   image: /assets/images/logos/logo-text-8c3ba8a6.svg
---

<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>regularization</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  }
  div.output_wrapper {
    display: block;
    page-break-inside: avoid;
  }
  div.output {
    display: block;
    page-break-inside: avoid;
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># code for loading the format for the notebook</span>
<span class="kn">import</span> <span class="nn">os</span>

<span class="c1"># path : store the current path to convert back to it later</span>
<span class="n">path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">()</span>
<span class="n">os</span><span class="o">.</span><span class="n">chdir</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s1">&#39;..&#39;</span><span class="p">,</span> <span class="s1">&#39;notebook_format&#39;</span><span class="p">))</span>
<span class="kn">from</span> <span class="nn">formats</span> <span class="kn">import</span> <span class="n">load_style</span>
<span class="n">load_style</span><span class="p">(</span><span class="n">plot_style</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[20]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<style>
@import url('http://fonts.googleapis.com/css?family=Source+Code+Pro');
@import url('http://fonts.googleapis.com/css?family=Vollkorn');
@import url('http://fonts.googleapis.com/css?family=Arimo');
@import url('http://fonts.googleapis.com/css?family=Fira_sans');

    div.cell {
        width: 1000px;
        margin-left: 0% !important;
        margin-right: auto;
    }
    div.text_cell code {
        background: transparent;
        color: #000000;
        font-weight: 600;
        font-size: 12pt;
        font-style: bold;
        font-family:  'Source Code Pro', Consolas, monocco, monospace;
    }
    h1 {
        font-family: 'Open sans',verdana,arial,sans-serif;
	}

    div.input_area {
        background: #F6F6F9;
        border: 1px solid #586e75;
    }

    .text_cell_render h1 {
        font-weight: 200;
        font-size: 30pt;
        line-height: 100%;
        color:#c76c0c;
        margin-bottom: 0.5em;
        margin-top: 1em;
        display: block;
        white-space: wrap;
        text-align: left;
    }
    h2 {
        font-family: 'Open sans',verdana,arial,sans-serif;
        text-align: left;
    }
    .text_cell_render h2 {
        font-weight: 200;
        font-size: 16pt;
        font-style: italic;
        line-height: 100%;
        color:#c76c0c;
        margin-bottom: 0.5em;
        margin-top: 1.5em;
        display: block;
        white-space: wrap;
        text-align: left;
    }
    h3 {
        font-family: 'Open sans',verdana,arial,sans-serif;
    }
    .text_cell_render h3 {
        font-weight: 200;
        font-size: 14pt;
        line-height: 100%;
        color:#d77c0c;
        margin-bottom: 0.5em;
        margin-top: 2em;
        display: block;
        white-space: wrap;
        text-align: left;
    }
    h4 {
        font-family: 'Open sans',verdana,arial,sans-serif;
    }
    .text_cell_render h4 {
        font-weight: 100;
        font-size: 14pt;
        color:#d77c0c;
        margin-bottom: 0.5em;
        margin-top: 0.5em;
        display: block;
        white-space: nowrap;
    }
    h5 {
        font-family: 'Open sans',verdana,arial,sans-serif;
    }
    .text_cell_render h5 {
        font-weight: 200;
        font-style: normal;
        color: #1d3b84;
        font-size: 16pt;
        margin-bottom: 0em;
        margin-top: 0.5em;
        display: block;
        white-space: nowrap;
    }
    div.text_cell_render{
        font-family: 'Fira sans', verdana,arial,sans-serif;
        line-height: 125%;
        font-size: 115%;
        text-align:justify;
        text-justify:inter-word;
    }
    div.output_wrapper{
        margin-top:0.2em;
        margin-bottom:0.2em;
    }

    code{
      font-size: 70%;
    }
    .rendered_html code{
    background-color: transparent;
    }
    ul{
        margin: 2em;
    }
    ul li{
        padding-left: 0.5em;
        margin-bottom: 0.5em;
        margin-top: 0.5em;
    }
    ul li li{
        padding-left: 0.2em;
        margin-bottom: 0.2em;
        margin-top: 0.2em;
    }
    ol{
        margin: 2em;
    }
    ol li{
        padding-left: 0.5em;
        margin-bottom: 0.5em;
        margin-top: 0.5em;
    }
    ul li{
        padding-left: 0.5em;
        margin-bottom: 0.5em;
        margin-top: 0.2em;
    }
    a:link{
       font-weight: bold;
       color:#447adb;
    }
    a:visited{
       font-weight: bold;
       color: #1d3b84;
    }
    a:hover{
       font-weight: bold;
       color: #1d3b84;
    }
    a:focus{
       font-weight: bold;
       color:#447adb;
    }
    a:active{
       font-weight: bold;
       color:#447adb;
    }
    .rendered_html :link {
       text-decoration: underline;
    }
    .rendered_html :hover {
       text-decoration: none;
    }
    .rendered_html :visited {
      text-decoration: none;
    }
    .rendered_html :focus {
      text-decoration: none;
    }
    .rendered_html :active {
      text-decoration: none;
    }
    .warning{
        color: rgb( 240, 20, 20 )
    }
    hr {
      color: #f3f3f3;
      background-color: #f3f3f3;
      height: 1px;
    }
    blockquote{
      display:block;
      background: #fcfcfc;
      border-left: 5px solid #c76c0c;
      font-family: 'Open sans',verdana,arial,sans-serif;
      width:680px;
      padding: 10px 10px 10px 10px;
      text-align:justify;
      text-justify:inter-word;
      }
      blockquote p {
        margin-bottom: 0;
        line-height: 125%;
        font-size: 100%;
      }
</style>
<script>
    MathJax.Hub.Config({
                        TeX: {
                           extensions: ["AMSmath.js"]
                           },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
                },
                displayAlign: 'center', // Change this to 'center' to center equations.
                "HTML-CSS": {
                    scale:100,
                        availableFonts: [],
                        preferredFont:null,
                        webFont: "TeX",
                    styles: {'.MathJax_Display': {"margin": 4}}
                }
        });
</script>

</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">os</span><span class="o">.</span><span class="n">chdir</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>

<span class="c1"># 1. magic for inline plot</span>
<span class="c1"># 2. magic to print version</span>
<span class="c1"># 3. magic so that the notebook will reload external python modules</span>
<span class="c1"># 4. magic to enable retina (high resolution) plots</span>
<span class="c1"># https://gist.github.com/minrk/3301035</span>
<span class="o">%</span><span class="k">matplotlib</span> inline
<span class="o">%</span><span class="k">load_ext</span> watermark
<span class="o">%</span><span class="k">load_ext</span> autoreload
<span class="o">%</span><span class="k">autoreload</span> 2
<span class="o">%</span><span class="k">config</span> InlineBackend.figure_format = &#39;retina&#39;

<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">from</span> <span class="nn">sklearn.datasets</span> <span class="kn">import</span> <span class="n">load_boston</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">Ridge</span><span class="p">,</span> <span class="n">RidgeCV</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">Lasso</span><span class="p">,</span> <span class="n">LassoCV</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LinearRegression</span>
<span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">StandardScaler</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>

<span class="o">%</span><span class="k">watermark</span> -a &#39;Jae H. Choi&#39; -d -t -v -p numpy,pandas,matplotlib,sklearn
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>The watermark extension is already loaded. To reload it, use:
  %reload_ext watermark
The autoreload extension is already loaded. To reload it, use:
  %reload_ext autoreload
Jae H. Choi 2020-07-30 22:04:44

CPython 3.8.3
IPython 7.16.1

numpy 1.18.5
pandas 1.0.5
matplotlib 3.2.2
sklearn 0.23.1
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Regularization">Regularization<a class="anchor-link" href="#Regularization">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Before discussing about regularization, we'll do a quick recap on the notion of <strong>overfitting</strong> and the <strong>bias-variance tradeoff</strong>.</p>
<p><strong>Overfitting:</strong> So what is overfitting? Well, to put it in more simple terms it's when we built a model that is too complex that it matches the training data "too closely" or we can say that the model has started to learn not only the signal, but also the noise in the data. The result of this is that our model will do well on the training data, but won't generalize to out-of-sample data, data that we have not seen before.</p>
<p><strong>Bias-Variance tradeoff:</strong> When we discuss prediction models, prediction errors can be decomposed into two main subcomponents we care about: error due to "bias" and error due to "variance". Understanding these two types of error can help us diagnose model results and avoid the mistake of over/under fitting. A typical graph of discussing this is shown below:</p>
<p><img src="images/bias_variance.png" alt="Bias-variance tradeoff"></p>
<ul>
<li><strong>Bias:</strong> The red line, measures how far off in general our models' predictions are from the correct value. Thus as our model gets more and more complex we will become more and more accurate about our predictions (Error steadily decreases).</li>
<li><strong>Variance:</strong> The cyan line, measures how different can our model be from one to another, as we're looking at different possible data sets. If the estimated model will vary dramatically from one data set to the other, then we will have very erratic predictions, because our prediction will be extremely sensitive to what data set we obtain. As the complexity of our model rises, variance becomes our primary concern.</li>
</ul>
<p>When creating a model, our goal is to locate the optimum model complexity. If our model complexity exceeds this sweet spot, we are in effect overfitting our model; while if our complexity falls short of the sweet spot, we are underfitting the model. With all of that in mind, the notion of <strong>regularization</strong> is simply a useful technique to use when we think our model is too complex (models that have low bias, but high variance). It is a method for "constraining" or "regularizing" the <strong>size of the coefficients</strong> ("shrinking" them towards zero). The specific regularization techniques we'll be discussing are <strong>Ridge Regression</strong> and <strong>Lasso Regression</strong>.</p>
<p>For those interested, the following link contains a nice infogprahics on Bias-Variance Tradeoff. <a href="https://elitedatascience.com/bias-variance-tradeoff">Blog: Bias-Variance Tradeoff Infographic</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Ridge-and-Lasso-Regression">Ridge and Lasso Regression<a class="anchor-link" href="#Ridge-and-Lasso-Regression">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Recall that for a normal linear regression model of:</p>
$$Y = \beta_0 + \beta_1X_1 + ... + \beta_pX_p$$<p>We would estimate its coefficients using the least squares criterion, which minimizes the residual sum of squares (RSS). Or graphically, we're fitting the blue line to our data (the black points) that minimizes the sum of the distances between the points and the blue line (sum of the red lines) as shown below.</p>
<p><img src="images/estimating_coefficients.png" alt="Estimating coefficients"></p>
<p>Mathematically, this can be denoted as:</p>
$$RSS = \sum_{i=1}^n \left( y_i - ( \beta_0 + \sum_{j=1}^p \beta_jx_{ij} ) \right)^2$$<p>Where:</p>
<ul>
<li>$n$ is the <strong>total number of observations (data)</strong>.</li>
<li>$y_i$ is the <strong>actual output value of the observation (data)</strong>.</li>
<li>$p$ is the <strong>total number of features</strong>.</li>
<li>$\beta_j$ is a <strong>model's coefficient</strong>.</li>
<li>$x_{ij}$ is the <strong>$i_{th}$ observation, $j_{th}$ feature's value</strong>.</li>
<li>$\beta_0 + \sum_{j=1}^p \beta_jx_{ij}$ is the <strong>predicted output of each observation</strong>.</li>
</ul>
<p>Regularized linear regression models are very similar to least squares, except that the coefficients are estimated by minimizing a slightly different objective function. we <strong>minimize the sum of RSS and a "penalty term"</strong> that penalizes coefficient size.</p>
<p><strong>Ridge regression</strong> (or "L2 regularization") minimizes:</p>
$$\text{RSS} + \alpha \sum_{j=1}^p \beta_j^2$$<p><strong>Lasso regression</strong> (or "L1 regularization") minimizes:</p>
$$\text{RSS} + \alpha \sum_{j=1}^p \lvert \beta_j \rvert$$<p>Where $\alpha$ is a <strong>tuning parameter</strong> that seeks to balance between the fit of the model to the data and the magnitude of the model's coefficients:</p>
<ul>
<li>A tiny $\alpha$ imposes no penalty on the coefficient size, and is equivalent to a normal linear regression.</li>
<li>Increasing $\alpha$ penalizes the coefficients and thus shrinks them towards zero.</li>
</ul>
<p>Thus you can think of it as, we're balancing two things to measure the model's total quality. The RSS, measures how well the model is going to fit the data, and then the magnitude of the coefficients, which can be problematic if they become too big.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Let's look at some examples. In the following section, we'll load the <a href="http://facweb.cs.depaul.edu/mobasher/classes/CSC478/Data/housing-dscr.txt">Boston Housing Dataset</a>, which contains some dataset about the housing values in suburbs of Boston. We'll choose the first few features, train a ridge and lasso regression separately at look at the estimated coefficients' weight for different $\alpha$ parameter.</p>
<p>Note that we're choosing the first few features because we'll later use a plot to show the affect of the $\alpha$ parameter on the estimated coefficients' weight and too many features will make the plot pretty unappealing. The model's interpreability or performance is not the main focus here.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># extract input and response variables (housing prices), </span>
<span class="c1"># meaning of each variable is in the link above</span>
<span class="n">feature_num</span> <span class="o">=</span> <span class="mi">7</span>
<span class="n">boston</span> <span class="o">=</span> <span class="n">load_boston</span><span class="p">()</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">boston</span><span class="o">.</span><span class="n">data</span><span class="p">[:,</span> <span class="p">:</span><span class="n">feature_num</span><span class="p">]</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">boston</span><span class="o">.</span><span class="n">target</span>
<span class="n">features</span> <span class="o">=</span> <span class="n">boston</span><span class="o">.</span><span class="n">feature_names</span><span class="p">[:</span><span class="n">feature_num</span><span class="p">]</span>
<span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">columns</span> <span class="o">=</span> <span class="n">features</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt">Out[22]:</div>



<div class="output_html rendered_html output_subarea output_execute_result">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>CRIM</th>
      <th>ZN</th>
      <th>INDUS</th>
      <th>CHAS</th>
      <th>NOX</th>
      <th>RM</th>
      <th>AGE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00632</td>
      <td>18.0</td>
      <td>2.31</td>
      <td>0.0</td>
      <td>0.538</td>
      <td>6.575</td>
      <td>65.2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.02731</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>6.421</td>
      <td>78.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02729</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0.0</td>
      <td>0.469</td>
      <td>7.185</td>
      <td>61.1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03237</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>6.998</td>
      <td>45.8</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.06905</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0.0</td>
      <td>0.458</td>
      <td>7.147</td>
      <td>54.2</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># split into training and testing sets and standardize them</span>
<span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">random_state</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
<span class="n">std</span> <span class="o">=</span> <span class="n">StandardScaler</span><span class="p">()</span>
<span class="n">X_train_std</span> <span class="o">=</span> <span class="n">std</span><span class="o">.</span><span class="n">fit_transform</span><span class="p">(</span><span class="n">X_train</span><span class="p">)</span>
<span class="n">X_test_std</span> <span class="o">=</span> <span class="n">std</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># loop through different penalty score (alpha) and obtain the estimated coefficient (weights)</span>
<span class="n">alphas</span> <span class="o">=</span> <span class="mi">10</span> <span class="o">**</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;different alpha values:&#39;</span><span class="p">,</span> <span class="n">alphas</span><span class="p">)</span>

<span class="c1"># stores the weights of each feature</span>
<span class="n">ridge_weight</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">alpha</span> <span class="ow">in</span> <span class="n">alphas</span><span class="p">:</span>    
    <span class="n">ridge</span> <span class="o">=</span> <span class="n">Ridge</span><span class="p">(</span><span class="n">alpha</span> <span class="o">=</span> <span class="n">alpha</span><span class="p">,</span> <span class="n">fit_intercept</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
    <span class="n">ridge</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_std</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
    <span class="n">ridge_weight</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ridge</span><span class="o">.</span><span class="n">coef_</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>different alpha values: [   10   100  1000 10000]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">weight_versus_alpha_plot</span><span class="p">(</span><span class="n">weight</span><span class="p">,</span> <span class="n">alphas</span><span class="p">,</span> <span class="n">features</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;</span>
<span class="sd">    Pass in the estimated weight, the alpha value and the names</span>
<span class="sd">    for the features and plot the model&#39;s estimated coefficient weight </span>
<span class="sd">    for different alpha values</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">fig</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">8</span><span class="p">,</span> <span class="mi">6</span><span class="p">))</span>

    <span class="c1"># ensure that the weight is an array</span>
    <span class="n">weight</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">weight</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">weight</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]):</span>
        <span class="n">plt</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">alphas</span><span class="p">,</span> <span class="n">weight</span><span class="p">[:,</span> <span class="n">col</span><span class="p">],</span> <span class="n">label</span> <span class="o">=</span> <span class="n">features</span><span class="p">[</span><span class="n">col</span><span class="p">])</span>

    <span class="n">plt</span><span class="o">.</span><span class="n">axhline</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;black&#39;</span><span class="p">,</span> <span class="n">linestyle</span> <span class="o">=</span> <span class="s1">&#39;--&#39;</span><span class="p">,</span> <span class="n">linewidth</span> <span class="o">=</span> <span class="mi">3</span><span class="p">)</span>

    <span class="c1"># manually specify the coordinate of the legend</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">legend</span><span class="p">(</span><span class="n">bbox_to_anchor</span> <span class="o">=</span> <span class="p">(</span><span class="mf">1.3</span><span class="p">,</span> <span class="mf">0.9</span><span class="p">))</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Coefficient Weight as Alpha Grows&#39;</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">ylabel</span><span class="p">(</span><span class="s1">&#39;Coefficient weight&#39;</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">xlabel</span><span class="p">(</span><span class="s1">&#39;alpha&#39;</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">fig</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># change default figure and font size</span>
<span class="n">plt</span><span class="o">.</span><span class="n">rcParams</span><span class="p">[</span><span class="s1">&#39;figure.figsize&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">6</span>
<span class="n">plt</span><span class="o">.</span><span class="n">rcParams</span><span class="p">[</span><span class="s1">&#39;font.size&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">12</span>


<span class="n">ridge_fig</span> <span class="o">=</span> <span class="n">weight_versus_alpha_plot</span><span class="p">(</span><span class="n">ridge_weight</span><span class="p">,</span> <span class="n">alphas</span><span class="p">,</span> <span class="n">features</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABOoAAAMRCAYAAABS8FmLAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAWJQAAFiUBSVIk8AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdeXxU9b3/8fcnCdnIAoQdQfZFRAWKuF3xWq12vVZsxa3FrddKe13aut4qaq1LvdpqpdalrnX353K117pSd1FARFBQBFQCGBASAgmQ5Pv743uGnISZyUwyyQzx9Xw8ziPnzPme7/nmnDMT5sPn+/2ac04AAAAAAAAA0isr3Q0AAAAAAAAAQKAOAAAAAAAAyAgE6gAAAAAAAIAMQKAOAAAAAAAAyAAE6gAAAAAAAIAMQKAOAAAAAAAAyAAE6gAAAAAAAIAMQKAOAAAAAAAAyAAE6gAAAAAAAIAMQKAOAAAAAAAAyAAE6gAAAAAAAIAMQKAOAAAAAAAAyAAE6gAAAAAAAIAMQKAOANLIzA43s/81s7VmVmdmLlgGNys3ycweMrMvzGxbqNwhwf6ZsY5NUTvbtX6knpkNDt2zme18rtnBeVa053mQmA6+9yuC88xuz/MAAAB8XRCoA7DLMLPJZvZ7M3vDzD43sxoz2xysP2tmvzWz4eluZ6LM7DRJz0n6nqTekrJjlDtS0huSfixpgKQuHdVGSGb2i1DQ41ctlM01sy2tLP95aluOXZ2Z3Rx6ljabWUm629QZmVmWmX3XzG40s7lmVm5mW4Nr/oWZvWRmfzCzKWbGv50BAEC74h8bADKemY0xs+ckvSXpQkn7S9pNUr6kwmD9CEmXS/rYzJ42szHpam8izKxA0rXB5hpJ0yV9Q9K4YFkVKn6DpBxJ1ZJ+IWlyqNw7HdPiXYuZTW+eddgGs0PrLdW1r6SCVpafHafc10KK79suzczyJR0XeqlQ0rQ0NafTMrPvSloo6WlJv5Q0QVI/Sbny13yApH+X9Gv59+hKM/ulmUX9jxUAAIC2ykl3AwAgHjP7jqQHJEUySVZKeljS6/IBLif/peoASUdJGinpu5I+kXR2R7c3CZMkdQ/Wr3TO3R2tkJkNkjQ62Pyrc+7maOWcczMlzUxxGzus/gy3SFKFpF6S/s3MspxzDTHKTgl+1stnSCZaXkpxoM45t0KSpbJOdKgfqvEzolpSkaSTJd2athZ1MkG34EvU+D6ZJ+kp+f8AWRe81kvSPpIOk3+/7ibpRkmPyP8NAgAASCky6gBkLDObIOkx+SCdk/9CNdI5d55z7knn3NvOuTnB+vnyAa1pkj5LX6sTNiC0viQF5dBOnHNO0ivBZqn8l/ZYDgl+PiT/zCZaXiKjDk2dHPz8QtKVwfp+mZ4tvKsws7MkXSofpNso6YfOuYnOucucc/8I/rbMcc4945y70jn375LGyv/HEQAAQLshUAcgI5lZF/mMhfzgpV86565wzm2LdYzzHpLvuvRyBzSzLfJC69tTUA7ta3ZofUq0AsEzu3+w+ZikD5Mo/4Vzblnbm4nOIMik/Wawea+ke+SzNKXGAB5ayczGSrou2KyRNMU590RLxznnPnTOHS+f7Vjbjk0EAABfYwTqAGSqkyQNDdZfiNXlMxrn3Hrn3JOx9pvZ/mb2NzP7JBgsvNrMPjaz281sUqLnMbMDzOw2M1tiZlXB5BbLzezvscbXisyQKOnO0Msvh8blcsEMq7ODcuGA453Nyt0VqjfhWVnNbA8zu8HM5pvZ+mDQ9JVm9pqZXWpme0Y5Jpn6xwaDsi80sw1B/V+Y2WNmdpSZxeyOac1mDzWzIjO7MGhrVXCvFpifOKQoyvGHJHB9m1y7BIXvwyExykyS1DVYf1WNWXiJlI8aWA4mmzjdzJ4xs1XBtdxgZvPM7Coz6xerwZbEzJ9m9gMz+4eZfWlmtcFzfFsQ0JCZ3RWpK149ofoy5b7JzLLNz658XfCMf2l+5uRNwXv3TjPbP4F6cszsVPMT10QmG9gUXKs3zex/zE/8kgrT1fhvtLudc+WSng+2TzKzNg1dEu3ZMLODzewR85Pz1AbP2wNmtm+Sdfc2P+nPYvOfr1Vm9raZ/Zf54HS8Y0eY2a/N7EkzW2Z+opWtwfX+PzP7mZnlxasjQRercfiXS51z7ydzsHPuCefcxijt32mMRTM7PvTM1JnZe1GO28P8xCEfWuPfkhXm/5YcFqsdZvZucK53Y+zPD+5lpE3fi1Hu8mB/g5n1bLbPzOxHZva4mX0W1LfF/N+Md4J2/7CtzyQAAAhxzrGwsLBk3CI/y6kLliNSVGe2pFtC9UZbGiT9UVJWnHoKJN3XQj1O0t2S8poduyKB42bKZ3C1VO6uUL0zQ68PjtHuHEl/ks/MiVfvxijHJlJ/lnyWSkv1PyupNEYdkd97haRhkpbGqWeBpO7Njj8kgevW5Nol8fx8GRz7VbTnQ36iEydpUbB9XILlnaRTouzfR9KyFn6PaklTY7R3cPiZivOeuCtO/TWSjg+X2QXv2x8TrPtGSRajjl6S5iZQR10KPqcsdN/fDL0+LXSe77dQR9x733y/pIvkP/ui/U71ks6Lc64VQbnZ8pOjrI5zfV6QlBujnn0SvE8LFeMzKMHrWyyfnRx5/5S09Z6F6p4eaucR8hNUNG//e82OuURSXQu/88OS8qOc79rQPeoeZf9hzeq5IUa7Xwv2L2j2eoH853Ui92W3VF1HFhYWFhaWr/vC/34ByDhBxk0ks22LpBdTVPUsST8L1lfLf8l5O9g+QNJ5knpLOkv+y/JZUdqWLel/1dgt7VX5gNynkqrkJ7P4mXzg4SfyX37DXdW+JT+b4H9I+l3w2ilqOnvrl0GdXeWvw9+C1/9bUjhTcEMCv3PY/ZJ+FKxXSPpL0P718uMA7iXpO/JftlvjDvkvqpIPxtwq6eOg/t3lsyR/KP8F9jEzO8I5Vx+lHsnPtviM/MDt/yPp/+R/32GSLpDv3ryXfGDw1NBx78jPhhvv+krJXztJ+pekY+QH+N9LUvPMmENC5cI/WyovNRufznxW46vyEwjUyl/bV+SDIrmSDpSfLKWvpIfM7FvOuZeS/o2kayT9NFiPvCfekn/+I++Jv0lanGB9mXjfcuRnUX5K/ndbJv+50k/S3vIzffYLfn4u6Q9R6rgxaLvkM9vulb8XmyT1kLSHpEPl399tdYgas4nDk8w8IalSftzDU+Q/h1LhO/KfMyvkn4d58l3uD5d0rvzn0DVmtto5d2+cevoFbeoiH/x7WdJmSXvKf3YNl//cPF/SFVGOz5G0VdJz8p/5i+SD3MWShsg/p4cE9T1uZvs651ozHMC/qTGb7lXnXFUr6kjENfLP13Py799l8vcuMjmQzOxCSZcFm5Xy75mXJW2TNF7Sb+TfOz+Sf98f1ewcLwVlsuSvzePN9h/awrbMrKsaP/Obf4ZcIv95LUlzJN0u/5m+Uf5vxqjgvN9vXi8AAGiDdEcKWVhYWJov8uN2Rf6X/o0U1XlIqM6PJPWKUqaffMAtUu6AKGUuUGMGw3Fxznd9qJ6DouyfHtp/SILtnh6n3MxQucFR9p8W2v+2pLI4dQ1qRf3hbJ/zFDsz6axQuROj7J8d2l8laXyUMoXy4785+S/2O/0uiV7fJJ+hGaE6z2q2L0c+aOMkHRt6/ZMEyn/WbF+2fJDCyU8gMjBGe3oH+yPlsprtHxxq78wox49VY/bjMkl9opQZID85y47MmRhtyeT7NlRSdpz9BfLBEScfgChqtj8vaK+T9HgL54r5vkqivfcG56qV1K3Zvr8G+7YpymdYEvc+vN/JZ6l1i1JugnzWmZMPmu2UfaamWcKfK/rnQ2/5/xxwktZGux+Suknq3cK1OSN0rpNaeX3Dmay/S8UzFuP5dZKui1N2hBoz+9ZIGh6lTLF8sDpS33HN9ncNngUn6aYox78VeW6Dnw3NnxtJR4bq/36zfSuD1+dI6hLndylWjExJFhYWFhYWluQXxqgDkInCY+SsTVGdZ4fWT3XOVTQv4JxbLek/YxwjMyuQ9Otg8w7nXLzZ/86Xz1CSGrP40sLMTL5rm+QziY52zq2PVd4515pZc38b/HzeOXetc87FqPtPkiLjKbV0XS51zs2PUscWSTcFm7lqnJChvc0OrR/SbN835LPfpMax6cLr8crPbrbvaPkMLUk62Tn3ebTGOOe+lPSrYHNklHO05Aw1joN2lnNup/eac26VfFZVMjLqvjnnPnWxMzflnKuRdE6wWSrfXTCsTL69UguT1MR7XyXCzErk778kPel2HgctkmHXRT5DNVVOi3IuOefmSboq2OyewDn/yzm3Iko9X6px/MHeknaaudY5tzEoF5Nz7hb5bF1JmtpCW2IJ/33Z6e9AmJkNMbM9YywD4h0rH/y+IM7+GWrM7PuVc+6T5gWcc5vkr3lD8NI5zfZvlg+iSY1Z3pG2F0uaGGzeIJ/ZbJL+vdlpIll29Wr62SX5/7ySpNdcnOxF59wmF2eiJwAAkBwCdQAyUUlovbqtlQXdVSNfYhY5516PVdY597x8FpQkHR4EuSKmyH9pl6R4QToFX2reCDYPTLrRqbWXfNcxSXowCL6kjJmNVmNgKe51CUS6hE4O7k0s8brZzQmtD0vgnG3mnFsk3y1Zkg5u9mwcEvz8OAj4RrzSQnlp5+BPJADxmXPuDcU3O7Se7HN2ePCzQtI/4pR7Qsl1Oc2o+9ac+YkuBpuf9GRP23nylPHNttfLZ9RJ0rSgq2B7mSafeSg17fYqSQqeh4+DzVTN/rrIOfd2nP23h9aPiFnKd92MOYmPkrz35icBGWBmo8MBMklfBEWa36dEJfP35U75bMNoy5UtHPugc64uzv7ItdwgPwZdVM65j9TYJfUbZtajWZHIvjFm1jf0+hT5QOBmSW+q8bMiVnfYec65ymb7In8rvm9mvWO1EQAApBaBOgCZaFNofacZIlthaKieNxMoHwmOdJMfWy0iPHbbS7bzjJRNFjUGXGLOzNlBJobW/xWzVOuFr8vfErgukSywXDUGPpurcM6ti3POr0LrJTFLpV7k+vWQH1MtYkqz/RGRQF2s8tLOGXWR6zkogWsZfq8k/JwFM2eODDbnOecaYpUNgg07ZcjFkJH3zcyGm9mfzc8mvEnSckkfqDHoEv79msx66ZzbKj95jOSzAFea2a1mNs3MBqW4qacEP9dI+meMMpEA3p6WxCzVccQL0inItFwRbO4Vp+jSeM+RErj3ZpZnfnbYt+QDTF/Id5cOB8i+GxTvGa2OBITHpEvF35dYdprdNcLMcuXHd5OkufGy1QKRv0mmne9BeFy5Q6OsvxrU/2LzMmbWTY0Bz2hjXN4R/BwuaZmZ3Wt+ZtsRLbQXAAC0AYE6AJko/EW/TwrqCweD1iRQPpwRFT62tRkFBa08LlV6hdbL26H+tmRaFMZ4fUsLx4UDAvGy8lJtdmj9EGlHxmYkm61JoM4596kaM4Cilf/MObe82Tlaez1jXctoust/6ZcaswTjSaSMlIH3zcyOkx/zb4aaBt5jiXYdz1JjtmiZpNOD7ZVmtsLMZplZazO8Iu0cI2lysHlfnO6696rxOqYiqy6Rexv53IwVWJfaeO+DrqTz5Wemniw/NmA8yTzvYeG/L71ilpLknDvEOWeRRY2ZyYmIl4XaQ43vv7b8TZL8fz7VBOvh7q+RgNxLzX6OMLOBwfohavwuEC1Qd5X8RCr18kHNE+WzDJea2Rozu9vMpkQ5DgAAtAGzvgLIRO9LqpP/jNrHzHJa6EKUjKhjpyVYPvyZeaQauwXtSpL9/RMRvi7RZuqMZ1e7hrND61Pkv8ROlB9MXdp5jCfJz956XIzys6OUj1zPd5VcIKY1M6ImylouknnMbLh8YCFXPpB0g6Rn5bu3bwiy5WRmWfLBCCnK7xqMBXa8mf1e0o/l7+Uk+SD87pJ+LunnZnajpLNjjdHYgvAsuL82s1/HLNnoODM71zlX24rzRSTS1o64//eocey6Z+SzuRbIj1NaE8nWM7N71Lbx+RaE1ifGLNV2McdFbKYtf5PknNtqZm/IB+kOlSQzK1Nj5t2LQbklZrZKfoKYQ+UzMyPBvO2SXtvpRD5YfJaZ/VHSsfLj2+0nnxHZR35m85+Y2SPykwMxTh0AAClAoA5AxnHOVZvZu/JfCArkB3d/tg1Vhgd4T6R7YHicn3B3rfDA4/XOuQ/a0KaOFG53SwOgt7X+7F3ouiTNObfYzL6Uz3qLjDt3SLB7RYyJOF6RD9Q1Ly9FD9RVSNpNUr92vJbhoF4iGXy76vhUp6gxM+to51ys7qTNx/2KKrgfH0iSmXWRnxTkh/KT0JRI+i9Ji+VnZ02YmeXIZyslq1tw/kTGhowlkazlyP1v02QZsZjZSDUGjR50zh0Xp3hC9yqOV9X4H0H/ZmYlzrmqFo5Jta/kA26mtv1NinhJPlA32MyGyAcgTf59Hu6C+7L8c9Y8UPd2MNlLVEHW79WSrg6C2ntL+oF8gLqPpB/JT55xYQK/CwAAaAFdXwFkqvAA5r+KWSoxn6px0PD9EigfmY1yo6SVodfnhta/3cY2daR3Q+vt0U0pE69Le2QORswOfvaUNFaxx6eLiGTZNS8vRZ9FNHI9B5jZuCj72yzIJItMSjAh+PIdVRBE2qc92hFFqu9b5Pp9FSdIJ/nsuKQ457Y75950zp2npjPFTku2Lvlx1yIBs1vlA7stLZHxCU9R20yOtzOYRGBwsPl+G88VS/g5jxl0DJ7TNmXBBTOpPhpsdlUaZuUOMs+WBJsTg6BvPAdEDlX0exDutrojs07Sy83GDYyU+2ZwX/do9nqLnHMNzrn5zrnL5P+eRgJ8rXnuAQBAFATqAGSqe+UHfJekw8xsRqIHmlkPM/uPyHbQfScykPaeZrZ/9CMlM/umGgfZf75ZF7YX1TgQ+WnNZtjLZAvlg5WSn7Uy1Vl1C0L1/0d7BZeSFO4K2NJYV8maHVr/pqSDgvWogTrn3GI1Zh2Gy690zq2Icsj/C63/d6tb2bLng5+9JH0nTrmj5Me06wipvm+RngP5LcwwnPDnSzTOuXfUmKUYd9yzGCLBNifpd865B1taJP1vcMyhbZzUYqyZ7Rtn/6lq7Pr6XBvOE0+4h0e8WXWPVtPssta6Uo1dUy83s3iTZLSXSOC4u6RjYhVqlm34rnMuWkbdO2r823Sodh6fLiLyd3CApDPUeF8TDtSFBZ9fkYBja557AAAQBYE6ABkpyDg4VtLW4KWbzOy/g9nyojLvGPkByf+92e4/htbvCMbwaX58HzXtshY+JpKJcV2wWSLpySArISYz+6aZHRivTHsLgo2/DzYLJT1mZjG7j4UGGk+m/pnBZrak/2dmw+IdY2YTzSxecKitwmPfpXqGwtmh9V+qcQbLaOPTRUTGfwqXnx29qO5X45ffH5vZpfEaY2aFZnZ2vKy4GG5R4wD/fwqe/+Z195d0fZL1tkWq79vS4GehfBbaTszsV2qcSTTa/qFmdmis/UGZfdUYzPw0Xtkox/ZWY6D0Tefc5wke+lDwM0vS9GTOGcVtZlYapW37SLoo2Nwo/x8o7WFpaP2UoIt487aMkXRzKk4WdGE+L9gskPQvMzsqgUPb2u027Gb5LriSdL2ZDW1ewMyK5MfuiwSZb4hWUfCfUa8Gm99R44yyLzYr95l8F1VJOjf4WSPprSjn7mFmR7WQbbu7GscVTOq5BwAAsTFGHYCM5Zx7x8x+JB+4KJJ0hXwm20PygY+1QdE+8t1Vj1Ljl4bmdc02s1vluzmNkfSemf1B0tvyWQX7y39xi2Rr3OiceyNKVb+Xn7HzCEn7SvrQzG6TD7qslc8C2k2+K90P5YMNp0t6vXVXITWcc3eY2RHyYwlNlvSRmc2S/3K3Xn5ygz0lfS/Y3zPJ+u81s4MlnSZpuKT3zexO+QycL+T/3vSV77b2A/mulFdK+kfbf7uo5kvaLJ+d8xszWy0/dtj2YH+Vcy7RmUybcM59aGZr5Z+7SEBylXNuWZzDXpF/HsIBzNkx6q8zs6nyz0yppJlm9j1Jd8lnL1YHr4+SdLD89SyW9Gc1nVmzpd9jYWTyA0lDJc0zs2vlv7SbfHe78+QDUPMltWlW0wSl+r7dLR8cNUm3BzOzPis/ztdQST+VD9K9psZMx+YGSXrRzJZJelLSHEmfyWf/9ZbvyvzzUPk/J9E+yQ/IH/n32MNJHPdPSZXyz8J0M7uilZNYvCP/eRW5//PkP8cOkx92oCgod45zrrIV9SfivWDZJzjvbDP7s3xWdYn85+2Z8gGruUrBJBDOueuD/7C4WH6sv8fNbL6kJ+SHC1gn/9yVymdZHybpP0JVtDTLbUvn/9jMLpH/m9JX0rtmdp18Zu42+ffbb+Q/TyXpSedcvLEIX5J/liMB13Ln3Ecxyg0LlXsjMqlKMyWSHpdUbmZPyH8ufCr//uwp//dvhqT8oPxN8X9jAACQMOccCwsLS0Yv8uN6vSTfLSyR5QlJI6LUkyOfRdTS8X+SlBWnPbny2RD1CdTVIOnYKHVMD5U5JM65DgmVmx6n3MxQucExynSRNCtoU7w2b2xl/Sbpt/JfMhO5T7+JUsfsYN+KFp6JwaF6ZsYoc2mcc9/VxmfyoWb1/b2F8hOitCHqdQwdM1o+MJfItaySn8gj2WuULZ8lFaverfLBrHuC7ZoY9WTsfZMPdsR75t+VD7hFPYeavgfjLVslzWhF+xap8bNiQJLH3hM6/78nep2b75cPVsW6RvWSLozThhVBudkttDV8HadH2b+H/H92xHvG/0M+YO0kuba8h0Pn/YGkjxK8x07+Px5+KSknSl3TQ+UOSfD8l8hn1sU758OS8luoZ59mx9wbo9y0ZuUuSuC9Gm+pl/T7VNwLFhYWFhYWFr/Q9RVAxnPOLXLOHSqf4XON/P/sl8t/Ma6R/+L0T/kg0XDn3FHOuY+j1FPnnDsjqOcu+eyAGvnMiE8k/U3Svs65s1zTAbib17PNOTdDPoB4nfwX/fXyX1g2y3ct+l/5bJThzrmHYtXVkZwf/P5M+UyNWfKZSpvkr+NK+ey636oVA+sH9Tvn3BXymUpXyGeEVch/Ca0JzvFP+XHXxjnn/tCmX6jl9lwm6Xj5rL61aszKSoWXm23H6/Yq+WyhcDZSrPHpdnA+G2a8pKnyWaXL5LPp6uTHQ5sv6Q75L959ne/+lhTnXL1z7iT5bL9n5bOItspnjN0jaT/n3N3yGUdq9ju0i1Tft+A5O1Q+G+5L+ev3pfw9myFpfxc/S+9V+SzTC+Wv0Ufy179OvjvoO/KfS2Occ0l1zTSzyWoc0P9159yqeOWjCH+2tHpSCefclfLjJ/4/+c/WbZJWyweIDnTOXdXaupNow2L52URvkO8Ku1X+8+nD4LW9nXNPtsN5n5K/Bz+Q/w+Y9yStkb8GW+S7Y78qPxTCEZIGOeducs7VRa8x6fNfLv97z5J/tqrlszVXyk+s8S3n3I+dc7Wxa5Hkg/rrQtuxxp2L/KdXS+VWBu06R/69syiov14+aLpAPotuvHPuohh1AACAVjDnXMulAADA15aZfSppiKRXnHNT0t0etI2ZDVbjZD2XOedmpq0xAAAAaIKMOgAAEFMwGcqQYDPauI0AAAAAUoRAHQAAX1NmVhpv5mIz6yfp9mDTyXcZBwAAANBOmPUVAICvryGS3jCzp+THD1wiPy5Xb/kZZc+QVBaUvdE5tyQtrQQAAAC+JgjUAQDw9VYg6dhgieVv8rOnAgAAAGhHBOoAAPj6+kh+htVvSZoon0nXQ37GzXJJr0n6m3Pu9bS1EAAAAPgaYdZXAAAAAAAAIAMwmQQAAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAWV/TyMyWSyqRtCLNTQEAAAAApN5gSVXOuSHpbgiAXQOBuvQqKSgo6DFmzJge6W4IAAAAACC1PvzwQ9XU1KS7GQB2IQTq0mvFmDFjesydOzfd7QAAAAAApNjEiRM1b968FeluB4BdB2PUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAQjUAQAAAAAAABmAQB0AAAAAAACQAXLS3QBkpqp1FVr40nOqqdqowtJuOuBHJ6S7SQAAAAAAAJ0agTpEVVu9SW899oAkqefA3QnUAQAAAAAAtDO6viKqgpKSHetbqirT2BIAAAAAAICvBwJ1iKqwpHTHek1VlVxDQxpbAwAAAAAA0PkRqENU2TldlNe1qyTJuQbVVG9Kc4sAAAAAAAA6NwJ1iKlpVh3dXwEAAAAAANoTgTrEVFDSbcf6lsqNaWwJAAAAAABA50egDjGFM+q2VFWlsSUAAAAAAACdH4E6xNQ0UEdGHQAAAAAAQHsiUIeYCktDgbpKxqgDAAAAAABoTwTqEFMBk0kAAAAAAAB0GAJ1iImurwAAAAAAAB2HQB1iKixtnPW1hskkAAAAAAAA2hWBOsQU7vq6pZKMOgAAAAAAgPZEoA4xNe36yhh1AAAAAAAA7YlAHWIqKC6RzCRJtdWb1FBfn+YWAQAAAAAAdF4E6hBTVna28ouKd2zXbGKcOgAAAAAAgPZCoA5xFTJOHQAAAAAAQIcgUIe4CksZpw4AAAAAAKAjEKhDXIXFBOoAAAAAAAA6AoE6xFVQ2m3Heg1dXwEAAAAAANoNgTrE1WSMuiomkwAAAAAAAGgvBOoQV9NAHRl1AAAAAAAA7YVAHeIKTyZRwxh1AAAAAAAA7YZAHeIqLGkco25LJYE6AAAAAACA9kKgDnEV0PUVAAAAAACgQxCoQ1xNu74ymQQAAAAAAEB7IVCHuHNkjXcAACAASURBVPK7Fsmy/GOydctm1W3fnuYWAQAAAAAAdE4E6hCXZWWpoLhkxzYTSgAAAAAAALQPAnVoUWFpaEIJAnUAAAAAAADtgkAdWlRYEsqoq2RCCQAAAAAAgPZAoA4tKighow4AAAAAAKC9EahDi8IzvxKoAwAAAAAAaB8E6tCiwmICdQAAAAAAAO2NQB1aFJ5MgllfAQAAAAAA2geBugSZWZGZfW5mLlimp7tNHaUg3PWVySQAAAAAAADaBYG6xP1O0m7pbkQ60PUVAAAAAACg/RGoS4CZTZD0C0lvp7st6RCeTIKurwAAAAAAAO2DQF0LzCxL0l+DzZ+nsy3pEh6jbkslgToAAAAAAID2QKCuZb+U9A1Jf3HOzU93Y9Iht6BQWdk5kqTtW2u1fWttmlsEAAAAAADQ+RCoi8PMBki6QtJaSf+d5uakjZk16/5alcbWAAAAAAAAdE4E6uK7SVKxpF87577WfT4LS8LdX5n5FQAAAAAAINVy0t2ATGVm35f0Q0mznXP3tbGuuTF2jW5LvR2poKRkxzozvwIAAAAAAKQeGXVRmFlXSX+WtF3SjDQ3JyM0mVCCQB0AAAAAAEDKkVEX3eWSBkm61jm3uK2VOecmRns9yLSb0Nb6O0JhSeMYdXR9BQAAAAAASD0y6poxs30knSXpc/mAHSQVhAJ1NZuYTAIAAAAAACDVyKjb2Z8kZUu6WJKZWVGMcnnBvgbn3JYOa12ahGd9JaMOAAAAAAAg9cio29nuwc97JG2KskTcEmy3uWvsrqDJrK+MUQcAAAAAAJByBOqQkPAYdTUE6gAAAAAAAFKOrq/NOOcGx9tvZi5YPdk5d1e7NyhDNO36SqAOAAAAAJCZ5s6de6CkwyR9Q1IvEftAx9gu6VNJL0h6cOLEiTWtqYSHFQlp2vV1o5xzMrM0tggAAAAAgEZz587NlnSWmf00JyenLCsrq6uZdZHEl1d0BNfQ0DC8vr7+G/X19fvPnTv3rNYE6wjUISFd8vOVk5unum1bVb99u7bX1ii3oDDdzQIAAAAAIOKIrKysU3JzcweWlZVtKCkp+SI/P39bVlaWa/lQoG3q6+uzqqurC9esWdO3pqZmSn19/TRJdyZbD2PUIWF0fwUAAAAAZLBjcnJyevbp02dd37591xUWFm4lSIeOkp2d3VBaWlrdp0+ftdnZ2T3ku18njUBdkpxzFix3pbstHa2gOBSoq9qYxpYAAAAAALCT0VlZWV27detGZgnSpri4eHNWVlaBpCGtOZ5AHRLWJKOuqiqNLQEAAAAAYCe5krJycnIa0t0QfH1lZWU1yI+LmNuq41PbHHRmTSaUqCSjDgAAAAAAIKytE28SqEPCCkpKdqzXVJFJDAAAAAAAkEoE6pCwwtJQRh2BOgAAAAAAgJQiUIeEFZaEZ32l6ysAAAAAAEAqEahDwsKBuppNTCYBAAAAAACQSgTqkLAmXV/JqAMAAAAAoNPatGlT1jXXXNPr0EMPHd6vX79xBQUF4wsKCsYPGDBg3JFHHjl01qxZPaqrq5vMnDBgwIBxZjYxvGRnZ08sKSnZZ6+99hr9q1/9qt/atWuzY53z6aefLo4ct2TJkiazpi5ZsiQ3XO/06dMHtvQ7jB49eo9I+QEDBoxr/dXoOATqkLCCcNdXxqgDAAAAAKBTuv/++0uHDh265wUXXDDo5ZdfLl2zZk2umSk7O1vl5eW5//znP7vPmDFjyNChQ8c99dRTxc2PLygoaCgrK6srKyurKy4urt+0aVP2woULu15//fX9x40bN3bBggV5bW3jU0891WPr1q0xp1idM2dOwZIlSwraep6ORqAOCWvS9bWqUs65NLYGAAAAAACk2o033lh20kknDV+3bl2XwYMH1958883LV69e/d6WLVvmV1dXz1+3bt17d95557J99913U0VFRZfZs2fvFKg744wz1q5bt27BunXrFmzcuPG9jRs3zr/qqqs+y8vLcxUVFV1OOumkIW1pY79+/bZt2LAh59FHHy2JVeb2228vk6T+/ftva8u5OhqBOiQsJzdXuQU+GN1QX6+tmzenuUUAAAAAACBV3n777YLf/OY3uzc0NGjKlCmVCxcuXHzmmWd+1bdv3/pImbKysvrp06dvfPvtt5fedtttnxYXF9fHq1OSSktLGy644IKKs88+u1ySFi5c2HX+/Pn5rW3n1KlTv5Kk++67ryza/rq6Oj3xxBM9zExHH330V609TzoQqENSCktC49RVMU4dAAAAAACdxYUXXjhg27Zt1rt37+2PPfbY8qKiorhd6U477bQNl1566dpE6//Od76zY2bK999/v9WBuh//+McbCgoKGl566aVu69at22nMuyeeeKKkoqKiy4QJE6qHDBmytbXnSQcCdUhKQUljVinj1AEAAAAA0DksX768y+zZs0sl6fTTT19bVlbWYqacJGVlJR5aCg+hVV9fH3N8uZYUFRU1HHHEERu2bdtmd955Z/fm++++++4ySTruuOPWt/Yc6UKgDkkJz/xaU0mgDgAAAACAzuDZZ58tjgTSpk6d2i5f+P/xj3/syP4ZMWJEmzLdfvrTn66XpAcffLBJ99cNGzZkvfDCC93y8vLc9OnTN7TlHOlAoA5JKWTmVwAAAAAAOp0PP/wwX5Jyc3Pd3nvvXZvKuisrK7OuueaaXn/605/6S9LQoUNrDzzwwC1tqfP73//+pj59+myfN29e0aJFi3bMInv33Xd3r62tzfrmN7+5MdGswExCoA5JKWgSqGOMOgAAAAAAOoP169fnSFJJSUldMt1Zo7nlllv69OzZc++ePXvu3b179727des2/oILLhi0detWKy0trb/77ruXt/Uc2dnZOvroo9dL0h133LEjq+7+++/vKUknnXTSLtftVZJy0t0A7FqaTCZB11cAAAAAwC5m8AXPTEx3G1JlxdXfnZvuNkRTU1OTVVNTs1Mkbo899tjy/PPPf9y/f/+6VJzn1FNPXf+Xv/yl7yOPPNLj+uuvL1+6dGnuu+++W9SjR4+69uq+297IqENSCksbM+pq6PoKAAAAAECnUFZWVidJVVVVOQ0NDW2q65xzzlntnJvrnJu7fv36+Y8//vjS0aNH1yxevLjwzDPPHJiSBkuaOHFi7dixY7d88cUXec8991zX22+/vcw5p6OOOuqrLl26pOo0HYpAHZJSwBh1AAAAAAB0OmPGjKmVpG3bttmCBQvyU1Vvjx49Go466qhNL7/88pJevXptf/LJJ3tcffXVvVJV/7Rp09ZL0l133dXz4YcfLpOkU045ZV2q6u9odH1FUppMJlHJGHUAAAAAgF1LpnYXTbdvfetbm8xMzjk99thjpePHj0/phBJ9+/atv+iii1adc845g6+66qoBp5566le9evVq82QPp5xyylczZ87c7ZFHHimrq6uz4cOH1x544IE1qWhzOpBRh6SEA3U1m6rS2BIAAAAAAJAqw4YN2z5lypRKSbr99tv7fPXVVwnFjJLpJjtjxoz1/fr121ZVVZV9xRVX9GllU5vo379/3cEHH1xVV1dnknTsscfustl0EoE6JKmgpGTHek1VlRoadrmZjgEAAAAAQBRXXnnlqtzcXLd27douU6dOHbplyxaLV/7222/vftlllyUccOvSpYvOOOOMtZJ055139l6/fn12W9ssSRdddNHq008/fe3pp5++9mc/+9kuOdtrBIE6JCU7p4vyuxZJkpxrUG11dZpbBAAAAAAAUuGAAw6oufrqqz8zM82ePbt0zz333GPWrFk91q5duyOgtn79+uy777672+TJk0eefvrpQzdt2pRUsO2ss85aV1JSUl9dXZ19zTXX9E5Fuw877LDNt9566xe33nrrF4MGDUrJjLLpQqAOSQtPKMHMrwAAAAAAdB7nnHPOurvvvntZjx496pYvX54/Y8aMIX379t2na9eu44uKisb37Nlzn+nTpw+bM2dOcf/+/bcdfvjhSY2LVVpa2vCTn/ykQpJuu+223pWVlcSmQrgYSFphKRNKAAAAAADQWZ100kkbly9fvvCqq676bMqUKZV9+vTZXl9fb/X19erfv/+2I488csMtt9yy/JNPPvng29/+dtJd7c4777y1eXl5buPGjTnXXXddymaA7QyY9RVJKyzptmN9SxUTSgAAAAAA0NmUlJQ0XHDBBRUXXHBBRaLHrFq1amEi5QYOHFhXW1s7r/nr3/ve9zY556LOyjtq1KhtsfbFc+65564799xzd5kJJsioQ9LCE0psqSKjDgAAAAAAIBUI1CFphaWhjLpKxqgDAAAAAABIBQJ1SFohk0kAAAAAAACkHIE6JC086ytdXwEAAAAAAFKDQB2S1mQyCbq+AgAAAAAApASBOiStsJSurwAAAAAAAKlGoA5JK2zS9ZVAHQAAAAAAQCoQqEPS8ouLJTNJUm31JtXX1aW5RQAAAAAAALs+AnVIWlZWtgqKS3Zs11ZvSmNrAAAAAAAAOgcCdWiVom7dd6xXrFyexpYAAAAAAAB0DgTq0CoD99x7x/rSt19PY0sAAAAAAAA6BwJ1aJWR+x20Y/2TOW+qob4+ja0BAAAAAADY9RGoQ6v0HzFKRd17SJJqNlXpiw8/SHOLAAAAAAAAdm0E6tAqlpWlEZMP3LG99K3X0tgaAAAAAACAXR+BOrTayP0aA3Ufz3lTDQ10fwUAAAAAAGgtAnVotf6jxqhrMPvrlsqNWvXR4jS3CAAAAAAAYNdFoA6tlpWVreH7HrBjm+6vAAAAAAAArUegDm0yKtz99e035Boa0tgaAAAAAACQrKlTpw42s4nJLkuWLMmVpCVLluSGX7///vtLY53rgw8+yGt+PBrlpLsB2LUNGDNWBSWlqqmq1OaNG7Rq6YfabfTYdDcLAAAAAAAkqKSkpL6srKwukbIbN27Mqa+vl5kpLy/PRStz+eWXD5g2bVplVhb5YckiUIc2ycrK1oh999f7LzwryXd/JVAHAAAAAMCu48477/xc0uctlXvooYdKjzvuuOGSdMYZZ6wZPHjw9mjllixZUnDHHXd0P/300zekuKmdHqFNtNnI/Q7asU73VwAAAAAAOp8lS5bk/ud//ucQ55wmTZpUfeONN66KVu7ggw+ulKTf//73/evqEkrSQwiBOrTZwD3GKb+4RJJU/dV6rf5kSZpbBAAAAAAAUqWmpsamTp06rLKyMrtXr17bH3300WU5OdE7aV544YVrCgsLG1asWJF/8803l3VwU3d5BOrQZlnZ2Roxab8d28z+CgAAAABA53HqqacOXLRoUWF2dra75557Ph00aFDMVLk+ffrUnXLKKV9K0rXXXtu/trbWOq6luz4CdUiJcPfXpW+9IeeijicJAAAAAAB2ITfffHOPBx54oJckXXzxxauOPPLI6paOufTSS9cUFxfXl5eX5/7xj3/s2f6t7DwI1CElBo7dS/ldiyRJm9ZXaM2ypWluEQAAAAAAaIt33nkn/9e//vXuknT44YdvvOyyy9YmclzPnj3rzzjjjLWSdP311/errq4mqy5BBOqQEtk5ORrWpPvr62lsDQAAAAAAaIsNGzZk/ehHPxpeW1ubNWjQoK0PPvjg8mSOv/jii9d27969rqKiosu1117bu73a2dlEH/kPaIVR+x2kRbNfkOQDdQefcLLMCJoDAAAAADLIzNKJ6W5CysysnNteVR9//PGDV65cmZefn9/w8MMPL+vRo0dDMseXlpY2/PKXv1xz+eWX73bTTTf1Peeccyq6d++eVB1fR2TUIWUGjdtbeYVdJUlVFWv15fJlaW4RAAAAAABI1mWXXdb72Wef7S5Jf/jDHz6bPHlyTWvqOf/887/s1avX9o0bN+b8/ve/75PaVnZOBOqQMtk5XTTsG5N3bC9h9lcAAAAAAHYpzz//fNff/e53u0nScccdt+4Xv/jF+tbWVVhY6M4999zVknTLLbf0qaioyE5VOzsrur4ipUbud5AWv/KSJOnjt17Xvx33U7q/AgAAAAAyRzt2F93VlZeX55x44onD6urqbOzYsVvuuOOOz9pa5znnnLPupptu6lteXp47c+bMvj//+c/XpaKtnRUZdUip3fcar9yCAknSxrWrVbEyqbEmAQAAAABAGtTX1+uYY44Z+uWXX3YpKSmpf/TRR5cVFBS4ttabl5fnzjvvvHJJ+tvf/ta7vLycpLE4CNQhpXK6dNGwiY3dX5fS/RUAAAAAgIx3zjnn9H/zzTeLzUx//etfl48ePXpbquqeMWPG+sGDB9fW1tZmXXXVVf1SVW9nRKAOKTdyv4N2rC996zU51+YAPAAAAAAAaCcPPfRQ6Z///Od+kvSLX/xi9bRp0ypTWX9OTo4uvPDCckmaPXt2aSrr7mwI1CHldt97vLrk++6vG1aXa93nK9PcIgAAAAAAEMv5558/MJJkc9999/Xq2bPn3okst912W/dEz3HaaadtGDlyZKtmj/06oV8wUq5Lbp6GTpikJW+8Isln1fUaNDi9jQIAAAAAAFFt3759xyyQGzZsSDhWVFNTk3ACWFZWli655JJVJ5544vBk2/d1QqAO7WLkfgeGAnWv68Afn5jmFgEAAAAAgGhWrVq1sC3Hjxo1aptzrsXZdE844YTKE044gVl346DrK9rFkH0mKicvT5L01arPtf6LNs/oDAAAAAAA0KkRqEO76JKXr6HjJ+3YXvrW62lsDQAAAAAAQOYjUId2M3K/A3esL33rtTS2BAAAAAAAIPMRqEO7GTL+G8rJ9d1f132+UutXfZ7mFgEAAAAAAGQuAnVoN7n5BRqyz8Qd2x+//UYaWwMAAAAAAJDZCNShXY2g+ysAAAAAAEBCCNShXQ2bMEnZXbpIkipWLteG1avS3CIAAAAAAIDMRKAO7Sq3oFCD927s/rqU7q8AAAAAAABREahDu2P2VwAAAAAAgJYRqEO7GzZxX2Xn5EiSvly+TBvXrklziwAAAAAAADIPgTq0u7zCrtp9r/E7tj9++/U0tgYAAAAAACAzEahDhxi530E71un+CgAAAAAAsDMCdegQwyZOVla27/66ZtnHqqr4Ms0tAgAAAAAAyCwE6tAh8ouKtPu4vXdsL6X7KwAAAAAAQBME6tBhRjD7KwAAAAAAQEwE6tBhhk/aX1nZ2ZKk1R8vUdW6ijS3CAAAAAAAIHMQqEOHKSgq1sCxe+3Y/mTOG2lsDQAAAAAAQGYhUIcONTLU/XXJW4xTBwAAAABAppg6depgM5u47777jgq/fu655/Y3s4lmNrF37957bdmyxWLV8V//9V/9o9XRvJ7IkpOTM7GkpGSfAQMGjJsyZcrws88+u/+cOXMK4rXz6aefLo4cv2TJkty2ln3yySeLv//97w/ZbbfdxuXn508oLCwcP3DgwD0nTZo0asaMGQMee+yxktra2pi/cyoRqEOHGj5pf1mWf+zKlyzWpq/WpblFAAAAAAAgURUVFV2uvfba3m2pIysrS2VlZXVlZWV13bp1q9u+fbuVl5fnvvLKK6V/+tOf+k2ePHmP/ffff+RHH30UNwjXVnV1dTr22GN3P+qoo0Y+/fTTPVatWpVbV1en3Nxct3r16rx33323aNasWX2POeaYEfPmzctvz7ZEEKhDhyosKdXAPcbt2P5kzptpbA0AAAAAAEjWjTfe2LeysrLVMaW+fftuW7du3YLIUlNTM7+ysnL+008/vWTatGnrunTp4t56663iSZMm7fH222/Hza5ri9/+9rd9H3744Z6SdMIJJ1TMmzdv0datW+dt3Ljxvc2bN8/717/+9eG5555b3r9//23t1YbmCNRFYWbfMLMrzOxZM/vEzCrNbKuZrTKzJ83sqHS3cVc2ssnsr3R/BQAAAABgVzBq1KiaXr16bd+wYUPOlVde2SeVdZeUlDR897vfrX7ggQdWvvDCCx917969rrq6Ovvoo48eHq+rbWs1NDTojjvu6C1JJ510UsV999332fjx42uzg0kw8/Ly3MEHH7zlf/7nf1Z/9tlnCydMmFCb6jZEQ6AuutMk/bekIyQNk79ODZL6S/qBpMfN7FEz65K+Ju66hk/aX2b+0fvio0XavHFDmlsEAAAAAABakpeX1/CrX/1qtST95S9/6VNRUZHdHuc5+OCDt8yaNWuFJJWXl+fecMMNvVJ9jjVr1uRUVFR0kaQf/OAHG+OVzc7OVn5+vkt1G6IhUBfdm5LOkTRRUrFzrtg5VyBpkKQ/BGWmSrogTe3bpXXt1l27jRnrN5zTx3R/BQAAAABgl3D22Wev69+//7bq6ursyy+/vG97nWfatGmVo0ePrpGkRx55pEd7nUeSPv/883YdCy8ZBOqicM7d7Zz7o3NunnOuOvT658658yTdF7w0PS0N7ARGNOn++loaWwIAAAAAABKVl5fnzj///HJJuuOOO3qvWrUqp73O9c1vfrNSkhYtWlRYXV2d0u6v/fv3r4uMPXfdddf1a2mm2Y5CoK513gl+9k9rK3ZhI/Y9QDL/Hvti8QfaUhk3yxQAAAAAAGSIM888c/3gwYNra2pqsi655JJ+7XWecePG1UhSXV2dLV++POVZb+edd1655LvXTp48eY+xY8eOOfnkkwfOmjWrxwcffJCX6vMlgkBd6xwQ/Fye1lbswoq699CAUXtIkpxr0CfvvJXmFgEAAAAAgETk5OTooosuKpek++67r9eyZcvaZQz/srKyush6RUVFyjP3zjrrrPU33HDDiu7du9dJ0uLFiwvvuuuu3jNmzBgybty4PQcMGDDu/PPP71tVVdVh8bN2S0/sbMysSNJQSf8p6djg5T+nr0W7vpH7HahVHy2SJC156zXtddiRaW4RAAAAAKCzG3f3uInpbkOqLPzpwrnpOvepp5664brrrqtZunRpwW9/+9v+999//8r2PJ+ZtctkDmefffb600477atHHnmk2wsvvFA8f/78rp988knB9u3brby8PPfaa68d8Oijj5bNnj17ycCBA+tarrFtyKiLw8x2MzMXPAybJC2QdKakWkmXOOdmJVjP3GiLpNHt1/rMN2LyATvWP1/0vrZUVaaxNQAAAAAAIFFZWVm65JJLVknSI488UrZ48eKUd01dv379jgSznj171qe6/oiioiJ38sknb/j73//+2eLFiz9cv379e3//+98/GT9+/GZJ+vTTT/NPOeWU3dvr/GEE6uKrl7Q2WLYFr9VJukpk07VZcY+e6j9yjCTJNTRo2btvp7lFAAAAAAAgUSeccELluHHjNtfV1dnFF1+c8nH8Fy5cWCBJOTk5bsiQIZG4jAoKChoi65s3b44b2wrvLywsbIhXNqK4uLjh+OOPr3z33Xc/OuCAA6ok6cUXX+y2Zs2a7GR/h2TR9TUO59xqSX0lycyyJA2XdL6kyySdambfcc4tSqCeqGm1QVbdhNS1eNczcr8DVb70Q0l+9tdxh34rzS0CAAAAAHRm6ewu2hlddtll5UcfffSIp556qmzu3LlrUln3iy++WCpJe+6555aioqIdXV979+69owvqF1980WXChAm1seooLy/vIvkMwF69eiWVlZeVlaWf/OQn6994440S55wWL16c37dv383J/yZJnLM9K+9MnHMNzrmlzrlTJV0vaZCk+4IAHlop3P31sw8WqKZ6UxpbAwAAAAAAkvHDH/6watKkSdUNDQ1KZVbdgw8+WPrRRx8VSNKPf/zj9eF9e+yxx9aioqJ6SXrttdeK4tXz5ptvdpWkYcOG1eTn5yc9zl3kPJKUl5eXUEZeWxBkap2bgp/7SBqfzobs6kp69la/4aMkSQ319XR/BQAAAABgF3PFFVeskqTnnnuu+4IFCwrbWt+rr75aeOaZZw6WpAEDBmw766yz1oX3Z2dn6/DDD98oSffee2/PysrKqPGtZcuWdXnmmWd6SNJ3v/vdjeF9tbW19swzz8QN8knSAw88UCZJ+fn5DXvttdfWVv1CSSBQ1zqrQuvD0taKTmLEfgfuWF/61mtpbAkAAAAAAEjWEUccUX3QQQdVOef0yiuvlLamjk2bNmX93//9X9Hxxx+/+2GHHTZ6w4YNOUVFRfWPP/74x4WFhTtlws2cOXN1QUFBw5o1a3IPOuigUc8++2xRXZ3vEVtbW2sPPfRQ6aGHHjpqy5YtWb169dp+3nnnfRk+fuvWrfa9731v1D777DP66quv7vX+++/nNTQ07Nj3yiuvFH77298e+swzz3SXpGOPPXZdcXFxu2fUMUZd6wwJrVenrRWdxMjJB+qV+/4mSVr5/nuq3Vyt/K4tBrUBAAAAAECGuPLKK1dNmTKlJJGya9asye3Zs+feke2ampqsLVu2NEkm23///avuvPPOlaNGjdq2cw3SXnvttfWee+5ZdvLJJw/94IMPCr/97W+P6tKli+vatWv9pk2bsuvr602SevXqtf2xxx77pF+/fnXh47OyspSdna0FCxZ0XbBgQdcLL7xQOTk5rmvXrg1VVVXZzjXGBg8//PCNs2bN+iKJy9FqBOqaMbNsSQ0ufEd29pvgZ52kN9u/VZ1bae8+6jN0hNZ++rEa6uv06dw52uPgQ9PdLAAAAAAAkKCDDz54y+GHH77x+eef79ZS2YaGBq1fvz5H8gGzwsLC+v79+28bNmxY7YQJEzafcMIJX02aNCnmBBERxxxzTNW+++77wXXXXdf7pZdeKl25cmXepk2bsouLi+uHDh1ae8QRR1See+65FT179txpEoni4uKGzz77bMEjjzxS+q9//av4gw8+KFy9enVudXV1dkFBQUPv3r237bPPPptPPPHEr6ZOnVrVuquSPIsfj/r6MbPBkh6TdLOk55xzXwSvZ0naSz5Id3xQ/Abn3LltONfcCRMmTJg7lwln5jz5qF69/y5J0tCJ++qH512S3gYBAAAAQBtNnDhR8+bNm+ecm5jutnwdzJ079938/PwxY8eO/TDdbcHX26JFi8bU1tZ+OHHixG8kXX4CywAAIABJREFUeyxj1EU3QdIdkj43sxozq5C0RdJ8NQbp7pJ0Xnqa1/mMnNw4Tt3KBfO0dcuWNLYGAAAAAACg4xGo21m5pGMl3SrpPUmVkrpJ2i5psXwA7yDn3MnOubqYtSAp3fr2U+/Bfl6O+ro6fTpvTppbBAAAAAAA0LEYo64Z59w2SQ8HCzrQyP0O1Jcrlknys7+OOeiQ9DYIAAAAAACgA5FRh4wxItT9dfl7c7Wthu6vAAAAAADg64NAHTJGj/4D1GvQYElS/fbt+nT+u+ltEAAAAAAAQAciUIeMMmK/xqy6pW+9lsaWAAAAAAAAdCwCdcgoIycftGN9+fy52l5bm8bWAAAAAAAAdBwCdcgoZbsNVNlugyRJddu2avl7dH8FAAAAAABfDwTqkHFGhrq/Lnnr9TS2BAAAAAAAoOMQqEPGGRme/XXeO9q+le6vAAAAAACg8yNQh4xTNnB39ei/myRp+9ZarVgwL80tAgAAAAAAaH8E6pBxzKxJ99eldH8FAAAAAABfAwTqkJFGhLq/Lps7R3XbtqWxNQAAAAAAAO2PQB0yUq/dh6h7v/6SpO21NVrx/vw0twgAAAAAAKB9EahDRjKzJll1S996LY2tAQAAAAAAaH//n707j666uvf//9rnZCZzAgkJgTCLgAhBJnGqQ9VaqxeHOlGs0kH6U9Fa9apt1Xodalu1FidAq4C2im2/ynW4WqkCgkJkRiaBABnIPE/nnP374yQxgQRC+ISThOdjrc865+zP/uz9/ljoWrzXfu9Nog5dVvPTX3euXiVPfX0AowEAAAAAAOhcJOrQZfUZOFgxScmSpLrqKmVtWBvgiAAAAAAAADoPiTp0WcaYFqvqKH8FAAAAAOD4KC8vdz3++OO9v/Od7wzp27fv6PDw8LHh4eFjU1NTR1944YWD5syZE19RUWGaP5OamjraGJNxxx13pBxp/KPp+9BDD/UxxmQYYzKuueaaAe19h3/9619R3//+9wf269dvdFhY2LiIiIixaWlpo0477bThs2bNSl28eHF0TU2NOfJIx09QoAMADmfYxNP15f9bLEnasXqlvJ56uYOCAxwVAAAAAAA916JFi2Juu+22AQUFBU3/AA8PD/e5XC5lZ2eHZGdnh3zwwQdxv/3tb/vNnTt316WXXlremfG8/vrriY3f33333biqqqqsiIgI21Z/j8ej6667bsDf//73pufcbreNjIy0OTk5ofv27QtdvXp15Jw5c5KXL1++ecqUKdWdGf/RYEUdurSkwUMV3buPJKm2slJZG9cHOCIAAAAAAHquZ555JuGGG24YUlBQEJyenl7zl7/8ZVdOTs7aqqqqryoqKr4qKChY+/LLL++cMGFCeX5+fvDSpUujOjOeVatWhX/99dfhKSkpdVOmTCmrqKhwL1iwIPZwzzzwwAPJjUm66667Lj8zM3NTbW1tZklJydrKysrM//znP1vuuOOO7JSUlLrOjL0jSNShS+P0VwAAAAAAjo9Vq1aF33XXXQN8Pp/OOuus0g0bNmy+5ZZbipKTk72NfRISErwzZswoWbVq1baXXnrpm6ioKO/hxjxWc+fOTZCkyy+/vOiaa64pkqQFCxYkttXf5/Np3rx5fSTphhtuyF+wYEHW2LFja9xutyQpNDTUnnnmmVV/+MMfcrKysjaMGzeupjPjP1ok6tDlNd+nbseXK+X1eAIYDQAAAAAAPdO9996bWldXZ/r06VO/ePHiXZGRkW2Wl0rSzTffXPyb3/wmr7Piqa+v1z/+8Y8ESZoxY0bhddddVxwWFuZbsWJF9J49e1rdFys3NzcoPz8/WJIuvfTSksON73a7FRYWdth3PN5I1KHL6zt0uKISekuSairKtXfzhgBHBAAAAABAz7Jr167gpUuXxkjSzJkz8xISEtq1Us7l6rzU0uLFi2MKCwuDhg0bVj1+/PiauLg437nnnlvq9Xo1d+7c+CM9v3fv3pBOC66TkKhDl+cvf53S9JvyVwAAAAAAnPX+++9HWetfXDZt2rTSAIcjSXr11VcTJOnKK68sbGy79tprCyXpjTfeaLX8NSUlxdO499yTTz7Z94svvgg/HrE6hUQduoUW5a9ffC6ft1NL4AEAAAAAOKFs2bIlTJJCQkLsmDFjjmnftueffz4pMTFxzOGu3Nzcw652y8/Pd3/88cexxhjNmDGjqLF92rRpZbGxsZ4dO3aEffbZZxGtPfurX/0qW5Kys7NDJk6cePLIkSNH3HjjjWlz5syJ37hxY+ixvFtnI1GHbiFl2EmKjPOvaq0uL9O+LRsDHBEAAAAAAD1HYWFhkCRFR0d7jrWctbq62lVYWBh0uMvn8x12jPnz58fX1dWZjIyMiiFDhtQ3toeGhtqLL764WJLmzZuX0Nqzt912W+Gf/vSn3XFxcR5J2rx5c8Qrr7zSZ9asWQNHjx49KjU1dfTdd9+dXFZW1uXyYkGBDgBoD+NyaejE0/XV++9I8pe/9h81JsBRAQAAAAC6my0njcgIdAxOGfH1ljWBjqE1s2fPzvnjH/+Yfbg+qampo7Ozs9tcVbdo0aIESbrqqqsKD743ffr0okWLFvX+17/+FV9bW7svNDT0kAMhbr/99sKbb7656M0334z96KOPor766qteO3bsCK+vrzfZ2dkhTzzxROpbb72VsHTp0q1paWld5tTKLpc5BNrSvPx1+xefy+ej/BUAAAAAACckJCR4JKmsrOyIq90627p160LXr1/fKygoyE6fPr344Pvnn39+RUpKSl1JSUnQm2++GdPWOJGRkfbGG28sXrhwYdbmzZu3FBYWrl24cOGOsWPHVkrSN998E/bjH/94QGe+y9EiUYduI+WkEeoVGydJqiot0f6vNwc4IgAAAAAAeoYRI0bUSFJdXZ1Zt25dWCBjeemllxIlyePxmOTk5FONMRnNL7fbndG4Gq/xwIn2iIqK8l177bWlq1ev/nrKlCllkvTxxx/H5ubmujvnTY4epa/oNlwut4ZMmKJ1Hy6R5C9/TTt5dICjAgAAAAB0J121XDTQLrjggnJjjKy1Wrx4cczYsWOP6UCJjvJ6vVq8eHF8e/t/8sknMbm5ue7k5OR2l925XC5Nnz69cMWKFdHWWm3evDksOTm5smMRO4sVdehWWpS/rlohG+DluAAAAAAA9ASDBw+uP+uss0olae7cuUlFRUXtyhk5XSb7zjvvROXm5oaEhoba3bt3r8/Pz1/b1jV8+PBqj8dj5s+f3+7EXqPIyMimxF5oaGiXSS6QqEO30u/kkQqP9pefV5YUa/+2LQGOCAAAAACAnuGRRx7ZHxISYvPy8oKnTZs2qKqqyhyu/9y5c+MefPDBJCdjeOWVVxIlaerUqaUDBgyoT0xM9LZ1ff/73y+WpEWLFiU2Pl9TU2OWLFkSeaR5Xn/99QRJCgsL851yyim1Tr7DsSBRh27F5XJr6ITJTb+3r1wewGgAAAAAAOg5pkyZUv3YY49lGWO0dOnSmFGjRp08Z86c+Ly8vKY93AoLC91//etfYydOnDhs5syZg8rLyx3b3620tNT1wQcfxErSZZddVnKk/ldffXWxJG3atClizZo1YZJUW1trLrnkkuGnnnrqSY899ljv9evXhzau+qutrTWffvppxEUXXTRoyZIlcQ1jFERFRXWZFXXsUYduZ9jEqVr/0fuSpG2rluvs6TfLuMg5AwAAAABwrGbPnl2QmJjouf322wfs2rUrbNasWQNnzZqliIgInzFGlZWVTf8AT0lJqTv//PPLnJr7lVdeiaupqXEFBQXZq6+++oiJuvHjx9ekp6fX7N69O2zu3LkJGRkZ+10ul9xut9atW9dr3bp1ve69914FBQXZXr16+crKytzW2qbnzz///JI5c+bscyp+J5DdQLeTNnK0wqKiJUkVRYXK2bE1wBEBAAAAANBz3HDDDSW7du3a8Oijj2adddZZpUlJSfVer9d4vV6lpKTUXXjhhcXPP//8rh07dmy86KKLKpyad+HChYmSNHHixPLevXu363CISy65pESSFi9enODxeBQVFeXLyspa99RTT+2+/PLLC4cOHVodFhbmq6iocIeHh/vS09NrLrvsssK33npr+4cffrgzIiLCHmmO48k0zyTi+DLGrBk3bty4NWs4cOZoffjCM9rw7w8lSRnfu0xnT785wBEBAAAAQEsZGRnKzMzMtNZmBDqWE8GaNWtWh4WFjRg5ciSbmSOgNm3aNKKmpmZLRkbG+KN9lhV16Jaan/66bdVykXAGAAAAAADdHYk6dEtpo8YorJf/EJfygnzl7twW4IgAAAAAAACODYk6dEvuoCANPm1S0+9tnP4KAAAAAAC6ORJ16LaGTWpW/rqS8lcAAAAAANC9OZaoM8b82xjz5lH0f90Y87FT8+PEM2D0qQqN6CVJKsvP04FdOwMcEQAAAAAAQMc5uaLubEmnH6lTM5MangE6xB0UrMHjJzb93rZyWQCjAQAAAAAAODaBLH11S6JWEceE8lcAAAAAANBTBCRRZ4wJldRHUlkg5kfPMWD0WIWEh0uSSvJylL9nV4AjAgAAAAAA6Jigjj5ojOkvKf2g5hBjzBmSTFuPSYqVdI2kEEkrOjo/IElBISEanDFRW5YtleRfVdcnfVBggwIAAAAAAOiADifqJN0o6dcHtcVJWtqOZxsTeU8dw/yAJGnopNObJeqW6fSrr5cxbeWKAQAAAAAAuqZjSdSVSMpq9nuAJJ+kfYd5xid/uesmSfOstZ8cw/yAJCl9zDgFh4WrvqZaxTn7VbB3j3r3Tw90WAAAAAAAAEelw4k6a+3Tkp5u/G2M8UnKt9YOdCIwoL2CQ0I1aNxp2rriU0n+8lcSdQAAAAAAoLtx8jCJByX9wcHxgHZrefrrsgBGAgAAAAAA0DHHUvragrX2QafGAo7WwFMzFBQaKk9trYr271Xhviwl9Osf6LAAAAAAAADazckVdUDABIeGadDY05p+b1u5PIDRAAAAAAAAHD3HE3XGmAuNMXONMSuNMVuNMd8c5trp9Pw4cVH+CgAAAAAAujPHSl+NMcGS/ibpB41N7XjMOjU/MHDseAUFh8hTX6eCvXtUuH+vElLTAh0WAAAAAABAuzi5ou5uSZc1fF8i6WZJF0k65zDXdxycHye4kLBwDRw7vun39lUrAhgNAAAAAADdy7Rp09KNMRnGmIxRo0aN8Pl8bfb9wQ9+MNAYkzFt2rT0tvrk5eW577333uSMjIzhiYmJY4KDg8clJCSMycjIGH7PPfck5+bmult77nvf+94gY0xGenr6qKqqqjYXgu3atSs4KirqVGNMxq9+9au+R/OuXZWTibrr5F8hd6+19lJr7Xxr7QfW2v8c7nJwfkBDKX8FAAAAAOCYbdq0KeK1116L7ejzzz//fPzQoUNHP/bYY6mZmZmRxcXFQREREb6SkpKgzMzMyMcffzx12LBho59//vn4g5998cUXs2JjYz179uwJvfPOO1PamuOmm24aUFFR4R4+fHj1ww8/nNvRWLsSJxN16ZJ8kv7s4JjAURk87jS5g4MlSfl7dqk4Z3+AIwIAAAAAoHv63e9+l+r1eo/6ud///veJt9xyy8Dy8nL3yJEjq/72t79tr6yszCwtLV1bVVWV+dZbb20fNWpUVXl5ufuWW24Z+Pvf/z6x+fOpqameRx55ZK8kvfTSS8mfffZZxMFzPPfcc/GffPJJjNvt1ksvvbQ7NDS0R2yv5mSirkRSubW22sExgaMSEh6h9DEZTb+3Uf4KAAAAAMBROe200yrCwsJ8O3bsCHvhhRcOWfF2OMuXLw+/7777+ltrde6555asWbPm66uuuqosLCzMSlJoaKidNm1aWWZm5pbzzjuvxFqr++67r/+KFSvCm49zyy23FJ111lmlXq9XM2fOTK+trW0qgd2/f3/Qf//3f6dJ0k9+8pPcM844o8qJ9+4KnEzU/UdSjDGG3fsRUJz+CgAAAABAx/Xp06d+xowZByTpscceS6mvr2/3s/fdd19qfX296d27d/3f//73XW2tdAsODtYbb7yxu3fv3vX19fXm/vvvTz24z9y5c/f06tXLt3Xr1vAHHnggubF95syZ/UtKSoIGDBhQ++STT2Z34BW7LCcTdb+TVCPpcQfHBI7a4IwJcgf5DzQ+sGunSvJ6RJk6AAAAAADHzW9/+9vcyMhI7969e0OfeeaZxCM/Ie3cuTP4008/jZGkm2666UB8fHzbp1FISkhI8P74xz8+IElLly6N2blzZ3Dz+0OGDKl/4IEH9knS008/3TczMzPstddei33vvffijDF6/vnnd0dERPSIktdGjiXqrLUb5T/19UJjzHvGmLONMb2cGh9or9CIXhpwytim39tXLQ9gNAAAAAAAdD9JSUnemTNnHpCkJ598sm91dXWbp682+vDDD6Os9efNrrzyypL2zNPYz1qr//u//4s6+P5dd92VP378+Iq6ujozY8aM9DvuuKO/JF1//fX5F154YcVRvFK30KFEnTHG29ol6X1JMZIukPSxpLK2+jZcHgffBWgybNLUpu+UvwIAAAAAcPTuv//+3JiYGG9ubm7Ik08+2ftI/Tdv3hwuSSEhIXbMmDE17Znj1FNPrQkODraStGXLlrCD77tcLs2fP393WFiYb8OGDb0KCgqC+/btW/fnP/9539G+T3fQ0RV1xqHLydJboMngjIlyuf3lr7k7t6ss/0CAIwIAAAAAoHuJj4/3zZo1K1eSnnrqqb5lZWWHzeMUFRW5JSk6OtrjdrvbNYfb7VZ0dLRXkgoLC4Na6zN69OjayZMnlzf+vv/++/fHxMQctqy2u2r1P0A7DHQ0CsBhYZGRGjB6jHatXSNJ2rZqucZfcnmAowIAAAAABNpffvbvjEDH4JRZz39nTWfPcc899xx44YUXkgoLC4MeffTRPo8++mibG8E3lr0erSM9984770QtXbo0pvH3ggULEm655ZaiDk3WxXVoRZu1do9Tl9MvBDQayumvAAAAAAAck6ioKN/tt9+eI0lz5sxJLiwsbHOpXEJCgleSysrKgrxeb7vG93q9Ki8vd0tSfHz8IVuklZeXu2bNmjXAWqtJkyaVu91u+/nnn0c//fTTCR16oS6O0lP0WEPGT5Jx+f+I52zfqrKC/ABHBAAAAABA93PnnXfmJycn15WVlbkffvjhpLb6jRgxolqS6urqzLp16w7Zb641a9euDauvrzeSdPLJJx+yr93s2bNT9u7dG5qQkOD55z//ufNnP/tZniT95je/Sdu7d29HK0W7rB73QkCj8Kho9R81RnvWfyVJ2vHFCo27+AcBjgoAAAAAEEjHo1y0pwkPD7e//OUvc375y18OmDt3btLdd9/d6kbw3/3ud8uNMbLW6s0334wdN25cm2Wyjd58881YSTLG6Pzzzy9vfu/f//53r5dffjlJkp544omspKQk7xNPPJH97rvvxu3Zsyf0Zz/7Wf8lS5Z848Q7dhWOragzxsw/yus5Y8yjxpjpxphUp+IAmhvWrPx168rlAYwEAAAAAIDu69Zbby1IS0urraysdP3mN79Jbq3P4MGD688888xSSZo3b16foqKiIx0+4Zo/f34fSTrrrLNKBw8eXN94r6amxvz0pz9N9/l8Ou+880p+/OMfF0tSRESEfe6553YbY/S///u/cYsWLYppa/zuyMnS1xkN14+aXTMOuprf+6mkX0l6WdJuY8wCY0y8g/EAGnLa5Kby1+ytm1VeVBDgiAAAAAAA6H6Cg4N1zz33ZEvSa6+91jsvLy+4tX4PP/xwdlBQkM3Pzw++6qqrBtbW1prW+tXX1+vqq68emJ+fHxwUFGQffvjh7Ob377333r47duwIi4qK8s6dOzer+b2LLrqo4oc//GG+JN1xxx0DiouLe8zWbk6+yIOSHpNUKslI2iXp1Ya2xyT9VdI3DfdKJD0q6RlJyyW5JV0j6UNjTKiDMeEEFxEdo7STRzf93vHF5wGMBgAAAACA7uunP/1p0eDBg2tqampcq1atimqtzxlnnFH10EMP7ZWkjz/+ODYjI+Okt956K7oxYVdfX6+33347OiMj46SPPvooVpIefvjhvVOnTq1qHOOLL74If/bZZ5Ml6cEHH9w3YMCA+oPnefbZZ/f17t27Pi8vL/jWW2/t1xnvGwhOJuoek3S2/Em3q621Q6y1M6y1/91w3WitHSrpSvn3xpsq6VfW2jMlnS6pWNJY+VfaAY4Z1uL0V8pfAQAAAADoCLfbrfvvv3//kfrde++9+c8+++yuyMhI76ZNmyKuvPLKoREREeNiY2NPDQ8Pz5g2bdrQDRs29IqMjPQ+++yzu+65556m0x89Ho9uuummdI/HYyZPnlw+e/bsVkvj4uPjfX/84x+zJGnhwoW9P/zww17OvWngOJmou1fSREk/tda+2VYna+1i+ZNxZ8hf+ipr7eeS7pB/td2VDsYE+Mtfjf+P+r6vN6mypDjAEQEAAAAA0D1Nnz695OSTT646Ur9Zs2YVbd++fcPdd9+9f9y4cRUxMTGeyspKV3R0tGfs2LGVd911V/a2bds2zpo1q6j5cw8++GDSxo0bI8LCwnzz58/ffbg5rr/++pKLLrqo2Fqrn//85+k1NTWtltl2J8Za68xAxmyRlC4p0lrrPUJft6QKSd9Ya0c2tPWSv2y21Fqb4EhQXZwxZs24cePGrVnDgTOd7e8P3qu9mzdIks696RadesHFAY4IAAAAQE+XkZGhzMzMTGttRqBjORGsWbNmdVhY2IiRI0duCXQsOLFt2rRpRE1NzZaMjIzxR/uskyvqBkiqOVKSTpIa+tTIn9hrbKuUf++6HrFUEV3L0Bblr8sCGAkAAAAAAEDrnEzUlUuKNsaMOFJHY8zJkmIkVTZrczW0FbX1HNBRQ0+bLBn/Cth9mzeqqrQkwBEBAAAAAAC05GSibqn8e8zNM8ZEt9XJGBMl6SVJVtInzW6ly38QxT4HYwIkSZHxCUod7s8hW+vTji9XBjgiAAAAAACAlpxM1P1W/nLWiZK2GmN+a4w53xgzquE63xjzoKStkiZLqpX0YLPnr274/I+DMQFNhk2a2vR9K+WvAAAAAACgiwlyaiBr7RZjzKWSXpeUJOmBNroa+ctbr7XWbm7WXiDpkYbnAccNnTBFn7zyoiRp76b1qiorVUR0TICjAgAAAAAA8HNyRZ2stR9JOknSw5I2yV/eahou29D2sKSTrLUfHvTsS9baBw5K3gGOiUpIVN9hJ0mSrM+nnatXBTgiAAAAAACAbzmaqJMka22htfY31tpTJEVI6ispRVKEtfaUhnsFTs8LtMfwZuWvnP4KAAAAAAC6EscTdc1Za+ustXnW2lxrbV1nzgW0x9CJU5q+Z21cp+qK8gBGAwAAAAAA8K1OTdQBXU10Yh8lDxkmSfJ5vZS/AgAAAACALqNDh0kYY85s+FplrV19UNtRsdZ+2pHngI4aNmmqcndsk+Qvfx119nkBjggAAAAAAKDjp74ulf9wiK2STj6o7WjYY4gB6JBhE6fo0wXzJUl71q9VTWWFwnpFBjgqAAAAAABwoutokixL/iRbdittQJcW0ydZSYOGKO+bHfJ5PfpmzRc6+czvBDosAAAAAABwgutQos5am96eNqCrGjZpqvK+2SFJ2rpyGYk6AAAAAAAQcBwm0QpjTH9jzO3GmHeMMVnGmFpjTLkxZp0x5jFjTN9Ax4hj0/z01z3rMlVbVRXAaAAAAAAAAEjUHcIYkyZpt6Q/SbpEUpqkGknhkk6RdLekTcaYcwIVI45dXHKKeqcPkiR5PR59k/lFgCMCAAAAAAAnuk5J1Bljxhlj7jbGPGuMmXfQvZCGFWtpnTG3A9wNn0skXSkp3lobIylC0sWSdkmKk/RPY0xyYEKEE4ZPmtr0fdvKZQGMBAAAAAAAwOFEnTGmtzHmPUlfSvofSbdImtHKnJ9L2mWMGebk/A4pljTWWnuJtfYta22xJFlr66y178mfrKuRFC3ppwGME8do6MTTm77vWrtGddWUvwIAAAAAgMBxLFFnjImQ9JGk70rKkTRfUuXB/ay1NZKea5j7Cqfmd4q1ttRau+4w97+WtLLhZ8bxiQqdIT4lVYn90yVJ3vp6ffPV6sAGBAAAAABAAE2bNi3dGJNx8NWrV6+xQ4YMGXn99df3z8zMDGvr+ebPfOc73xlypPnOO++8wc2fcfZtuicnV9T9QtJo+ZNYI621MyVVtNH37YbPixyc/3gqbPh0H7YXurxhk75dVUf5KwAAAAAAUlBQkE1ISPAkJCR44uPjPTU1Na6dO3eGLVy4sPekSZNOnj9/ftyRxvjss8+is7Ozg9q6n5ub6/7Pf/4T42zk3Z+TibqrJFlJt1lrS4/Qd4ukeknDHZz/uDDGBElqzO5sDGQsOHbDJn67T92ur9aovqYmgNEAAAAAABB4Y8eOrSwoKFhXUFCwrrCwcF1VVVXmm2++uT0lJaWuvr7e/OIXv0g/XBKub9++dR6Px8yfPz++rT7z58+P93g8JiUlpa5z3qJ7cjJRN0xSnaQj1g9aa62kMkmxDs5/vMySlCzJJ+nV9jxgjFnT2iXppM4MFEeW0C9NCf36S5I8dbXatZbyVwAAAAAAmgsNDbVXXHFF2SuvvPKNJFVXV7sWLFjQ5qq6adOmFUnSG2+8kdBWn9dffz2xoW9hW31ORE4m6tySvA1JuMMyxrglRamVPey6MmPMKfIfkiFJz1prNwUyHjijefnr1pXLAxgJAAAAAABd17nnnlsZERHhk6TNmze3uVfdGWecUZ6amlq3adOmiNb2tFu3bl3oxo0bI/r27Vt3zjnntLVt2gnJyUTdXknhxph+7eh7tqQQSTscnL9TGWP6SvqnpAhJayTd3d5nrbUZrV2Svu6kcHEUhjU//TXzS9XXUv4KAAAAAEBrGtdneb1e01Yfl8ulK664olCS5s2bd8jYR1XpAAAgAElEQVSqupdeeqlxNV2RMeaIC75OJE4m6v6v4fPnh+tkjAmX9IT8+9n9r4PzdxpjTLykDyUNlLRd0vcaTq9FD5CQNkBxKf78cn1tjXavywxwRAAAAAAAdD0fffRRr+rqapckDRo0qPZwfW+++eZCSXr77bfjvV5vU7vP59Pbb78d39CnoBPD7ZacTNQ9KalW0l3GmFuNMaHNbxpjXMaYC+U/FXaspFJJf3Zw/k5hjImR9IGkUZKyJJ1nrc0LbFRwkjFGw1uc/kr5KwAAAAAAjWpra83ixYujb7zxxkGS/1TY6dOnFx3umVGjRtWeeuqplbm5uSFLliyJamx/9913o3JyckJGjx5dOWbMmMMm+05EjiXqrLV7JF0v/0q5P0kqlJQgScaY1ZKKJS2RNFr+hN411tounTk1xvSSf9XfeEm58ifpsgIbFTrD0GblrzvXfCFPHYfOAAAAAABOTF999VWvxMTEMYmJiWMSEhLGREREjLviiiuGZmdnh7hcLv3+97/fM3jw4PojjXPNNdcUStJf//rXpvLXxu+N99BSm0fpdoS19m1jzFT5E3VTmt0a1+z7Skn/n7V2jZNzO62hRPcd+d+jUP4k3fbARoXO0nvAQMUm91VJbo7qa6q1e/1XGjJ+YqDDAgAAAAA47A9XX5IR6Biccuff3u2U3IrH4zGFhYWH5IxiYmK8//rXv7adddZZVe0Z58Ybbyx64IEH0t5///248vLyLEn64IMP4oKCguyNN9542BV5JyonS18lSdbaL621UyUNkTRd/kMX7pX0Y0kjrLVTukGSLkTS25LOkVQi6QJOeO3ZjDEaNmlq0+9tK5cFMBoAAAAAAALntNNOq7DWrrHWrqmqqspcsWLF5gsvvLC4tLTU/ZOf/CQ9Pz/f3Z5xevfu7T3nnHNKqqqqXAsWLIh97bXXYisrK11nn312aXJysvfII5x4HE/UNbLWfmOtXWCt/b219nFr7SvW2q2dNZ9TjDFuSYskXSipXNJF1lpOFzgBND/9defqVfLUH3EVLwAAAAAAPVp4eLidPHly9ZIlS76ZOnVq2bZt28J/9KMfDWjv8zfccEOhJC1cuDBh4cKFCc3bcCjHSl+NMcHW2p6Q2Thd0rSG78GS/mlMmycO77XWnnZcokKn6zNwsGL6JKn0QJ7qqquUtWGtBo3jf14AAAAA6Ek6q1y0p3O5XPrLX/6SNW7cuFHvvfde3JIlSyK/973vVRzpuSuuuKLsF7/4hWflypXR1lrFxMR4r7rqqtLjEXN35OSKulJjzL+NMb81xpxjjAlzcOzjqfl/kzBJSYe5eh/36NBpDi1/5fRXAAAAAAAanXLKKbUXX3xxkST9+te/Tm3PM6GhofbSSy8t8nq98vl8uuSSS4rCwsJs50bafTmZqAuTdLakByR9JKnEGPOZMeZ3xpgLGk5Q7fKstUuttaadV3qg44Wzmpe/7lj9ubyenrBIFAAAAAAAZ9xzzz25kpSZmRn57rvvRrXnmdtvvz1/5syZeTNnzsybPXv2gc6NsHtzMlE3QtJPJb0uKVtSiPxlpPdKek9SsTFmpTHmcWPMxcaYaAfnBhyRNHioonv3kSTVVlYqa+P6AEcEAAAAAEDXMWXKlOrJkyeXSdL//M//9G3PM2PHjq158cUX97344ov7MjIyajo3wu7NsUSdtXartfYla+311to0+U99vUnSa5Ky5N8Pb4KkX0p6R1KhMWa1U/MDTjDGaGizVXWUvwIAAAAA0NJdd92VJ0mff/551EcffdQtKii7i84+9fVla+0Ma+1ASemSZkhaLclIcksa21nzAx3Vovz1y8/l9XgCGA0AAAAAAF3L5ZdfXjZixIgqSfrd737XrlV1aB/HTn1tizHmFElnNVxnSkpodruqs+cHjlbfIcMUmZCoisIC1VSUa+/mDUo/hZwyAAAAAKBnW7x48W5Ju9vTd/PmzVsObrPWHvWJupdddll5R57rqRxdUWf8xhljZhtj/mmMKZT0laSnJf2X/AdOfCjpv+Xfvy7OyfkBJxiXq8Wquu2UvwIAAAAAgOPAsUSdMeZdScWSvpT0B0mXyl/iukTSXfLvTxdrrb3IWvuYtfZzay01heiSWiTqvlghn9cbwGgAAAAAAMCJwMnS14slWUnlkp6V9Kak9dZa6+AcwHGRMuwk9YqLV2VxkarLy7Rvy0b1HzUm0GEBAAAAAIAezOnDJIykaEn3Sloo6c/GmCuMMX0cngfoVMbl0tAJU5p+c/orAAAAAADobE4m6npLmibpGUnrJZ0k6RZJf5OUY4zZbIx5zhhztTEm2cF5gU4xfNLUpu/bv1ghn4/yVwAAAAAA0HkcS9RZawuttf+w1t5urR0rKVHSDyQ9Jf+BEkMl/VTSIkn7jTFfG2Oed2p+wGkpJ41QREysJKmqtET7v94c4IgAAAAAAEBP5nTpaxNrbYm19h1r7Z3W2vGS4iVdIWm1/CWywyTN7Kz5gWPlcrkpfwUAAAAAAMdNpyXqJMkYE26M+Y4x5kFJ78i/b934zpwTcNKwg8pfrc8XwGgAAAAAAEBP5uSprzLG9JJ0uqSzGq7xkoIbbzd85kv6TNJ/Gi6gy+o3YqTCo2NUXVaqyuIi7d+2Rf1OGhnosAAAAAAAQA/kWKLOGLNS0jhJ7samhs9sSZ/Kn5T71Fq7xak5gc7mcrs19LTJWv/x+5Kk7SuXk6gDAAAAAACdwsnS1wnyJ/6yJL0m6WZJQ621/ay111prXyBJh+6oefnrtlXLKX8FAAAAAACdwsnS1+mS/mOt3evgmEDA9Tt5lMKiolVTXqaKokLl7NiqlGEjAh0WAAAAAADoYRxbUWetXUCSDj2ROyhIQ8ZPavrN6a8AAAAAAKAzdOqpr0BPMXzS6U3ft61aLmttAKMBAAAAAAA9EYk6oB3SRo1RWK9ISVJ5Qb5yd24LcEQAAAAAAKCnIVEHtIM7KEiDKX8FAAAAAACdiEQd0E7DJjcrf11J+SsAAAAAAHCWk6e+Aj1a/1GnKjSil2qrKlWWn6cDu3YqadCQQIcFAAAAAIDjXnvttdjp06cPlqQpU6aULV++fHt7nquqqjLPPfdcwocffhizcePGiOLi4iCPx2Oio6O9Q4YMqZ44cWLFtddeWzxx4sTq1p43xmS0N8b8/Py1iYmJ3vb27w5I1AHtFBQcrMEZE7T5s08kSdtWLiNRBwAAAADokV599dWExu8rV66M3rlzZ/DgwYPrD/fMokWLYm6//fYB+fn5wY1toaGhNjw83FdcXBy0atWqqFWrVkU988wzfadMmVL21ltv7erbt6+ntbEiIyO9oaGhhy1lc7lcPa7UjdJX4CgMmzy16TvlrwAAAACAnig3N9e9dOnSmLCwMN/3v//9Ip/Pp3nz5iUc7pk//elPiTfccMOQ/Pz84PT09Jqnnnpq9+7du9fX1NRklpaWrq2trV3z2Wefbbnrrruye/fuXb9ixYroXbt2Bbc13iOPPLK3oKBg3eGu+Ph4n/NvH1iOJeqMMWcaYyYduWdT/wnGmDOdmh84HgaMHquQ8HBJUklejvL37ApwRAAAAAAAOGvevHkJHo/HnHfeeSU///nP8yXpjTfeaDNRt2zZsoi77767v8/n07nnnluyadOmzbfddlvhgAEDmlbgBQUFaerUqVVPPPFETlZW1oZbb701JyQkhNUvB3FyRd1SSYuPov/fJP3bwfmBThcUEqJB4yY0/eb0VwAAAABAT/P6668nSNJ1111X9N3vfreib9++dbt27Qr75JNPIlrrf99996XU19eblJSUusWLF++KiIg4bAIuLCzMPv3009njx4+v6Yz4uzOnS19NJ/cHAq5l+esyyl8BAAAAAD3G6tWrwzZt2hQRGxvrufzyy8tcLpcuu+yyIkmaP39+4sH9d+zYEfzpp5/GSNJPfvKTvJiYmB5Xjno8BXKPuihJdQGcH+iQ9DHjFBwaJkkqztmvgr17AhwRAAAAAADOmDt3bqIkfe973ytuPMxhxowZRZL0zjvvxNfU1LRYdPXhhx9GNX6//PLLS49nrD1RQBJ1xpgJkuIl7Q/E/MCxCA4J1aBxpzX9pvwVAAAAANATeDwevf322/GSdMMNNxQ1tk+YMKF66NCh1aWlpe433ngjpvkzW7ZsCZf8p7uOGjWq1qlY7rvvvrTExMQxbV1XXHFFulNzdSUdTtQZY35kjPl349XQHN+8rZXrE2PMV5I+k2QlvefESwDH28HlrwAAAAAAdHdvv/12dH5+fnBKSkrd+eefX9H83pVXXlkkSa+++mqL8teioiK3JEVFRXlcrtbTTHfffXdya8m2G2+8Ma2tWCoqKtyFhYVBbV0lJSXuY37hLijoGJ5Nl3T2QW0hrbS15VNJvz6G+YGAGXhqhoJCQ+WprVXR/r0q3JelhH79Ax0WAAAAAOAI9t3zWUagY3BKv8fOWOPkeI1JuMsuu6zo4KTbjBkzih599NHUTz/9NDo7OzsoJSXF095xy8vL3YWFhYfkoMrKytpMtj399NO7b7311sKjCL9HOJbS139KurHh+nFDW2mzttauH0m6XNIwa+3Z1triY5gfCJjg0DANOnV802/KXwEAAAAA3VlhYaH7o48+ipWkH/3oR0UH3x86dGhdRkZGhdfrNfPmzYtvbI+Pj/dKUnl5eZDP1/o5EnPmzNlvrV3TeF166aWHjA+/Dq+os9auk7Su8bcxZr6kamvtX50IDOjqhk2eqm2r/Am6bSuXafIV1wQ4IgAAAAAAOubll1+Oq62tNZI0ceLEkw/X9/XXX0944IEHDkjSiBEjqiWptrbWbNy4MfSUU05xbJ+6E9GxlL62YK0N5AmywHE3cOx4BQWHyFNfp4K9e1S4f68SUtssrwcAAAAAdAFOl4v2FIsWLUo8ci+/LVu2RHzxxRfhEyZMqL7gggvKG9v/8Y9/xJxyyikHOifCEwPJNaCDQsLClX7qt1sbbF+1IoDRAAAAAADQMRs3bgz96quveknSihUrNufn569t6zrnnHNKJWnu3LkJkjRkyJD6M888s1SSXnzxxaTS0lJyTcegU/7jGWPSjDEXGmOuMcZMP9zVGfMDxwunvwIAAAAAuruXXnopQZKGDx9ePXny5OrExERvW9e0adOKJOkf//hHvMfjP0/ikUceyQ4ODrbZ2dkh06ZNG1hVVWUC+DrdmqOJOmPMRGPMSkm7JS2RtEDSy0e4gG5r0NjT5A4OliTl79ml4pz9AY4IAAAAAID28/l8euuttxIk6ZJLLjnioZ9XX311aVBQkC0oKAhevHhxjCRNnTq16vHHH89yuVz6+OOPY0eOHHnyU089lbBnz57g5vNs2rQp9IEHHkj69NNPozvvjbo3x/aoM8ZkSPq3pDBJRtI+Sfsl1Tg1B9DVhEZEKH3MOO1cvUqStG3VCk287MoARwUAAAAAQPssWbIkKjs7O0SSfvjDHx4xUZeYmOidNGlS+bJly6JfffXVhKuvvrpUkmbPnl2QlJRUf9tttw3YvXt32OzZs9Nnz56t0NBQGx4e7q2qqnLX1dU1rbQ788wzS3/961/ntDXPfffdl/bQQw/1O1wsr7/++o7zzz+/sv1v2/U5lqiT9FtJ4ZI2SLrRWpvp4NhAlzVs0tRvE3Url5GoAwAAAAB0G6+88kqCJA0YMKB2/Pjx7VpsddlllxUvW7Ys+qOPPootKChwJyYmeiXp2muvLb300ks3vPDCCwkffPBBzKZNmyKKioqCKisr3TExMZ6BAwfWTpw4sWLGjBmFGRkZh52roqLCXVFRcdg4amtre9x+eE4m6qZIspKus9ZudHBcoEsbnDFBLneQfF6PDuzaqZK8XMUmJQc6LAAAAAAAjmjx4sW75d/CrN3uvPPOgjvvvLOgtXuRkZH2cPePxFp7Qp/K62TmMUxSBUk6nGhCI3opfczYpt/bVy0PYDQAAAAAAKC7cjJRt0NSqDHGyVV6QLcwbBKnvwIAAAAAgGPjZKLuZUkhkn7g4JhAtzA4Y6JcbrckKXfndpXlHwhwRAAAAAAAoLtxMlH3jKQPJD1vjJns4LhAlxcWGan+o09t+r2N8lcAAAAAAHCUnCxTvV/Sl5ImSlpmjPms4Xf54R6y1j7kYAxAwAybeLp2r/Xveblt5TKNv+TyAEcEAAAAAAC6EycTdb+V/9RX0/D7TElnHKa/aehPog49wpDTJun/XnpW1udTzvatKivIV3Ri70CHBQAAAAAAugknE3Wvyp94A05I4VHR6j9qjPas/0qStOOLFRp3MVs2AgAAAACA9nEsUWetneHUWEB3NWzi6U2Juq0rl5OoAwAAAAAA7ebkYRLACW/IhMkyxv/XKnvrZpUXFQQ4IgAAAAAAcLxYe2zFpiTqAAdFRMcobeSopt87vvg8gNEAAAAAwAmlXpL1+XzmiD2BTmKtbTyTwdOR5x1P1BljBhpjnjHGbDHGVBhjPAfdjzXG/NoY84Axxu30/ECgDZ04ten7tpXLAxgJAAAAAJxQcqy1tVVVVeGBDgQnrpqamhBrbb2k/I4872iizhhzuaT1kmZJGi4pQt+eAitJstaWSDpH/lNiz3NyfqArGDphsmT8f+z3fb1JlSXFAY4IAAAAAE4IS71eb1lRUVHcsZYfAh1VVlYW5fP5KiV92ZHnHUvUGWNOkrRQUi9Jz0s6Q1JbG3S9KH8Cb5pT8wNdRa/YOPUbMdL/w1ptp/wVAAAAAI6H//V4PAfKysqC9+7dm1pRURHh8/kMSTt0NmutPB6Pq6CgIK6wsDDO4/EUSvq4I2M5duqrpLskhUl60lr7K0kyxnjb6PtRw+fpDs4PdBnDJp6ufZs3SpK2rVymUy+4OMARAQAAAEDPlpGRsWPNmjV31NbW/rG4uLhPWVlZkjEmVAdV+gGdxOfz+So9Hs9ea+1fMzIyOrQXlpOJunPl3yzv90fqaK3NN8ZUSEpzcH6gyxg6YYr+/cqLkrXau2m95t02U/Ep/RSfmub/TOmn+NR+Co+KDnSoAAAAANBjZGRkLF+zZs21Ho/nYo/Hc46kZEkhgY4LJ4RaSV9LekvShx0dxMlEXbKkcmttezfLq5e/TBbocSLjE5Q6/GTt/3qTJKkkN0cluTn6JrNliXp4VLTimiXuGj9jeifJ5easFQAAAAA4WhkZGTsl/bnhAroVJxN1lZKijTFB1trDHkFrjImTFCspz8H5gS7l7Btu0vvPPaXC/XulNvZEqC4vU/XWzcreurlFuzsoSLHJKd8m7xquuJR+Co2IOB7hAwAAAACA48zJRN0m+fecmyBpxRH63iB/jfgaB+cHupTkIcM04w9zVF9bo+KcbBVl71PR/n3+z+x9Ks7eL09dbavPej0eFe7LUuG+rEPuRcbFKz61n+JS0hSfktq0Ci8qPlHG5ehBzgAAAAAA4DhyMlH3d0lTJf3OGHNBW6vqjDFnSfof+fezW+jg/ECXFBwapj7pg9QnfVCLduvzqbyo4NvkXbMkXmVxUZvjVRQXqaK4SFkb17doDwoNVXzfliW0cX1TFZeSquCQ0E55NwAAAAAA4BwnE3UvSLpZ0lmSPjPGzJEULEnGmJGSRkr6L0nTJLklLZP0NwfnB7oV43IpOrGPohP7KH3MuBb3aquqVJz9beKuMYlXnJMtn7f1ynJPba0O7N6pA7t3HjSRUXRin5ZltA3fI2JiZQwHIAEAAAAA0BU4lqiz1tYbYy6U9P8kTZS/BLZR86U/RtJKSf9lbRsbdwEnuNCICCUPGabkIcNatPu8XpXm5x26Cm//XtVUlLc+mLUqy89TWX6edq9tWW0eGtHr29V3zRJ4sUl95Q5yMo8PAAAAAACOxNF/iVtrc40xUyTNkPQjSafp22OQvZJWS3pF0rwjHTgB4FAut1txySmKS07R4IwJLe5VlZU27X3XmLwryt6n0rw8Wetrdbzaqkrl7NiqnB1bD5knpk9yK6vw0hQWGdlp7wcAAAAAwInM8SUzDQm4uZLmGmPckuIluSQVkpwDOk9EdIwiomPU76SRLdo99fUqyf32MIvmJbV11dWtjuXzelWcs1/FOfu1U6tazhMTq7i+qS32wotPSVN0795yudyd9n4AAAAAAPR0nVrbZq31SsrvzDkAHF5QcLAS0wYoMW1Ai3ZrrSqLiw45yKIoe5/KC9r+a1tVWqKq0hLt/3pTi3Z3cLA/gZfSr9lptGmKS0lVSFh4p7wbAAAAAAA9CZtQAScoY4wi4xMUGZ+g/qPGtLhXX1Ojopz9LQ+y2L9XxTnZ8tTXtTqet75eBVm7VZC1+5B7kQmJ35bQpqQqPiVN8an9FBmfwGEWAAAAAAA06FCizhhzZsPXKmvt6oPajoq19tOOPAeg8wSHhSlp4GAlDRzcot36fCoryG+WwNvb9L2qtKTN8SoKC1RRWKCsDWsPmif829V3zQ61iEtOUVBISBujAQAAAADQM3V0Rd1SSVbSVkknH9R2NOwxxADgODMul2L6JCmmT5IGnprR4l5NZcUhB1kU7d+nkrwc+bzeVserr6lW3jc7lPfNjoMmMorpk3TQQRb+UtrwqGhW4QEAAAAAeqSOJsmy5E+yZbfSBuAEFNYrUn2HDlffocNbtHs9HpUeyGuZwGv4XltZ2fpg1qo0L1elebna9dXqQ+aJa3EabZriU/oppk+S3EHk/QEAAAAA3VeH/lVrrU1vTxsAuIOCGspbU6XxE5varbWqLiv1l9DmtDzQovRAnmRbz/vXVFYoZ9vXytn2dYt2lztIsUnJLVbfxaf0U1xKqsJ6RXbqOwIAAAAA4ASWnwAICGOMImJiFRETq34nj2pxz1NXp+Lc7KZ98L4tqd2n+tqaVsfzeT1Nib6D9YqNa0raNR5kEZ/ST9GJvWVcrk55PwAAAAAAjhaJOgBdTlBIiHr3T1fv/ukt2q21qigqPOQgi6Kc/aooLGhzvMqSYlWWFGvv5g0t5wkOaUje+Q+xaFqN1zdVwWFhnfFqAAAAAAC0ybFEnTEmXtIlkoqtte8coe+lkmIl/T9rbdtHRQJAM8YYRSUkKiohUQNOObXFvbrqKhXnZLc4yKIoe5+Kc7Plra9vdTxPfZ3y9+xS/p5dh9yLSuz97UEWfb9N4vWKi+cwCwAAAABAp3ByRd10SX+Q9JCkwybqJJ0pabak2yQ962AMAE5QIeERSho0REmDhrRo9/m8KsvP96/Aa9wHr+Gzuqy0zfHKC/JVXpCvPeu/Omie8EMOsohLSVVscoqCgoM75d0AAAAAACcGJxN1lzd8vtmOvn+VdIek/xKJOgCdyOVyKzYpWbFJyRo09rQW96orylWc3fIgi6L9+1SSlyPr87U6Xl11tXJ3blfuzu0t2o1xKSYpqUUCr3FFXnhUdKe9HwAAAACg53AyUTdYkk/Stnb0/bqh75AjdQSAzhIeGaXwYSOUMmxEi3avp14lublNp9E2T+bVVlW2Opa1PpXk5qgkN0ffZH7Z4l5YVHSLxF3jZ0zvJLnc7k57PwAAAABA9+Jkoi5RUpm11nOkjtbaemNMqaQ+Ds4PAI5wBwUroV+aEvqlSc0W4VlrVVVa0rAP3v4Wq/DKCg5I1rY6Xk15mbK3blb21s0HzROk2OSUlgm8hoMtQiMiOvMVAQAAAABdkJOJumJJvY0x0dbassN1NMbESIqRVOjg/ADQqYwx6hUbp16xcUobeUqLe/W1Nf7DLLL3qbgxibd/n4py9slTW9vqeF6PR4X7slS4L+uQe5Fx8YpP7ae4vi1X4UXFJ8q4XJ3yfgAAAACAwHIyUbdG0kWSbpD0lyP0vUGSS9JaB+cHgIAJDg1Tn/RB6pM+qEW79flUXlTQ4iCL4oaS2oriojbHqyguUkVxkbI2rm/RHhQa2nQKbVzf1KYkXlxKqoJDQjvl3QAAAAAAx4eTibrXJF0s6XFjzDZr7f+11skYc4GkxyTZhmfQhXlLSuSKiZExJtChAN2ScbkUndhH0Yl9lD5mXIt7tVVV/v3vslueRlucky2ft/VdBDy1tTqwe6cO7N550ERG0Yl9WpTQxqekKj41TRExsfwdBgAAAIBuwLFEnbX2b8aYmyWdK+k9Y8z7kt6T1FjTNUD+RN4F8q+mW2qtXeDU/HCW9XpV/Pobyn/qKaU89qiizjsv0CEBPU5oRISShwxT8pBhLdp9Xq9K8/NarMJrTObVlLexs4C1KsvPU1l+nnavXXPQPL2aSmfjGvfD69tPscnJcgcFd9brAQAAAACOkrFtbH7eocGMiZa0SP6EnORfNdeiS8Pne5KutdaWOjZ5N2SMWTNu3Lhxa9asOXLn46zgueeU//QzkqSglL4a/O67crG5PRBwVWWl3+6Bl72v4WCLfSrNy5O1vqMay7hcik3q23IVXkMyLzwyqpPeAAAA4MSRkZGhzMzMTGttRqBjAdA9OFn6qoZDJC4xxlwkabqkSZKSGm7nSVop6VVr7XtOzus0Y0yUpHPkP+9xfMNnQsPtEdbarwMV2/ESd801Knr1NXmLi+XJzlHBc8+rz513BDos4IQXER2jiOgYpZ50cot2T329SnKzmx1ksbcpmVdXXd3qWNbnU3HOfhXn7NdOrWpxLzw6puVptKn9FJ+SpujeveVyuTvt/QAAAADgROZooq5RQyKuSyfjjuBcSf8IdBCB5I6NVZ9f/lI5990nSSp85RXFXPYDhQ4eHODIALQmKDhYiWkDlJg2oEW7tVaVxUUNSbv9Ksre21RKW16Q3+Z41WWl2l9Wqv1fb2rR7g4O9h9i0ewgi/jUNMWlpCokLLxT3g0AAAAAThSdkqjrIQ5IWi3pS0n7Jb0Y2HCOv5jLL1PJ4sWqzsyU6uuV+9DD6v/Ky2xKD3QjxhhFxicoMj5B/UeNaXGvvqZGRTn7vz2NtmEFXnH2fnnq61odz1tfr4Ks3SrI2n3IvciExG8PsUjxr8CLT+2nyPgE/n8DAAAAANqBRDDKpOoAACAASURBVF3r3rHW/rPxhzEmPXChBI5xuZT8m19r139Nk7xeVa1apbJ3lyjm+5cEOjQADggOC1PSwMFKGthypaz1+VRWkN/sIIu9TQm8ypLiNserKCxQRWGBsjasPWie8KbkXVxKalMCLy45RUEhIZ3ybgAAAADQHXUoUff/s3fncZKkdZ34P09E5F2VR3V33T0X49yMMOOIrj8F9YcrKIgcu7qIq+su/BZlOEYFAQFdERjlmGF1ddabBXVBdFmV9UBEWUVgBmYcEGaYs+vs6rozI+N+fn9EZGZEZmRVZWVkZVbV5/16xauynsyKfLJtme5Pf5/vVwjxw8HDbSnl/2pb64mU8vcO83ODJKV0h72HUZG99lpM/NAPYeN3fxcAsHrnuzD2rGdCHWejeaKTSigKSpNTKE1O4cqnRfseG7VqZx+8xQVsrS7Dc+P/p9M26lh99GtYffRrbW8kUJqcigyymJjxv+aKJVbhERERERHRqXOoqa9CCA/+RNevSilvaFvriZRy5LuSBxV1jwXfJjZMYpSnvoa51Soefe73wLl4EQBQednLMP2mNw55V0Q0SlzHwfbF1Y5BFpuLCzBq1Z7vly2MoRKZRnseE7NzKE1OQ9VYDE5ERETHA6e+ElGvDvu3nb+DH8o9GbNGJ4w6NoapN7wei6+7AwCw+cEPovzC70f2+uuHvDMiGhWqpgXHW+eAb3hGc11KifrOdjO4awyy2FhawPbFVaDLPxYZtSqWH/oKlh+K/ruIoqooT81EBlk0jtRmC2MD/YxERERERESDdqigTkr5rIOskU8I0a1k7roj3Ugfxp/zHBQ+8hHU/uEfAc/Dytt+Dpf//ocgFGXYWyOiESaEQL5URr5Uxvz1N0WecywLmytL/hCLUIC3sbgA2zRi7+e5bvN17QrlStADrzXIYmJ2HsWz5/i/VUREREREdCwctkfdWwDsSinfm/B+aEQJITD15p/Fo9/3fYBto37//dj+6EdRfvGLh701IjqmtHQa5y67AucuuyKyLqVEdWPdD++WoyFedf1S1/vVtjZR29rEwpcfjL5PKo3K7Bwq4V54s/OYmJlDKpsdxEcjIiIiIiI6lH561K1IKWdDa48BWJVSflOC+xsJp71HXdjF970P67/26wAAtVzGVR//c2iVypB3RUSnhVXXsbm8FOqD5w+22FxehGvbPd9v/Oy5Vh+8UIhXqExwmAURERH1jT3qiKhXh+1RJwG0nyO6HECmv+3QqDv7ildg52P/G/bSEtytLVz85V/GzC/8Av9CS0RHIp3LY+qqqzF11dWRdc9zsbO2ho2lC80KvMZ0Wn17q+v9di+tYffSGp544Att75OLDLJoHKktT89CS6UG8tmIiIiIiIgOG9RtADgjhBiXUu4muSEabUouh6k3vxkLr3wlAGD7jz4KuB6m3/ZWKDxCRkRDoigqylPTKE9N46qn3xZ5rl7dje2Dt7W6DOl5sfez6nWsPPIwVh55OLIuhILS1FTHIIuJ2Xnki6WBfT4iIiIiIjodDhvUfQbAcwF8TAjxYQDVYD0nhPjhXm4kpfy9Q+6BhmT8O74d489+Nnb/6q8AANt/8icwvvpVzN99F9Lnzw95d0REUbmxceSuuR6z10QnVbuOja3VlWZwFw7zTL0Wey8pPWytLGNrZRmP3ve5yHPZ8WLHEdqJ2TmUJqehqOrAPh8REREREZ0ch+1RdxuATwLIwz8GCwAi9PjApJQj/7cX9qjr5BkGVn7u57H9x3/cXFOKRcz90p0Ye+Yzh7gzIqL+SCmhb281A7xwFd7OpYtAj//dVFQNlZnZtgBvHpXZeWTy+QF9CiIiIhoF7FFHRL06VEWdlPJzQoinAXg5gBsB5AA8C4AN4B8T2x2NLCWbxcwvvh25r/96rL797ZC2DW9nBxde8f/h7CtfibM//koIVpAQ0TEkhEChXEGhXMH5G54aec42DWwuL2FzebEV4gXTaR3TjL2f5zpYX3gS6wtPdjxXqEx0VuHNzWN84iyE0t4KloiIiIiITrpDVdTF3ihmEuxxJoQ4G/r2PID7gsffDOBroec2pJTxTY72f49jW1EXVn/gASy8+jVwlpeba4Vv/VbM/dKdUMvlIe6MiOhoSM/D7salUAXeIjaDwRbVzY2e76dlMpiYafW/a4R4ldk5pNKc20RERHRcsKKOiHp12KOvlwFwpZSLobXHAFyUUj4jwf0NjRDioL8wV0opHz/ke5yIoA4AnI0NLN5xB/R//ExzLTU3h7m770LuxhuHuDMiouEydd3vf7fUNsxiZQmu4/R2MyFQPDvpB3czc6EqvPPIl8qcwE1ERDRiGNQRUa8OO0zicQDLAOZCa78DgBNgTyltYgKX/cZvYO2uu7F+zz0AAHtxEU/84L/D9FvfivKLXjjkHRIRDUcmn8f01ddg+uprIuue62J7bTVyhHZz2f9a392Jv5mU2Flbxc7aKh7/YvQfeTL5QrP6rhIMspiYPY/y9DRULTWoj0dERERERAk6bEVdxzHXYG1ZSjnX/Scp7CRV1IXtfuITWHr9G+BVq8218ktegqk3vwlKhke2iIj2o+9sY3NpMVSBdwEbSwvYXl1Fr90WhKKgPDXTMchiYm4eubHxAX0CIiIiAlhRR0S9O2xQVwMAKWUhtHaietQdhZMa1AGA9fjjWHjV7TAffri5lr3pJszf9T6k5pjlEhEdhmPb2F5dDlXhXWiGeVa93vP9csVSxyCLiZl5FCcnoSgcCERERNQvBnVE1KvDHn19CMDNQojbAfyGlFJPcE90AqSvuAJX/OEfYPktb8XOn/4pAMB48EE89qIXY/bdv4yxb/mWIe+QiOj40VIpnJm/DGfmL4usSylR29zARrMK70IzzNu9tNb1fvWdbSzubGPxK1+KrKupFCrTs20h3nlUZueQzuYG8tmIiIiIiOjwFXU/AeBuAOEfFm3fH4SUUh42LDz2TnJFXYOUEpv/44NYfde7gEbTdEXBudtvx5mX/ycIRRnuBomITjjbMLCxvNgaaBEEeJtLi3Bsq+f7jU2ciQZ4s+cxMTePsYkzHGZBRETUhhV1RNSrQwV1ACCEeBOA2wGc62cDUspTm9SchqCuQb/vPiy++jVw1lqVHWPf8R2Yfec7oBaLQ9wZEdHpJD0PO5fWOgZZbCwtoLa12fP9UpmsP8iiOY3WD/Aq07PQ0ukBfAIiIqLRx6COiHp16KCueQMhzgHIA3gMwBqAb+zl56WUT/S1gWPsNAV1AOCsrWHxta+D/vnPN9dSl1+G+bvfj+y11+zxk0REdJSMWrU1zGLxQvNI7dbKEjzX7e1mQqA0OdUcZNG85uaRK5ZYhUdERCcagzoi6lXfQV3zRhwm0bPTFtQBgLRtXHz3e7DxO7/TXBPZLGb+y8+j9LznDW9jRES0L9dxsH1xNTLIYnNpERuLF2DUqvvfoE22MIbKXGeAV5qchqqd2s4YRER0gjCoI6JeJRnUPROAJaX8x0RueAqcxqCuYefjH8fSm94MqbfmkFRe+lJMvf6nIXhEiojoWJFSor6705pC25hKu7SAnYsXIaXX0/0UVUV5aiY6yCI4UpstjA3oUxARESWPQR0R9Sqxf66WUn4qqXvRyVd8znOQ+bqvw8Krbof12GMAgM0PfhDGl76Eubveh9TU1JB3SEREByWEQL5YQr5Ywvz1N0WecywLWytLHQHexuICbNOIvZ/nus3XtcuXyh2DLCZm51E8e44DioiIiIjo2Eusoq55QyGuBPBaAM8GcB5ANjzZVQhRhj+EQgL4RSllj81uTo7TXFHX4FarWH7jm7D7l3/ZXFPPnMHce96DwjN6andIRETHiJQS1Y31SHDXeFxdv9Tz/bRUGpWZWVTmzken0s7MIZXNDuATEBER7Y8VdUTUq0SDOiHE9wP4PfjDJRrdoaWUUm173ScBfBuA50op/yKxDRwzDOp8Ukps/NZv4+K73w14wfEoVcXkHXdg4kd/hI3GiYhOGauuY3N5yT9Ku7zYDPE2lxfh2nbP9xs/cy5UhdcK8QqVCf43hoiIBopBHRH1KrGjr0KI6wB8EEAWwH8D8CEAfwzgTMzL7wHwTAAvAnBqgzryCSFw5sf+A7I33ojFO+6Au74OuC4u3nkn6vffj5m3vx3qWGHY2yQioiOSzuUxddXVmLrq6si657nYWVvDxtIFbCwutCbTLi1A397qer/d9TXsrq/hiQe+0PY+OUzMzqPSFuCVp2ehpVID+WxERERERHtJcqTaT8EP6X5ZSvnTACCE6Has9a+Dr9+S4PvTMVf4pmfgyo/+ERZf/RrUv/hFAMDuX/wFzIcfxvz770bmKU8Z8g6JiGiYFEVFeWoa5alpXPX02yLP1au72IwcofVDvK2VJUgvfpiFVa9j5ZGHsfLIw5F1IRSUpqY6BllMzM4jXywN7PMRERERESU59fVx+D3ppqWUa8HaMoDJ9qOvwXM7ACClLCaygWOIR1/jScvC6rvuxOYHP9hcU/J5zPzi21H87u8e4s6IiOi4cR0bW6srzT544TDP1Gs93y87Xmw7QjuHidl5lCanoagdf9whIqJTjkdfiahXSQZ1BgBDSlkOre0V1K0DKEgpT22HZwZ1e9v+2Mew/Ja3QhqtqYATP/qjmLzjdRBaksWgRER02kgpoW9vxU6j3bl0Eejxz0eKqqEyMxs5QlsJQrxMnu0biIhOKwZ1RNSrJNOOGoCiEEKTUjp7vVAIUQFQBrCa4PvTCVN6/vORufZaLLzqdthPPgkA2Pjt34bx4IOYe+97oJ09O+QdEhHRcSWEQKFcQaFcwfkbnhp5zrZMbC0vRUO8xQVsLC/AMc3Y+3mug/WFJ7G+8GTHc4XKRMcgi4m5eYxPnIVQlIF8PiIiIiI6npIM6r4Ev+fcNwL4h31e+zL4U2FZSkZ7yl57La78yIex9Po3oPrJTwIA9M99Do+98EWYe9/7kL/l6UPeIRERnTSpdAbnLr8S5y6/MrIuPQ+7G+uRAG8zGGxR3dzoer/a5gZqmxu48KUHIutaOtOsuotU4s3MIpU5tQcOiIiIiE61JI++/gSAuwH8LYDvklI6cUdfhRDPBPBnAHIAXiql/INENnAM8ejrwUnPw/o992Dtrrtbx5E0DVNveAMqL/13EEIMd4NERHSqmbru979rDrLwA7ytlSW4zp4HDToJgeLZczFVeOeRL5X53zwiomOER1+JqFdJBnUpAJ8D8FQAnwXwqwDeC6AC4GYANwJ4IYAXAVABfBrAM2VSGziGGNT1rvrp/4ulO+6Au73dXCs+73mY+bm3Qcnnh7gzIiKiTp7rYnttNVSB1zpKW9/d6fl+mXyhGd61ptGeR3l6GqqWGsAnICKifjCoI6JeJRbUAYAQYhrAxwB8A4BuNxYAPgPg+VLKS4m9+THEoO5w7MVFLLz6NTAefLC5lvm6r8P8++9G+oorhrcxIiKiHug729hcWmwNsgiCvK2VFUjp9XQvoSgoT820DbI4j4m5eeTGxgf0CYiIaD8M6oioV4kGdQAghNAA/AiAfw/gNgDp4CkXwOcB/A6A39xv4MRpwKDu8DzTxOovvB1bH/5wc00ZG8Psu96J8e/8ziHujIiIqD+ObWN7dTk0yOJCM8iz6vWe75crlqJHaIOrODkJRVH3vwERER0agzoi6lXiQV3k5kKoACYAKADWGc5FMajr39ZHPoKVn/8vkJbVXDvzilfg3O2vglD5lw8iIjo5pJSobW22ArygD97G0gJ2L631fD81lUJlerajD15lZhbpHNtJEBElgUEdEfUqyamvHaSULoDe/+RIdEDlF78Ymeuux+Ltt8NeWgIArP/6r8P45wcw++53Q6tUhrxDIiKiZAghMFaZwFhlApfddHPkOdswsLmy1Kq+a/bEW4RjW7H3c20bly48gUsXnuh4bmziTFsVnn+MdmziDIdZEBEREQ3QoCvqcgDOBt9eklL2fl7jBGNFXXKczU0s/dRPo/bpTzfXtJkZzN/1PuRuvnmPnyQiIjq5pOdhd/1S5PhsI8SrbW32fL9UJhv0v5tvDrKYmJtHZXoWWjq9/w2IiE4ZVtQRUa8G0aNuAsDtAP4NgGvgD48A/OESDwH4QwB3Syl7/9PhCcOgLlnSdXHpV34Vl371V5trIpXC1JvfjPK/eQkrAIiIiEKMWjU6zCII8LZWluC5bm83EwKlySlMhCbRNsK8XLHE/wYT0anFoI6IepX01NdvBPAnAKbQCujaSQArAL5fSvnZxN78GGJQNxi7n/wkll7/Bng7O8210gtfiOm3/CyUbHaIOyMiIhp9ruNg++Jqc5DF5vKiH+ItXoBRq/Z8v2xhDJW2QRYTc/MoTU5D1QbahYWIaOgY1BFRrxIL6oQQUwC+DKACYBPArwH4GwALwUvmAXwngFcEr1kHcJOUcjWRDRxDDOoGx3rySSzc/mqYX/lKcy1zw/WYv/tupOfnh7gzIiKi40lKifruTmwfvO2Lq5DS6+l+iqqiPDXT7INXCYV42cLYgD4FEdHRYlBHRL1KMqh7N4DXAngAwHdJKS92ed0UgL8EcBOA90opfzKRDRxDDOoGy6vXsfK2t2H7f32suaaUSpj7pTsx9m3fNsSdERERnSyOZWFrZSkS4PnXImyj9xbF+VI5Oshi1j9SWzw7CaEoA/gERESDwaCOiHqVZFD3FQBfB+A2KeV9+7z2VgCfA/CQlPK6RDZwDDGoGzwpJbb+4A+w8ovvAGzbXxQCZ3/ix3H2P/9n/mGfiIhogKSUqG6ut8K7UIhXXb/U8/20VBqVmVlU5s5Hp9LOzCHF9hZENIIY1BFRr5IM6nQAlpSyfMDXbwNISSnziWzgGGJQd3TqX/wiFl79GjirrZPWhWd+G+buvBNqqTTEnREREZ1OllGPHWaxubwIt/GPaz0YP3MuVIXXCvEKlQkOsyCioWFQR0S9SjKo2wKQBlCQ+9xUCKEAqKKHYO8kYlB3tJz1dSy+7g7o//RPzbXU/Dzm774L2RtuGOLOiIiIqMHzXOysrWFzqbMKT9/e6vl+6VwOlZlQ9V3wtTw9Cy2VGsAnICJqYVBHRL1KMqj7DIDbALxESvnRfV77IgAfBvA5KeUzEtnAMcSg7uhJx8HaXXdh/b//RnNNZDKYftvbUP7+FwxxZ0RERLSfenU3CPAWIyHe1soSpNfbMAshFJQmpzAxFx1kMTE7j3yR1fZElAwGdUTUKy3Be/1PAN8I4B4hxK6U8q/iXiSEeD6AewBIAL+f4PsT7UtoGibvuAPZpz4Vyz/zRni1GqRpYvlnfgb1+7+IqTe+EUo6PextEhERUYzc2Dhy11yP2Wuuj6y7jo2t1ZVmeOcfqb2AjcUFmHot9l5SethaXcbW6jJw3+ciz2XHi8ER2rlIgFeanIaiqgP7fERERERJVtSlAXwGwNPgh3CfB/BJAIsAMgAuB/BMADcCEAC+AOCbpZRWIhs4hlhRN1zmo49h4fZXwfraI8217M03Y/6u9yE1MzPEnREREVESpJTQt7c6jtBuLi1ge+0i0OOfgxVVQ2VmthneVWbmmiFeJl8Y0KcgouOMFXVE1KvEgjoAEEKcBfABAP86WGq/eaOT7/8B8MNSyt7HfZ0gDOqGz6vVsPyzP4udP/94c02tVDD3nnej8M3fPMSdERER0SDZlomt5aVoiLe4gI3lBTim2fP9CpWJjkEWE7PzGD9zllPmiU4xBnVE1KtEg7rmTYX4fwC8GMAtAM4Fy2sA7gPwESnlpxN/02OIQd1okFJi8wMfwOqdvwQ4jr+oKDj3mtfgzH/6j5wUR0REdIpIz8Puxnp0Em1wjLa6udHz/bR0BpXGEdpQiFeZmUUqkx3AJyCiUcKgjoh6NZCgjg6GQd1o0T//eSy89rVw11qFnmP/73di9h3vgDo+PsSdERER0SgwdR2by+FBFn6At7WyBLfxj309KJ6b7KzCmzuPfKnMfygkOiEY1BFRrxjUDdGxDupql4AvfACwaoCaAdQUoKZbX7XwWvu132tSwJD+cGpfvIjF174O9dD/TdKXX46599+N7DXXDGVPRERENNo818X22qo/xGLxQrMX3sbiAuq7Oz3fL53LR47P+o/Pozw9DVVLDeATENGgMKgjol71FdQJIZ4F4NsA7Eop33vAn3kdgDEAf3Paj8Ae26BOSuC3nws8+Q+Dew+lEea1B3zt4V4qCPzS3UO/2FAw5l7Be0mp4OJvfAQbf9TqWyeyWcz87OtR+t7v8V+rpAD2myEiIqJ96DvbfoC3HD5Ku4CtlRVI6fV0L6EoKE/NtI7SBgHexNw8cmOs/icaRQzqiKhXhw7qhBBZAF8DMAPg30opP3LAn3sJgD8E8BiA66SU9qE2cAIc26Dua38N/I8XDXsXA7f9RBbLny1Duq1ArnJNFVNP24FQAChafDDYHgqm8kBmHMiMAZmi/zg9FqyFruZa0X+tlhnehyciIqKBcmwb26vLkWm0jSo8q673fL9csdQK72bmMDF3HhOz8yhOTkJR1AF8AiI6CAZ1RNQrrY+ffRGAWQCfPGhIBwBSyg8LIV4JvxLv+wH8zz72QEdNSuBv39X6/qpnAfO3AY4JuDbgWsFlA27bmmO1PW+1XbZ/H280stvS5Qay5UtY+PQErF3//1U2HxqDsZHC3LdsIpVzAM8B7N7/MH0garozvDtoyNf+OpXHZIiIiEaJlkrhzPxlODN/WWRdSona1mYowPP74G0uL2Jn7WLX+9V3trG4s43Fr3wpsq6mUqhMzzZDvErjOO3sHNK5/EA+GxERER1eP0HdCwBIAP/1ED/7fgDPhB/2Mag7Th79JLDwWf+xmga+71eA0nyy7yFl9yDPtfYIBbu9pvG19+AwM2HiimkLy3/jYPcJv29e/VIGj/3FOcz/q03kJ61kP3uYawH1Df/ql5ZtC/VCgV6va/xXeSIiooERQmCsMoGxygQuu+nmyHO2YWBzZanVB69xlHZ5CY5lxt7PtW1cuvAELl14ouO5sYkz0UEWs+dRmZ3D+JmzHGZBREQ0JP0EdY3S3b8+xM82fuYb+nh/OmpSAn/7ztb3T39Z8iEd4A+S0IKecSNABTD30xIbv/mbuPie9wKeB9dQ8cSnpjD5utsx8QMvgvCc7hWCtg6YO4BZBcxd/7Kqe6wF33u9T4/ryjH8q7bW/71ShR5CvvFQhV+4CnDMvw/7/BERER1YKpvF5BVXYfKKqyLr0vOwu36pY5DFxtICalubXe9X3VhHdWMdTz54f/R9MtnYPniV6Vlo6dH48xkREdFJ1U+PuioAR0pZPuTPbwNQpZRjh9rACXDsetQ98kngAy/wHysp4PYvAOXzw93TEat95jNYfN0dcDdaVW7jz/luzP7CL0ApFJJ7Iyn9kC8S3lVjAr3G2m4r4It7XY/Nqo+GaDvGO7ZHyBezlim2fj6VG9qkYCIiolFm6rVIcNf4urWyDM/t8R8FhUDp3GQ0wAse54olVuERxWCPOiLqVT8VdQJAP+UwIrjoOGivprvlZacupAOAwjd9E678o49g4TWvgXH/AwCA3Y//Hzz20MOYf//dyFx11T53OCAhgFTWvwpn+7uXlIBd7x7ymTvB+n5rwc/j8JOi2zbmB4zWLrDb562E0hneRSr8xruHfO1rWoahHxERnRiZfAEzV1+Lmauvjay7joPti6vYXG4L8RYvwKhV428mJbYvrmL74ioe+2L0H5ozhULz+GzzKO3cPEqT01C1fv7KQUREdLr0U1H3BIB5AGellN1r6uN/tgJgHcAFKeXlh9rACXCsKuoe/Vvg977Pf3xKq+nCPMvCxXe+E5sf+v3mmpLPY+Yd70DxX3/XEHc2YJ4H2LW28K69mi8c8u2xZteG/WniKanolN6Oqr+DrHGIBxERHU9SStR3d4JjtIt+D7wgxNu+uArZY5W+oqooT834QyyavfD8Kzt2ag/W0CnCijoi6lU//7x1P/yg7rsB/P4+r2333ODrA328Px2V9kmvT/+hUx3SAYCSTmP6LW9B9uabsfLWt0GaJjxdx+KrX436j/0HTL72tRAn8V+PFaUVQmGmv3t57sECvUYFYKTCr23NMRL5eP6+7OSGeKiZg4V8kSm9cWvjHOJBRERHQgiBfLGEfLGE+etvijznWBa2VpZa1XfLi81qPNuox97Pc91m37xHPh99Ll8qd4R3E3PzGD97Dgr/u0dERKdUP0nCxwF8L4A3CyE+KqWMHzXVRgiRAfAm+Ofn/qyP96ej8tjfAU/+g/9YSQHf+rrh7meElF/wAmSvvRYLt78a9oULAICN3/wtGP/8IObe825oZ/s8tnqSKSqQLflXv1y7bShHt5BvN+Z1bZdn97+f5r5MQDcB/VL/90rlO8O7yPCObiFfaNBHeiyY3MshHkRE1DstncbZy67A2cuuiKxLKVHdXO/og7e5tIjd9e6DrPTtLejbW1j48oPR90mlUZmZRWWu1QNvYsYfbpHKZgfx0YiIiEZGP0dfcwAeATAFP3B7qZRyz05TQogxAB+CH/CtArhKShn/z2+nwLE4+iol8DvfAzzxf/3vb/n3wPPvHu6eRpC7vY2ln349qp/6VHNNm5rC3Pvei/zTnz7EnVHPHHP/QM8K9fKLDO9oe510h/1p4qXbB3V0C/7i1kLBXyrPfn5ERLQny6hjMzhCGwnxlhfh2r3/49j4mXPRKry5eVRm5zBWOcNhFjSSePSViHp16KAOAIQQzwPwx/CHQiwCuAvA/5ZSPtT2umsAPB/Aq+Afl5UAXiil/Nih3/wEOBZB3WN/B/zu8/zHiga86j6gcmrbCu5Jeh4u/dqv4dL7/6sfcAJAKoXKS14C9ewZKPl8cBVajwv50Lp/iRT7mp0IjSEeXYO+UMi351rwOLEhHgkSSsygjvCU3h7WtCxDPyKiU8TzXOxeWuuowttYWoC+vdXz/VLZXGgabetrFFpJhgAAIABJREFUeXoWGv9sRUPEoI6IetVXUAcAQogfAfDfAGTQ+pukCaAxYKISPAf4gZ4J4MellL/V1xufAMciqPvt7wGe+LT/+JYfBp7//uHu5xio/v3fY/Enfwre9vahfl6k05EgT8QFfPk8lMLegZ+SD362UICSTif8KelIeR5g690n9/ayZnWZ5DdsitZlQm840GuvBGxfC16v8fc7EdFxZlSrrQq8UIi3tbIE6fU2zEIIBaXJqaDyLhri5YsJtN8g2geDOiLqVd9BHQAIIZ4K4BfhD4noVhIhAfw5gDdLKe/v+01PgJEP6h77e+B3v9d/rGjAq+4FKlcMdUvHhbWwgMXbXw3jy18e9lZ8qVRskNdxFQqR0E9Enm97LpPhEZPjqDnEI25yb49rzoh2LlAzneHdfiFfXEiYHgfUEzgUhojomHIdG1urK62jtIsL2Fi6gI3FBZh679Pks+NFv/ddWxVeaXIaisphFpQMBnVE1KtE/gYipfxnAM8TQswCeBaA6wGcCZ5eB/AvAD4lpVxM4v3oiHwqNOn163+QIV0P0vPzuPz3P4TqJz4Ba2ERnl6Dp+vwdB1S1+HVdHi11lr4Qo//Unwgtg1ve/vQVX6xVHWPwC8U8oUr//Y79pvLMfwbtESHeDgHDPnipvmGX7cLuFb/+2nuqzHEY73/e2m5tkCv2Da8o0vI1/669Bgn9xIR9UnVUjgzdx5n5s5H1qWU0Le3mgMsGuHdxtICttcutlqStDF2d7C0u4Olh/4lsq6omj/MIibEy+QLA/t8REREQEJBXYOUcgn+sAg67h7/NPD43/uPhQp86x3D3c8xpGQyKD73uT39jJQS0jRbwV0k0GsL+xrPh4O+uPCvVgPcAQw1cF14u7vwdvecIdMbIaLBXSHfJeRrPwbc5dhvvgAln4PglNPBUDUgV/GvfjmmH+CFw7vG5N6OkK99mm94uEfCQzycun/VLvZ/r8bU3UiFX7H3tXSB/fyIiEKEECiUKyiUKzh/w1Mjz9mWia3lpY4+eBtLC3BMM/Z+nutgfeFJrC88CXwu+lyhMtEaZDE7F4R45zF+5iz/vEFERIngmR6KZ+4CxTlgZxF42g8CE1cOe0enghACIpuFks0CExOJ3FNKCWnb8Gq1VsAXF+q1h34dr/O/yuB18hCT2g6wWf/9ar0fX9mL6Fb51x72tQWAHf0Bw0d/eSQmWVrGvwpn9n/tXqQEHGOPQO8ga6H1JId4NHoEVlf6u49QQqFdTKAXWY9bC10c4kFEJ1wqncG5y6/Eucujf5aVnofdjfXoJNqlC9hYWkR1o3tFdm1zA7XNDVz40gORdS2dQaUR3IUq8Cozs0hlsgP5bEREdDIxqKN41z4HeMp3AF/4APCU7xz2bqgPQgh/QEU6DVQSqHwKSMuCV6/Hh3qR0K9LJWBM9Z/s8i/bfe9V1+HqOpKsKxTZbPfAL3/Io7+cStc/IYBUzr/GzvV3LylbQzw6pvb2uJbkEA/pBeHiTv/3EmpneHfQkC8dOuabGfODViKiY0IoCopnz6F49hyuuPnpkedMXcfmcmcfvK2VJbiOE3s/xzKx9vijWHv80Y7niucmOwO82XkUyhW2/CAiog6JDJOgwxn5YRJER0w6Tiv8q4XDv5iw74BHf2V9RAcexEh64q9aKEBw4u9o8LxWcNc11Ntp6/XX5XW2PuxPE09Nd4Z3Bw352tdVhtZENHo8z8XOxYtBgHchMpW2vtv7P56kc/lWD7xmiHce5elpqBr/d/Ck4DAJIuoVK+qIaGQITYM6Pg51fDyxe0rXhVc34Ol7HP3tduxXr4Weix79HQRpWXAtC+7WVnI35cTf0aAoQLboX/1ync5qvcbxXbPa25qbYBWrawH1Df/ql5ZtC+/iAr0DrnGIBxElRFFUlKdnUJ6ewVW33BZ5rr67g422QRabSwvYWl2B7DIozKrrWPnaQ1j52kORdaEoKE9No9IW4E3MzSM3ltyfkYiIaDQxqCOiE02oKtSxAtSx5Ka0Sc+DNIz4fn4doV/MxN8u1X+c+Mvw70BUDciV/atfjtVZzRcX6MVO822b3OvFHwc73L4M/6qt9X+vVCE6kTcdOtK751q4CnDMvw8bxRNRF7nxIuauLWLu2usj645tY3t1uXOYxeICrHr8P/xJz8Pm8hI2l5fw6L2fjb5PsdQaYhEMspiYnUdxchIK/2GCiOhEYFBHRNQjoSjNMCopsRN/mxV9B5j4GzsghBN/OYFvH1oa0CaAfJ/Da6QMJvfuF+h1CfmaIWHwvUwwtLZr/tV3m0ARM7yjS8gXCfpCx3wbP5/KcYgH0SmhpVI4M38ZzsxfFlmXUqK2tRmpvmuEeDtr3SeN13e2sbizjcWvfDmyrmoaKjNzwUCL86EjtXNI55L78woREQ0egzoiohFwpBN/ezn6G3rtyZ34W+gI/Djxt0dCAKmsfyGpIR7VLoHeTvyE3o614GcTI/37WbtAv7cVamtYR2R4xwFCvvCgj3QwxIOhH9GxI4TAWGUCY5UJXHbTzZHnbNPA5vJSqA/eYhDmLcKx4lsWuI6DSxeewKULT3Q8NzZxpnmEtjLTGmgxfuYsq9mJiEYQgzoiohPqaCf+xlX17VEJ2Fb9d9Im/qqFQmefP078PRghgHTBv8an+ruX5/nVdJFqvnCoFzrmu+fabrJDPKQLGNv+1S8l1RnexQV6e66Nc4gH0QhJZbKYvOIqTF5xVWRdeh521y91DLLYWF5EbbN7f9DqxjqqG+t48sH7O96n0jhG2+iDNzuH8swsUmlO8iYiGhYGdURE1BORTkNNp6GWSondM3bib3tF314Tf2MqBQc18VcaBlzDgLuRwNCEACf+DoiitEKofjWGeHSd2tvDmmP0v58Gz052iEekwq/YNqX3oGvjHOJBNABCUVA8N4niuUlc8bToAFFTr0X74AVft1aW4bnxPURt08DFxx7BxcceaXsjgdK5ybYAbx6V2TnkS2VW4RERDRiDOiIiGrojnfgbDvT2O/Ybc/R3EI7FxN8g/Du1f0FLcoiHa/cX9IUvL8Gj6I0hHvql/u+VyneGd5EJvd3WQpN702PB5F72miTaTyZfwMzV12Lm6msj657rYvviSmeIt3gBRq1L804psX1xFdsXV/HYF++Nvk+hEPS+C/XBm5tHaXIaqsa/WhIRJYH/a0pERCfS0U78PcDR31p85R8n/p7Cib9qyh/g0e8QD6A1xCM20Ntnmm/762SCh8RtPTguvNr/vdLtwzsOEPxFBn00hnjk2c+PTh1FVf0hEzNzeMqtz2iuSylR392JBHibwePti6uQXYb6mLUalh/+KpYf/mrH+5SmZkJVeK0rOzY20M9IRHTSMKgjIiI6oCOd+Nte0bfv8I9wpSAn/p6aib9axr8KZ/u7j5SAXT94yNd1mm/wGDKRjwcgNMRjub/7CCVmUEdMoHeQNS3L0I+ONSEE8sUS8sUS5q+7MfKcY1nYWlmKDLJohHm2Ed9WwnNdbAZh3yOfjz6XL5VbwV2oCm/87DkoPCZPRNSBQR0REdEQHfnE3x6O/kpdh1urceLvaZj4KwSQzvvX2GR/9/K8YHLvXoHeXmuhdTvB3xfSA8xt/+qXorVN6G2v+iseYC34OY39JGm0aOk0zl52Bc5edkVkXUqJ6uZ6qAKvFeLtrq91vZ++vQV9ewsL//Jg9H1SaVRmZlFpq8KrzM4hnc0N4qMRER0LDOqIiIhOmKFM/I0c6d1j4m/70A9O/E1whyNCUYIwagzATH/38ty2ibxdAr24tfYJv06CA2Y8B6hv+le/1ExneNdR9XeAtfS430uRaECEEBifOIvxibO4/KlPizxnGfVWcBdU4m0uXsDG8iLcLv/I49gW1p58HGtPPt7x3PiZc83wLjyZdqxy5vS1SyCiU4f/NSciIqIDOeqJv82KvoNM/A0fE+bE38T2N3SKCmRL/tWvxhCP9uCvPdBrHPPd63Wu1f9+mvsyAd0E9PX+76Xl2gK9YtuE3m7BXzHa649DPKhH6WwOU1ddjamrro6se56L3UtrHdNoN5YWoG93H6C0u76G3fU1PPHAFyLrqWyu4wjtxMwcyjNz0E7iP3wQ0anEoI6IiIiG5sgn/jYCvQNM/JU1Ha5e48TfkzLxN/EhHtW2kK+Xqb2hQDDJIR5O3b9qF/u/V2PqbqTCr9j7WrrAfn6nmKKoKE1OozQ5jSuf/g2R54xqNVSB1wrxtleX4XXps2obdaw++jBWH304sn7Dt347nvMTdwzscxARHSUGdURERHSiDGXi715Hf9tDwdDR31M78bdQgMhmj2/41xzicaa/+0gJOMb+Id++4V8Q/CU6xKPqX9WV/u4jlM5qvXCgt+9a6OIQjxMlOzaG2Wuuw+w110XWXcfB9sWVtiq8C9hYWoDZpZ/pxNz5o9gyEdGRYFBHREREtI9hTPztOPq717HfZqXg6Z34qxYKELljNvFXCCCV869+h3hICVi1fQK99mm+XdasajKfDwiGeOwEQWKfhNoZ3sUFenuuNSb3ZvrfDw2EqmnNwRJhUkro21uhXngXmmHexDyDOiI6ORjUEREREQ3BUCb+HvDob7MSsNH3jxN/E93jQAjRGuIxPt3fvTwvGtrFBno7MZN7q9HXmbvJDvGQLmBs+Ve/1HRneLdv0NfldSp7ox0FIQQK5QoK5Qrmb7hp2NshIhoYBnVEREREJ8TQJv7qtdiKwNhKwEb4x4m/Ce4wYYoCZIv+1S/XCabyhgO99gm9+60F626Cv2dcC6hv+Fe/tOwBAr1ua+HJvWP+ABUiIjrVGNQRERER0Z6GMfG3vZ/fQY7+nriJvwc49jvyE39VDchV/KtfjhVfzdce6B1kzXP6309zX4Z/1db6v1eq0BnexQV6HWvhCsAx/z7H6Rg4ERE1MagjIiIioiM3nIm/MQFgl4m/zdfV637/t4QNbeJvIeZo73GZ+KulAS2Byb1SBpN7d9sm91Z7XAvCP5ngUBi75l99twkUMYM6xttCvb3WQpN7UzkO8SAiOkIM6oiIiIjoRBjaxN9uR3+7VQHWaidq4m9Px35HYeKvEEAq619j5/q7l5SArXcJ9A46tTcI/6wEh7VAtoZ49HtbobYm8u4Z/I3HvK5tTcsw9CMi2geDOiIiIiKiLoY18TdS+bffsd9G+OckeJyzgRN/9/0sSBf8a3yqv3t5nl9NFzmyu3PAoK9tzdaT+XxAMMRj27/6paQOFui1r8UN+eAQDyI6oRjUEREREREdoeFN/N3/6K9se92pnfhbKEDJ5Y524q+itEKofrlOzOTeg1b4tU34dYz+99Pg2ckO8WiEd7f9GPCvXtX/PYmIRgCDOiIiIiKiY26oE3/bwr+uE38bzxsJBj/hvXLib4uqAbmyf/WrOcRjn0Cvfa253ljbGcwQD/2Sf38iohOCQR0REREREcUa2sTfHo/+Sj3Bo57hvXLib/JDPCLhXVygFxrU0TG8I3QcODzEI4kqRCKiEcGgjoiIiIiIjsxQJ/7GHv2NmfgbXJz4m+Dgh/AQj8LZ/u4lJWDXW+FdNoHKQSKiEcGgjoiIiIiIjrWhTvyNO/rLib+DnfgrBJDO+xf6HOJBRDRiGNTtQQgxDeBnAHwvgDkA2wA+C+B9UspPDHNvREREREQ0OEOd+NsI/zjxd3Qn/hIRDQiDui6EEDcD+BsAZ4KlHQBn4Yd23yOEeKOU8p3D2h8RERERER0vg5j4CwCeZR1s4u8eR3/bKwGlZSW2v6YBTfw984pXYPK1r0n0nkREw8KgLoYQIgfgY/BDui8AeJmU8ktCiCKAtwC4A8A7hBD3SSn/cohbJSIiIiKiU04Z5sTfUPg3rIm/In0Ek3SJiI4Ig7p4rwBwOYAqgOdJKRcBQEq5A+AnhRBPAfACAO8AwKCOiIiIiIhOlIFM/HXdmNAvZuJvD0d/pa5DySfXm5CIaNgY1MV7afD1Q42Qrs0vwQ/qbhFCXCel/MrRbY2IiIiIiOj4Eaqa/MRfzxvMgA4ioiFh1802QohxALcG3/5Fl5d9Bv5gCQD4jn7e77777vN7VSR83Xvvvfu+97333juQ9z7oJKd77rlnIO9966237v/mAF7+8pcP5P1f/vKXH+j9b7311oG8/z333HOg9x/U/+35e29//L3H33v8vcffe/y9x997/L3H33v8vZfM7z2hKBBaZ/3JqPzeu++++w70eiKiBgZ1na4H0Phf/y/FvUBK6QH4avDtDUexKSIiIiIiIiIiOtl49LXTTOjx0h6vazw3s8drAABCiG7/5HTdQTdFREREREREREQnGyvqOoU7kdb3eJ0efB0b4F6IiIiIiIiIiOiUYEVdp4M13OiBlDK2kUFQaXdL0u9HRERERERERETHDyvqOlVDj3N7vC4f83oiIiIiIiIiIqJDEVLKYe9hpAghbgPw2eDb66SUX+3yun8C8I0AfkVK+ROHfK97b7nlllsOMjWJiIiIiIiIjpdbb70V9913333dTlkREbVjRV2nrwBopJc3xr1ACKEAuDb49stHsSkiIiIiIiIiIjrZGNS1kVLuAvh88O2zu7zsGQBKweNPDHxTRERERERERER04jGoi/eh4OtLhRAzMc//ZPD13m5HY4mIiIiIiIiIiHrBoC7erwN4AsA4gD8VQtwAAEKIcSHEnQBeGLzujUPaHxERERERERERnTDasDcwiqSUdSHE98E/1noLgC8JIXYAjMEPNyWAN0op/3KI2yQiIiIiIiIiohOEFXVdSCnvB3ATgLsBPAogA2AdwJ8BeLaU8p1D3B4REREREREREZ0wrKjbg5RyBcCrg4uIiIiIiIiOgJQSuuViq25js2ZhS7exVbewqdvY1v2vm7qFbd3GD9x2Hs++cXrYWyYiSgSDOiIiIiIiIhoYy/GwFYRr4a9+CGdC37Fh1kyYugNXt+EZLmC4yEqJMQgUIDAWus4BzccFKfA1uQIwqCOiE4JBHREREREREe3L9SS266GwrWZiZ9dCdcdEfdeCWbNg1Wy4dQfScAHThWK5yHgIAjeEwjY/gMsDUCBC76IEV+pgmxKAt1RN/LMSEQ0LgzoiIiIiIqJTREqJXdPB9o6Jra06drdN1HZMGLs2zJoNW7f8sM10IUwXiu0hZUtkPNmqZAPwFAhokZCtnRpcg5VXagN/DyKio8KgjoiIiIiI6JiRroRnODCqFra36tjdsqBXTRhBZZutO/AMv7JNsVyotoeUI5FxJXLSr2xLQ6ACoLLvuw12BqEtJWwJOLL12P8+/Lj7c+5lO/j2ge6QiOjoMKgjIiIiIiI6QtKTkJYLr+7AM1xIw4Fds/0jpFUT9aoNq2rDqdvwDAcwXCiWB9XxkHYksp5ERkYr2QrBtTcRXMlxpAxCtPbAzf8+/jkJG60ADgBsxYSp1WGqOkxNh6nVYQVf/bV6az14jZ0ykc2n8AM3/ttEPxMR0TAxqCMiIiIiIjogKSWk5UEafsWaZ7hB5Zr/2NX9KrdwvzbPcADTg2K5SDkeUm73uCyFg3RnSyZs87pUqEVCNrQ/Fw3jZOh+lmq0grZUEKyp/tdW6NYI3Frhm6XWUcjmUc6UUUqXUMqWUM6UcSZdQjkzg1KmhFLGXytnys3vx1JjECLZ4JGIaNgY1BERERER0akhbS8I2PxjoZHH9dZjt+7AqduwdRtOMByh0a9Nkfu/jwIgO8jPEQ7ZcLjjo177PeH5YVsoRAtXs1lxQVsQzFmaASk85LScH6SlS81QbSpTRikz2Qzbwl9LmRKK6SI0hX81JSICGNQREREREdEx0ejLJmMq2bx6l3XDgVd3WsMR3AOkbG0G8ZemPY+Fth0fjXvO6XJfD25wbLSzcs1UQ8dJ24I2/0ipAQj/10cTWkegNpspo5SZj61uazzOqJkB/GoREZ0eDOqIiIiIiGjgmn3ZDAde3Y0cHY08rndZNxxIq70GrDdJHZJs78vWetwZwEUCN7QCuL24wmmrVoseI+0M3lqhm62akQ8qIDCeHo+EavOZMyhnnoJiptgK3EJHTkvpEgqpAo+VEhENAYM6IiIiIiLak5QS0g76stXjQ7T9qtqk6UYbmg3JXn3ZnMiQA9klfDvYx3CE5YdnqegxUj906zxW2hqSUIejWLGpYk7LNYO1cqaIcmYG5UwZxXQQuGXL0e8zZYynx6EqatK/jERENCAM6oiIiIiITjjpeJH+ax092urh9fhqt46GZsP4HAPoy7YXfxJpey+2eseR0eYRU7V15NRVuh1OBTRFawZpZzMllNKTKGfLkd5u5Uw5WvGWKSGtpvv+NSQiotHGoI6IiIiIaITt2ZfNcIKjojHroUAOzgiUsmGv6aGdx0d76cu2F1Otw0q1HRttn0QaW91Wh6e4e95bQDTDtKlMCaX0+Y5hCe193MqZMnJajsdKiYgoFoM6IiIiIqIBCfdla58q6rVXrXU5UtpvX7akhPuytR8Ztbs9h+hghMOQ8IJgLTx5tG0ggqY3j42Ge7k1JpEeRCFVQCldwpnM2dghCXFfx9PjUIRyuA9GREQUg0EdEREREVGMSF+2/fqvdatqG8m+bDEVa9j/yGg/H6MxibRxRNQKBW9xx0gtNVzZ1ppEehApJYVypozJzOy+1W2ldMk/cpouIaWm+viEREREyWBQR0REREQnknS8/fuv7TFh1DNcwBt+yialhIXOI6KxgVuX5/Y+wHkw/iTSzl5s8dVt0e9txex55KoiFJTSJcxmprqGbI0ppc3vMyUeKyUiomONQR0RERERjRzpSkizdRw0tv9a4xipGX+kdFT6sllSwgqCM1cCbpdJotHv++vL1o2j2J3hWnMSaVy/tsYkUh2OYvcctjWMpcY6jpI2qtnap5Q2XsdjpUREdBoxqCMiIiKiRHX0ZYupaosEb6EjpY2qtpHpywY/ZGsEbbaHZtjmdJkyaiNa9ZZ0XGirVtCnrQ5DrXaZPNrZr83U9H2HI+wno2Y6BiPEhWzhqaWlTAkphcdKiYiIDoJBHRERERE1dfRl22+qaEwl28j0ZQNgC8BCUNXm+UGb7Ul4ocq2bn3ZHOnfYxAs1YKtGUGYVoOhVmFotUilW+fQBD2YRNr/rlShNkO1UjrmWGlb4Nb4PqflEvj0RERE1A2DOiIiIqITpNmXbZ9JopFKNjNa1TYSfdkAuIpoC9oQhG0SjivhejJ0jHQwfdm68SBhqxZszYKlGbBSOgytBkPdQb1Z5dY+NKHV2032MBxhP+Op8a4TSrutjaXGeKyUiIhoBDGoIyIiIhoRzb5s3SrVwsdIzdBwhNBABDijcWRUqgKuKmArAjYAMwjaTNeD5UpYroTjSLiujPRsG0Rftm48eLBUB5bmV7dZqcaR0Rrq2jZ0dTs4Nto+rVSHpZo9TSI9iKya3T9ka0wpDdaK6SI0hX+kJyIiOin4X3UiIiKiBLT6svUwVbQerXCT1iBrwHqgCsiUCqkJuIpoVrQZnoTpSpiOhOl4sBwPtu2Hbe3HR4+qJs+BB1N1gr5tFpyUATtVh5WqwdCqMNQd1NTNjmOl/nAE69DDEfaiCQ3FTHHPI6ThKaWN9ayWTX4zREREdKwwqCMiIqJTr9WXra16bb+qttBwBGk6I9GXDYoA0gqQViE1BZ4q4Aq/qs1wJQzHQ91xYdgShu3CsjxYtgfHGXxftm5seDAVB4Zqw9ZsOCkDTsqEndJhpWqwtF3UtW3U1E3o6k7kGKmr2gPd23h6PDIYoRm4pbsHcIVUAUIMIAEkIiKiE49BHRERER17HX3ZDAde3W0bfNA2HMGMDkoYhb5sEIDIqBBpFTIUtHmKgAP/OKjpSui2h7rlQrdc1E0XhunBsly/um1IW7eEB0O4QeBmwdEsOGkTTqoOJ12HnarCTO3A0LZRUzdQVTea00j7nUR6EDkt13mEdJ+Kt2K6CFVRB743IiIiogYGdURERDRU0pOREC1cqdYxYbTL0dFR6csm0gpEVoPIqEBwdNTTFLiKgAs/aLM8vz+baXuomS6qhgPdcFE3XBiGC7iDrRDbiyEkTOHCUFyYig1TtWBpJry0CSddh5uuwc5UYaV2YGhbqKkb2FUuwVRriUwiPQhNaPtOJo17nFEzR7I/IiIion4wqCMiIqJD69qXraOqrW3aaKiSbWT6smkCSlaDktUgsqp/dDSl+EMRhIAjBBwpYUnAcj1YjoRh+ZVttbqDqm7DqLlwLlmQQ6rO8yBhinDg5sBUbZiqCUs14GVMeBkdbqYGO12Fnd6GkdqCrm6gqlyCDfPI9iogIsdK9wrZwl/zWp7HSomIiOjEYlBHRER0SnXty9bRf63tcX0U+7IhCNg0KFm1Gbb5QZtf0eYIv/+aX9Hmh22G7aFuBsdHdce/NnTYdQdySJ/LhYQhAFNIGEK2qtsUG6ZqwNQMeBkDMqvDy1ThZqqw0zswU5vQ1Q1YqMLy9CPdc17LHyhkCx85HU+P81gpERERURsGdURERMdUXF+21gCEuKOjbY/ro9WXTQlCNhFUtSlZFchozcmjjYo2W8I/Oup4MG0PdcuDUbdh1l2YugPzogGj5sAyhhciOkHY5le2BcGb4sJQ/Oo2P3Crw0vXIXN1yOwu3EwVTmYbjrYNR9RgyV2YXg2yl9EOfZ4+TSmpvavb0jHBW6aEtJru742JiIiICACDOiIioqFo78vWfFw/QF+2Rsg2Yn3ZWpVsocc5DSKtwBV+2GZLwJZBjzbH79NmmE4rZNNtGJdMmHoVlu7AMoZ3LNYKHSP1A7fGYw+maoUCNx1ORofI6kC+Ci+7A5mqAaoOT1RhySpMrwpXHrD3XAL/Z1WEgmK62NHDrZgudj1qWs6UkdNyPFZKRERENEQM6oiIiHokZdCXLbb/WvC43qUvW6Nv26j0ZVMFlFyrL1tcVZvIakBa8SvavCBo8xpBmwvTcGHWgpBNd2BumDB1B1bdP0rqmMP7rCZCIZuFU6DiAAAgAElEQVQSDd4MIWEqFgzVhKnVYWk12CkdSr4K5GpQMzrUVB1C0eGJGmz4oZvl1Q/25gl97EKq0BGyFTPxgVvj+/H0OBShJLMBIiIiIjoyDOqIiOhU2bMvW6T/WkyPtvpx6MsW7dGmZDUoOX8KqacpcCBhe36fNtP2YFkeTN2BodvNijZz24a5VPcf1x2YugPXHk71noxUtaF5jDR8pNTv4+b3b7M0HaZWg6lVoeRryOYMpNIGNK0OoemQQoeDVpWbPMj/IRP66Gkl7Qdp2VLkCGmk4q09gEuXkFJTyWyAiIiIiEYegzoiIjpWGn3Z4gcgHKAvm+EC7iikbKG+bLnOCrZm0JZrrYmMCk8RwTAECcv2YNTdaMimOzB3HZir9WCtte4N6XN7iIZszSEJzcAtdLxUcWFqdZiqDjNVha1Vkc4YyGYNZNImtHQdiqpDBlVufuC2C1c60V9b+FlqPbiCjSRCEQpK6VLXPm6xAVy6yGOlRERERLQvBnVERHRkuvZlM5zgqKgLz9y7qk0OqbKrnUgFfdlycZVsbesZP3ATWb9fmw1/GIJVd/yKtVooZNMdmDUb5poRPBdarzuQQxr+4KJLsBaqdosMThAeDK0OU6vB1moQmg5NqyOfM5HNGNBSBlRNBxQdnqLDDgI3WxrN91SDCwCs4ALgJ3AJHSsdS43tO620Uf3WqIYbS43xWCkRERERDQSDOiIiOpBmX7bY/muhx/UufdkMF3KIvcoiDtiXrfk419avLSX8I6M1PzwzwiGbbvvr60YzXItUu9WHd2zWDh0jjRwbDVe5KWh7TsJUDTiqDqHpEKoORa0jnzWQzZpIpevQNANQa/6xUlGD5TWmlUqkAYTngToAquFNeUik0i2jZmJDtsak0rjnipkiUgqPlRIRERHR6GBQR0R0CkgpAcdrThXtfnS0+5HSkenLJtCsTlMyQaCWi+nLltUgcqHH4fWUAtfxIgGaHg7TdBvGlu4PRNBDQxKC5+0RmkTaDNmUziq39te5ig2h6hBqHUKtQag6chkTmayBTNqvchOqDig1QNSgyio0rwrRdqwU8LM1vX0hAapQo5Vt6YMdL81q2WQ2QEREREQ0RAzqiIiOgc6+bNFKNj9g61LhNqJ92Vr919pCtGx837bGMVKRVpp9vhzLjTk6GoRqF/1hCJbuREK2xmsca3hHaNsnkXYeG41WtIXXPAEALoRaB9R6ELzVkE4ZyOdMpNMGUuk6VK2OlKJDFVWkZQ0Zbxe2NLvsx78AJHqsdDw13jVk6za1dCw1xj5uRERERHRqMagjIhqwzr5sMZNEzfBU0WPQly3b6rkWO200F/Rlaw/kMiqE0gphpJRwLK8ZotV1G0YtCNPWwkdHg5CtrZeb64zeJNL2tbjBCVK07gTFDKrb/NBN03TkcyYyaX9aaSZVR1bR4Sk1OPAnlZpeLXZfg+rjltNyKKaL+4Zs4eeK6SI0hX/MICIiIiLqBf8ETUS0h0hftn36r4Wr2ka2L1t7z7VMZ/+1yONceF2FUDsb6EspYRtuZ5+2TRNmrQaz3rY+opNI9zs22v4c2ou+hN2sbmuEbvmsiWzWQDptoJzy1/w+blV/Wqm7Cy/mzKgTXKHNJnK0VBNa15AtbkppY53HSomIiIiIjgaDOiI6sSJ92fbovxauZIs7Ojoqfdliq9f2PDoaHZQATel6pFB6sjn0oN4I07YtmMu1mJDN/9o4TmrpDuSQfo26TSLtDNaCtdAxUxvoDNuCu4rmkVIdUHVkMwZyWRNjQeCmBNNKXVGDLaswvCqcmGOlEkA9uAAk1scNAIrp4t7TSoNJpaVsa2ppIVXgsVIiIiIiohHGoI6IRpZ0vS6VbF0mjJqdVW2j1Zdt70mi3SvZon3ZuvFcL9SvzYG5Y8FcCR0drXWGbKbuwKqPziTSrsdGlZjppCKoOuv6yyIBxWgGbkLVkUrVkc+ZGMsYSKUMqJoOqHV4onGsdBemp8febVB93HJarjNs6zKltDmtNF2EqqjJbICIiIiIiEYGgzoiGgjpSUhznwmj7cMR2qraRrIv20GGILRXtbX1ZdtLYxKpHgRrxsW6H6RFJo86MGuhI6T10ZhEGq1q86vXzJgjpe2DE9x9f2lk6FipfymajkLOQjbjHyvVtDqg1iAVHS5qMOUuTLcae6zUDq6mhH7ZNEXrCNnK2e5TSxtf02o6mQ0QEREREdGxx6COiDr4fdm8A/Vf8wwnCNiigxJGsi9bo1Ito/Y0EEFonX3Z9uJYblC1ZsPcMGC1h2wxfdpGYRKpFQRn9Y5ebeEebvHTSb0Dn6Z0I4GbUHWMB33cMmkTWqoORdUhlRpcUfP7uHm7cKTdcScPgB5czYUEfvkERLOP214hW7ifWylTQl7L81gpERERERH1hUEd0Qkkba9zqmi3Sra4I6Wmk2gvrUPr1pftIFVtuf37snUjpYRt+mGbuWnCqocmke4Rsg1/EingqIApAB0e9Jgqt70GJ8iefpm8yLFSVdWRThuRaaWqpkMqevNYqeHtwvLqsXczgqv5QRLKefNa/kAhW/jI6Xh6nMdKiYj+//buPD6uq7z/+PeZVYu12rLlLV6T2GT3IihrAiElhIRCWVqWxDEQaEsLBX4tUCiBlBIoEMpSUgjOwpoUyhLWhK1laSLbsbPaWbwk3jftGmk0y/n9ca9G49HMWLJHmpH8eb9e5zVzz73nzhnp2NI8Ouc8AACgLAjUARXmuH3ZxjKTLT56VltF78uWJ5NobnKETIbRSPCkZyg55zQ0mFK8ezCTJCETTOvPDqwlss6P7OWWTpfna+hMSgZNCX9Ptpic+lxag8pNkjDGTKQnfkXJhmTBAQWC/bJgTKHwgGqqhhStGlQkMqBgaEAWiCkd6FdS3iy3wVSfXJ5o7pBfhm9dqoBbOBDOn5k0N4NpZGTJaX2knmWlAAAAAKYUAnXABHGptBL7+5XqHVI6Pnr/tUIJESprX7YimUSjJ06IMNZ92QpJp92oTKO52UcHY8nM0tJKyUTqAlI6ZEoETfGANCinfpdWbzqtfpc+PnFC4PhZboUzkY5FUhaKyQIDsmC/LBRTTdWQqqv8fdzCA7LggLesVH0acv0aTPcqlWdZadIv/cMVJVpWGrCA6iP1RYNs2VlKh89Vh6pZVgoAAABg2iNQB5SISzslDvQrvqPLK7u65cq131jQ8s9ky31eHSy4dHS8+7IVMioTaU6QLR5LaihPJtJ4LKmhwfJlIlXQ5MKmZGh4dpu3nLQ/7dSTSqnHpfIsKR1LJtKxSEvBAT/gFpOFYqqKDKi6akjR6KDC4QEF/OQJKfUroX7FCywrdZqYfdwkqTZcOzrIFm3Im0Bh+LEuUqeAlWZsAQAAAMB0Q6AOOEnOOSUPxxTf0a3BHV2K7+yWG0ie+o1NsmjxIFpmVluebKOB6pPbl62Y4UykmVlr/Tmz24aXjubWx5JKlDGphIVNigSUDgWUCEpDAWlATv3OqS+dUncqpa5kSgN5EicUzEQa9MuYOCkw5M1uC3pBt3B4QDXVcVVF4gpHBhQMxaTgQGYft5FlpaMjlHG/DN9aJRhukhQJRDIz2fIlUMh9HC7hQLg0HQAAAAAASCJQB4xL8tjASGBuR5fSfaOXDGYLNkYVnlMzOpNo3uQIXpDtVPZlK9r37EykOfuxeYG2PEtL/cBbsozLcYPRgCwSlAubUv5y0kFzijmnfqXV4wfbOoaSiil93L5tx2UizTeTLCBprFuYWfK4TKWBYEy11XFVVcUV8RMnBPxlpd4+br0aTPcp5UZH0xJ+yShRLDNggYJZSvMlVBh+rApWsawUAAAAACoAgTqgiFRP/LjAXKozXvT6QF1Y0WWNqlrWqOiyRoWaq0rWl+MykeYsIR2pG10/vIdbuTKRmkmhqqAC0aA/u81bTjo8uy0mp950Wt3JpLoSKR1LJNSTSo/ORJpWVpaCPMb8v1laFhyQsoJuNVWDqvYDbuHwoAJ+tlJvWWmv4uk+DaUHR90pJW8Pt1Lv4yZJdeG64/ZwG7WfW3YALtKghqoGzQjPYFkpAAAAAExhBOqALKn+hOI7uzP7zCWPjN7zK5tVh1S1tEHR5X5grqX4hvcu7TQUT2UtEfUfM3u4jQ6yxWMJDfnny5WJNBAwhWtCCkWDsmhALhzwkyV4e7cN+MkSMrPbkkkdiyd0NJH0YmvDX5LjUoIWMaalpU4KxI+b5RaNDKqmKq5oNHtZaUxp61fC9Sme7tNgui/v3Qb8IqmkAbeqYFXRINtwYoXsfd3qo/UsKwUAAACA0xCBOpzW0oNJxXf3KP6UF5hLHOwvmrzAIgFFlzQo6s+YC8+tHZXZ1KWdju3v057HOrX/qS71d8UzS0vLmYk0EDJFa8KKVHuz2ywSUDocUDIoDQVNg3KKyctM2pNKqSuR1LGhpA7HEzo2mPDiVillZSUYg7GuprTEcQG3YGjAW1YaHVQkElcw7NU7iylpfsAt1at0njWjE7WPW9CCo5aOZjKTVmUF3HKCcVWh0s2qBAAAAABMbwTqcFpxiZTiT/covsObNTe0t7f4zKmQKXpGvReYW96oyIIZsuDopYW9HYPas61De7d3au/2Dg30Ft+77mSFIgFFq0OK1oYVrg4qEPGWkw7v3RY3581uU1q9qbQ6k0l1JlM6Gh/SscGkumODGoqnsyJZpZbKJE0YzlZaUxXPWlbqnXOBmFL+LLfBVK8SbnSHkpL6jr91ydRF6o5bMjr8PO+MN3823IzwDPZxAwAAAABMKAJ1mNZcKq2hvX2ZGXPxZ3qkZJEpbQEpsqAuM2MuuqhOFh69DjM+kNS+xzu1d1uH9mzvVNehsU8zC0eDitaEFK0JK1oTUqQmJIt4y0mTIVMi4DRgUsyl1Z9OqzuVUmcqpY6hhDoGkuoeGFJnrE+xYxOZTXV4WWl/JuhWHY2rujquaHTA28ctOCAF+5W2mL+stFeD6f58d1JMWRPxSristDpUfdzMtkLJErLP1UfqFQrwXx8AAAAAoPLwaRXTiks7JQ70Z/aYi+/qlhsqEhUyKTy3diQwt6RegejofxapVFqHdvV4s+a2dejQ7l65IvvFVc0Ia8GKJg02R3Qs5C0l7U6l1TmUUOdgUl0DCXXF+tXZO6SeIyVam1mIDfmz3LygW9jfx626ykucEAx5s9zSfrbSeLrXX1Y6+us26BdJJV1WGrJQ3kylJwq8RYPR0nQAAAAAAIAKQKAOU5pzTsnDsZHMrDu75QaKR49CLdWKLvcys0aWNChYO3rTfuecOg/EtGe7F5jb90SXEvHCM9iC4YDmLW/QgpXNWriyWTUtVXrnt7foN+1Pn/J7HJHyZ7d5gbVgOKaaqiEv4Ja9rNT6lfSXlQ6kepV0o7M3JPySdeuSLC012ciy0gJLSPMtOa0N17KsFAAAAABw2iNQhykn2TGo+I4uLzC3o0vpE+wHF2yMZgJz0WUNCtbnn4XV3x3X3u2dmVlz/d1F0pOa1LKwTgtXNmvByibNXdagkL9EtqN/SG/8Wru27ukq0DgtBQaP28utpmpQ1VVDI8tKQ94+bsPZSgfTvYqnRy+vTWni9nGrDlXnDbJlZyk97jjaqLpInYKBMaVsBQAAAAAAOQjUoeKleuIjM+Z2dCnVWTwTQqAurOiy4cBco0LN+bNuJuIp7X+yS3u2dWjPtg517B+9v1q2uplVWujPmJt/dqOqZ0RGXbO3M6arN7RrV+c+hep3KlizW63NQwqGYkqoT0PpPg2k+uTyLCsd8Iukku7jFgqEjs9GGmlQY1VO1tLcGW/RBkWCo98fAAAAAACYOATqUHFS/QnFd3Zn9plLHhkoer1Vh1S1tEHR5X5grqU67zLKdNrp8NM9XgKIbZ06uLNb6VThfeaiNSHNP7vJD841qX5W/vtK0uHYYf1g+//oP/7vHiXqn9SMWccy5zqcctaZnhyTZYJpuQkU8iVNGA66VYcK9xsAAAAAAFQOAnUou/RgUvHdPZnMrImD/V6iggIsElR0SX0mAUR4bq0sMDoQ5ZxT95GBTGBu3xOdiscK718XCJrmLmvQghXerLmWRXUK5LmvJB0dOKqNBzeq/WC7Nh3cpN09u70TM6TAGN5zTaimYHCtUMCtLlKngI3l7gAAAAAAYCoiUIeC9vTu0YZHNuiqZVfpotkXley+LpFS/OnezIy5ob29xZd5hkzRM/zA3PJGRRbMkAXzB6wG+oa0d3tnJjjX2zGY97phM+fXZhJAzFveqHA0//5qxwaOaeOhjdp0cJPaD7ZrV/euovcNByJaNecitbW2aVnjskzShMYq7zEcHJ3AAgAAAAAAnN4I1CGv7z3xPd1w3w1KuZQO9B/QzZfefNL3cqm0hvb2ZWbMxZ/pkZJFpswFpMiCusyMueiiOlk4fwAtmUjpwFPdXgKI7Z06sqe36Gy82oaInwCiWQtWNKm2IX9iic7BTm06tEkbD27UxoMb9VTXU8XfYzqk1MAZqkqepQ+95EpdueI57PEGAAAAAADGhUAd8lo9Z7WcH/H6w74/6NFjj+qcmeeMqa1LOyUO9GdmzMV3dcsNFZkyZ1J4bu1IYG5JvQLR/EPTpZ2O7u3LJIA4sKNbqUThe4ejQc0/u0kLVnh7zTW11uTdr6073p0JzLUfbNeTnU8WfY/hQFjNoTP1zL65SsWWKjVwhpbObNTt69u0sLmmaFsAAAAAAIB8CNQhr8UNi3XZosv0890/lyTd8tAtuumSm/Je65xT8nBsJDPrzm65gcJ7wUlSaHZ1JjNrZEmDgrWFl4L2HBvQ3m2d2rPdmzU32Fc4M4MFTHMW12vhyiYtWNmsOUvqFcyzTLZnqEebD27WxkPejLnHOx7PBCbz9jcQ0nmzztPa1rVaPXuNfnBfWHdtPJQ5f8HCRm24Zo1mzsg/Qw8AAAAAAOBECNShoLee99ZMoO6Xz/xST3U+peVNyyV5+8zFHjyiQX85a7q3eFrTYFPUC8wtb1R0aaOC9YWXhcZjCe17vMubNbe9Q92Hi2d9bWqt8RNANGn+WU2KVI8e1n1DfXrg8ANqP9CujYc2anvHdqVd4Zl4IQvpnFnnaG3rWq1tXasLWy5UTbhGg4mU3vmtLfrltpEg3YvOatGX37RKNRH+OQEAAAAAgJNHZAEFnd18ti5eeLF+u+e3kqRbHrlFN77gRiUOx3TsG9uUPBwr2DZQF87MmIsua1SouargtalkWod2dWvPtk7t2dahw7t75IrsM1ddF84E5hasaFZdnnv3J/q15fAWtR9s18YDG/VYx2NFA3MBC+icmSOBuVWzV6kmfPwS1q7YkN5y+yZtfrozU/fqVfP1yT8/X+ECyS0AAAAAAADGikAdirruvOsygbqf7fqZ/ia6ToEfd8gNpY67zqpDqlraoOhyPzDXUp13LzjJWyrbsb8/kwBi35NdSsZTea+VpFA4oHlnNmays86cVysLHH/vWCKmrYe3auMhb4+5R48+qpQrfM+ABbSieYXaWtsygbkZkRkFr9/fNaBrNrTrycN9mbq3v2ip3v+yFQXfJwAAAAAAwHgQqENR57Wcp+fMfY7a97fr2kOvlD12ZGQnt1BA9ZcsVNWKZoXnjg6eZevvimvPdi8BxN5tnYr1DBV+UZNmn1GXCczNXdqgYPj4GWuDyUFtPbJV7QfatenQJj189GEl04X3xTOZVjSv0JrWNWprbdOqOatUH6kf09fgiUO9umZDuw50D2bqPvyKZ+ktz18ypvYAAAAAAABjQaAOJ/SOZW/Tq+57js6PnZWpCzZXaeabVioyL/8stKHBpPY/0eUH5zrVeaC/6GvUz6rSwpXNWrCiWQtWNKkqJ7lEPBXXQ0ceUvvBdrUfaNfDRx9WIl18X7yzms5SW2ub1rSu0Zo5a9QQbRjjOx6xaXeH3nL7JnUPeK8VDpo+87oLddUF88Z9LwAAAAAAgGII1KGo+O5uzf2O05ysIN3e1g61XfdyBWpGgmnpVFqHn+71EkBs69ChnT1KpwtvNBetCWnBiqZMcK6hpfq480OpIT105KFMVtYHDz+ooXSRWXiSljcu19rWtWprbdPqOavVVNV0ku/ac+9jh/TObz2geNLb2642EtR/vnmNnn/mrFO6LwAAAAAAQD4E6pBXciilo/c+reQf9kl+Doa00rqr8Tf6efX9+uqRtaoL1uvAU1521n2Pd2posMiecCHT3GWNWrjSC87NWlinQNZS2UQqoUeOPZLJyvrg4Qc1mBoseD9JWtqwNJP8Yc2cNZpZPbMk712SvtP+jD74/Yc1HGucNSOiW9e16bwF45+VBwAAAAAAMBYE6pBXx893K/nH/ZnjeNppcyyt6q4X6lW7X6ifbtl+wnvMXDBDC1c2a+GKJs09s1HhSDBzLpFO6KHDj2rToU1qP9CurUe2aiA5UPR+i+sXZ2bMrWldo1nVpZ/Z5pzTF379lD577xOZukUza3TH+jYtmllb8tcDAAAAAAAYRqAOeYXOmaWe3+9TVcDUmUxrY39KA4VXskqSZjRF/QQQTVpwdrNq6iOZc8l0Ug8feVjtB70Zc1sObVEsGSt6vzPqzsjMmFvbulaza2aX4q0VlEo7feRHj+gb9z2TqTt3fr1uXdemlrrohL42AAAAAAAAgTrkFWqI6ImasGYl09pZHVZVnSnqnPb17lUilZBkaow2avGied6suZVNapxTIzNvOWsqndKjxx7VxgMb1X6wXQ8cfkD9ieIJJebPmK+21rZMYK61tnUS3qlnMJHS39+5VT975GCm7vnLZ+nmN6/WjCj/TAAAAAAAwMQjAoG86mdV6+XX/4kkqS2r/u4dd+uDv/+oJKkh2qB7/vwe1YRrlHZpbe/Yro0HveQPmw9tVm+it+hrzK2dm1nKurZ1rebNKE8m1e6BhK67Y5Pu39WRqbvqgnn69GsvUCQUKEufAAAAAADA6YdAHcbl8iWX60tbv6R9ffvUHe/Wh//wYSXTSW06tEk9Qz1F286uma221rZMYG7+jPmZGXjlcqhnUNdsaNf2gyNBxfXPW6IPXbHyuGQXAAAAAAAAE41AHcYlFAjpLee9RR/7v49Jku55+p6C17ZUt2SWsba1tmlh3cKyB+ayPXW4T9dsaNe+rpEkFh+4fIWue+HSiuonAAAAAAA4PRCow7i9ctkrdfODN+tw7PBx9TOrZh6X/GFx/eKKDXhteaZT62/bqM5YQpIUCpg+9Zrz9epVC8rcMwAAAAAAcLoiUIdxiwQj+uzFn9UXtnxB9ZH6zHLWJQ1LKjYwl+032w/rr7/5gAYSKUlSdTioL79plS4+e2KzygIAAAAAABRDoA4n5YKWC3TLZbeUuxvj9l+b9uj9//2wUmknSWqujWjDurW6cGFjmXsGAAAAAABOdwTqcFpwzunL/7NDn/r545m6BU3VumN9m5a2zChjzwAAAAAAADwE6jDtpdNOH/vxY7rtj7szdSvn1uv2a9dqdn1V+ToGAAAAAACQhUAdprV4MqX33vWgfvzQgUzdc5Y26ytXr1F9VbiMPQMAAAAAADgegbocZhaVdLGktVllrn/6cufcz8vUNYxT72BC7/jGZv3hqWOZuivOm6vPvv4CRUPBMvYMAAAAAABgNAJ1o62URDBuijvcO6hrb92oR/f3ZOqu+ZNF+ucrz1EwUPmZaQEAAAAAwOmHQF1+XZI2S9ooaZOk75a3OxiPXUf7dfWG+7WnYyBT9//+9Gz99cXLZEaQDgAAAAAAVCYCdaM9JKnZOeeGKwjuTB0P7e3Stbdu1LH+IUlSMGD6xKvO0+vWLixzzwAAAAAAAIojUJfDOZcudx9wcv73iSN6xzc2KzaUkiRVhQP60htW6SUr55S5ZwAAAAAAACdGoA7Twg+27NP7/utBJdPeRMjGmrC+ds1arV7UVOaeAQAAAAAAjA2BOkx5t/xup/7lJ9syx/MaqnTHW9q0fHZdGXsFAAAAAAAwPgTqJoGZbS5wasWkdmSaSaedPvGzbfrq73Zl6s6aM0O3r2/T3IbqMvYMAAAAAABg/AjUYUoaSqb1D999UD/Yuj9Tt3Zxk265eq0aasJl7BkAAAAAAMDJmRaBOjP7Z0n/fJLNP+mc+6dS9ieXc251vnp/pt2qiXzt6ag/ntQ7vrFZv3vyaKbusmfN0ef/8iJVhYNl7BkAAAAAAMDJmxaBOkkBSScboSGyM4Uc7Ytr/W0b9dDe7kzdG559hm545bkKBqyMPQMAAAAAADg10yJQ55y7XtL1Ze4GJtgzx2K6esP92n0slql796Vn6l0vOVNmBOkAAAAAAMDUNi0CdZj+HtnXrXW3btTRvrgkKWDSDX92rt747EVl7hkAAAAAAEBpEKhDxfvjU0d13dc3qy+elCRFQgF9/i8u0svObS1zzwAAAAAAAEqHQB0q2t0P7td77tqqRMpJkuqrQrrlmrVqW9Jc5p4BAAAAAACUFoG6PMysSfmTTNSb2ays427nXGKSunXaue0Pu/TRHz8m58Xo1FpfpdvXt+ns1rrydgwAAAAAAGACEKjLb4ukfJuf3ZlzfImk3054b04zzjn92y8e13/8dkembllLre54y7M1v7G6jD0DAAAAAACYOATqUFESqbQ+8N8P67ub92bqVp3RqK9ds1ZNtZEy9gwAAAAAAGBiEajLwzm3uNx9OB3FhpL6m28+oN88fiRT95IVs/XFN6xSdSTfSmQAAAAAAIDpg0AdKkJH/5DW37ZRW/d0Zepet2aB/vVV5ykUDJSxZwAAAAAAAJODQB3Kbm9nTFdvaNfOI/2ZundeslzvvewsmVkZewYAAAAAADB5CNShrLYf7NE1G9p1qCcuSTKTrr/yHF3z3MXl7RgAAAAAAMAkI1CHsrl/5zG99Y5N6h1MSpIiwYBuev2FuuL8uWXuGQAAAAAAwOQjUIey+PkjB/R339mqoWRaklQXDek/r16t5y6bVeaeAQAAAAAAlAeBOs3H8fIAABfnSURBVEy6r9/3tP75h4/IOe+4pS6q265dq3PmNZS3YwAAAAAAAGVEoA6Txjmnm375pD7/qyczdUtm1eqO9W1a2FxTxp4BAAAAAACUH4E6TIpkKq0P//BRfbv9mUzdBQsatGHdWs2cES1jzwAAAAAAACoDgTpMuMFESn/77S2697FDmboXndWi/3jjKtVGGYIAAAAAAAASgTpMsK7YkN56+yZterozU/fqi+brk685X+FgoIw9AwAAAAAAqCwE6jBh9ncN6JoN7XrycF+m7u0vXKp/fNkKBQJWxp4BAAAAAABUHgJ1mBBPHurV1RvadaB7MFP3oStW6q0vWFrGXgEAAAAAAFQuAnUouc1Pd2j9bZvUPZCQJIWDpk+/9gK98sL5Ze4ZAAAAAABA5SJQh5K697FDeue3HlA8mZYk1UaCuvnNq/WCM1vK3DMAAAAAAIDKRqAOJfOd9mf0we8/rLTzjmfNiOjWdW06b0FDeTsGAAAAAAAwBRCowylzzumLv35Kn7n3iUzdGc01+vpb2rRoZm0ZewYAAAAAADB1EKjDKUmlna7/0aP6+n1PZ+rOnV+vW9e1qaUuWsaeAQAAAAAATC0E6nDSBhMpveeurfrpwwczdc9fPks3v3m1ZkQZWgAAAAAAAONBNAUnpWcwobfdvkn37+rI1F11wTx9+rUXKBIKlLFnAAAAAAAAUxOBOpyU93/voeOCdOuft0QfumKlAgErY68AAAAAAACmLgJ1GLf9XQP62SMjy10/cPkKXffCpTIjSAcAAAAAAHCyCNRh3L67ea+c854/f/ksvf1Fy8rbIQAAAAAAgGmAzcQwLum0012b9mSOX7d2YRl7AwAAAAAAMH0QqMO4/HHHMe3tHJAkNVSHddmz5pS5RwAAAAAAANMDgTqMy51Zs+leddF8VYWDZewNAAAAAADA9EGgDmPW2T+kX2QlkXg9y14BAAAAAABKhkAdxuwHW/dpKJWWJJ2/oEEr59aXuUcAAAAAAADTB4E6jIlzTnduzEoisYbZdAAAAAAAAKVEoA5j8vC+bm0/2CtJqgoHdNWF88rcIwAAAAAAgOmFQB3G5DtZs+left5c1VeFy9gbAAAAAACA6YdAHU5oYCilu7fuzxy/nmWvAAAAAAAAJUegDif004cPqDeelCQtmVWrtiXNZe4RAAAAAADA9EOgDieUnUTitWsWyMzK2BsAAAAAAIDpiUAditp5pE/tuzskScGA6TWrFpS5RwAAAAAAANMTgToUddemvZnnl5w9W7Prq8rYGwAAAAAAgOmLQB0KSqTS+t4DI4G6168liQQAAAAAAMBEIVCHgn6z/bCO9MYlSS11UV1ydkuZewQAAAAAADB9EahDQXdtGkki8ZrVCxQKMlwAAAAAAAAmCpEX5HWoZ1C/efxI5vh1a1j2CgAAAAAAMJEI1CGvex49qFTaSZLaljRryazaMvcIAAAAAABgeguVuwOoTG96ziI9a1697ty4Ry88i73pAAAAAAAAJhqBOuRlZlq9qFmrFzWXuysAAAAAAACnBZa+AgAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAQjUAQAAAAAAABWAQB0AAAAAAABQAcw5V+4+nLbM7Fh1dXXzypUry90VAAAAAECJbdu2TQMDAx3OuZnl7guAqYFAXRmZ2S5J9ZJ2l7krhazwH7eXtRc43TEOUSkYi6gEjENUCsYiKsFUGIeLJfU455aUuyMApgYCdSjIzDZLknNudbn7gtMX4xCVgrGISsA4RKVgLKISMA4BTEfsUQcAAAAAAABUAAJ1AAAAAAAAQAUgUAcAAAAAAABUAAJ1AAAAAAAAQAUgUAcAAAAAAABUALK+AgAAAAAAABWAGXUAAAAAAABABSBQBwAAAAAAAFQAAnUAAAAAAABABSBQBwAAAAAAAFQAAnUAAAAAAABABSBQBwAAAAAAAFQAAnUAAAAAAABABSBQh1HMrNXM/t3MdpjZoJkdMrO7zewl5e4bKoOZnWFm7/bHxTNmFjezXjN70MxuNLO5J2gfMbN/MLOtZtZnZl1m9n9mdp2Z2Rhe/7Vm9mszO2ZmMTPbZmb/YmZ1Y2i7xsy+Y2b7/fH9jJndYmbLx/M1QGUysxlmtsfMnF/WFbmWcYiSM7OlZnaTPx76zKzbf77BzF5UoA1jESVjZgEzu9bMfmlmR8ws4Y+p+83sn4qNC8YixsrM6szsKjO7wcx+ZmZHs372rhhD+yk51ozPSQAmg3OOQskUSedLOirJ+aVbUsp/npb0/nL3kVL2MbLQHwsuZ5wks447JF1SoH29pE1Z1/ZLimcd3y0pVOT1v5J1bUJSb9bxDknzirS9xm8zPJ67str2SXpxub++lFMen5/LGZvrClzHOKRMxPhbLymW8/3MPr6FsUiZ4DFYI+lXeX5GZ//c3i1pKWORcopj7c9yxll2WXGCtlNyrInPSRQKZZJK2TtAqZwiqdr/5c1JekDSOX59vaRPZ/1QuqzcfaWUdZws9n8Z+bGk10hq8usjki6XtDPrl5fWPO3v9M8fk/QKSSYp6P/iNOCf+3iB1/4r/3xK0vskRf3652aN3d8XaHu+pCH/mm9IavHrF0m6x6/vHK6nTL0iaZW8gPF9Wf9frStwLeOQUurx9xcaCYZ8QVmBEElzJL1J0nrGImWCx+EnNBI0+ICkBr8+4o/RTv/8rxmLlFMca38m6ZCkn0i6XtLbNPZA3ZQba+JzEoVCmcRS9g5QKqdIerf/A6ZX0vw857/vn99c7r5SylckNUi6oMj5FVm/ZH0k59xFWb/IXJWn7bv8czFJs3PORf1fCJ2kz+Zpe5FGPiRfmef8D/xzGyUFc87NkPSMf/4z5f4aU05qXAb8720yZ5ytKzBWGIeUUo6/2fJmEjtJHxhHO8YipdRj8Wn/+/a1AufXZY25ppzxwlikjGes5X6vFmeNoYKBuqk61sTnJAqFMomFPeqQ7Y3+47ecc/vynP83/3HVWPaewPTknOt2zj1Y5Px2eTOaJGl1zuk3+I+PO+d+lKf5V+TNxKuW9Oqcc5fK+zDsJH0mz+tukfRL//CN2efMrFHSy/3DzzrnUjlt+yTd7B/+5Vj2RkHF+VtJayR92R8LxTAOUWp/JalJ0uOSPjmOdoxFlNoc/7HQ/4Obs57XZD1nLGJccr9X4zBVxxqfkwBMGgJ1kORtCKuRoMovClx2n7wfnJL04gnvFKayY/5jMKf+Ev/xnnyNnHMDkn7nH+aOseG2jxT4BUkaGbu5bZ8vKVzstbPazpW0ssA1qEBmNl/SDfL+yv6hMTRhHKLUhj/A3eGcS4+jHWMRpbbbf7yowPnh3/UOSdqfVc9YxGSZcmONz0kAJhuBOgxbKW9/CEl6NN8F/oePx/3DZ01GpzD1mFlI0vP8w0ey6k3eslipwBjzPeY/5o6x4eOxtG0xs1l52h50zh1Tfo9lPWd8Ty1fkFQn6X3Oue5iFzIOUWpmNlPSmf7h783sxWb2CzPr9DMRPmZeNuxZOe0Yi5gIX/UfrzWz95tZg5TJsPl6STfJm430Puec888xFjEppvBY43MSgElFoA7D5mY931/wqpFzc4tcg9Pb30hqlbdHyB1Z9fWSav3nJzPG5uacL9Y2t/0J2/p/we0q8NqoUGZ2paRXSfqtc+4bY2jCOESpnZn1/DJ5y64u08iM4pWS/lHSVjPLng3EWMRE+JykL8kLKnxCUpeZdcnbO/Y7krbL2xcs+/9LxiImy1Qda3xOAjCpCNRhWG3W84Ei18X8xxkT2BdMUWZ2vqR/9Q+/6JzL/qvjqY6x4fZjaZvbfixti702KpCZ1Ur6oqSEvADxWDAOUWqNWc8/KG+2xbOdc/Xyvocvl3RY0nxJ3/NnHUuMRUwAf9+td0t6r7zkOpKXBGr4d/46SS05zRiLmCxTdazxOQnApCJQh2FszotTYmZz5WXTqpG3WfU/5l6S9dydzEuUqS0q18cknSHpJufcYye62Mc4RKll/y6VkvQq51y75C2Fcs79TNJ6//xKeTNAJcYiJoCZtUr6g7yN9r8p6QJ5QYMzJX1A0lJJG8zsE9nNsp4zFjGRpupY43MSgElFoA7D+rKeVxe5bjhDWF+Ra3CaMbNmeRvzLpH0pKQrnHODOZdlj5kaFVZojPXlnC/WNrf9WNoWe21UGDO7UNK7JO2RF7AbK8YhSi37+/QT59xTuRc4534i6Qn/8NI87RiLKJU7JLVJ+ppzbp1z7iHnXL9z7inn3I2S3u5f9w9mdq7/nLGIyTJVxxqfkwBMKgJ1GJa938K8ItcNnzswgX3BFOJvVP0LSedKekbSpc65Q3ku7ZHU7z8/mTG2P+d8sba57U/Y1syqNbKEjfFd+f5d3h5g/yRvf+oZ2SXruqhfN/zLM+MQpZb98/PxgleNnFvoPzIWUVJm9ixJL/UPb8p3jXPu6/IyswckvcKvZixiskzVscbnJACTikAdhm3XyFTwc/JdYGYBSWf7h2NdZoZpzN8j7KeS1kg6KC9I90y+a/3sctv8w7xjzDecKSt3jA0fj6XtEefc0TxtW/0MjcXa5nttVJ5F/uMdknrzlGE3+8ePSYxDTIidGtmzaCxLqpzEWMSEyE5WsqvIdTv9x8USYxGTZwqPNT4nAZhUBOogSXLO9Ura5B++tMBlz5a3IbEk/WrCO4WK5v/V8W5Jz5X31/lLnXNPnqDZb/zHvGPMzKokvcA/zB1jw23PMbNCf828rEDb38tLOCCNLDsr1PaARn6JxPTEOETJOOfSkn7rH64ocunwB7ins+oYiyildNbzM4pcN/yHjuw/ajAWMVmm3FjjcxKAyUagDtm+5T++0U8MkOt9/uNm51yx5T2Y5swsIum/JV0iL439ZTkZXgv5tv+4wsxekef82+T9kjMg6fs5534lL3NiQNJ78vTpAo384vXN7HPOuW55M/8k6T3+Xz2z29ZKeod/+C3/L76oYM65xc45K1SyLr3Wr1ucVcc4RKl93X+8wsyW5540syskneUf/jTrFGMRpbQ16/nb8l1gZldKmu0f3p91irGIyTJVxxqfkwBMHucchSLnnORtjrpb3tTuzZKe5dfXSfqUX+/kBWXK3l9K2cZJUNJ3/bHQI+k542x/p9/2qKSXZ93zanlp7Z2kjxdo+1f++ZSk90qK+vV/Im8pj5P0+wJtL5A05F9zh6RZfv0Z8vbYc5I6JbWU+2tMOfWS9f/VugLnGYeUUo63gLzZFk7Sw5LWZtW/TN7WAE5eYMQYi5QJHIu/yBoTn5A026+fIWmdvBnwTt7S2AhjkXKK421WVrlIIz97n5NzLjDVx5r4nEShUCaxlL0DlMoq/g+wo1k/bLr9H4RO3pKK95e7j5Syj5EXZo2PAXkfQAuVjXna12vkA62Tt6nwYNbx3ZJCRV7/K1nXDslbujN8vEPSvCJtr5G37GF4PHdlte2T9OJyf30pJRunJwrUMQ4ppR5zC/zv/fD3cnjT9OHj7ZIWMhYpEzwO58rbH8vp+LGYfXxQ0kWMRUoJxpsbY1k8Hcaa+JxEoVAmqbD0Fcdxzj0oL3vn5+X9VSoq76+vP5H0UufcjWXsHipD9v8bVZLmFCktuY2dcz3y9rV7v6QH5f1yE5d0n6S3S7rKOZcs9OLOueskvV7ePiV9kkLyPgB/XNKFzrn9RdreLu8vrndJOiTvr6N7JG3w2/76hO8e0wLjEKXmnNsr70PcRyU9Im92iJO0RV524jXOuT152jEWUTLOuQOSVkt6t6T/ldQhqUZesO4BSTdIOs85tyVPW8YiJsVUHWt8TgIwWcw5V+4+AAAAAAAAAKc9ZtQBAAAAAAAAFYBAHQAAAAAAAFABCNQBAAAAAAAAFYBAHQAAAAAAAFABCNQBAAAAAAAAFYBAHQAAAAAAAFABCNQBAAAAAAAAFYBAHQAAAAAAAFABCNQBAAAAAAAAFYBAHQAAAAAAAFABCNQBAAAAAAAAFYBAHQAAAAAAAFABCNQBAIAxMTPnl8UlvOfF/j13l+qeAAAAwFRFoA4AAAAAAACoAATqAAAAAAAAgApAoA4AAAAAAACoAATqAAAAAAAAgApAoA4AgNOMmTWb2TVm9j0z225mvWbWb2aPmdlnzWzeOO93vZ8Q4jYzC5jZ35vZg/49j5nZj8ysbYz3ep6Z/djMjprZgH+fd5qZFbh+qZm918x+ZWa7zGzQzLrM7D6/vno87wUAAAAoJ3POlbsPAABgEpnZpyW9N6uqR1KtpKB/fETSpc65h3LaDf/SsMQ5tzur/npJH5F0h6QZkl4tKSmpX1KDf1lK0hudc3fm3PNiSb+R9LSk6yXdIu8PiT1ZbSXp351z787zXjZJWu0fOkndfrvhwN4mSS92zvXm+VIAAAAAFYUZdQAAnH72SbpR0ipJdc65BklRSWsk/UJSi6RvFZrFVsQr/fIeSfXOuUZJyyXdKy8IeKuZLSvQtkXSf0r6sqS5ftsmSV/wz/+dmZ2Tp90WSe/2X6fKOdckqVrSVZKe8N/TjeN8HwAAAEBZMKMOAABkmFlU0gOSniXpYufc/2SdO9GMOkn6kHPu4zn3rJK0VdLZkr7mnHtr1rmL5c2ok6RbnHNvy9OnhySdJ+kjzrmPjeO9LJX0uKQhSS3OudhY2wIAAADlwIw6AACQ4ZyLy5sBJ0nPG2fzmKTP5bnnoKTP+Id/XmSm3icK1P/Qfzx3PJ1xzu2U9KikGkkXjqctAAAAUA6hcncAAABMPjNbIemdkl4oabG8veVyA2jjSiohaZNzrr/AueGZeY2SlkjamXO+ww+s5bPPf2zKd9LMXippvaQ2SXPlLX3NNd73AgAAAEw6AnUAAJxmzOwv5CV+CPtVaXlJGOL+8Qx5ySVqx3nrfWM816LRgbpiyR4G/cdw7gkz+7ykv82qSkjq8B8lqdlvN973AgAAAEw6lr4CAHAaMbMWSV+VF7y6U16yhSrnXJNzrtU51yrppuHLS/nSJbyXd0Ozy+UF6VLyMsYulxR1zs3Mei/3T9TrAwAAAKXGjDoAAE4vl8ubMfeYpDc459J5rplzkvcutrx0btbzIyd5/1yv9R9vcc59tMA1J/teAAAAgEnHjDoAAE4vC/zHh/IF6fxEDy8+yXuvNbOaAude5D92Sdp1kvfPNfxetuQ7aWaL5M2yAwAAAKYEAnUAAJxeuv3HcwtkX32bpGUnee8aSe/KrTSzqKT3+Iffdc65k7x/ruH3cl6B8/8qlrwCAABgCiFQBwDA6eWXkpykcyV93swaJcnM6s3s/0n6kqRjJ3nvbkk3mNm7zKzav+9SST+UtFJeUogbT7H/2e71H99uZuvNLOK/5hlmdrukv5TUWcLXAwAAACYUgToAAE4jzrnHJX3OP3ynpE4z65CXKfVTkn4l6eaTvP0PJf3Iv3+3mXVK2iHpT+UlfLjWObfjFLqf6zZJ98nbc/drkmL+az4t6WpJH5H0UAlfDwAAAJhQBOoAADjNOOfeI+k6eXu7xeUFurZKerekKyQlT/bW8hI8vEfSNkkReTPafizpuc6575xaz3NezLkhSZfKm6W3U1JaXt/vlXSlc+6GUr4eAAAAMNGsdNvEAACA05GZXS9v9trtzrl15e0NAAAAMHUxow4AAAAAAACoAATqAAAAAAAAgApAoA4AAAAAAACoAATqAAAAAAAAgApAMgkAAAAAAACgAjCjDgAAAAAAAKgABOoAAAAAAACACkCgDgAAAAAAAKgABOoAAAAAAACACkCgDgAAAAAAAKgABOoAAAAAAACACkCgDgAAAAAAAKgABOoAAAAAAACACkCgDgAAAAAAAKgABOoAAAAAAACACkCgDgAAAAAAAKgABOoAAAAAAACACkCgDgAAAAAAAKgA/x9PB1pqNjngUgAAAABJRU5ErkJggg==
"
width=629
height=392
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># does the same thing above except for lasso</span>
<span class="n">alphas</span> <span class="o">=</span> <span class="p">[</span><span class="mf">0.01</span><span class="p">,</span> <span class="mf">0.1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">8</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;different alpha values:&#39;</span><span class="p">,</span> <span class="n">alphas</span><span class="p">)</span>

<span class="n">lasso_weight</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">alpha</span> <span class="ow">in</span> <span class="n">alphas</span><span class="p">:</span>    
    <span class="n">lasso</span> <span class="o">=</span> <span class="n">Lasso</span><span class="p">(</span><span class="n">alpha</span> <span class="o">=</span> <span class="n">alpha</span><span class="p">,</span> <span class="n">fit_intercept</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
    <span class="n">lasso</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_std</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
    <span class="n">lasso_weight</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">lasso</span><span class="o">.</span><span class="n">coef_</span><span class="p">)</span>

<span class="n">lasso_fig</span> <span class="o">=</span> <span class="n">weight_versus_alpha_plot</span><span class="p">(</span><span class="n">lasso_weight</span><span class="p">,</span> <span class="n">alphas</span><span class="p">,</span> <span class="n">features</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>different alpha values: [0.01, 0.1, 1, 5, 8]
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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/cKFC68BwOeff+75888/2949x2effeZ68OBBJ7Vajc8//zzJ2tq6VjxezZyNujsAsqWU+Wa8JhERUaUIIeD/zHMYMXcx7F3diopS4si2jfj6g/eRn5OtbEAiIiIiokdEly5dcjQajfHy5cuaf/3rX39Z8VaeX375xebdd99tJKXEU089dScmJubC8OHDszQajQQAa2trGRQUlBUbG3v+6aefviOlxLvvvtvoyJEjNqWvM2nSpFu9e/fONBgMmDhxom9BQYFpC+z169ctZs6c2RAAXnvttZSePXvmmeO+awJzNuoOA3ASQjQ04zWJiIjui3fLNhgTHoGG7TqYaoknjiMyNASpiXzZOBERERFRRerVq6cbN27cTQAIDw/31ul0lT733Xff9dHpdMLDw0O3devWxLJWullaWmLz5s1JHh4eOp1OJ2bNmuVz95i1a9desbOzM/7xxx82s2fP9iypT5w4sdGdO3csGjduXLB06dLkKtxijWXORt0CAFoAS8x4TSIiovtm6+SMYe/OR5fnh5lqWWmpiJo9DWcO7lMwGRERERHRo2Hu3Lkp9vb2hmvXrll//PHH7hWfAcTHx1v+9NNPTgDwyiuv3HR1dS33GTRubm6GCRMm3ASAQ4cOOcXHx1uW/rx58+a62bNn/wkAERERXrGxsZoNGzY4//DDDy5CCKxevTrJ1ta2Vmx5LWG2Rp2U8gyK3vraXwjxgxDiSSGEnbmuT0REdD9UajV6jRyHwdPehZVN0SMtDDod9qyOwN41n0BfWKhwQiIiIiKimqt+/fqGiRMn3gSApUuXeuXn55f59tUSe/fudZCyqG/24osv3qnMPCXjpJTYt2+fw92fT58+Pa1z5845hYWFYty4cb5Tp05tBACjR49O69+/f8593NIjoUqNOiGE4V4HgN0AnAD8DcABAFlljS0+9Ga8FyIior9o0aUbRi1aDveGjU210wf2YPN7M5CVdlPBZERERERENdusWbNSnJycDCkpKVZLly71qGj8uXPnbADAyspKduzYUVuZOTp16qS1tLSUAHD+/HnN3Z+rVCqsX78+SaPRGE+fPm2Xnp5u6eXlVfjJJ5/8eb/38yio6oo6YabDnFtviYiI7snV2wcjFyxD6yd6m2qpCZexIXQykk7GKJiMiIiIiKjmcnV1NQYHB6cAwIoVK7yysrLK7ePcunVLDQCOjo56tVpdqTnUajUcHR0NAJCRkWFxrzF+fn4F3bp1M70dbtasWdednJzK3Vb7qLrnX0AlNDFrCiIiompmqdFg4JvT4N2yNQ59tQ5Ggx7anGxEh89F92Ej8fgLIyBU/P6IiIiIqLb79I0fA5XOYC7Bq/tW+7fOoaGhN//1r3/Vz8jIsFi8eHG9xYsXp5Q1tmTb6/2q6Lzvv//e4dChQ04lf46MjHSbNGnSrSpNVsNV6f9IpJRXzHWY+4aIiIjKIoSAf/9BGDF3Mexd3YqKUuLIto34+oP3kZ+TXf4FiIiIiIjqGAcHB2NISMgNAFi1apVnRkZGmUvl3NzcDACQlZVlYTAYKnV9g8GA7OxsNQC4urr+5RFp2dnZquDg4MZSSjz++OPZarVa/vrrr44RERFuVbqhGo5LB4iIqM7xbtkGY8Ij0LBdB1Mt8cRxRIaGIDUxXsFkREREREQ1z9tvv53m6elZmJWVpZ4/f379ssa1adMmHwAKCwtFXFzcX543dy8nT57U6HQ6AQBt27b9y3PtpkyZ4n3t2jVrNzc3/TfffBP/xhtvpALAe++91/DatWtV3SlaY9W6GyIiIqoMWydnDHt3Pv5vywb8/u12AEBWWiqiZk/D069MQvs+/RROSERERETV4WFsF61tbGxs5LRp025Mmzat8dq1a+u/884793wr2zPPPJMthICUEtu2bXMOCAgoc5tsiW3btjkDRbtf+vXr9z9bXH788Ue7L774oj4AfPDBB1fr169v+OCDD5J37tzpcuXKFes33nij0a5duxLMcY81hdlW1Akh1t/n8ZkQYrEQYqwQwsdcOYiIiCpLpVaj18hxGDztXVjZ2AIADDod9qyOwN41n0BfWKhwQiIiIiKimuGtt95Kb9iwYUFubq7qvffe87zXmGbNmul69eqVCQDr1q2rd+vWrYpePqFav359PQDo3bt3ZrNmzXQln2m1WvH666/7Go1GPP3003cmTJhwGwBsbW3lZ599liSEwH/+8x+XTZs2OZV1/UeRObe+jis+/l7qGHfXUfqz1wHMAPAFgCQhRKQQwtWMeYiIiCqlRZduGLVoOdwbNjbVTh/Yg83vzUBW2j2/LCQiIiIiqlMsLS0RGhqaDAAbNmzwSE1NtbzXuPnz5ydbWFjItLQ0y+HDhzcpKCgQ9xqn0+kwYsSIJmlpaZYWFhZy/vz5yaU/DwsL87p8+bLGwcHBsHbt2qulPxswYEDOSy+9lAYAU6dObXz79u1a82g3c97IPADhADIBCACJAL4qroUD+DeAhOLP7gBYDOBjAL8AUAN4GcBeIYS1GTMRERFViqu3D0YuWIbWT/Q21VITLmND6GQkneTuCCIiIiKi119//VazZs20Wq1WdezYMYd7jenZs2fe+++/fw0ADhw44BwYGNh6+/btjiUNO51Ohx07djgGBga23r9/vzMAzJ8//1qPHj3ySq7x22+/2axcudITAObNm/dn48aNdXfPs3Llyj89PDx0qamplm+99VaD6rhfJZizURcO4EkUNd1GSCmbSynHSSlnFh/jpZQtALyIomfj9QAwQ0rZC8ATAG4D8EfRSjsiIqKHzlKjwcA3p6Hv+NehUhe9zEqbk43o8Ln4NToK0mhUOCERERERkXLUajVmzZp1vaJxYWFhaStXrky0t7c3nD171vbFF19sYWtrG+Ds7NzJxsYmMCgoqMXp06ft7O3tDStXrkwMDQ1NKzlXr9fjlVde8dXr9aJbt27ZU6ZMSb/XHK6ursaPPvroKgBs3LjRY+/evXbmu1PlmLNRFwagK4DXpZTbyhokpYxGUTOuJ4q2vkJK+SuAqShabfeiGTMRERHdFyEE/PsPwoi54bB3KX4ig5Q4snUjvvlwPrQ5OcoGJCIiIiJS0NixY++0bds2r6JxwcHBty5dunT6nXfeuR4QEJDj5OSkz83NVTk6Our9/f1zp0+fnnzx4sUzwcHBt0qfN2/evPpnzpyx1Wg0xvXr1yeVN8fo0aPvDBgw4LaUEv/4xz98tVrtPbfZPkqElNI8FxLiPABfAPZSSkMFY9UAcgAkSCnbFdfsULRtNlNK6WaWUDWcECImICAgICaGW6qIiGqi3Du3sSviA1w7d9pUc6pXH4OmzkT9Js0UTEZERESPgsDAQMTGxsZKKQOVzlIXxMTEHNdoNG3atWt3XuksVLedPXu2jVarPR8YGNj5fs8154q6xgC0FTXpAKB4jBZFjb2SWi6Knl1XK5YqEhHRo8/O2QXDZi1Al8FBplrmzVRsnj0dZw7uUzAZERERERHVRuZs1GUDcBRCtKlooBCiLQAnALmlaqri2q2yziMiInrYVGo1eo0aj8Fvz4SVjQ0AQK8rxJ7VEdi3ZiX0hYUKJyQiIiIiotrCnI26Qyh6xtw6IYRjWYOEEA4APgcgARws9ZEvil5E8acZMxEREZlFi8e6Y9SiFXBr0MhUO3VgNza/9w6y0m4qmIyIiIiIiGoLczbq5qJoO2tXAH8IIeYKIfoJIdoXH/2EEPMA/AGgG4ACAPNKnT+i+OdhM2YiIiIyG1dvH4xa+BFaP9HbVEtNuIQNoZORFBerYDIiIiIiIqoNzNaok1KeBzAYRVtX6wOYDWA3gLjiYzeAWQA8i8cMkVKeK3WJdAALAXxhrkxERETmZqnRYOCb09B3/OtQqdUAAG1ONqIXv4dfo6MgjUaFExIRERER0aPKnCvqIKXcD6A1gPkAzqJoe6soPmRxbT6A1lLKvXed+7mUcvZdzTsiIqIaRwgB//6DMGJuOOxdXIuKUuLI1o345sP50ObkKBuQiIiIiIgeSWZt1AGAlDJDSvmelLIDAFsAXgC8AdhKKTsUf5Zu7nmJiIgeNu+WbTA6PAIN2/qZagmxvyMybDJSE+MVTEZERERERI8iszfqSpNSFkopU6WUKVJKvhaPiIhqHTtnFwybtQBdBgeZapk3U7F59nScObhPwWRERERERPSoqdZGHRERUV2gUqvRa9R4DH57JqxsbAAAel0h9qyOwL41K6Ev5HdVRERERERUMYuqnCSE6FX8a56U8vhdtfsipfypKucRERHVNC0e6w63Bo3x3bKFyPjzKgDg1IHdSE2Mx+CpYXD0qKdwQiIiIiIiqsmq1KgDcAhFL4f4A0Dbu2r3Qz5ABiIiohrH1dsHoxZ+hL1rPsGFXw4DAFITLmFD6GQ8+9Z0+HYMUDghERERERHVVFVtkl1FUZMt+R41IiKiOs1So8HAN6fBq0VrHN6wFkaDAdqcbEQvfg/dXxyJx4eOgFDx6RNERERERPS/qtSok1L6VqZGRERUVwkhEDBgEOo3bY6dyxcj5/YtQEoc2boRKZcvYkDw29DY2ysdk4iIiIiIahB+nU9ERFSNfFq1wejwCDRs62eqJcT+jsiZIbiZlKBgMiIiIiIiqmnYqCMiIqpmds4uGDZrAToPesFUy0xNQdSsaThzaL+CyYiIiIiIqCaplkadECJACPGOEGKlEGLdXZ9ZCSEaCSEaVsfcRERENZFKrUbv0RMweOpMWNnYAAD0ukLs+WwF9q1ZCb1Op3BCIiIiIiJSmlnfuCqE8ADwFYC/lZRQ9IKJV0oNUwH4FUB9IURbKeVFc2YgIiKqyVp07Q63ho3w3bJFyPjzKgDg1IHduJkUj0FTw+DoXk/hhEREREREpBSzragTQtgC2A/gGQA3AKwHkHv3OCmlFsBnxXMPM9f8REREjwpX7wYYtfAjtH6it6mWEn8JG0JDkBQXq2AyIiIiIqrLgoKCfIUQgXcfdnZ2/s2bN283evToRrGxsZqyzi99Tt++fZtXNN/TTz/drPQ55r2bR5M5t77+E4AfgKMA2kkpJwLIKWPsjuKfA8w4PxER0SPDUqPBwDenoc+416FSqwEA2uwsRC9+D0ejN0MajQonJCIiIqK6ysLCQrq5uend3Nz0rq6ueq1Wq4qPj9ds3LjR4/HHH2+7fv16l4qu8fPPPzsmJyeXuZMzJSVFffjwYSfzJn/0mbNRNxxF21wnSykzKxh7HoAOQCszzm82xc/QCxFCfC+EuCqEKBBCZAsh4oQQ4UIIL6UzEhHRo08IgYABgzD8vXDYu7gWFaXEL1sj8c2H86HNKev7LiIiIiKi6uPv75+bnp4el56eHpeRkRGXl5cXu23btkve3t6FOp1O/POf//Qtrwnn5eVVqNfrxfr1613LGrN+/XpXvV4vvL29C6vnLh5N5mzUtQRQCOB4RQOllBJAFgBnM85vFsUvuUgCsBzAcwAaAtACsAHQAcA7AM4KIfoolZGIiGoXn1ZtMDo8Ag3b+plqCbG/I3JmCG4mJSiYjIiIiIgIsLa2lsOGDcv68ssvEwAgPz9fFRkZWeaquqCgoFsAsHnzZreyxkRFRbkXj80wd95HmTkbdWoAhuImXLmEEGoADrjHM+xqAHXxz10AXgTgKqV0AmALYCCARAAuAL4RQngqE5GIiGobO2cXDJu1AJ0HvWCqZaamIGrWNJw5tF/BZERERERERZ566qlcW1tbIwCcO3euzGfV9ezZM9vHx6fw7Nmztvd6pl1cXJz1mTNnbL28vAr79OnDbSSlmLNRdw2AjRCiQSXGPgnACsBlM85vLrcB+Espn5NSbpdS3gYAKWWhlPIHFDXrtAAcAbyuYE4iIqplVGo1eo+egMFTZ8LKxgYAoNcVYs9nK7BvzUrodTqFExIRERFRXVeyPstgMIiyxqhUKgwbNiwDANatW/eXVXWff/55yWq6W0KIChd81SXmbNTtK/75j/IGCSFsAHyAoufZ/ceM85uFlDJTShlXzucXUPTCDADgG0mIiMjsWnTtjlGLlsOtQSNT7dSB3djy3gxkpd9UMBkRERER1WX79++3y8/PVwFA06ZNC8ob++qrr2YAwI4dO1wNBoOpbjQasWPHDtfiMenVGPeRZM5G3VIABQCmCyHeEkJYl/5QCKESQvRHUZPLH0AmgE/MOP/DVLJ/Wl3uKCIioipy9W6AkQuXofUTvU21lPhL2BAagqS4WAWTEREREVFdU1BQIKKjox3Hjx/fFCh6K+zYsWNvlXdO+/btCzp16pSbkpJitWvXLoeS+s6dOx1u3Lhh5efnl9uxY8dym311kdkadVLKKwBGo2il3HIUNbPcAEAIcRxFW0p3AfBDUUPvZSnlI9c5FUJYAHii+I9nlMxCRES1m5XGBgPfnIY+416DSl303ZA2OwvRi9/D0ejNkEajwgmJiIiIqDY6ceKEnbu7e0d3d/eObm5uHW1tbQOGDRvWIjk52UqlUuHDDz+80qxZswqfy/Lyyy9nAMC///1v0/bXkt9LPqP/VeardKtCSrlDCNEDRY267qU+Cij1+1EAb0opY8w590MUDMATgBHAV5U5QQhR1r22NlcoIiKqnYQQCBgwGPWbNMfOFeHIuX0LkBK/bI3Ejct/YEDw29DY2ysdk4iIiOiRsWzEc7XmMVZvb9lZLb0VvV4vMjIy/tIzcnJyMnz77bcXe/funVeZ64wfP/7W7NmzG+7evdslOzv7KgDs2bPHxcLCQo4fP77cFXl1lTm3vgIApJS/Syl7AGgOYCyAdwCEAZgAoI2Usvuj2qQTQnQAsKj4jyullGeVzENERHWHT+u2GB0egQZt25tqCbG/I3JmCG4mJSiYjIiIiIhqmy5duuRIKWOklDF5eXmxR44cOde/f//bmZmZ6tdee803LS2tUo8C8/DwMPTp0+dOXl6eKjIy0nnDhg3Oubm5qieffDLT09PTUPEV6h6zN+pKSCkTpJSRUsoPpZRLpJRfSin/qK75qpsQwgvANwBsAcSgqAFZKVLKwHsdAC5UU1wiIqqF7Jxd8OKsheg86AVTLTM1BVGzpuHs4QMKJiMiIiKi2srGxkZ269Ytf9euXQk9evTIunjxos3f//73xpU9f8yYMRkAsHHjRreNGze6la7RX5lt66sQwlJKWeH+5EeREMIVwF4ATQBcAvCslFKrbCoiIqqLVGo1eo+eAK8WrbDnsxUozM+HXleI3auWI/niefQZ9zosLC2VjklERERUY1XXdtHaTqVS4dNPP70aEBDQ/ocffnDZtWuX/bPPPptT0XnDhg3L+uc//6k/evSoo5QSTk5OhuHDh2c+jMyPInOuqMsUQvwohJgrhOgjhNCY8dqKEUI4AdgDoD2AqwCellKmKpuKiIjqupZdn8CoRcvh1qCRqXZq/25seW8GstJvKpiMiIiIiGqrDh06FAwcOPAWAMyZM8enMudYW1vLwYMH3zIYDDAajXjuueduaTQaWb1JH13mbNRpADwJYDaA/QDuCCF+FkIsEEL8TQhhZ8a5HorizP8B0BlACoqadFeVTUVERFTE1bsBRi5chtZP9DbVUuIvYUNoCJJOnVAwGRERERHVVqGhoSkAEBsba79z506HypwTEhKSNnHixNSJEyemTpkyhd8ql8Ocjbo2AF4HEAUgGYAVgCdQ9CKJHwDcFkIcFUIsEUIMFEI4mnFusxNC2AD4HkVvr81AUZPukrKpiIiI/peVxgYD35yGPuNeg0pd9ExfbXYWohfNwdEdWyCNRoUTEhEREVFt0r179/xu3bplAcCiRYu8KnOOv7+/ds2aNX+uWbPmz8DAQD5KrBxma9RJKf+QUn4upRwtpWyIore+vgJgA4q2jFoAeAzANBQ1wDKEEMfNNb85CSGsAOwA0AfAHQB/4xteiYiophJCIGDAYAyfsxj2Lq5FRSnxy5YN+ObD+dDmVPjoECIiIiKiSps+fXoqAPz6668O+/fvf+R2UNZk1f3W1y+klOOklE0A+AIYB+A4AAFADcC/uuavKiGEGsAmAP0BZAMYIKWMVTYVERFRxXxat8Xo8Ag0aNveVEuI/R2RM0NwMylBwWREREREVJsMHTo0q02bNnkAsGDBgkqtqqPKMdtbX8sihOgAoHfx0QuAW6mP86p7/ip4AkBQ8e+WAL4RQpQ19pqUsstDSUVERFQJds4ueHHWQvwc9W8c/34HACAzNQVRs6bh6YnBaNf7KYUTEhEREVFNFR0dnQQgqTJjz507d/7umpTyvt+oO2TIkOyqnFdbmbVRJ4o6Wv74b2OuJwBnFK2gA4AcAHsBHC4+fjfn/GZSepWhpvgoC/dVExFRjaNSq9F79AR4tWiFPZ+tQGF+PvS6QuxetRzJF8+jz7jXYWFpqXRMIiIiIiK6i9kadUKInQB6AHDAfxtzdwDswn8bc7FSyhr9VGsp5SH8Nz8REdEjq2XXJ+DesDG+W7YIGX8WvbT81P7duJkYj0FTw+DoXk/hhEREREREVJo5n1E3EEVNumwAi1C0ss5NSjlYSrlMSnm8pjfpiIiIahtX7wYYuXAZWnXvZaqlxF/ChtAQJJ06oWAyIiIiIiK6m7lfJiEAOAIIA7ARwCdCiGFCCH5lT0REpBArjQ2efWs6+ox7DSq1GgCgzc5C9KI5OLpjC6SR36MREREREdUE5mzUeaDoJQwfAzgFoDWASQC2ALghhDgnhPhMCDFCCOFpxnmJiIioAkIIBAwYjOFzFsPOxbWoKCV+2bIB3yxdAG1ujrIBiYiIiIjIfI06KWWGlPJrKWWIlNIfgDuA5wGsAHACQAsArwPYBOC6EOKCEGK1ueYnIiKiivm0bosx4RFo0La9qZYQ8xsiw0JwMylBwWRERERERGTura8mUso7UsrvpZRvSyk7A3AFMAzAcRRtkW0JYGJ1zU9ERET3ZufsghdnLUTnQS+YapmpKYiaNQ1nDx9QMBkRERERUd1mtre+3osQwgZANwC9i4+uAKyqc04iIiKqmEqtRu/RE+DVohX2fLYChfn50OsKsXvVcty4dAFP/v01WFhaKh2TiIiIiKhOMWujTghhB+AJ/Lcx1xlAyX/li+KfaQB+BnC4+CAiIiKFtOz6BNwbNsZ3yxYh48+rAIC4fT8gNTEeg6aEwtGd74MiIiIiInpYzLb1VQhxFMBtAD8ACAXQHUWr526g6IUS/wDQTkpZX0o5TEr5iZTylLnmJyIioqpx9W6AkQuXoVX3XqZayuWL2BAagiunTiqYjIiIiIiobjHnM+oeQ9EKvasANgB4FUALKWUDKeVIKeW/pJTnzTgfERERmYmVxgbPvjUdfca9BpVaDQDQZmdh+6LZOLpjC6TRqHBCIiIiIqLaz5xbX8cCOCylvGbGaxIREdFDIoRAwIDBqN+kOb5fEY7c27cAKfHLlg24cfkPDAieCo2dvdIxiYiIiIhqLbOtqJNSRrJJR0RE9Ojzad0WY8Ij0KBte1MtIeY3RIaF4GZSgoLJiIiIiIhqN3NufSUiIqJaws7ZBS/OWojOg14w1TJTUxA1axrOHj6gYDIiIiIiotqLjToiIiK6J5Vajd6jJ2DQlFBYamwAAHpdIXavWo79az+FXqdTOCERERERUe3CRh0RERGVq+XjPTBq0Udw9WloqsXt+wFb5r6DrPSbCiYjIiIiIqpd2KgjIiKiCrn5NMSoRR+hVbeeplrK5YvYEBqCK6dOKpiMiIiIiKj2YKOOiIiIKsVKY4NnJ89An79PhEqtBgBos7MQvWgOjn29FdJoVDghEREREZnLhg0bnIUQgUKIwCeeeKJFZc/Ly8sTy5Ytc3/mmWea+fj4+Nna2vpbWVkFuLu7d3z88cdbTp482fvYsWM2ZZ1fMmdljvT0dLV57rbmsFA6ABERET06hBAIGPg86jVtjp0rliD39i1IacT/bf4KyZcuYEDwVGjs7JWOSUREREQP6KuvvnIr+f3o0aOO8fHxls2aNSv3IcWbNm1yCgkJaZyWlmZZUrO2tpY2NjbG27dvWxw7dszh2LFjDh9//LFX9+7ds7Zv357o5eWlv9e17O3tDdbW1rK8+VQqVbmfP4q4oo6IiIjuW4PW7TAmPAIN2rQ31RJifsPGsCm4mZSgYDIiIiIielApKSnqQ4cOOWk0GuOgQYNuGY1GrFu3zq28c5YvX+4+ZsyY5mlpaZa+vr7aFStWJCUlJZ3SarWxmZmZJwsKCmJ+/vnn89OnT0/28PDQHTlyxDExMdGyrOstXLjwWnp6elx5h6ura63b0mG2Rp0QopcQ4vH7GP+YEKKXueYnIiKih8vO2QXDZi1A4HP/z96dR0ddHfwff9+ZTFYgCQlbVlzYSQjEpVoXfOUQGQYAACAASURBVFptq2C1Vvt7irgv9WkrrhUXbPs8QrWtKGrriloX1NalbrjXqrR1Y0uILKKQBBKWJCQh2ySTub8/JowISWSSyXyzfF7nzIHcuTPfDxyPZ/jMvd97enCsens5T827lqL33nEwmYiIiIh0x+LFi1N8Pp/57ne/W33ZZZftBHj66ac7LOqWLVsWf91112X5/X6+853vVBcVFX02Z86cyuzs7OAKvKioKI455piG3//+9+UlJSWFl19+eXl0dHS/WxHXXeFcUfdP4LkQ5j8D/COM1xcREZEIc0dFMX32hcy8ci6e2MCtRnzNXl7/8x28/dCf8bV0ujtCRERERHqhp556KgVg1qxZVd/73vfqRo0a1bxp06bYd999N769+TfeeGNaS0uLSUtLa37uuec2xcfHd1rAxcbG2kWLFpUddthhTT2Rvy8L99ZX08PzRUREpBca+61jmLVgIUPTM4Njq99ayjO/uY7aip0OJhMRERGRUHz66aexRUVF8UlJSb7TTz+91uVycdppp1UBPPzww6n7zt+4caPn/fffTwS45JJLticmJva77aiR5OQ96gYDzQ5eX0RERMIoJT2TWQsWMu6oY4Nj2zZu4Im5cyguWOVgMhERERE5UA899FAqwCmnnLJrz2EO5513XhXAyy+/PLSpqelri67efPPNwXt+f/rpp9dEMmt/5EhRZ4w5AhgKbHXi+iIiItIzomPjOGXOrzjh3Itxud0ANO6u5bkFN/PRC3/F+vUFq4iIiEhv5fP5eP7554cCzJ49u2rP+BFHHNE4ZsyYxpqaGvfTTz+duPdr1q5dGweB010nT57sDVeWG2+8MTM1NXVKR48f//jHo8N1rd4kqqsvNMacC5y7z/BQY0xn950zQBIwEbDAa129voiIiPROxhimnfxDhh98KK/ceRv1u6qw1s+ypx+j7PN1/ODnVxGbMMjpmCIiIiKyj+eff37Izp07PWlpac0nnnhi3d7PnXnmmVULFixIf+yxx1LPO++86j3jVVVVboDBgwf7XK7214Ndd911IxcvXjxi3/GZM2dWPfLII6Xtvaaurs5dV1fX3lMAVFdXuw/sT9W3dLmoA0YD0/cZi25nrCPvAzd34/oiIiLSi2WMn8TsWxfxyp23sWXtGgC+XP4xT15/JTOvup7how92OKGIiIgMRFvmfpDvdIZwybj12OXhfL/HHnssFeC0006r2rd0O++886p+97vfpb///vtDysrKotLS0nwH+r67d+92V1ZW7tdB1dbWdli2LVq0aPPll19eGUL8fqE7W1//Dpzf9rigbaxmr7H2HucCpwNjrbXTrbW7unF9ERER6eUSkpL58U23kD/j9OBY9fZynpp3LUXvveNgMhERERHZW2Vlpfvtt99OAjj33HOr9n1+zJgxzfn5+XWtra1m8eLFQ/eMDx06tBVg9+7dUf4ObnPy5z//eau1dvmex6mnnrrf+0tAl1fUWWtXA6v3/GyMeRhotNb+JRzBREREpH9wR0UxffaFpI0Zx+v3LqKlqRFfs5fX/3wH5Z+vZ/q5FxPl8TgdU0RERGRAe+SRR5K9Xq8BOPLIIyd2Nvepp55KmTdv3g6ACRMmNAJ4vV6zZs2amNzc3LDdp24g6s7W16+x1jp5gqyIiIj0cmO/dQwpmdm8dPsCqrYGbkWy+q2lbN+0kZlXXs+Q1GEOJxQREZGBINzbRfuLJUuWpB7o3LVr18Z//PHHcUcccUTjSSedtHvP+AsvvJCYm5u7o2cSDgwq10RERCRiUtIzmbVgIWOPOjY4tm3jBp6YO4figlUOJhMREREZuNasWROzcuXKBIB///vfn+3cuXNVR48TTjihBuChhx5KATj00ENbjjvuuBqABx54YERNTY26pm7okb88Y0ymMeb7xpj/Nsac09mjJ64vIiIivVd0bBwz5vyK6edcjMsduH9w4+5anltwMx+98FdsB/c2EREREZGe8eCDD6YAjBs3rvGoo45qTE1Nbe3occYZZ1QBvPDCC0N9vsB5EvPnzy/zeDy2rKws+owzzjiooaHBOPjH6dPCWtQZY440xnwIbAZeBZ4AHvmGh4iIiAwwxhjyT/khZ968gISkZACs9bPs6cd48fb5NNXXOZxQREREZGDw+/08++yzKQAzZsz4xkM/f/KTn9RERUXZiooKz3PPPZcIcMwxxzTcdtttJS6Xi3feeSdp0qRJE++8886U4uLi4I2I/X4/RUVFMfPmzRvx/vvvD+m5P1HfZqy14XkjY/KB94FYwABbgK1AU2evs9aeEJYAfZAxZvm0adOmLV+u7fEiIjJw1e2q4pU7b2PruqLgWNKIUZx69Q0Myz7IwWQiIiLdk5+fz4oVK1ZYa/OdzjIQLF++/NPY2NgJkyZNWut0lr7k5ZdfHnzqqaeOBfjkk0+KDjvssE57HIBjjz12zLJly4acfPLJu1599dUv94wvWbIkcc6cOdkVFRXBgi4mJsbGxcW1NjQ0uJubm4Mr7Y477riau+66q3TKlClfO3yirV9i0KBBrTExMZ2WVk899dTGE088sf7A/7SRUVRUNKGpqWltfn7+YaG+NmyHSQC/AeKAQuB8a+2KML63iIiI9FODkody5rz5fPDUX1j+ygsAVG8vZ8lN13DixT9n4nH/5XBCERERkf7r0UcfTQHIzs72HkhJB3DaaaftWrZs2ZC33347qaKiwp2amtoK8NOf/rTm1FNPLbz//vtT3njjjcSioqL4qqqqqPr6endiYqLvoIMO8h555JF15513XmV+fn6n16qrq3PX1XW+y8Lr9fa7++GFc0VdJZAETLHWrgnLm/ZzWlEnIiLydRs+XMbr9y6ipakxODblxJOZfu7FRHk8nbxSRESk99GKusjSijrpLbqzoi6czWMsUKeSTkRERLpq7LeOYdaChQxNzwyOrX5rKX/9zVxqK3Y6mExEREREpOeFs6jbCMQYY8K5nVZEREQGmJT0TGYtWMjYo44NjpVvXM8Tc+dQXLjKwWQiIiIiIj0rnEXdI0A08MMwvqeIiIgMQNGxccyY8yumn3MxLrcbgMbdtTw3/2Y+euGvWL/f4YQiIiIiIuEXzqLuLuAN4D5jzFFhfF8REREZgIwx5J/yQ868eQEJSckAWOtn2dOP8eLt82mq7/zmwiIiIiIifU04t6neBHwCHAksM8Z80Pbz7s5eZK393zBmEBERkX4mY/wkzr51Ea/ceRtb1xUB8MWnH/Hk9Vdy6tU3MCz7IIcTioiIiIiERziLut8AFjBtPx8HHNvh7MA8C6ioExERkU4NSh7KmfPm88GSR1n+6t8BqN5ezpKbruHEi3/OxOP+y+GEIiIiIiLdF86i7jECxZuIiIhI2Lmjoph+zkWMGjOeN+5bREtTI75mL6/9aSFlG9Yx/dyLifJ4nI4pIiIiItJlYSvqrLXnheu9RERERDoy7qhjSM3M5qWFC6jaWgrA6reWsmPTF8y4ci5DUoc5nFBEREREpGvCeZiEiIiISESkZGQya/7tjP3WMcGx8o3reWLuHIoLVzmYTEREREQGMmu7t9lURZ2IiIj0SdFx8cy44jqmn3MRxhX4SNO4u5bn5t/MRy/8Fev3O5xQREREIqwFsH6/33zjTJEeYq3dcyaDryuvD3tRZ4w5yBhzlzFmrTGmzhjj2+f5JGPMzcaYecYYd7ivLyIiIgOHMYb8U07jrJsXkJCUDIC1fpY9/Rgv3j6fpvo6hxOKiIhIBJVba70NDQ1xTgeRgaupqSnaWtsC7OzK68Na1BljTgcKgJ8D44B4vjoFFgBrbTVwAoFTYr8bzuuLiIjIwJQxYTJn37qI9PGTgmNffPoRT95wJTuLNzmYTERERCLon62trbVVVVXJ3d1+KNJVtbW1g/1+fz3wSVdeH7aizhgzHngSSADuA44FKjqY/gCBAu+McF1fREREBrZByUM5c9588k85LThWva2cJTddw2cfvOtgMhEREYmQpT6fb0dtba2ntLQ0va6uLt7v9xuVdtLTrLX4fD5XRUVFcmVlZbLP56sE3unKe4Xt1FfgWiAW+KO19lcAxpjWDua+3fbrt8N4fRERERng3FFRTD/nIkaNGc8b9y2ipakRX7OX1+65nbIN6zjh3ItwR3mcjikiIiI9ID8/f+Py5cuv8nq9C3ft2jW8trZ2hDEmhn12+on0EL/f76/3+Xyl1tq/5Ofn/6srbxLOou47BG6W94dvmmit3WmMqQMyw3h9EREREQDGHXUMqZnZvLRwAVVbSwFY/ear7PhyIzOvup7BKakOJxQREZGekJ+f/6/ly5f/1Ofznezz+U4ARgLRTueSAcELrAOeBd7s6puEbQmoMaYJaLLWJu01Vg4Mt9bud2iEMaYSSLDWxoYlQB9kjFk+bdq0acuXL3c6ioiISL/U3NjAG/fdxYYPlwXH4oYkMmPOr8iaPMXBZCIiMhDk5+ezYsWKFdbafKeziEjfEM7DJOqBBGPMN67SM8YkA0lAVRivLyIiIvI10XHxzLjiOqafcxHGFfjY01hbw7O3zOOjv/8N3bNGRERERHqTcBZ1RW3vd8QBzJ1NYI+4lpKJiIhIjzLGkH/KaZx18wISkpIBsNbPsqf+wot/nI+3od7hhCIiIiIiAeEs6v5KoHy7pbNVdcaY44EFBO5n92QYry8iIiLSoYwJkzn71kWkj58UHPvi0w954vor2Fm8ycFkIiIiIiIB4Szq7gcKgOOBD4wxswEPgDFmkjHmLGPM0wROfI0H/gU8E8bri4iIiHRqUPJQzpw3n/xTfhgcq95WzpKbruGzD951MJmIiIiISBhPfbXWthhjvg+8BBzJ17fAFuz1ewN8CPzI6sYwIiIiEmHuqCimn3Mxo8aM5417F9HibcLX7OW1e26nbMM6Tjj3ItxRHqdjioiIiMgAFM4VdVhrtwFHA5cA/wZaCBRzBvADHwOXAcdZayvCeW0RERGRUIw76lhmLbiDoWkZwbHVb77KM7+ey+5KfUwRERERkcgLa1EHYK31WWsfstYeCyQAI4BRQJy19ihr7f3WWl+4rysiIiISqpSMTGYtWMjYbx0THCvfuJ7H586hZM1qB5OJiIiIyEAU9qJub9baVmvtTmvtdpVzIiIi0htFx8Uz44rrOH72hRhX4KNRY20Nz94yj4/+/jd0pw4RERERiZQeLepERERE+gJjDIfNOJ2z5i0gISkZAGv9LHvqL7z4x/l4G+odTigiIiIiA0GXDpMwxhzX9tsGa+2n+4yFxFr7fldeJyIiIhJuGRMnc/ati3jlzlvZuu4zAL749EOeuP4KTr36RoZljXY2oIiIiIj0a6Yr2zmMMX7AAuuttRP3GQuFtdaG7eTZvsYYs3zatGnTli9f7nQUERER2Uurz8cHSx5h+asvBseiomM46ZJfMOHYExxMJiIifUl+fj4rVqxYYa3NdzqLiPQNXS3JSgiUcmXtjImIiIj0ae6oKKafczGjxoznjXsX0eJtwtfsZek9t1P2+Tqmn3MR7iiP0zFFREREpJ/pUlFnrR19IGMiIiIifdm4o44lNXM0L90+n6qyLQCseuNVtn+5kZlXXs/glFSHE4qIiIhIf6LDJEREREQ6kZKRyawFCxn7rWOCY+Wfr+fxuXMoWbPawWQiIiIi0t+oqBMRERH5BtFx8cy44jqOn30hxhX4+NRYW8Ozt8zj4xefpSv3/BURERER2VfYijpjzFBjzDnGmJkHMPfUtrlJ4bq+iIiISE8yxnDYjNM5a94CEpKSAbDWzwdLHuWl2+fjbah3OKGIiIiI9HXhXFF3DvAIMO0A5h7XNvfsMF5fREREpMdlTJzM2bcuIn38xODYxk8+5Inrr2BnyWbngomIiIhInxfOou70tl//dgBz/wIY4EdhvL6IiIhIRAxKHsqZ8xaQf8oPg2PV28pZcuPVrP3gXQeTiYiIiEhfFs6i7hDAD2w4gLnr2uYeGsbri4iIiESMOyqK6edczIwrrsMTEwuAr9nL0ntu552H76XV1+JwQhERERHpa8JZ1KUCtdZa3zdNtNa2ADXA8DBeX0RERCTixh11LLMWLGRoWkZwbNUbr/LMb+ayu7LCwWQiIiIi0teEs6jbBSQaY4Z800RjTCKQSKCsExEREenTUjKymLVgIWOP/HZwrPzz9Tw+dw4la1Y7mExERERE+pJwFnXLCdx3bvYBzJ3ddu1VYby+iIiIiGOi4+KZceVcjp99IcYV+IjVWFvDs7fM4+MXn8Va63BCEREREentwlnUPU6gqLvNGHNiR5OMMScBtwK27TUiIiIi/YIxhsNmnM5Z8xaQkJQMgLV+PljyKC/dPh9vQ73DCUVERESkNwtbUWetfQZ4B4gHXjPGvGKM+bkxZmbb4xfGmKXA0rY571lrnwjX9UVERER6i4yJkzn71kWkj58YHNv4yYc8ecOV7CzZ7FwwEREREenVwrmiDuAMAkWcCzgZuAv4e9tjEfD9tudeA04P87VFREREeo1ByUM5c94C8k/5YXBsV3kZS266mrUfvOtgMhERERHprcJa1Flra621M4BTgGeAEsDb9ihpGzvFWnuKtVYHSYiIiEi/5o6KYvo5FzPjiuvwxMQC4PN6WXrP7bzz8H20+locTigiIiIivUlUT7yptfY1AqvmpA+zfj/ejRuJHTvW6SgiIiJ92rijjiU1M5uXbl9AVdkWAFa98QrbN21k5hVzGZyS6nBCEREREekNwr31VfoJay3b5y9g84/PZPc/tD1HRESku1Iyspi1YCFjj/x2cKx8wzoenzuHkjUFDiYTERERkd5CRZ20q/Khh9j15JPY5ma2XH45Na++6nQkERGRPi86Lp4ZV87l+NkXYlyBj2GNtTU8e8tNfPzis1hrHU4oIiIiIk7q0tZXY8w5bb+tsda+uM9YSKy1j3XldT3JGDMYOAE4HDis7deUtqcnWGvXOZUtUob84GSq//o3WkpLweej7Jpr8Tc0kHzmmU5HExER6dOMMRw243RGHjyGl++8lYaaaqz188GSRyn/fB3f/58riYlPcDqmiIiIiDjAdOWbW2OMH7DAemvtxH3GQmKtdYccoIcZY04DXujg6bAVdcaY5dOmTZu2fPnycLxd2LVs30HJhRfQvPGL4NiI6+cy9NxzHUwlIiLSf9RVVfLynbdRtv6z4FjyqDRmXnUDw7JGOxdMRETCIj8/nxUrVqyw1uY7nUVE+oauHibxPoFSrqSdsf5iB/Ap8AmwFXjA2TiR5xkxnOzHH6f0woto+izwD4jtv7uV1vp6Ui+7DGOMwwlFRET6tkFDUzjr5gW8/+QjrFj6IgC7ystYctPVnHTxL5hw7AkOJxQRERGRSOrSirr+zhjjtta27vXzaGBT248DZkXdHq27d1N66c9oXLEiODb0wgsYfs01KutERETCZN2/3+fN++6ixdsUHMv73gymn3Mh7iiPg8lERKSrtKJORELVpcMkjDE3G2OuDHeY3mLvkk7APXgwWQ89SMLRRwXHqhY/zLbf/hbr9zuYTEREpP8Yf/RxzFqwkOS0jODYqjde4ZnfXs/uygoHk4mIiIhIpHT11NffANfuPWCM2WSM+bDbiaRXcsXHk3HvvQz6zneCY9VPP0PZ3LlYn8/BZCIiIv1HSkYWs+YvZMyRRwfHyjes4/G5cyhZU+BgMhERERGJhK4Wdbad12YDWd2LI72ZKyaGjDvvYMiMGcGx2pdeZuuVV+JvbnYwmYiISP8REx/PzCuv5/izL8C4Ah+3GmtrePaWm/j4xWfRbUtERERE+q+uFnVVQIoxZnA4w/RXxpjl7T2A8U5nC5XxeEi77VaSzjorOLb7rbfZctn/4G9sdDCZiIhI/2GM4bCZP+LMefOJT0wCwFo/Hyx5lJduX4C3od7hhCIiIiLSE7p66uuHwMnAS8aYvwF1beNxxphzQnkja+1jXcwgDjFuNyN/+xtcCQlUPfIIAPX/+hclF11M5n334h6s/lZERCQcMifmMPvWRbx8522UrQ+cwL7xk//w5A3FnHrVDaRmjXY2oIiIiIiEVZdOfTXGHA68C8QT2AYLYPb6/QGz1rpDDhBhA/3U145Ya6n405+puOee4FjspElkPvQgUcnJDiYTERHpX1p9Pt5/8hFWLH0xOBYVE8NJl/ySCcdMdy6YiIh0Sqe+ikiourSizlr7iTEmD7gEmATEAdOBFuA/YUsnvZoxhmG/+DmuhAR23HYbAE1FRZSccw6ZixfjGT7c4YQiIiL9gzsqihPOvZhRY8bx5n130eJtwuf1svTuP1L++XqOn30B7iiP0zFFREREpJu6uvUVa+1G4Fd7fjbG+IEqa+0J4QgmfUfK+efhio9n229+A9bi/XwjxWfPJvuRh/GkpzsdT0REpN8Yf/RxDMsazYu3L2BX2RYAVr7+Mtu+/JyZV85l8NBUhxOKiIiISHd06TAJY0yWMWbfBqYYKO1+JOmLkn9yFmm//z24AzuZW0pK2DzrbLybNn3DK0VERCQUKRlZzJq/kDFHHh0cK9+wjifmXkHJmgIHk4mIiIhId3X11NfNwMf7jD0KPNOdMNK3Jc6cQcZdizCewNYb37ZtFJ89m6b16x1OJiIi0r/ExMcz88rrOf7sCzCuwMe5hppqnr3lJj5+8Vm6cg9iEREREXFeV4s6CBwesbdfA1d34/2kHxj8ne+Qef99mLg4AForKymefQ6Nq1c7nExERKR/McZw2Mwfcea8+cQnJgFgrZ8PljzKS7cvwNtQ73BCEREREQlVV4u6RiCxnfF9y7s+yxiTuucB7H2EadLezxljulN29ksJRx9N1uLFuAYPBsBfW0vJ+RdQ/9G+izBFRESkuzIn5jD71kWkjZsYHNv4yX948oYrqSjZ7FwwEREREQlZV0umDUCsMeZyY0x8OAP1Ijv3eqzYa/w/+zyXFflovV/8tKlkPfoI7uRAx+lvaKD0kkvY/c9/OhtMRESkHxo0NIWzbl7AtB+cGhzbVV7Gkzddzdpl/3QumIiIiIiEpKtF3WICq+fuAHYbY1rbxkcYY1pDePjC8qeQXilu0iSyH3+MqOHDAbBeL1t+8UtqX3/d4WQiIiL9jzsqihPOu4RTLr8WT0wsAD6vl6V3/5F/PHI/rb4WhxOKiIiIyDfpUlFnrb0HmAdUECjs9mx5NSE+eu22UWutOcDHZqez9mYxhx5K9pNP4ElvOyTY52PrVVdT/dzzzgYTERHpp8Z/+3h+Ov92ktMygmMrX3+ZZ357PburKhxMJiIiIiLfpMtFmbV2vrV2BDACOKhteGfb70N5SD8XnZlJ9pIniT744MCA30/5jTdS9fgTzgYTERHpp1Izs5k1fyFjjjg6OFa+YR1PzL2CkjUFDiYTERERkc50e0WbtXantba47cdWa21xKI/uXl/6Bs+IEWQ//hgxEyYEx7bPn0/Fffc7mEpERKT/iomPZ+ZV13P82RdgXIGPfA011Tx7y018/OKzWGsdTigiIiIi+wrn1tMTgDPC+H7Sz0SlpJD9l0eJy8sLju2880523L5Q/1gQERHpAcYYDpv5I86cN5/4xCQArPXzwZJHeXnh7/A2NDicUERERET2Fraizlr7nrX2P+F6P+mf3EOGkLX4IeKP+lZwrPLBB9n+f7dg/X4Hk4mIiPRfmRNzmH3rItLGTQyOff7xv3nyhiupKNUGBxEREZHeIuyHORhjDjLG3GWMWWuMqdv3ZFdjTJIx5mZjzDxjjDvc15fez5WQQOZ99zHohBOCY7uWLKH8+huwPh0ELCIi0hMGDU3hrJsXMO0HpwbHdpVv5ckbr2Lp3X+k6L13qKuqdDChiIiIiJhwbjk0xpwOPAbE89VJsNZa695n3rvAccDJ1to3whagjzHGLJ82bdq05cuXOx3FEbalhbLr5lK7dGlwbPCJJ5J2+x9xRUc7mExERKR/W/ev93jz/rtp8Tbt91xKRhbZOXlk504lY+JkomPjHEgoItI/5Ofns2LFihXW2nyns4hI3xAVrjcyxowHngRigXuBJcALQEo70x8AjidwT7sBW9QNdMbjIe0Pv8eVEE/1354FYPdbb7Hl578g465FuOL0DwMREZGeMP7bx5OaNZpXF/1+v62vlVtKqNxSworXXsLldjNqzHiyc/PIzpnKyEPG4HJrQ4SIiIhITwnbijpjzGLgfOCP1tpftY2VA8PbWVE3DNgOrLXWTgpLgD5ooK+o28Nay45bb6PqL38JjsUfdhgZ992Le9AgB5OJiIj0b9bvZ8fmL9lcsJKSwpVsXfcZrZ3chiImPoHMSbltK+7ySBqZhjGmw/kiIgOdVtSJSKjCWdRtBjKBkdbanW1j7RZ1bc/VAlhrh4QlQB+kou4r1loq7r6Hij//OTgWm5ND5gP3E5Wc7GAyERGRgaPF28TWtUUUr1lNccFKdhZv6nT+kGHDg9tksyZPIW7wgP1YJyLSLhV1IhKqcBZ1TUCTtTZpr7HOirpKIMFaGxuWAH2Qirr9VS5+mB1/+EPw55gxY8h6eDFRw4Y5mEpERGRgqq/eRcma1RQXrKK4cGXnh00Yw4iDDiErJ4/snDzSx00kSvecFZEBTkWdiIQqnEVdJTAEiLPW+trGOtr6mgxUANuttWlhCdAHqahr366nn2Hbb38Lbf9terKzyH74YTzp6Q4nExERGbistVSVbQmWdqVFhbQ0NXY4Pyo6hvTxE8nOnUp2Th7DskZjXK4IJhYRcZ6KOhEJVdgOkwCKgG8DRwD//oa5swmcCquGSvaT/P9+gis+jrLrb4DWVlqKS9h89myyH3mY6NGjnY4nIiIyIBljSEnPJCU9k2k/mEmrz0f5xvWUFK6iuGAV5RvXY/3+4Hxfs5figpUUF6wEID4xiazJU4JbZQenpDr1RxERERHptcK5ou4XwF3AP4GTrLW+9lbUGWOOB14F4oBZ1tqnwxKgD9KKus7tfvtttl55R3YLowAAIABJREFUFbalBQB3aipZix8idtw4h5OJiIjIvrwN9ZQWFVJcuJLiglXsKt/a6fyhaRmBe9vl5JE5MYeY+PgIJRURiRytqBORUIWzqPMAnwA5wMfAn4E7gGQgF5gE/Ag4A3ADy4DjbbgC9EEq6r5Z3b/+xZZf/BLbGNha40pMJOvBB4jLzXU4mYiIiHSmtmIHxW2r7UoKV9G4u7bDuS63m5GHjguutht16Fhc7v1ucSwi0ueoqBORUIWtqAMwxowEXgIOAzp6YwN8CJxqra0I28X7IBV1B6Zh+XJKL/0Z/ro6AFzx8WTcdy8JRxzhcDIRERE5ENbvZ0fxpsBW2MJVbF1XRGvbivn2RMfFkzkpJ1jcJY9KxxgTwcQiIuGhok5EQhXWog7AGBMFnAecCxwO7DnuqxX4FHgUWLznwImBTEXdgWtcU0TpRRfRWl0NgImJIePuuxh03HEOJxMREZFQtTR7KVu3NrhNdsfmLzqdPzhlGNm5gdNks3LyiB+SGKGkIiLdo6JOREIV9qLua29ujBsYCriASpVzX6eiLjTezz+n5IIL8e3cGRjweEj/wx8Y8v3vORtMREREuqWhtiZwKEXhaooLV7K7Ymen84eNPji42i59/EQ80TERSioiEhoVdSISqh4t6qRzKupC11xSQsl559NSVhYYcLkYNX8+Saef5mwwERERCQtrLbvKy4Kr7UqLCmhubOhwvtvjIX38pEBxl5PH8NEHY1yuCCYWEemYijoRCVVPr6iLA1Lbfqyw1jb22MX6IBV1XdOybRsl519A86ZNwbER825i6KxZDqYSERGRnuBvbWXbFxsoLlhFceFKyj9fj7+1tcP5cYOHkDV5Ctm5U8nOzWNI6vAIphUR+ToVdSISqp64R91Q4HLgLGAsgcMjIHC4xAbgGeAua+2usF64D1JR13W+ykpKLrwI77p1wbFhV11F6iUXO5hKREREelpzYwOlnxUGiruClVSVbel0fvKodLJy8sjOzSNrUi4x8QkRSioioqJOREIX7lNfjwD+Dozgq4JuXxbYBpxurf04bBfvg1TUdU9rTQ2ll1xK4+rVwbGUSy5h2JVX6GQ4ERGRAWJ3ZQXFhYHSrmTNahpqqjuca1wuRh46luycwGq7UYeOwx0VFcG0IjLQqKgTkVCFragzxowAPgOSgV3AfcA/gD1fc2YA3wEubZtTCUy21m4PS4A+SEVd9/nr6yn9+S9o+PDD4FjyrFmMuPEG3Z9GRERkgLF+PztLNlNcuIqSwlVsWVuEr9nb4XxPbByZEycHtsnmTGVoeoa+7BORsFJRJyKhCmdRdztwJVAAnGSt3dHBvBHAm8Bk4A5r7TVhCdAHqagLD7/Xy9Y5V1D3z38GxxJPP51R//e/GH1LLiIiMmD5mpsp27CW4oKVFBeuYvumL6CTz76DhqYEV9tlTZ5CQlJyBNOKSH+kok5EQhXOom4dMAY43Fq74hvm5gOfABustePDEqAPUlEXPralhbLrrqN26WvBscHf+x7pf/g9JjrawWQiIiLSWzTurqVkTUHwRNnanZ1v7BiWNZqs3KmMzskjfcIkPDGxEUoqIv2FijoRCVU4i7oGoNlam3SA82sAj7U2PiwB+iAVdeFlW1spv/lmap57PjiWcNyxZNx1F65YfbAWERGRr1hrqd5eHjyUorSoAG9DfYfz3VFRpI+fSNbkPLJzpzL8oINxudwRTCwifZGKOhEJVTiLumogGkiw3/CmxhgXUEcIxV5/pKIu/Kzfz/Zbb2XXY48Hx+IPP5yMe+/FPUinvImIiEj7/K2tbP9yY3CbbNmGdfhbfR3Ojx00mKzJU8jOzSM7ZyqJw0dEMK2I9BUq6kQkVOEs6j4EDgfOtNY+/w1zzwD+BnxirT0yLAH6IBV1PcNay8677qLy3vuCY7G5uWQ9cD/upAHbC4uIiEgImpsa2fLZmmBxV7mlpNP5SSNGBUu7zMm5xCYMilBSEenNVNSJSKjCeaf9vwJHAA8YY3Zba99qb5Ix5lTgAcACT4Xx+iIAGGMYPmcO7oQEdvzxdgCaCgooPudcsh5eTFRqqsMJRUREpLeLjo3j4GmHc/C0wwGoq6qkuHBV8ETZ+updX5tfvb2c6rfKWf3WaxjjYuQhY4LF3aix43BHeZz4Y4iIiEgfE84VddHAh0AegRLuU+BdYCsQA2QDxwOTAAOsBI6y1jaHJUAfpBV1PW/XU0+x7bf/G/w5OjubrEcexpOW5mAqERER6custVSUFlNS2HZ/u7Vr8Hm9Hc73xMSSMXFy8ETZlIwsjDERTCwiTtGKOhEJVdiKOgBjTCrwOPC9tqF933zPJ5LXgXOstRVhu3gfpKIuMmpefJGyG26E1lYAotJGkf3ww0SPHu1sMBEREekXfC0tlG9YG1hxV7CSbV9uhE4+Yw9KHkpWTh7ZOXlk5eQxKHloBNOKSCSpqBORUIW1qAu+qTHHAD8GpgHD2oZ3AiuAZ621y8J+0T5IRV3k1L71FluvuhpaWgBwp6aStXgxsePGOpxMRERE+pvGut2UFhUE729Xs31bp/NTM7OD22QzJkzGo9PqRfoNFXUiEqoeKerkwKioi6y6D5ax5Ze/xDY1AeBOTCTzoQeJy8lxOJmIiIj0Z9Xbt1FcsJKSwlWUrFlNU31dh3Nd7ijSxo0PbpMdcfChuFzuCKYVkXBSUScioVJR5yAVdZHX8OmnlF76M/z19QC4EhLIvO9e4g8/3OFkIiIiMhD4/a3s+PKL4DbZrevX4m/1dTg/NmEQmZNzA8VdTh5JI0dFMK2IdJeKOhEJVbeKOmPMdOA4YLe19o4DfM1VwCDgHwN9C6yKOmc0Fq6h9KKLaK2pAcDExpJx910MOvZYh5OJiIjIQNPS1MSWtWuCJ8pWlGzudH7i8BHB1XaZk6cQN2hwZIKKSJeoqBORUHW5qDPGxAIbgVHAT6y1zx7g684EngE2AeOttS1dCtAPqKhzTtOGDZRceCGtO9vOM/F4SP/jHxnyvZOcDSYiIiIDWn31ruBqu+LCVdTvqup4sjGMPPhQsnOnkjU5j7RxE4jyeCIXVkS+kYo6EQlVd4q6WQROeH3XWvudEF/7LoGVeP9trf1rlwL0AyrqnNVcXEzx+efjKysPDLhcjFown6TTTnM2mIiIiAhgraVqa2mwtCstKqTF29Th/KiYGDImTCY7J4/s3KmkZmZjjIlgYhHZl4o6EQlVVDdeexpggXu68Nq7geOBM4ABW9SJs6Kzsxn95JOUnH8BzZs3g99P+dzr8Tc0MPSnP3U6noiIiAxwxhhSMrJIychi2sk/pNXXQvmG9RQXBoq7bRs/x1p/cL7P62XzquVsXhX4Ejg+MSlY2mXn5DFoaIpTfxQRERE5QN1ZUfclkA0kWWt3h/jaIUA1sMlae0iXAvQDWlHXO/gqKii54EK8GzYEx4ZdfRWpF1/sYCoRERGRzjXV11FaVEBxwSqKC1dSva280/kpGVnB4i5j4mSiY+MilFRk4NKKOhEJVXeKujrAZ61N6uLrawC3tXZQlwL0Ayrqeo/W6mpKLr2UptUFwbGUSy9l2BVztGVERERE+oSaHduDh1KUrFlN0+7aDue63G5GjRlPdm4e2TlTGXnIGFxudwTTigwMKupEJFTdKerqgVZr7ZAuvr6WQFGX0KUA/YCKut6lta6eLf/zPzR8/HFwLHn2bEZcPxfjcjmYTERERCQ01u9nx+Yv2VywkpLClWxd9xmtPl+H82PiE8iclNu24i6PpJFp+rJSJAxU1IlIqLpT1BUDGUCqtXZXiK9NBiqBUmttdpcC9AMq6noff1MTW+bMof6994NjiT/6EaP+738x+pZZRERE+qgWbxNb130WPFF2Z/GmTucPGTY8uE02a/IU4gZ36bt5kQFPRZ2IhKo7h0msJlDUfR94KsTXntz2a0Gns0QizBUbS+bdd7P1V9ex+/XXAah5/nn8DQ2k//42THS0wwlFREREQueJiWX0lGmMnjINgPrqXZSsWR28v11dVeXX5tfu3EHhP96k8B9vgjGMOOgQsnLyyM7JI33cRKL0mUhERKRHdGdF3WXAn4C1wDRrrfcAXxcDrATGAT+31t7XpQD9gFbU9V62tZXyeTdT8/zzwbFBxx9P+qI7ccXGOphMREREJLystVSVbQmWdqVFhbQ0NXY4Pyo6hvTxE4OnyQ7LGq3bhIh0QCvqRCRU3Snq4oAvgBHAq8Csbzr91RgzCFgCzAC2Awdbazv+FNDPqajr3azfz/YFv2PXE08Ex+KPPJKMP/0J96ABe2tFERER6edafT7KN66npHAVxQWrKN+4Huv3dzg/PjGJrMlTgltlB6ekRjCtSO+mok5EQtXlog7AGDMTeAEwwFZgEfCytXbDPvPGAqcCvySwXdYCP7LWvtTli/cDKup6P2stO+9cROX99wfHYqfkkvXAA7gTEx1MJiIiIhIZ3oZ6SosKKS5cSXHBKnaVb+10/tC0jMC97XLyyJyYQ0x8fISSivQ+KupEJFTdKuoAjDHnAfcCMQQKOAAvsOeAieS25yBQ6HkJbHl9uFsX7gdU1PUdFQ88yM6FC4M/x4wbR9bih4hK1TfGIiIiMrDUVuxoO5RiFSWFq2jcXdvhXJfbzchDxwVX2406dCwuHdAlA4iKOhEJVbeLOgBjTA6wgMAhER2d426BpcBN1trV3b5oP6Cirm+pWrKE7f/7f8Gfo0ePJuuRh/GMGuVgKhERERHnWL+fHcWbKC5YSXHhKrauK6K1paXD+dFx8WROygkWd8mj0jGmo38+iPR9KupEJFRhKeqCb2ZMGjAdmACktA1XEjhw4j1rbefr5AcYFXV9T/Xf/075DTdC231aPGlpZD3yMNHZ2Q4nExEREXFeS7OXsnVrg9tkd2z+otP5g1OGkZ2bFzxRNn6Ibi0i/YuKOhEJVViLOgmNirq+qfaNN9l6zTXQ9m2xe1gqWYsXEzt2rMPJRERERHqXhtqawKEUhaspLlzJ7oqdnc4fNvrg4Gq79PET8UTHdDpfpLdTUScioVJR5yAVdX1X3QcfsOUXv8R6vQC4ExPJfOgh4nImO5xMREREpHey1rKrvCy42q60qIDmxoYO57s9HtLHTSQ7dyrZOXkMH30wxuWKYGKR7lNRJyKhUlHnIBV1fVvDJ59Q+rPL8NfXA+BKSCDz/vuIP+wwh5OJiIiI9H7+1la2fbGB4oJVFBeupPzz9fhbWzucHzd4CFmTpwSKu9w8hqQOj2Baka5RUScioVJR5yAVdX1fY2EhJRddjL+mBgATG0vGPfcw6JhvO5xMREREpG9pbmyg9LPCQHFXsJKqsi2dzk8elUZWTqC0y5qUS0x8QoSSihw4FXUiEioVdQ7q9UXd2pchLhmyvw06jatDTes3UHLhhbRWVABgPB7SFt7OkBNPdDiZiIiISN+1u7KC4sJAaVeyZjUNNdUdzjUuFyMPHUt2zlSyc6Ywasx43FFREUwr0j4VdSISKhV1DurVRZ2vGRblwu5ySJsKR/8SJvwQ3PrA057mzZspPv8CfOXlgQG3m7TfLSDx1FOdDSYiIiLSD1i/n50lmykuXEVJ4Sq2rC3C1+ztcL4nNo7MiZPb7m83laHpGRh98SwOUFEnIqFSUeegXl3UrXoK/v6zr48lZsFR/wNTz4aYwc7k6sVaysooPv98WopLgmMjf30zyf/93w6mEhEREel/fM3NlG1YS3HBSooLV7F90xfQyb9rBg1NCZwmm5NHVk4eCUnJEUwrA5mKOhEJlYo6B/Xqoq7yC/j3XYHCrnWfbytjE+GwC+CIS2HIKGfy9VK+nTspufAivBs2BMeGX3sNKRde6GAqERERkf6tcXctJWsKgifK1u7c3un8YVmjycqdyuicPNInTMITExuhpDLQqKgTkVCpqHNQry7q9qjbCZ88CB8/CI1VX3/O5YHcs+CoX8CIic7k64Vaq6spueRSmgoKgmMpl/2MYZdfri0XIiIiIj3MWkv19vLgoRSlRQV4G+o7nO+OiiJt3MTAirvcqQw/6GBcLncEE0t/pqJOREKlos5BfaKo26O5AVYvgf/8Caq+3P/5jMNh/AyYMBNSDol8vl6mta6eLZddRsMnnwTHks+ZzYjrr1dZJyIiIhJB/tZWtn+5MbhNtmzDOvytvg7nxw4aTNbkKWTnBrbKJg4fGcG00t+oqBORUKmoc1CfKur28LfC+qXw77uh9KP25wyf+FVpNzJnwJ4Y629sZMucOdS//0FwLPHHZzDqt7/FuPUtrYiIiIgTmpsa2fLZmmBxV7mlpNP5SSNGtZV2U8mcnEtswqAIJZX+QEWdiIRKRZ2D+mRRt7eSj+A/d8O6pWBb25+TlAXjZ8KEGZB5JAywbQS2uZmt11zL7jffDI4NOfkHpN12G8bjcTCZiIiIiADUVVVSXLgqeKJsffWuDuca42LkIWPIyskjOzePtLHjcUfpM510TEWdiIRKRZ2D+nxRt0dDFWx4Hda+Al+8A76m9uclDINxJwdW2h10HETFRDanQ6zPR/lN86j5+9+DY4OmTyd90Z24YgbG34GIiIhIX2CtpaK0mJLCtvvbrV2Dz+vtcL4nJpaMiZPJzplKdm4eKRlZus2JfI2KOhEJlYo6B/Wbom5vzfWw8W1Y+zJseAO8te3PixkCY04KlHaHfhdi+vcWAuv3s/2W+exasiQ4Fv+tb5H5p3twJSQ4mExEREREOuJraaF8w9rAiruClWz7ciN08u+nhOShZE+eQnbuVLJy8hiUPDSCaaU3UlEnIqFSUeegflnU7c3XDJvfD5R265ZC/Y7257lj4JD/CpR2434A8f3zA421lp0L76DywQeDY3FTppD5wP24ExMdTCYiIiIiB6KxbjelRQXB+9vVbN/W6fzUzGyyc/PIyskjc0IOntjYCCWV3kJFnYiESkWdg/p9Ubc3fyts+SRQ2q19GaqL259n3JB9dKC0G38KJGZENmcEVNz/ADvvuCP4c8z48WQtfoiolBQHU4mIiIhIqKq3b6O4YCUlhasoWbOapvq6Due63FGkjRsf3CY74uBDcQ2w+zcPRCrqRCRUKuocNKCKur1ZC9vXBO5pt/Zl2FHU8dy0aYGDKCacCqljIpexh1U98STbb7kl+HP0QQeR9cjDeEaOdDCViIiIiHSV39/Kji+/CG6T3bp+Lf5WX4fzYxMGkTk5l+ycwImySSNHRTCtRIqKOhEJlYo6Bw3Yom5flV/AulcCxd2WjzuelzousNJuwgwYlQd9/Ea91c+/QPlNN4HfD4AnPZ2sRx4mOivL4WQiIiIi0l0tTU1sWbsmeKJsRcnmTucnDh8RXG2XOXkKcYMGRyao9CgVdSISKhV1DlJR147aclj/aqC02/wB+Dv4FjIxE8bPCJR2WUdBH902UPv6G2y99lpoaQEgatgwsh55mJhDD3U4mYiIiIiEU331ruBqu+LCVdTvqup4sjGMOOhQsnMDq+3Sxk0gyuOJXFgJGxV1IhIqFXUOUlH3DRp3BU6OXfsybHwHfI3tz4tPgXEnB1bbHXQ8ePrWTXrr3nuPLZfPwXq9ALiTkshc/BBxkyY5nExEREREeoK1lqqtpcHSrrSokBZvU4fzo2JiyJgwuW2bbB6pWaMxfXx3yUChok5EQqWizkEq6kLQ3ABfvBNYabfhNWiqaX9e9CAYc2KgtBtzEsT0jS0D9R99zJbLLsPf0ACAa9AgMh+4n/hp0xxOJiIiIiI9rdXXQvmG9RQXBoq7bRs/x1p/h/PjE5MCpV3uVLJypjB4aGoE00ooVNSJSKhU1DlIRV0XtbYEtsWufQXWvQp129qf546Gg08IbI8ddzIk9O4PMI2rV1NyyaX4awIlpImLI+Oeuxn07W87nExEREREIqmpvo7SogKKC1ZRXLiS6m3lnc5PycgiK2cK2TlTyZw4mei4+AgllW+iok5EQqWizkEq6sLA74etnwa2x657Baq+bH+ecUHW0YHSbvwMSMqMbM4D1LR+PSUXXEhrZSUAxuMh/Y6FDP7udx1OJiIiIiJOqdmxPXgoRcma1TTtru1wrsvtZtSY8cH72408ZAwud9+8n3N/oKJOREKlos5BKurCzFrY8VnbSruXYVthx3NH5bWVdjNh2LhedYKsd9MmSi64EF952zenbjdpt/6OxJkznQ0mIiIiIo6zfj87Nn/J5oKVlBSuZOu6z2j1dXAAGxATn0DmpJzgibJJI9N0f7sIUlEnIqFSUecgFXU9bNfmttLuFSj5EOjgv/WUQwP3tBs/E9Kn9YrSrmXrVorPv4CWkpLAgDGM/PWvSf5/P3E2mIiIiIj0Ki3eJrau+yx4ouzO4k2dzh8ybHjw/naZk3KJH5IYoaQDk4o6EQmVijoHqaiLoN3bYf3SQGn35Xvgb2l/3pB0GH9KYHts9rfBHRXZnHtp2bGD0gsvwvv558Gx4ddeS8qFFziWSURERER6t/rqXZSsWR28v11dVWXHk41h+OiDyc6dSnZOHunjJhIVHR25sAOAijoRCZWKOgepqHNIUw1seDOwPfbzt6Clof15cUNh3A8Cpd0hJ4AnLrI5Ad+uXZRefAlNa9YEx5LOPJPoQw7GREfjionBREdjPNGBX2OicUW3/T46GvO15z1fzY9yroAUERERkciw1lJVtiVY2pUWFdLS1Njh/ChPNOkTJgVX3A3LGo1xuSKYuP9RUScioVJR5yAVdb1ASyN88W5gpd36pdC4q/15ngQY893A9tixJ0Fs5LYItNbVUfqzn9H4aRj/O3G59iryPLg8+xR70W3FXvTePweKQBO9dxm4z/yYfeZHB94/+Jp9nndFR4PHo/ukiIiIiERAq89H+cb1lBSuorhgFeUb12P9/g7nxw1JDJR2bcXd4JTUCKbtH1TUiUioVNQ5SEVdL9Pqg+J/BUq7ta/A7rL257k8cPDxgZV240+BQcN7PJq/sZEtv7yc+mXLevxaTthvBWC0p60M3L8odH1tBeFX84MrDD2dFItfe769YjFa3xqLiIjIgOFtqKe0qJDiwpUUF6xiV/nWTucnp2V8dX+7iTnExMdHKGnfpaJOREKlos5BKup6Mb8fylYGtseufRkqN3Yw0UDWtwKl3YQZkDy6xyLZ5mZqX38d74YN+L3N2Oa9H178wd+3YL3erz3v33uu1xs4IVfa5/Hg8njaWWG4z7bivVYkfvXcPvNj9pn/DSsM97uGtiiLiIhIBNVW7Gg7lGIVJYWraNxd2+Fc43Ixasz4YHE38pAxuPXZZT8q6kQkVCrqHKSiro+wFnau/6q0K1/d8dyROYHtsRNmwvAJveIE2X1Za8Hn26vAa8E271Pseb1t418VgV8r/PYpCv3B17cEy8Dgcy37z7deL/6WwFx8Pqf/Snovt7vjrch7ti3vWWG477bl/e5f2EFJ6OmgVNzreVe0R1uURUREBhjr97OjeBPFBSspWbOarWuL8LU0dzg/Oi6OzEm5weIueVS6Pjugok5EQqeirhPGmJHA9cAMIB2oAT4G7rTWvhOG91dR1xdVl8C6VwOlXcl/wHZwX4+hB7ettDsV0vNBWyrbZVtb91kd2BxYMdiyT7G374rBlgMtFttbYbjP/D3Pt3RwGrCAMftvQ/a0U+wFy8Dw3N/Qtd/7tz30wV9ERCSiWpq9lK1bG9wmu2PzF53OH5wyjOzcPLLa7nEXPyRy93juTVTUiUioVNR1wBiTC/wDSGkbqgUGAS7AAjdYa2/t5jVU1PV19RWBQyjWvgxf/hNaO/iWcdDIwP3sJsyE0ceA2xPRmHJgrLXYlnaKvQ6KwGAZuPeKwZY989tZYdjSzvzgCsP952uLcsfMnu3J7W1D3m+F4V4rBjtbYbjP/Q33O0G5o/sbut1O/3WIiIhEXENtDSVrVgdPlN1dsbPT+cNGHxxcbZc+fiKe6JgIJXWWijoRCZWKunYYY+KAtUA2sBKYba0tMsYMAW4Grm6b+j1r7ZvduI6Kuv6kqRY+fzNwGMXnb0FzXfvzYpNg7PcDpd0h/wXRugmv7G//LcrN+60ADO/W5XZWGDY3B7Yoe73Q2ur0X0nv5XZjYmK+urdhD56g3NEKwz3jREVptaGIiESctZZd5WXB1XalRQU0NzZ0ON/t8ZA+biLZuVPJzslj+OiD++2BXirqRCRUKuraYYy5ArgDqAPGW2u37vP8C8BpQLf+h6uirh9raYJN78Hal2D9a9BQ2f68qDg49DuB7bFjvwdxSZHNKXKA9t6i/LUisGWfYq+dFYbtbl3e89yerc7trjBsf+uytih3Ys8W5b1PUG5nhWFXTlB27VccdlIsxsQEVj2qNBQRGZD8ra1s+2JDcLVd+efr8XfypV/c4CFkTZ4SKO5y8xiSOjyCaXuWijoRCZWKunYYYz4BDgMesNZe2s7zRwP/avtxgrV2XRevo6JuIGj1QemHge2xa1+B2i3tz3NFwehjAyvtxp8Cg0dGNqdIH2H9/sAW5R5dYXjgh6Noi3LHTLsnKLe3wnCfFYOdFYGe6I4PR9lzAMp+Jy5ri7KIiJOaGxso/awweKJs1dbSTucnj0ojKydQ2mVNyiUmPuH/s3fv0W2n933nP88Pd5AESFASJUoUAWmkkeZmj0ZSmqsdx5Nt3WyaNqebJm1aJ62TNknrS3pOu2m2mzY9vey2dpI6abxJ09yaNtskbpPU23js2HFSxxY1mhnNXSMJICVRokgCJEiCuD/7xw+ECN5ASgQBku/XOTgg8fsBzwMCpMiPvs/z3aGZbj+COgBbRVC3gjGmR27TCCPpO621v7PGOY6ktKSopB+21v7cQ45FULffWCuNv+Quj33z96Wpt9c50UjHLrih3dlvcxtTAOg41lqpVFK1WHrQ4GTVHofLqgvXa47SUGG4xlLk0kbNUZaFhixRXp/XW9vD0Ld2heGq6sJlIeGqxinr72+4Zgdl31JAWfvc6233VwPDzCHBAAAgAElEQVQA2mpueqoW2rkdZXOzM+ueaxxHhx87reGnn9Xw0+/SkVNn5NlFP0cJ6gBsmbWWy7KLpItym0VYSY9vcN5Xa+d88hHGenHZWNt6uXz5sm3m8uXLLRnbfVs196lPfaolY587d25T43/oQx9qyfgf+tCHNjX+uXPnWjL+pz71qU2Nz3uP9x7vvb333quWSraysGDLmYwtTkzYwq3bNn/jhl18802be+UV+33f8R0tGf+7jh61177pPfbtP/O19q1nz9k3nnravvH4mVWXJwKBloz/EwOH1xxv5aVVr/1/GY43Hfu/DMdbNv70r/26Tf/mb9rMpz9tZz/zGZv93Ofs3Je+ZOf/9Ct24coVm3vtNfvJf/pPW/rea4afe6157fm51xzvvb353vudf/kT9sXP/Dc7dWvMVqvVNcfvsPfei7YD/tblwoXL7rjsnv+K2DlHln08vsF5S8eObHAOsPP++49KE/+ofeP/4vulzzT50TJebt34P3mw+TmX860Z++4rmxv/ylxrxr/yq9JPfrr5eXczrRmf917zc1r83jNyy8Elaa2Fnt5brXnvRQ5P6dT7Cw23WSvZqmQrRrYi2apR4Jcr0sT2j+/rrigYK8lWjKrVB+PZSm386t7eK2/in/2zDY+XfV26m6+2ZOzinXmN/oMvNT1v/qt3WzL+/Ffvbmr84p11Gjw9ounfvqbRG83Hb5W7P3NFo4cXNj7n3nrV+49uM1/76ZevtWRs3nv7+713Lv1N0hel+S9e17xu6NrcK3r+5z7csvEAYCcR1K22fAOExQ3OW2pj1N3sAY0x661tPbPZSQGbVi1LlWL7xq+UpEqTPwhbuTxvM8+92qqwxm5ufNuaP5hlq5t87W1rxue91/ycffTeq4eGHtVTQ+O0ZvwDZ+eUeK6w7nFrJVUlbZxnPbTwoby6u91QsLoUEi4LCqtVI9PsvfkIioGoStG4qpEhqfuwTPiAvKGofP4uBb1+dTtGPa/8nnT9pW0f20jybKJpSKsaixhjNjd+S0aXnE2O3yqbGd9p4fw289xbNT7vvf3+3uPPWAB7Fz/hVtvb/+0OAMA+Y4zWLjHcJgPvntPQYG7Dc+bGK9L11owf+7P/Fx12AexrjvG3ewoAsG0I6lZbXp8ekrTeOqHwGuevya6zcWit0u7clmYHNPOBfy196G81P++fBFsz/t98QXquydv6xSvSL3xda8b/8fvNz/mFX5R+/0e2f+zD75J+/E+bn3f7h6Qrv7T94z/7vdKPb6K3ze9+rXR3+ytreO/x3muK915Lhm8W0llrVWhRNaVzKKDwh082Pc97OyK9sv3je5+KbGp85zOBliy79n/LQYX/WvPx9a+2f2xJCn73MYWf2Xj84NUF6VdaM/5mvvb+Xz8o/cH2j817j/eeJFUrVU3fHtW5xF9qzUAA0AYEdast35duUNJ6mysM1q5bs/EF8LA8PskbaN/4Xn/z8b0t/F/PzTx3j681YxuzufGdFpX2OJ7Njd+qyhvee83P4b3XmvE7+L1XyJWUnczpzmvrdzR8VFVrlVNFM2ZRaWde9z1zGvcsaMwp6KaxSvu65R9szbJvj8+n2JHBpucFwuGm5zyMQDi8qfE9vtZ873VFezc1fqtEDxxsOn50vHW/qm7muXdFe1syNu893ntLDhw71rJxAKAdjLUt2qtolzLG9EialbsE9juttb+zxjmOpLSkqKQfttZuooxgzbFePHfu3LkXX1xvCzsAANCpbNUqN1dUdjKnhVvzWpxYUHkqr+psQSZXlq9UUVBSyHm0gLJqrRZU1qxZ1JRnTpPetMb9UxrzZnXTs6jb8qpUPKhq7XIs2quL8ZguJGK6EI/p5MEulsYCQJs899xzunLlypX1VlkBwEpU1K1grZ0zxlyWdEHS85JWBXWSvkZuSCdJn9+puQEAgJ1TqVS1kCkoez+nhTvzyk/kVJ7Oq5otyMmV5StXFTJuEBeUtGph7SYDuqUgbsbkNOXN6r43rfHAfd0K3lYqOKG71qNiqV/VwiE3jCsclJ07pqWN9x4f6NGFJ/p0IR7TxURMR6Kh7fwyAAAAYAcR1K3tN+QGdX/VGPNPrbUr67b/fu36RWtt6/qOAwCAlikVKppL5zU3mdPCnQXlJxZUTueluaKcxbL85apCjlHIMepSY1t4SZJn80HcvEqacXKa8mQ14ZvWeGBCt0K3NRq6pUl/Wl4TU2GxX8XcAVWLh9xQbv5J2UqXlve58jpG7z4WdSvm4jGdj/epN8wm6gAAAHsFQd3aPiXpI5KGJf2+MeZ7rbVv1JbF/h+SlnYr/bF2TRAAAKzPWqvCQtkN4u7ntDC+oML9nMqZWhCXryhQrSpcC+IikiIrH8TrbGqsqrWaN0VlTE5T3lnd801rPHBXY6HbuhW8oyl/RhVTVcAT1KHgkHzVAc3PxXR36gnl09+oavGAZNfexyrs9+jccbda7kKiT88O9Snkb2ELWwAAALQVQd0arLWLxpi/IHdZ6zlJrxtjspK6JTmSrKQfs9Z+to3TBABg36pWrXKzBc1N5zU3lVNufEGFyUVVMgVpvihPvqKQrMKOUdAxWlVz5khythbEpZ0FTXpnNOGb0p3gPY2FbulO4J6mfG4Qt6Q/2K8TvSd0NHxKR0tfr5nZXt28261rtx1NVTeuwot1+XV+uE8Xa/vLPTEYkc+zuXkCAABg9yOoW4e19hVjzFOS/ndJ3ybpqKRpSZckfcJay950AAC0SKVU1VwmX6+IW7y3oOLkoiozBZn5kjzFisJGCjvGvax8AK/R8iWjG6laqzlTUNqZ16RvRvd8U7oTHNdY6Lbu+idXBXGS5DEeDfUM6YnoM0pEE0pEE+p2BjU5HdGrt0saeT2tP7w/33Tso72heih3MdGnkwe7afwAAACwjxHUbcBae0/Sh2sXAACwTYqLtWWp0+4ecYv3cipOL6o6U5BZKMlXqirsuEFcpLY0tYFv81VmVbkVcVNOVpPejO76J3UneFdjwdua8E+vGcQt6fJ16Ynok/UwLhFxr491H9PodEGXUmmNvJPWb6UyujMzKWlyw7mcHuiuN324EI9psJfGDwAAAHiAoA4AAGwra60W50rLgrhF5ScWVJxaVDVblJMrKVCx9SCuzzHqW/4ARpJ/80GcldWCU1bGu6Bxz33d8d3T7eC4bgfuasI/rWnfzLpB3JLDXYfrIdzS5UT0hA6EDsgYo3KlqtfHsxpJpfWbybQuj95QeqG44WN6HaOnjkbrodz54T71ddH4AQAAAOsjqAMAAFtSrVQ1P1PQ/FIQN7Wo/EROpem8bC2IC0r1IO6gs2Ipp8dsumOq5G4Mm/dWNecvaMo/ozHfHb3teUd3/Pc04dtcECdJPsen4chwQxi3VCUX9jUunl0sVvTSrYx+I3ldI6m0roxllCtWNnz8kM+jc8O9bsVcPKZ3H+9V2M+vWgAAANg8fnsEAAANysWKWw23LIgr3K8FcXNuowZ3fzg3iDu8MojbQjWc5AZxZb9RPlRVNpTT/eC0bvpTeqNyTdeV2nQQtyQaiOpE9ETDUtUT0RMa7B6Ux1m7Y+pMrqjLqYxGUmldSqX12p1ZlSp2w3H6wj6dr4VyFxIxPUnjBwAAADwigjoAAPYRa60KuWX7w6Xzmq8FceV0Xna+JF+xUmvS4AZx0ZVBXGDrQVw16JHt9qrQXVW2Z153gxO6oTG9XnlbV/Ova9HmV99x7UxNkmRkdLT76KqlqoloQn3BvvXvWHN3dlGXkmmNpNIaSWb09sRc0/sc7Q3pQrxPFxJuOHfyYLeclV8bAAAA4BEQ1AEAsIfYqlVurlgP4eama0HcZE7lTEGaL9b2h3ODuC7HqH952ORICm6QkK01pqRq0CsT8csbC6gaM8p0ZXXbuafrSumN4tu6MXdTdxfuuncoS2reEFWSFPKGFI/EFY/GG8K44ciwAp7A5uZnrW5MLtRCObdi7nZmsen9HjvUXe/GeiEe07G+Vb1lAQAAgG1FUAcAwC5SKVc1nymsroibXFRlJi+zUFJIqgdxEcfo0PIgzudIvq2NaSXZkBvE+fpDCgyE5In5NR3IaswZ1/VKUjfnkkrNppScTWouMydltjbGgdCB+lLVE70n6ktWB7oG5JitVfCVK1W9cTdbr5i7nMpouknjB49j9NRgRBdqy1gvxGOK0fgBAAAAO4ygDgCADlIqVB5Uwy2riCtOLaoyW5CzWK7tD+cGcTHHaHB5ELfFajipFsSFvXIiAfkOBBU4FJYvFpKnL6BCd1mj9o6S824Il5xNKplN6tabt1S25S2N4zEeDfUMNVTGJaIJxaNxRfyRLc97Sb5U0UtjM27FXCqtK6MZLTRp/BD0OXp26MEy1meP96orwK9FAAAAaC9+IwUAYIdYa5VfKDUsS12qiCtNL6o6W5S3WK3vDRd2pIOO0dDyIC70EEGckRTyyukNyH8gJP/BkLx9bhDn7QvKRLy6n5+shXBvutfTSSVvJjW5OLnl8bp93as7q0YTGuoeks+zxXK+NczmSro86i5hHUmm9eomGj9EQz53f7laxdxTg1H5vTR+AAAAQGchqAMAYJtUq1YLMwXNp1dUxE0vqjSVVzVbUKCqhiDuiGMUXArivEbyPmQQF/bJUwvifAdC8vYF60GcJxqQ8RgVKgWNZkeVnH3bDePuJJV8I6lUNqXFcvM921Y63HV4VXfVRDShA6EDMmb7mizcm83XQ7mRVFpvT8zJbpzL6Ug0WA/lLsZjOnWIxg8AAADofAR1AABsUqVUfRDAraiIK6fz0lxJQdMYxB1bHsQ9xLJUyQ3iTJdPnr6gG8T1B+XpC8rbF5CnLyhPxA3ilmTyGb29tEz1hrtU9ebMTd2ZvyOrJgnXCn7Hr+HocEMQl4gmFI/EFfZtf3MFa61uTi3Umz6MpNK6lW4eIp482KWLtb3l3MYPoW0NCwEAAICdQFAHAEBNYbHsVsOtXJo67QZxJleuB3BL1/3Lg7iuRwjiun3y1oI4b2zjIE6SKtWKxufHlcxeVXLcDeVuzt5UcjapmcLMlufQG+ht2DduqUpusHtQHufhntdmlCtVvXl3rl4xd3k0ran55o0fnlxq/BCP6UK8T/3dm+sACwAAAHQygjoAwL5grdXi3Or94ebSeS1MLao8U5C3WGkI4rod6dBSEOdI6n64fzbdIM4vXywo34FgbVnqxkHcklwpp9TMm/VGDkth3Fh2TMXqxoHWSo5xdLT76KqlqoloQn3Bvod6bluVL1X08q2ZesXcS2Mzmi9s3JQi4HX07PFeXawtZX32eJ+6afwAAACAPYjfcgEAe0K1UtV8pqD5zOqKuIXpvMozBQWqtiGI63WkwaUgzm8k/8MHcU6PX95YUL7+UD2A20wQJ7kh4mRuclUYl8wmdW/h3pbnE/KGFI/EVzVzGI4MK+DZ2cqz2cWSXhxN61Iyo5FUWq/enlWxUt3wPpGgt76/3IV4TE8fpfEDAAAA9geCOgDArlAqVtZclrpUEVedKypkTEMQ1+9IQ0tBXPgRlm8ayUTcijhvbOtBXP05VEu6NXerHsgtv8yX5rc8rYOhg6uWqiaiCQ10Dcgx7Qm2JrJ5Xao1fbiU3Fzjh8ORYK3pQ58uJGI6faiHxg8AAADYlwjqAABtZ61VIVduCN/cveFqQVw6L7NQUshpDOIGHCmxFMT1+B5+AkZyIgF5+91lqQ8bxC3JFrNKzaYaq+Nmk7o9d1tlu/Eyz5W8xquhyFDDUtUT0ROKR+Pq8fds9ZluK2utUtO5+jLWS8m0xtK5pvc7cbDLXcYaj+ligsYPAAAAwBKCOgBAy9mqVS5bbKyEW14RN52Xr1RZFcQN1q6DHiNFHjGIiwbkW9Gk4WGDOEmq2qomFiZWLVVNziY1tTi15Sl2+7rrAdzyQO5YzzH5nEd47tuoUrV6825WI6mlirmMpuYLG97HMdITgxFdjPfrYqJP5+MxHaDxAwAAALAmgjoAwCOrlKur94bLFOqf5zJ5Bev7w7lBXMgx6lsK4kKOFHqEpZpG8kQDq7qlPkoQt6RQKWg0O9pQGZeaTSmVTWmxvLjlxzvSdaRhqeqJXrfTan+wv+OqyvKliq7enq0vY70ymtFck8YPfq+jdw89aPxw7niveoKdETQCAAAAnY6gDgDQVDFfrgdw8+n8qsq4xWxRYaOGIK7LMTq4FMQ9ZLfUOiN5egOruqVuRxC3JJPPNIRxS5c783dk1WSTtRX8jl/D0eH6ctUT0RP1Zg5hX/iR5tlK2XxJL45mNFLbY+6VW80bP/QEvTo/3FfbYy6mp49FFfA+wn6AAAAAwD5GUAcA+5y1Vvn50rrLUufSeZUWyvXlqEtBXMQxOrwUxEUfsWJq3SAuKE8sIE/PowdxklSpVnRn/s6DIC77IJCbKcxs+fH6An2rOqsmogkNdg3K43R+WHV/Lq+RWjfWS8m03rqXVbVJJnmoJ1AP5S7EY3r8cI88NH4AAAAAtgVBHQDscdWq1cJMYVUAN7/s42qxuiqIizlGxxwp7DEK9m5DENcXlLc30NIgbkmulGsI4ZYuo9lRlaqlLT2WYxwd7T7aUBmXiCYUj8TVF+zbtjm3mrVWo9M5XUql6xVzqenmjR8SB7p0Id5Xb/xwPBbuuCW6AAAAwF5BUAcAu1y5VNF8utBYBbe8UUOmIFXtqiDuoGM07EjhoKNg+BGrvxzJ07tzQZzkBk+Ti5OrwrhkNql7C/e2/Hghb0jxSNzdM25Zh9XjkeMKeHZf84NK1eqte9laKJfRpVRak3PNGz+cPRKph3Ln43061BPcoRkDAAAAIKgDgA5XWCyvXpK6LIhbzBblSKuCuCOO0UlHCnd7FHzUpYltCOKWlCol3Zq7tWqpanI2qfnS/JYf72Do4JrdVQ+FD8kxj9DQos0KZbfxw6VatdyLoxnN5TfR+OFYry4k3Iq554b7aPwAAAAAtBFBHQC0kbVWuWyxIXybX1EZV8xX1gziemvX4Yh3VwdxS7LF7OrquNmkbs3dUsVWtvRYXuPV8cjxxr3jIgnFo3H1+Hta9Ax21txS44dUWiPJjF6+PaNiuUnjh4BXzy1bxvr00aiCvs7fSw8AAADYLwjqAKCFKpWqFjKF1UtSl0K5dEGVcnXNIK7fMQp7904QJ0lVW9W9hXsNQdxSp9Xp/PSWH6/H16NEb6JhqWoimtCxnmPyOXurMmxyrlBv+jCSSuvNu80bPxzsCdSaPrhdWc8cjtD4AQAAAOhgBHUA8AhKxcqay1Lnl/aHmynIWq0K4iKONOAYhYNGYWc7gjjjdk1tcxC3JF/OazQ7+mCp6oy7bDU1m1K+kt/y4w12Da7ZXbU/2L8nGxtYazWWztVDuZFURsmphab3i/eHdSEeq3dlHe6n8QMAAACwmxDUAcA6rLUq5NbYH27Zx/l5t4OoR1JoWRDX50hHHaNwl0chx+y5IE5yvz6ZQmbN6rjx+XFZNSn3WsHv+Bv2jVuqkhuODCvsC7foWXSGatXqrXtzbsVcKq3LqbQmshs3fjBGOns4oouJmBvOxft0KELjBwAAAGA3I6gDsG/ZqtXCbG1/uPRiLXwrLFuWmlep4O6NtjKIO+hIw45RuHvvBnFLytWyxufHV4VxyWxSs4XZLT9eLBhTPBJvqIw7ET2hI11H5HH2x35pxXJVr96Z0aWku8fc5VRa2WaNHzyO3jUUrVfMPTfcpwiNHwAAAIA9haAOwJ5VKVU1l3mwDHVlRdx8pqBqxa36WhnEHXGksKcFQdzyAK4vULsOyhPxy7R577BcKVdfqnpz5qZS2ZSSs0mNZkdVqpa29FiOcXSs+9jq5aqRhHqDvS16Bp1rvlDWlVrjh0vJtF6+NaNCk8YP3QGvzg336WK8TxcT/XrmGI0fAAAAgL2OoA7ArlXMb7wsNZctamn15cog7pgjhQOOwo72TRAnuctVJxcnGyvjapeJ3MSWHy/kDa1aqnoiekLHI8fl9/hb8Ax2h6n5gi6n0vWKudfHZ5s2fjjQ7a8tYXU7sp49QuMHAAAAYL8hqAPQkay1WpwrLat+Wx3GFXIPlgquDOL6HSkc8uy7IG5JqVLSrblbq8K4ZDaphVLzpgQrHQodUiKaqO8hdyJ6QoloQgPhgX3frMBaq9uZxXrjh0uptG5ONv8aH4+Fa6Fcny7EY0oc6Nr3X0sAAABgvyOoA9AW1UrV3R9unYq4+XRe5dKDpYHLg7hux+iQI4XD+zeIWzJbmG0I4ZKzbmfVW3O3VLGVLT2W13h1PHK8IYhLRBOKR+Lq9ne36BnsPtWq1bX7cxpJpnUpldFIMq172Y072RojPT7QU2/8cDER0wCNHwAAAACsQFAHoCXKxcqqpajz6cKDIG6mILtsLeDyIK7XMRr0SGEfQZwkVW1VdxfuNlbG1S7T+ektP16Pr0eJ3mVhXG3J6tGeo/I5NCdYyW38MKuRVFojybQuj2Y0u7jxnn0+j9Ezx3rrFXPPDccUDfG1BQAAALAxgjoAD6WQKzVWwq24XpxrDDKWB3H9jtGQ3yjs7L894jaSL+c1mh1dtVQ1NZtSvrJxxdZaBrsGleh9EMQtXfqD/Syx3MBCoawrY5laxZzb+CFf2rjxQ5ffU2v84HZkffdQL40fAAAAAGwZQR2AVWzVKje3elnq8u6pxXzjssrlQdyAYxQOOrX94gjilrPWKp1PNyxVXbqMz4/LqknHgRUCnoCGI8MNS1UT0YSGI8MKeUMtehZ7y/R8QSMpt+mD2/ghq0qTzg/9XbXGD4mYLsZjOnukR16Ps0MzBgAAALBXEdQB+1ClUtVCprBmp1S3cUNBlXJjBdHyIG6QIK6pcrWsO/N3Vi1VvTl7U9lidsuPFwvGVnVXTUQTOtJ1RB6Hyq3NWmr8sBTKXUqmdWMTjR+GYiF3GWstnDtB4wcAAAAALUBQB+xBpUJlgxAur4WZguyKgiGPVA/d+lYEcWHHKEAQt6aF0oJSs6l6d9VUNqWbMzc1OjeqcrXc/AGWcYyjoZ6hVUtV45G4eoO9LXoGe1u1avXO/Xldqu0vN5JK6+7s5ho/LK+YOxyl8QMAAACA1iOoA3YZa60KC+W194erfZxfWL3R/VIQF3aMDvic+sfbGsQtBW+9tetYsB7MeXp2ZxAnuV/z+7n7DUtVl4K5+7n7W368sDfcEMQtVckdjxyX3+NvwTPYP0qVWuOHWih3eTSjmVzzxg9PH43WQ7nzwzFFwzR+AAAAALDzCOqADmerVvdH55S8Oqmx19PKTORULlRWnbcUxEUco8P+FgRxHvMggNtjQdySUqWksbmxVWFccjapXDm35cc7FD60aqlqIprQQHiAZZPbJFcs66WxGX016VbMvXQr07TxQ9jv0XPDfW7FXNxt/BDys3wYAAAAQPsR1AEdqFSo6NabaaVendLoq9PKZYuS3CAu5hiFCeIeyWxhdtXecclsUrfnbqtiV4egG/E6Xg33DK+qkItH4ur2d7foGexfmYXig/3lUhm9fmdW5SaNH2Jdfl2Iu8HcxURMTxyJ0PgBAAAAQEciqAM6xHymoNSrU0q9OqXbb2VUKVVlJPV7jRJBR4d9jro9jxCU7aMgTpKqtqq7C3fXrI5L59Nbfrwef09jZ9VIQid6T+ho91F5HX6UtsqdmUWNJNP1PebeuT/f9D5He0O6mIjVgrk+nTzYTQUjAAAAgF2Bvy6BNrHWaurWvJJXp5S6OqXJsTlJkt9IR7xGh8MeHfIZ+TYbMOyzIG5JvpzXaHZ0VRiXyqZUqBS29FhGRoPdg4pH4/XlqkvhXCwYI+xpMWutrjc0fsjozsxi0/udHuiuV8tdiMc02BvagdkCAAAAwPYjqAN2ULlU0e23Mkq9Oq3U1SktzLhBUsSRTgUcDfiMYh6zbiBkfI78Qz21AG5/BHGSG+Ck8+nGMC6bVGo2pfH5cVltvPRxpYAnoHgkXq+OWwrjjkeOK+Ql5NkppUpVr49n6xVzl1NpZZo0fvA6Rk8djdZDufPDferrogEHAAAAgL2BoA5osVy26C5pvTqlW2+mVS5W5Ug64DU6GXI04HMU3iBg8/QGFDwbU+hMTIETvTK+vbu3Vrla1p35O7o5c7Ohw2pyNqlsMbvlx4sFY6vCuEQ0oSNdR+SYvft17FSLxYpeGsu4FXOptK6MzmixtPGegCGfR+eGe92KuXhM7z7eq7Cff7oAAAAA7E38tQNsM2ut0uMLSr7i7jc3kcpKVgoa6ajPaKDLo4NeI+96yyiN5B+OKHgmptDZmLyHwntuyeVCaWF1M4fZpEbnRlWulrf0WI5xNNQz5C5V7W3ssBoNRFv0DLAZM7miRlIZt/FDMq3XNtH4oS/s0/laKHchEdOTgxH5aPwAAAAAYJ8gqAO2QaVc1fi1mfp+c3PpvCSp12N0JuBowOuo17t+2GaCHgUfr1XNne6Tp8u3U1NvGWutJnITqzqrJmeTup+7v+XHC3vDqyrjEtGEhnqG5Pew9LETjM8s1kO5kVRa1yY21/jhQrxPFxJuOHfyYLecPbqEGwAAAACaIagDHtLifFGjr7l7zY29kVYpX5FX0kGf0WMhtxFEcIPAwXswVF/S6h+OyOzSqqFipaix7NiqparJ2aRy5dyWH+9Q+NDqQC6S0KHwoT1XWbibWWt1Y3Jel5IPKuY20/jh1KHueih3IRHTURo/AAAAAEAdQR2wSdZaZe7llLrqLmm9d2NW1kphRxryOhro8uiA18hZL0zyGAUSUXdJ65mYvAd2V0AxW5hdvVw1m9Ttuduq2I33GVvJ63jrzRyWrk9ETygejavL19WiZ4BHUV5q/FAL5S6PZpReKG54H89S44d4n9v4IR5TjMYPAAAAALAugjpgA5VKVXevz7rh3NUpzU4uykiKeYzOBhwd9jnq8axf5eV0+xR8PKbgmZiCp3rlBDv7W65qqxqfH1+1VDU5m1Q6n97y40X8kVVLVQlrquEAACAASURBVBPRhI52H5XX6eyvxX63WKzopVsZjdQq5q6MZZQrbhzIBn2Ozh13Q7mLiZiepfEDAAAAAGwJf0EBK+QXShp7Y1qpq9Mae31ahVxZPiMNeI0eC3t0yGvk32BJq2+wq9YIol++o90yHbjf1mJ5UaPZ0YbquJuzNzWaHVWhUtjSYxkZDXYPNoZxtYYOsWCM5aq7xGyupJFaN9ZLKbfxQ6myceOH3rBP54djuphww7mnjkZp/AAAAAAAj4CgDpA0cz9Xr5obvz4rW7XqcaQhn6PD3R7FPGbdwMn4HAUe63Wr5s7E5I0Gdnj2a7PWajo/vWZ31fGF8S0/XtATVDwab+iqmogmNBwZVtAbbMEzQCvdm83rUiqtkaS7lPXtibmm9xmMBnUhEatXzD1G4wcAAAAA2FYEddiXqlWrezdnlXrF3W8ucy8nR9IBr9FTAaPDPo/CGwQQnmhAwbO1Ja0nozI+z85NfoVytazbc7frS1VvztysL1mdKzYPX1bqD/avWqqaiCZ0pOuIHEO11G5krdXNqQU3lKtVzd1KN2/8cPJgly4m+usVc8f6wjswWwAAAADYvwjqsG8UF8saeyOt1NUpjb42rfxCSUEjHfIZnery6KDXyLveMk0j+Y9H6lVzvsPhbV3Saa1V2ZZVqpRUqrqXYqXYcL308b2Fe/WlqsnZpMbmxlSulrc0nsd4NNQz5FbILVuqmogmFA1Et+15oT3KlarevDtXr5i7PJrW1Hzzxg9PDkZ0IR6rXfrU390Z1aEAAAAAsF8Q1GFPy04tKvWqu6T1zrUZVStWvR6jYZ/R4W6Per3rV4hV/FbzxyrKHC9o+khOi4E7bmg2VVLxfrEhVCtVSipWVwRrldKaQVvDseqDx7HaeD+wh9Hl61q1VPVE9ISGeobk8/i2fTy0R75U0cu3ZuoVc1dGM1po0vgh4HX07PFeXYzHdCER07njfeoK8E8CAAAAALQTf5VhTZVqRblyTo5x5BhHHuORMUYe41l3+WPVVleFUUvh1crQamV4Va6WHxyrhVcr77ve/Rseu1JSON2vg5MJDUw+pt6FAXnkVs0943c04DMKbrCk9bZ/Ql/tflWXul/T6+HrqpiqNCH30sEGwgOrwrhENKGDoYM0c9iDZhdLenE0rUu1jqxXb880bfwQCXrdSrnaHnNPH43Kv0FQDQAAAADYeQR1WNP4/Lg+8OkPrHu8IcCTUblaVtlubfnldvFW/Do2+7iG0+c0PPOkwqUehR1pwOvocJdRv9fIs05YVVZFr4Xf0Ve7X9NI92u6E7i/w7N/wGM88nv88jpe+R2/fB6fe+346h97Ha/6Q/2KR+I60euGcfFIXF2+rrbNG603kc3rUrLWkbXW+ME2KcA8HHEbP1yM9+lCIqbTh3po/AAAAAAAHY6gDmuq2I2XzVVtVVVbVVntCee6ClENZ55SPPOUBmdPyWd96vMYHfYZDQQdRTzrBxJZz7xejl7TK73X9U70lsqBqvyOX33OIQ14jtWDMZ/jXvwef8P10rGlMG3lx8sDtvp91rr/smM+xyeP076GFOgc1lolpxZqoZxbMTeWzjW934mDXe4y1lpH1mN9IaopAQAAAGCXIajDurp8XfVAbunSLMDbani1MrRa85jjl9fxyZkKqXQzqPxNr4oTjnxGOuQ1Ggg5GvAa+TeoFvIeCSt0pl/BszEdPdajJ5w/p+/Z7i8Y8BAqVas372brFXMjqYym5gsb3scx0pOD0Voo16fz8ZgO0PgBAAAAAHY9gjqsKR6N6yvf85U1j1lrVbGVhgDP5/HJa7zbWsFTLlZ0++2Mki9PafTqlBZmi+p2pOM+RwPdRjGPkbPeeF5Hwcd6611avb2EGOgM+VJFr9yacSvmUhldGc1ovrBxZWrA6+jdQ726WNtf7txwn7pp/AAAAAAAew5/6WHLjDHymta8dRZmCxp9dVrJq1O6/WZa1VJV/V6jEz6jgR6vujZY0uqJ+BU86wZzgZO9cvwsJUX7ZfMlvZjK6FIqrZFkWldvz6pYqW54n0jQq/P1Zax9eupoVAEv72cAAAAA2OsI6tBW1lpN35lX6uqUklendT+VVcBIAz6jZ32ODoW98q5XNWck/1CPgo/HFDwbk+9IF3tyoe3uZ/P1UO5SKqO37mWbNn4YiATqe8tdiMf0+ACNHwAAAABgPyKow46rlKq6cy3jhnOvTmk+XVDU43ZpPdPtUZ/XWfe+JuBR8HSfu6T18T55uv07OHOgkbVWqelcLZRz95gbnd5E44cDXboQj9W6ssY0FKPxAwAAAACAoA47ZHGuqNHXppW6OqWxN9KqFio66DU66XM0EPEqtEH1kKc/qNAZt2ouEI/KbBDkAa1UqVq9dS+rkaTb9OFSKq3JueaNH54YjLgVc/GYzsdjOtjDnokAAAAAgNUI6tAS1lpl7uaUenVKqatTuntzViFJh32OnvMZHQh65VmvgsiRAvGoWzV3NibvAaqN0B6FckVXb8/WO7K+mMporknjB/9S44daxdy5473qCfp2aMYAAAAAgN2MoA7bplKp6u47M0pedcO57FReMY/RgM/oTLdXkQ0aQThhb32vueCpPjkh3prYeXP5kl4czWgkldZIMqOXb8+oWN648UNP0Kvzw331ZaxPH6PxAwAAAADg4ZCG4JHkF0oae93t0jr2elrVfFmHvEaP+RwdingV2GBJq+9wWMEz/Qqejck/1CPD5vnYYZNzBY2k0vWKuTfvZlVt0vjhUE+gHspdiMf0+OEeeXjvAgAAAAC2AUEdtsRaq5mJnJJXpzT66rTu3phVl6wGfI7Oe436I1456y1T9RoFT/a6S1rPxOTtC+7s5LGvWWs1ls7VQ7mRVEbJqYWm94v3hxsaPwz3h1mKDQAAAABoCYI6NFUpVzV+fUajV6eVvDqpajqvfq+jw16jp7o9GzaCcCJ+txHEmZgCj/XK8bMkEDujUrV6+96cWzGXSmskmdb9Jo0fjJHOHo7oYiJWC+f6dKiHQBkAAAAAsDMI6rCm/EJJo69OKfnKlGbeSitaser3Gn2d1ygQ2XhjfN9QTz2c8w12UX2EHVEoV/Tq7dl6KHd5NKO5fJPGDx5H7xqK1ivmnhvuU4TGDwAAAACANiGow5pu/8kdZT87qtMeI3/A2fBcE/Ao+Fiv2wji8Zg8Pf4dmiX2s/lC2W38kHQr5l65NaNCs8YPAa/ODffVK+aeORZV0EeVJwAAAACgMxDUYU0DwxEFfWsHdCbkVSARdS8novId6aIRBFpuar5QD+VGUmm9Md688cOB7oAuJvrcirl4TGePRGj8AAAAAADoWAR1WFP3Y73KGMmxksJehU72KnDCDee8h8IEc2gpa61upRfry1hHUmnd3ETjh+Fa44eLtaWscRo/AAAAAAB2EYI6rMl4HR3860/IeyAk74EQYQdaqlq1enui1vihFsxNZJs3fjhzOKKL8T5dqC1lHYjQ+AEAAAAAsHsR1GFdobP97Z4C9qhiuapX78zWQ7nLqbSym2j88MyxqC4k3Iq5c8N9ioZo/AAAAAAA2DsI6gC03EKhrCtjDxo/vHxrRvnSxo0fupcaP8TdPebeNdRL4wcAAAAAwJ5GUAdg203PFzSSymik1vjh9fGsKk06Pxzo9tebPlxMxHTmcI+8no07DgMAAAAAsJcQ1AF4JNZa3c4s1kO5S8m0bkw2b/xwPFZr/FDrypo40MVeiAAAAACAfY2gDsCWVKtW79yfb+jIenc2v+F9jJEeH+jRxVrThwvxmA5HafwAAAAAAMByBHUANlQsV/Xa+Gw9lLs8mtFMrrThfXweo6ePPmj8cH44pmiYxg8AAAAAAGyEoA5Ag4VCWS+NzdQr5l66lWna+KHL79G54b56tdyzx2n8AAAAAADAVhHUrWCMCUh6r6QLyy5Haof/nLX2f7RpakBLpBeK7v5ytYq51zbR+KG/y6/ztW6sFxMxPXEkQuMHAAAAAAAeEUHdamclEcZhz7qdydWaPrhdWa/fn296n2N9IV2Mx3ShtsfcyYM0fgAAAAAAYLsR1K1tRtKLkkYkXZb0W+2dDvBwqlWr65PzulSrlhtJpjXepPGD5DZ+uJB4UDF3JBragdkCAAAAALC/EdStdlVSzFpbX/tH5RB2i1KlqtfuzNYr5i6Ppps2fvA6Rk8fi7oVc/GYzsf71Bv279CMAQAAAADAEoK6Fay1G++aD3SQXLHW+KFWMffS2IwWS5UN7xP2e3TueK3xQ6JPzw71KeSn8QMAAAAAAO1GUAfsIjO5Yj2Uu5TK6PU7syo3afwQ6/Lr/HCfLtb2l3tiMCIfjR8AAAAAAOg4BHXALnBvNq+f/cJ1/eeRMZUqGwdzR3tD9VDuYqJPJw92s3wbAAAAAIBdgKAO6GCTcwX9uy/e0K9/dVTF8tqrsk8PdNebPlyIxzTYS+MHAAAAAAB2I4K6HWCMeXGdQ2d2dCLYNdILRX3qSzf0q18eXbXn3NkjEX3DY/26mOjX+eE+9XXR+AEAAAAAgL1gTwR1xph/LOkfP+Td/5W19h9t53yAhzW7WNIv/vFN/dKfJLVQbAzonjkW1ceeP633nD7IUlYAAAAAAPagPRHUSXIkPWzbypa3u7TWPrfW7bVKu3OtHh+dby5f0n/4nyn9wh/f1Fy+3HDs7JGIPvb8ab3/7CECOgAAAAAA9rA9EdRZa39C0k+0eRrAluWKZf3Kl0f1qS/d0Eyu1HDs1KFuffT50/qzTx6W4xDQAQAAAACw1+2JoA7YbfKlin79K6P6+T+6oan5YsOxxIEufeT9p/RtzwzKQ0AHAAAAAMC+QVAH7KBCuaLfHLmln/3CdU1kCw3HhmIh/b33ndJffPaovB6nTTMEAAAAAADtQlAH7IBSparfevG2PvmH13VnZrHh2GA0qB953yn95fPH5COgAwAAAABg3yKoW4Mxpk9rN5mIGGMOLPt81lpbWuM8QJJUrlT1X18e1898/h2NpXMNxw71BPTD3/yY/srFIQW8Le9pAgAAAAAAOhxB3dpekjS8xu2/ueLzb5b0xZbPBrtOtWr1e1fH9dOff0c3JxcajvV3+fV33ntSf+3PDCvoI6ADAAAAAAAugjpgG1lr9Qev39MnXnhHb0/MNRyLhnz6wfec0N/42ri6AnzrAQAAAACARqQFa7DWxts9B+wu1lp9/s37+sTnrun18WzDsZ6AV3/rG0/o+78hrp6gr00zBAAAAAAAnY6gDngE1lp96Z0pffyFa3rl1kzDsS6/R9/39Ql96BtPKBomoAMAAAAAABsjqAMe0p/emNbHX3hbI6lMw+1Bn6O/8bVx/eB7TirW5W/T7AAAAAAAwG5DUAds0Yujaf2bz17Tl29MN9zu9zr6q19zXH/nvSd1qCfYptkBAAAAAIDdiqAO2KRXbs3o4y9c0x9dm2y43ecx+q4LQ/rhb35MR6KhNs0OAAAAAADsdgR1QBNvjGf18Reu6XNvTjTc7nGMvvPcUf3d953SUCzcptkBAAAAAIC9gqAOWMc7E3P6xOeu6TOv3mu43RjpO959VB/+llOKH+hq0+wAAAAAAMBeQ1AHrHBzcl4//fl39LuvjMvaxmN//pkj+uj7T+mxQz3tmRwAAAAAANizCOqAmlvpnH768+/o0y/dUaXamNB96xMD+ujzp3X2SKRNswMAAAAAAHsdQR32vfGZRf3bP7yu/3L5lsorArpvfvygPvb843r6WLRNswMAAAAAAPsFQR32rfvZvH72C9f1ny7dUrFSbTj2DY8d0EefP63nhvvaNDsAAAAAALDfENRh35maL+jnv3hDv/aVURXKjQHdxURMP/r8aX3Nif42zQ4AAAAAAOxXBHXYN2ZyRX3qSzf1K19OKVesNBx79nivfvT5x/X1j/XLGNOmGQIAAAAAgP2MoA57XjZf0r//46T+/Z8kNV8oNxx76mhEP/r843rv4wcJ6AAAAAAAQFsR1GHPWiiU9ctfTun/+dJNzS6WGo6dOdyjjz5/Wt/6xAABHQAAAAAA6AgEddhzFosV/dpXUvr5P7qp9EKx4djJg1366POn9YGnjshxCOgAAAAAAEDnIKjDnpEvVfSfLo3p5754Q5NzhYZj8f6wPvz+U/r2dx2Vh4AOAAAAAAB0III67HrFclX/7+Vb+tkvXNfd2XzDsaO9IX34W07pL507Kq/HadMMAQAAAAAAmiOow65VrlT1O1fu6Gf+8B3dziw2HDscCepH3veY/rfzQ/J7CegAAAAAAEDnI6jDrlOpWv3uK3f00597R6npXMOxA90B/dB7T+p7vua4gj5Pm2YIAAAAAACwdQR12DWqVavPvHZXP/W5d3T9/nzDsb6wT3/7PSf11782rpCfgA4AAAAAAOw+BHXoeNZaffaNCX3ihWt6695cw7FI0Ksf+KYT+uDXJ9Qd4O0MAAAAAAB2L5INdCxrrb749qQ+/sI1vXpntuFYd8Cr7/+GhP7mNyQUDfnaNEMAAAAAAIDtQ1CHjmOt1f+8Pq2Pv/C2rozNNBwL+Tz64NfH9QPfeEJ9Xf42zRAAAAAAAGD7EdSho1xKpvVvPvu2vppMN9we8Dr63j8zrL/93pM60B1o0+wAAAAAAABah6AOHeHKWEafeOGa/vidqYbb/R5H331xSD/0zY9pIBJs0+wAAAAAAABaj6AObfXq7Vl9/IW39YW3Jxtu9zpGf/n8kH7kfY/paG+oTbMDAAAAAADYOQR1aIu37mX18c9e02ffmGi43THSXzp3TH/vfad0vD/cptkBAAAAAADsPII67Kjr9+f1U5+7pv/+6l1Z++B2Y6Rvf9egPvwtp3TiYHf7JggAAAAAANAmBHXYEampBf3M59/Rf335jqq28dgHnj6sj7z/tE4P9LRncgAAAAAAAB2AoA4tdTuT07/9/HX91pXbqqxI6N5/dkAfff6UnhyMtml2AAAAAAAAnYOgDi1xbzavT37hHf3myC2VKo0B3XtOH9THnj+tdw31tml2AAAAAAAAnYegDtvq/lxe/+6LN/QfvzqmYrnacOzrTvbrY8+f1vl4rE2zAwAAAAAA6FwEddgW6YWiPvVHN/Qrf5pSvtQY0J0f7tPHvvW0vu7kgfZMDgAAAAAAYBcgqMMjmc2V9At/fFP/4X8mtVCsNBx717GoPvatj+ubTh2QMaZNMwQAAAAAANgdCOrwUBYKZf3yl1P61B/dUDZfbjj2xJGIPvb8aX3L2UMEdAAAAAAAAJtEUIctyZcq+o2vjunnvnhdU/PFhmOnB7r10fef1v/y5GE5DgEdAAAAAADAVhDUYVPKlap++8pt/fTn3tH4bL7hWOJAlz7y/lP6tmcG5SGgAwAAAAAAeCgEddhQtWr1+6/e1SdeuKbk1ELDscFoUB9+/yl957lj8nqcNs0QAAAAAABgbyCow5qstfr8m/f1rz/7tt66N9dw7EC3Xz/8zY/puy8eV9DnadMMAQAAAAAA9haCOqzpF/74pv75Z95quK0n6NXffs9JffDr4uoK8NYBAAAAAADYTqQtWNN3PHtUH3/hmvKlqkI+j77/G+L6gW88qWjY1+6pAQAAAAAA7EkEdVjToZ6gfvCbTiqbL+mH3vuYDvYE2j0lAAAAAACAPY2gDuv66POn2z0FAAAAAACAfYNWnQAAAAAAAEAHIKgDAAAAAAAAOgBBHQAAAAAAANABCOoAAAAAAACADkBQBwAAAAAAAHQAgjoAAAAAAACgAxDUAQAAAAAAAB2AoA4AAAAAAADoAAR1AAAAAAAAQAcgqAMAAAAAAAA6AEEdAAAAAAAA0AEI6gAAAAAAAIAOQFAHAAAAAAAAdACCOgAAAAAAAKADENQBAAAAAAAAHYCgDgAAAAAAAOgABHUAAAAAAABAByCoAwAAAAAAADoAQR0AAAAAAADQAQjqAAAAAAAAgA5AUAcAAAAAAAB0AII6AAAAAAAAoAMQ1AEAAAAAAAAdgKAOAAAAAAAA6AAEdQAAAAAAAEAHIKgDAAAAAAAAOoCx1rZ7DvuWMWY6FArFzp492+6pAAAAAAC22ZtvvqnFxcW0tba/3XMBsDsQ1LWRMSYpKSIp1eaprOVM7fqtts4CK/G6dCZel87Da9KZeF06D69JZ+J16Ty8Jp1pN7wucUlZa22i3RMBsDsQ1GFNxpgXJcla+1y754IHeF06E69L5+E16Uy8Lp2H16Qz8bp0Hl6TzsTrAmAvYo86AAAAAAAAoAMQ1AEAAAAAAAAdgKAOAAAAAAAA6AAEdQAAAAAAAEAHIKgDAAAAAAAAOgBdXwEAAAAAAIAOQEUdAAAAAAAA0AEI6gAAAAAAAIAOQFAHAAAAAAAAdACCOgAAAAAAAKADENQBAAAAAAAAHYCgDgAAAAAAAOgABHUAAAAAAABAByCoQwNjzGFjzE8bY24YY/LGmAljzO8ZY76l3XPbj4wxPcaYbzfG/KQx5v8zxkwZY2ztcqbd89uvjDHHjTEfqX1vjBljCsaYOWPMK8aYf2mMOdLuOe43xpjzte+T/2GMuW6Mma29LneMMf/NGPMd7Z4jJGNMtzHm1rKfYx9s95z2G2PMB5d9/de7zLd7nvuZMeaEMeYTxpg3jTHztZ9nbxpjfskY8552z2+/2MT3yfILr8sOMsY4xpjvM8Z8zhgzaYwpGWNmjDFfNcb8I2NMT7vnCACPwlhr2z0HdAhjzDOS/lBSf+2mrKRuuYGulfRj1tp/2abp7Uu1cOHT6xw+a619ayfnA8kYMyRpVJJZdnNWUpckT+3zjKTvtNZ+YYent28ZY35e0g8uu2lekldScNltvy3pu621pZ2cGx4wxvyUpA8vu+n7rLW/3Kbp7Eu1cPQ/SCpJSq9z2oK19uSOTQp1xpjvl/RJSaHaTQtyfw9b+vzfW2v/Vjvmtt8YY+41OSUi93UpShq01k63flYwxoQl/Z6k9y27OSupRw9+NxuV9D5r7c0dnh4AbAsq6iBJMsaEJP2u3JDuJUlPWWujkvok/Ru5//D9C2PMt7ZvlvvWfUmfkfRPJP1Am+eCB2Hcf5f0lyXFat8rYUkfkJSU+33zX40xh9szxX3pTyV9VNJzknqstT3W2pCk45L+79o53ynpH7ZpfvueMeacpB+R9NV2zwWSpC9baw+vcyGkawNjzF+R9Ityw59PSjppre221oYlHZb0vZK+3MYp7isbfH8cttYelnStdurvE9LtqP9DbkhnJf2YpN7a72FBSd8taUbSsNzvJQDYlaiogyTJGPMRSZ+QW4Vyxlp7Z8XxT0v6DklXrLXPtWGK+5IxxmOtrSz7PC43CJKoqGsLY0xUUtxa+8o6x8/IDbuDkn7CWvtPdnJ+WJsx5tck/TVJNwkhdp4xxpEb0D0r6YKkK7VDVNTtsGUVdX9krX1ve2eDJcaYQ5LekvsfPT9mrf0XbZ4SNmCMebfcf+sl6S9Ya3+3nfPZT4wxo3L/E+6XrLV/c43jH5T7M05y/zM1s4PTA4BtQUUdlvzV2vVvrAzpapYqUs6xN9rOWR7SoTNYa2fXC+lqx9+S9JXap4TanWOkdj3Y1lnsX39X0nlJ/85a+1Kzk4F96O/IDenelvSv2jwXNPc3ateTclc9YOcM1K7X+7fkxWUfh1s8FwBoCYI6qLbh6lKg8AfrnPYVSbO1j9+3zjkAXEtLYDwbnoWd9HW16+SGZ2HbGWOOSvpJSROSfrzN0wE61dJ/mP6qtbba1plgQ8YYr6TvqX36H6215XbOZx9K1a6fXef40t80E5LGWz4bAGgBgjpI0lk92Hz19bVOqP3S+Hbt0yd2YlLAblT7Bf7ra5++1s657He1DqPPGGN+VtJ31W7+ZDvntE/9W7mbfP99a+1ss5OxY540xrxujFmsda1+rdZpNNHuie03xph+Sadqn/6JMeZ9xpg/MMZkjDE5Y8wbtY7iB9o5T9T9OUmHah//Sjsnsk/9Qu36+4wx/7C2JYmMMX5jzHfJ3crHyv03hz2eAOxKBHWQpCPLPt7of56Wjh3Z4Bxgv/thuZt+VyX9apvnsu8YY44ZY6wxxkqak/SKpB+SlJf0j621P9fWCe4zxpj/VdJflPRFa+2vt3s+aHBA7n/U5eTuqfmkpI9Iet0Y8z0b3RHb7tSyj79V0udq10tV2Wcl/QNJLxtjzu7w3LDaB2vXV621L7dzIvvUT0n6WdUa3UmaMcbMSFqU9J/l7vX47fybA2A3I6iDJHUt+3hxg/NytevuFs4F2LWMMc9I+ue1Tz9prV2zQhUtVZG73GVCUrF2W1nuL/NU0+0gY0yX3K95SW6Ajc4wLun/lPSUpKC1tl/uv+t/XtIbcjuO/qox5pvaN8V9p3fZxz8md3XD11hrI3Jfmw/I7QB/VNJv1yq3///27jVWrqoK4Ph/8WgpUqBgtcUHbUFQLIEooEGjqK1CEI0S30YBQf2AUkFU0ATEKA0RQYhRI2hFRUl8gYARJMoHImAVbCLKq4CIgMijlGJB6PLD3tMO48yl93LvnFPn/0smZ/bZ++xZ597cOzPr7LO3GhAROwBvrsVlDYYysur8zUuA4yjv7wDbseF77UxgdgOhSdKkMVEn2HDbq6QJioi5wM8pExf/gTL6QUOWmXdn5pzMnENJOOxOGdn4ecpolJc2GuBoOYWyMt8ZmXlD08GoyMzLMvOUzPxzZj5e9z2WmZdS5nK8hTKSa2mTcY6Y7s/jTwJvy8xroUw9kpm/BI6o9S+hjFJVM94DTKMkiH7QcCwjKSLmAFcBp1N+B3tREtovAk4AFgDfjghXTpa0yTJRJ4BHup7PGKNdZ+WkR8ZoI42ceoX9MmA+cDNwcGaubTYq1S+4N2Xmh4CvUJJG348I3/umWETsDRwD3ElJ2GkTUOcQ7IwKfmVEOCplOLo/V12Smbf0NsjMS4CbanHRUKJSP53VXn+Zmf9sNJLRdR6wH3BuZh6WmSsyc01m3pKZS4GP1HafioiF8sILWQAACc1JREFUzYUpSRPnlxXBU+el22mMdp26u6cwFmmTUicx/hXlNrK/AYsy895mo1IfZ9ft3gxeKU6T56uUUVmfBaIu7LH+0dVuet23df9u1IBr6jaAeQ3GMUq6P4fdOLDVhroXTGEsGqDOD7hvLbqIRAMiYg9gcS2e0a9NZn4PuJ/yPffN/dpIUtuZqBOUSVc7qyL1vS2sjkDZvRa9hUli/RxclwL7APdQknR/azYqDXBX1/NdGotidOxct+dRFvXofXR8o5Z9X2mP7ukwXDFxOFayYY7gjfmZ+3tpxmF1+wDwiwbjGGXdi6ncNka7lXU7b+pCkaSpY6JOZOZqYHktLh7Q7BWUiVoBrpjyoKSWi4gZlA/q+1Ou3C7KzJubjUpjmN/13Nv3pcH263p+R2NRjJDMXAf8thZfPEbTzgVTfy9DVi9Yv78Wf9iZ31FDt67r+QvHaNe5WLR6jDaS1Fom6tRxft2+r06K3+uTdfuHzBzrtgzp/15ETAN+CrwOeAh4oyu8NiciNo+Ip1sU5/i6fQL43RSHNPIyc15mxqBHV9PD6755TcU6Sp7u7yQitgU+U4vXZuZ9Ux+Vqu/V7cERsWtvZUQcDOxWi5cOLSp1LGbDFDDe9tqc67ueH9WvQUQcAjynFq/p10aS2s5EnTq+SblCOxO4uM4BQUTMjIjTgLfXdic2FN/Iiohndx7ArK6q7bvrnCB/OCJic0pi+0DKldqDMvOPzUY18l4ALI+IIyLi+Z2dEbFZROwdET8Ajqy7z87MBxuJUmrezhFxdUR8KCLWj0aJiGkRcSBlJcXdKKNWTmgqyBF1AWXF8C2An0XEvrD+/9iBwLm13bXAJc2EONI6i0jckJm/bzSSEZaZt1EW7wJYEhGnRsRzAOp8p4cBy2r97cBFw45RkiZDZDrNhYqI2ItyW+uOddfDlOXON6PMh3JiXU1JQxQRG/tHOj8zb5/KWAQR8RrgylpcC6wao/mdmbnvGPWaBBExj6fOVbOWcnvrTGB61/5lwFGZ+cSwYlN/Xf/XDs/MZU3GMkoG/K2sAbYFtqz7HgU+Widk1xDVCw1XAgvqrtWURVk6i63cCCzOzDsbCG9k1ZGm9wAzgE9n5mkNhzTS6p0/V/DU+epWU97zO+6lXEi9bpixSdJk2aLpANQemfmnuoz5CZRVkp5HmXvrWuCMzHRuOumpI5G3qo9B1k5xLCr+AbwLeANlfq25lAsOa4FbKbe6ficzr2osQqkd7gU+Drwa2AuYTZl/dg1wM+XL79cz0znQGpCZf68XTT8JHEpJ2CVwHfBj4KzMdI7N4XsnJUm3Dvh+w7GMvMy8OyJeDnyYcsfPQsr/sYeBWygjTs/21n1JmzJH1EmSJEmSJEkt4JxWkiRJkiRJUguYqJMkSZIkSZJawESdJEmSJEmS1AIm6iRJkiRJkqQWMFEnSZIkSZIktYCJOkmSJEmSJKkFTNRJkiRJkiRJLWCiTpIkSZIkSWoBE3WSJEmSJElSC5iokyRJkiRJklrARJ0kSZIkSZLUAibqJEmSJEmSpBYwUSdJkjZKRGR9zJvEPg+ofd4+WX1KkiRJmyoTdZIkSZIkSVILmKiTJEmSJEmSWsBEnSRJkiRJktQCJuokSZIkSZKkFjBRJ0nSiImIHSLigxHxk4j4a0Ssjog1EXFDRHwlInYaZ38n1wUhlkXEZhHxiYj4U+3z/oi4KCL228i+XhURF0fEvyLi37WfoyMiBrRfEBHHRcQVEXFbRKyNiIci4uq6f8Z4zkWSJElqUmRm0zFIkqQhiogvA8d17XoYeBaweS3fByzKzBU9x3U+NMzPzNu79p8MnAScB2wDvB14AlgDbFebPQm8LzMv6OnzAOA3wB3AycA5lAuJD3cdC/DVzFzS51yWAy+vxQRW1eM6ib3lwOszc3WfH4UkSZLUKo6okyRp9NwFLAVeBszMzO2A6cA+wK+A2cD5g0axjeGt9XEssG1mbg/sClxOSQJ+JyJ2GXDsbOCbwNeBufXYWcDZtf7jEfHSPsddByypr7NVZs4CZgBvAW6q57R0nOchSZIkNcIRdZIkab2ImA78EdgDOCAzr+yqe7oRdQCfy8wv9vS5FXA9sDtwbmYe2VV3AGVEHcA5mXlUn5hWAHsCJ2XmKeM4lwXAjcDjwOzMfHRjj5UkSZKa4Ig6SZK0XmY+RhkBB/CqcR7+KHBmnz7XAqfX4qFjjNQ7dcD+C+t24XiCycyVwJ+BrYG9x3OsJEmS1IQtmg5AkiQNX0S8GDgaeA0wjzK3XG8CbVyLSgDLM3PNgLrOyLztgfnAyp76B2pirZ+76nZWv8qIWAwcAewHzKXc+tprvOciSZIkDZ2JOkmSRkxEvJuy8MOWddc6yiIMj9XyNpTFJZ41zq7v2si62fxvom6sxR7W1u2WvRURcRbwsa5d/wEeqFuAHepx4z0XSZIkaei89VWSpBESEbOBb1GSVxdQFlvYKjNnZeaczJwDnNFpPpkvPYl9lQ4jDqIk6Z6krBi7KzA9M3fsOpdrpur1JUmSpMnmiDpJkkbLQZQRczcA783MdX3aPHeCfY91e+ncruf3TbD/Xu+o23My8/MD2kz0XCRJkqShc0SdJEmj5fl1u6Jfkq4u9PD6Cfa9b0RsPaDutXX7EHDbBPvv1TmX6/pVRsTOlFF2kiRJ0ibBRJ0kSaNlVd0uHLD66lHALhPse2vgmN6dETEdOLYWf5yZOcH+e3XOZc8B9V/CW14lSZK0CTFRJ0nSaPk1kMBC4KyI2B4gIraNiOOBrwH3T7DvVcAXIuKYiJhR+10AXAi8hLIoxNJnGH+3y+v2IxFxRERMq6/5woj4LvAe4MFJfD1JkiRpSpmokyRphGTmjcCZtXg08GBEPEBZKfU04ArgGxPs/kLgotr/qoh4ELgVeBNlwYfDM/PWZxB+r2XA1ZQ5d88FHq2veQfwAeAkYMUkvp4kSZI0pUzUSZI0YjLzWODDlLndHqMkuq4HlgAHA09MtGvKAg/HAn8BplFGtF0M7J+ZP3pmkfe8WObjwCLKKL2VwDpK7JcDh2TmFybz9SRJkqSpFpM3TYwkSRpFEXEyZfTadzPzsGajkSRJkjZdjqiTJEmSJEmSWsBEnSRJkiRJktQCJuokSZIkSZKkFjBRJ0mSJEmSJLWAi0lIkiRJkiRJLeCIOkmSJEmSJKkFTNRJkiRJkiRJLWCiTpIkSZIkSWoBE3WSJEmSJElSC5iokyRJkiRJklrARJ0kSZIkSZLUAibqJEmSJEmSpBYwUSdJkiRJkiS1gIk6SZIkSZIkqQVM1EmSJEmSJEktYKJOkiRJkiRJagETdZIkSZIkSVILmKiTJEmSJEmSWuC/LUNs0JuwxVEAAAAASUVORK5CYII=
"
width=629
height=392
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Visualizing-Regularization">Visualizing Regularization<a class="anchor-link" href="#Visualizing-Regularization">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>From the result above, we can see that as the penalty value, $\alpha$ increases:</p>
<ul>
<li><strong>Lasso regression</strong> shrinks coefficients all the way to zero, thus removing them from the model.</li>
<li><strong>Ridge regression</strong> shrinks coefficients toward zero, but they rarely reach zero.</li>
</ul>
<p>To get a sense of why this is happening, the visualization below depicts what happens when we apply the two different regularization. The general idea is that we are restricting the allowed values of our coefficients to a certain "region" and within that region, we wish to find the coefficients that result in the best model.</p>
<p><img src="images/lasso_ridge_coefficients.png" alt="Lasso and Ridge Coefficient Plots"></p>
<p>In this diagram, we are fitting a linear regression model with two features, $x_1$ and $x_2$.</p>
<ul>
<li>$\hat\beta$ represents the set of two coefficients, $\beta_1$ and $\beta_2$, which minimize the RSS for the <strong>unregularized model</strong>.</li>
<li>The ellipses that are centered around $\hat\beta$ represent <strong>regions of constant RSS</strong>. In other words, all of the points on a given ellipse share a common value of the RSS, despite the fact that they may have different values for $\beta_1$ and $\beta_2$. As the ellipses expand away from the least squares coefficient estimates, the RSS increases.</li>
<li>Regularization restricts the allowed positions of $\hat\beta$ to the <strong>blue constraint region</strong>. In this case, $\hat\beta$ is <strong>not</strong> within the blue constraint region. Thus, we need to move $\hat\beta$ until it intersects the blue region, while increasing the RSS as little as possible.<ul>
<li>For <strong>ridge</strong>, this region is a <strong>circle</strong> because it constrains the square of the coefficients. Thus the intersection will not generally occur on an axis, and so the coefficient estimates will be typically be non-zero.</li>
<li>For <strong>lasso</strong>, this region is a <strong>diamond</strong> because it constrains the absolute value of the coefficients. Because the constraint has corners at each of the axes, and so the ellipse will often intersect the constraint region at an axis. When this occurs, one of the coefficients will equal zero. In higher dimensions, many of the coefficient estimates may equal zero simultaneously. In the figure above, the intersection occurs at $\beta_1 = 0$, and so the resulting model will only include $\beta_2$.</li>
</ul>
</li>
<li>The <strong>size of the blue constraint region</strong> is determined by $\alpha$, with a smaller $\alpha$ resulting in a larger region:<ul>
<li>When $\alpha$ is zero, the blue region is infinitely large, and thus the coefficient sizes are not constrained.</li>
<li>When $\alpha$ increases, the blue region gets smaller and smaller. </li>
</ul>
</li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Advice-For-Applying-Regularization">Advice For Applying Regularization<a class="anchor-link" href="#Advice-For-Applying-Regularization">&#182;</a></h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>Signs and causes of overfitting in the original regression model</strong></p>
<ul>
<li>Linear models can overfit if you include irrelevant features, meaning features that are unrelated to the response. Or if you include highly correlated features, meaning two or more predictor variables are closely related to one another. Because it will learn a coefficient for every feature you include in the model, regardless of whether that feature has the signal or the noise. This is especially a problem when $p$ (number of features) is close to $n$ (number of observations).</li>
<li>Linear models that have large estimated coefficients is a sign that the model may be overfitting the data. The larger the absolute value of the coefficient, the more power it has to change the predicted response, resulting in a higher variance.</li>
</ul>
<p><strong>Should features be standardized?</strong></p>
<p>Yes, because L1 and L2 regularizers of linear models assume that all features are centered around 0 and have variance in the same order. If a feature has a variance that is orders of magnitude larger that others, features would be penalized simply because of their scale and make the model unable to learn from other features correctly as expected. Also, standardizing avoids penalizing the intercept, which wouldn't make intuitive sense.</p>
<p><strong>How should we choose between Lasso regression (L1) and Ridge regression (L2)?</strong></p>
<ul>
<li>If model performance is our primary concern or that we are not concerned with explicit feature selection, it is best to try both and see which one works better. Usually L2 regularization can be expected to give superior performance over L1.</li>
<li>Note that there's also a ElasticNet regression, which is a combination of Lasso regression and Ridge regression.</li>
<li>Lasso regression is preferred if we want a sparse model, meaning that we believe many features are irrelevant to the output.</li>
<li>When the dataset includes collinear features, Lasso regression is unstable in a similar way as unregularized linear models are, meaning that the coefficients (and thus feature ranks) can vary significantly even on small data changes. We will elaborate on this point in the following section.</li>
</ul>
<p>When using L2-norm, since the coefficients are squared in the penalty expression, it has a different effect from L1-norm, namely it forces the coefficient values to be spread out more equally. When the dataset at hand contains correlated features, it means that these features should get similar coefficients. Using an example of a linear model $Y = X1 + X2$, with strongly correlated feature of $X1$ and $X2$, then for L1-norm, the penalty is the same whether the learned model is $Y=1∗X1+1∗X2$ or $Y=2∗X1+0∗X2$. In both cases the penalty is $2∗α$. For L2-norm, however, the first model's penalty is $1^2+1^2=2α$, while for the second model is penalized with $2^2+0^2=4α$.</p>
<p>The effect of this is that models are much more stable (coefficients do not fluctuate on small data changes as is the case with unregularized or L1 models). So while L2 regularization does not perform feature selection the same way as L1 does, it is more useful for feature interpretation due to its stability and the fact that useful features still tend to have non-zero coefficients. But again, please do remove collinear features to prevent a bunch of downstream headaches.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">generate_random_data</span><span class="p">(</span><span class="n">size</span><span class="p">,</span> <span class="n">seed</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Example of collinear features existing within the data&quot;&quot;&quot;</span>
    <span class="n">rstate</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">RandomState</span><span class="p">(</span><span class="n">seed</span><span class="p">)</span>
    <span class="n">X_seed</span> <span class="o">=</span> <span class="n">rstate</span><span class="o">.</span><span class="n">normal</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">size</span><span class="p">)</span>
    <span class="n">X1</span> <span class="o">=</span> <span class="n">X_seed</span> <span class="o">+</span> <span class="n">rstate</span><span class="o">.</span><span class="n">normal</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="o">.</span><span class="mi">1</span><span class="p">,</span> <span class="n">size</span><span class="p">)</span>
    <span class="n">X2</span> <span class="o">=</span> <span class="n">X_seed</span> <span class="o">+</span> <span class="n">rstate</span><span class="o">.</span><span class="n">normal</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="o">.</span><span class="mi">1</span><span class="p">,</span> <span class="n">size</span><span class="p">)</span>
    <span class="n">X3</span> <span class="o">=</span> <span class="n">X_seed</span> <span class="o">+</span> <span class="n">rstate</span><span class="o">.</span><span class="n">normal</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="o">.</span><span class="mi">1</span><span class="p">,</span> <span class="n">size</span><span class="p">)</span>
    <span class="n">y</span> <span class="o">=</span> <span class="n">X1</span> <span class="o">+</span> <span class="n">X2</span> <span class="o">+</span> <span class="n">X3</span> <span class="o">+</span> <span class="n">rstate</span><span class="o">.</span><span class="n">normal</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">size</span><span class="p">)</span>
    <span class="n">X</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">X1</span><span class="p">,</span> <span class="n">X2</span><span class="p">,</span> <span class="n">X3</span><span class="p">])</span><span class="o">.</span><span class="n">T</span>
    <span class="k">return</span> <span class="n">X</span><span class="p">,</span> <span class="n">y</span>


<span class="k">def</span> <span class="nf">pretty_print_linear</span><span class="p">(</span><span class="n">estimator</span><span class="p">,</span> <span class="n">names</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">sort</span> <span class="o">=</span> <span class="kc">False</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;A helper method for pretty-printing linear models&#39; coefficients&quot;&quot;&quot;</span>
    <span class="n">coef</span> <span class="o">=</span> <span class="n">estimator</span><span class="o">.</span><span class="n">coef_</span>
    <span class="k">if</span> <span class="n">names</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">names</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;X</span><span class="si">%s</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">coef</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)]</span>

    <span class="n">info</span> <span class="o">=</span> <span class="nb">zip</span><span class="p">(</span><span class="n">coef</span><span class="p">,</span> <span class="n">names</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">sort</span><span class="p">:</span>
        <span class="n">info</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">info</span><span class="p">,</span> <span class="n">key</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">x</span><span class="p">:</span> <span class="o">-</span><span class="n">np</span><span class="o">.</span><span class="n">abs</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>

    <span class="n">output</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;</span><span class="si">{}</span><span class="s1"> * </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">coef</span><span class="p">,</span> <span class="mi">3</span><span class="p">),</span> <span class="n">name</span><span class="p">)</span> <span class="k">for</span> <span class="n">coef</span><span class="p">,</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">info</span><span class="p">]</span>
    <span class="n">output</span> <span class="o">=</span> <span class="s1">&#39; + &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">output</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># We run the two method 10 times with different random seeds</span>
<span class="c1"># confirming that Ridge is more stable than Lasso</span>
<span class="n">size</span> <span class="o">=</span> <span class="mi">100</span>
<span class="k">for</span> <span class="n">seed</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Random seed:&#39;</span><span class="p">,</span> <span class="n">seed</span><span class="p">)</span>
    <span class="n">X</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">generate_random_data</span><span class="p">(</span><span class="n">size</span><span class="p">,</span> <span class="n">seed</span><span class="p">)</span>

    <span class="n">lasso</span> <span class="o">=</span> <span class="n">Lasso</span><span class="p">()</span>
    <span class="n">lasso</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Lasso model:&#39;</span><span class="p">,</span> <span class="n">pretty_print_linear</span><span class="p">(</span><span class="n">lasso</span><span class="p">))</span>

    <span class="n">ridge</span> <span class="o">=</span> <span class="n">Ridge</span><span class="p">(</span><span class="n">alpha</span> <span class="o">=</span> <span class="mi">10</span><span class="p">)</span>
    <span class="n">ridge</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Ridge model:&#39;</span><span class="p">,</span> <span class="n">pretty_print_linear</span><span class="p">(</span><span class="n">ridge</span><span class="p">))</span>
    <span class="nb">print</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Random seed: 0
Lasso model: 0.486 * X1 + 1.508 * X2 + 0.0 * X3
Ridge model: 0.938 * X1 + 1.059 * X2 + 0.877 * X3

Random seed: 1
Lasso model: 1.034 * X1 + 0.626 * X2 + 0.0 * X3
Ridge model: 0.984 * X1 + 1.068 * X2 + 0.759 * X3

Random seed: 2
Lasso model: 1.361 * X1 + 0.0 * X2 + 0.782 * X3
Ridge model: 0.972 * X1 + 0.943 * X2 + 1.085 * X3

Random seed: 3
Lasso model: 0.0 * X1 + 1.008 * X2 + 1.134 * X3
Ridge model: 0.919 * X1 + 1.005 * X2 + 1.033 * X3

Random seed: 4
Lasso model: 0.27 * X1 + 0.0 * X2 + 1.832 * X3
Ridge model: 0.964 * X1 + 0.982 * X2 + 1.098 * X3

Random seed: 5
Lasso model: 0.0 * X1 + 0.035 * X2 + 1.854 * X3
Ridge model: 0.758 * X1 + 1.011 * X2 + 1.139 * X3

Random seed: 6
Lasso model: 0.486 * X1 + 0.0 * X2 + 1.601 * X3
Ridge model: 1.016 * X1 + 0.89 * X2 + 1.091 * X3

Random seed: 7
Lasso model: 0.441 * X1 + 0.036 * X2 + 1.582 * X3
Ridge model: 1.018 * X1 + 1.039 * X2 + 0.901 * X3

Random seed: 8
Lasso model: 0.28 * X1 + 1.974 * X2 + 0.0 * X3
Ridge model: 0.907 * X1 + 1.071 * X2 + 1.008 * X3

Random seed: 9
Lasso model: 0.0 * X1 + 0.0 * X2 + 1.912 * X3
Ridge model: 0.896 * X1 + 0.903 * X2 + 0.98 * X3

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>How do we choose the $\alpha$ parameter?</strong></p>
<p>We can either use a validation set if we have lots of data or use cross validation for smaller data sets. See a quick examples below that uses cross validation with <code>RidgeCV</code> and <code>LassoCV</code>, which is function that performs ridge regression and lasso regression with built-in cross-validation of the alpha parameter.</p>
<blockquote><p>From R's <a href="https://web.stanford.edu/~hastie/glmnet/glmnet_alpha.html">glmnet package vignette</a></p>
<p>It is known that the ridge penalty shrinks the coefficients of correlated predictors towards each other while the lasso tends to pick one of them and discard the others. The elastic-net penalty mixes these two; if predictors are correlated in groups, an $\alpha = 0.5$ tends to select the groups in or out together. This is a higher level parameter, and users might pick a value upfront, else experiment with a few different values. One use of $\alpha$ is for numerical stability; for example, the elastic net with $\alpha = 1−\epsilon$ for some small $\epsilon &gt; 0$ performs much like the lasso, but removes any degeneracies and wild behavior caused by extreme correlations.</p>
</blockquote>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># alpha: array of alpha values to try; must be positive, increase for more regularization</span>
<span class="c1"># create an array of alpha values and select the best one with RidgeCV</span>
<span class="n">alpha_range</span> <span class="o">=</span> <span class="mf">10.</span> <span class="o">**</span> <span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="o">-</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
<span class="n">ridge_cv</span> <span class="o">=</span> <span class="n">RidgeCV</span><span class="p">(</span><span class="n">alphas</span> <span class="o">=</span> <span class="n">alpha_range</span><span class="p">,</span> <span class="n">fit_intercept</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">ridge_cv</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_std</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>

<span class="c1"># examine the coefficients and the errors of the predictions </span>
<span class="c1"># using the best alpha value</span>
<span class="n">y_pred</span> <span class="o">=</span> <span class="n">ridge_cv</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test_std</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;coefficients:</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">ridge_cv</span><span class="o">.</span><span class="n">coef_</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;best alpha:</span><span class="se">\n</span><span class="s1">&#39;</span> <span class="p">,</span> <span class="n">ridge_cv</span><span class="o">.</span><span class="n">alpha_</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">RSS:&#39;</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">((</span><span class="n">y_test</span> <span class="o">-</span> <span class="n">y_pred</span><span class="p">)</span> <span class="o">**</span> <span class="mi">2</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>coefficients:
 [-1.49246448  0.37088936 -0.70836731  1.08568161 -0.80970633  4.4075122
 -0.80450999]
best alpha:
 10.0

RSS: 4366.321935003472
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># n_alphas: number of alpha values (automatically chosen) to try</span>
<span class="c1"># select the best alpha with LassoCV</span>
<span class="n">lasso_cv</span> <span class="o">=</span> <span class="n">LassoCV</span><span class="p">(</span><span class="n">n_alphas</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span> <span class="n">fit_intercept</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">lasso_cv</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train_std</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>

<span class="c1"># examine the coefficients and the errors of the predictions </span>
<span class="c1"># using the best alpha value</span>
<span class="n">y_pred</span> <span class="o">=</span> <span class="n">lasso_cv</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test_std</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;coefficients:</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">lasso_cv</span><span class="o">.</span><span class="n">coef_</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;best alpha:</span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">lasso_cv</span><span class="o">.</span><span class="n">alpha_</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;</span><span class="se">\n</span><span class="s1">RSS:&#39;</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">((</span> <span class="n">y_test</span> <span class="o">-</span> <span class="n">y_pred</span> <span class="p">)</span> <span class="o">**</span> <span class="mi">2</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>coefficients:
 [-1.5149245   0.34021279 -0.67185865  1.09280671 -0.81071974  4.53310098
 -0.81752854]
best alpha:
 0.005835182912170716

RSS: 4296.025010307988
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>To sum it up, overfitting is when we build a predictive model that fits the data "too closely", so that it captures the random noise in the data rather than true patterns. As a result, the model predictions will be wrong when applied to new data. Give that our data is sufficiently large and clean, regularization is one good way to prevent overfitting from occurring.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Reference">Reference<a class="anchor-link" href="#Reference">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<ul>
<li><a href="http://nbviewer.jupyter.org/github/justmarkham/DAT8/blob/master/notebooks/20_regularization.ipynb">Notebook: Regularization</a></li>
<li><a href="http://scott.fortmann-roe.com/docs/BiasVariance.html">Blog: Understanding the Bias-Variance Tradeoff</a></li>
<li><a href="http://blog.datadive.net/selecting-good-features-part-ii-linear-models-and-regularization/">Blog: Selecting good features – Part II: linear models and regularization</a></li>
</ul>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span>
</pre></div>

    </div>
</div>
</div>

</div>
    </div>
  </div>
</body>



</html>
