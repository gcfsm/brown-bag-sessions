#!/usr/bin/env python3
"""Put a follow-along QR code on a deck's title slide.

The QR is generated once and inlined as SVG. Nothing is fetched at view
time, so the deck still opens with no network — same as every other asset
in these files.

    pip install segno
    python3 tools/add-qr.py sessions/05-data-modeling-nosql

Re-running on a deck that already has one replaces it, so this is safe to
run again after a slug changes.
"""

import io
import re
import sys
from pathlib import Path

import segno

BASE = "https://gcfsm.github.io/brown-bag-sessions"
HUB = "gcfsm.github.io/brown-bag-sessions"

CSS = """  /* ---------- follow-along qr (title slide) ---------- */

  .qr {
    position: absolute;
    right: var(--pad-x);
    bottom: 3rem;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 0.7rem;
  }

  .qr__cap {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    line-height: 1.7;
    letter-spacing: 0.1em;
    color: var(--gold-dim);
    text-align: right;
    white-space: nowrap;
  }

  .qr__cap span {
    display: block;
    font-size: 0.68rem;
    letter-spacing: 0.02em;
    color: var(--muted);
  }

  .qr svg {
    display: block;
    width: 10rem;
    height: 10rem;
    border-radius: 3px;
  }

  @media (max-width: 900px) {
    .qr { position: static; align-items: flex-start; }
    .qr__cap { text-align: left; }
  }
"""

CSS_MARK = "  /* ---------- follow-along qr (title slide) ---------- */"


def qr_svg(url):
    """An inline SVG QR, parchment on ink so it scans off a projector."""
    code = segno.make(url, error="m")
    buf = io.BytesIO()
    code.save(buf, kind="svg", scale=10, border=3,
              dark="#0e1116", light="#e8e1cf",
              xmldecl=False, svgns=True, svgclass=None, lineclass=None,
              omitsize=True, nl=False)
    return code.version, buf.getvalue().decode("utf-8")


def main(deck_dir):
    deck = Path(deck_dir)
    path = deck / "slides.html"
    html = path.read_text()

    url = "%s/sessions/%s/slides.html" % (BASE, deck.name)
    version, svg = qr_svg(url)

    # Drop any previous block and its stylesheet, so this is idempotent.
    html = re.sub(r'\n *<div class="qr">.*?</div>\n', "", html, flags=re.S)
    if CSS_MARK in html:
        start = html.index(CSS_MARK)
        html = html[:start] + html[html.index("</style>", start):]

    html = html.replace("</style>", CSS + "</style>", 1)

    block = (
        '\n      <div class="qr">\n'
        "        %s\n"
        '        <p class="qr__cap">Scan to follow along<span>%s</span></p>\n'
        "      </div>\n" % (svg, HUB)
    )

    # The footline is the last thing on every title slide.
    foot = re.search(r'^ *<p class="footline">.*$', html, flags=re.M)
    if not foot:
        raise SystemExit("%s: no .footline on the title slide" % path)
    html = html[: foot.start()] + block + html[foot.start():]

    path.write_text(html)
    print("%s  QR v%d  ->  %s" % (path, version, url))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for arg in sys.argv[1:]:
        main(arg)
