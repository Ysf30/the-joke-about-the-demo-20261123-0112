#!/usr/bin/env python3
"""Write this entry's one-line joke to /output/entry.txt.

The joke, picked against the judge's brief (most important first):

1. On subject: an AI coding agent, a live demo, a client in the room.
2. Surprise punchline: the agent demos a feature nobody asked for — and
   the client buys *that* one, not the real one. The listener expects a
   complaint about the demo going wrong; instead the wrong demo wins.
3. Truth devs recognise: agents go off-script in demos and invent things,
   and the accidental demo is often the one the client falls for.
4. Economy: one line, 110 characters, no setup beyond the scene itself.
5. Freshness: none of the stock angles — no deleted tests, no blamed
   prompt, no ticket filed, no lockout, no swapped recording.

Why not the alternates: ALT-1 ("I said I don't know, it wrote it") is
snappier but its twist is a stock trope — devs not understanding
agent-written code is recognition, not surprise. ALT-2 ("I'm the intern
now") telegraphs its punchline; the reversal is a known meme format.
ALT-3 ("holding the clicker") is a vivid image but ends on an observation,
not a reversal — no stakes, no surprise. The chosen joke is the only one
with a real reversal and real stakes (a sale) at the end.

The program validates the joke against the sealed gate first (UTF-8,
1-280 Unicode code points, not blank), writes exactly the joke bytes with
no trailing newline, then reads the file back and proves the bytes on
disk are the joke.
"""

import hashlib
import os
import sys
from pathlib import Path

JOKE = "I asked my agent to demo the feature; it demoed one I never asked for, and the client bought that one instead."


def validate_joke(text: str) -> bytes:
    """Gate-check the joke; return its exact UTF-8 bytes."""
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"gate fail: {len(text)} code points, need 1..280")
    if not text.strip():
        raise SystemExit("gate fail: joke is blank")
    data = text.encode("utf-8")
    if data.endswith(b"\n"):
        raise SystemExit("gate fail: trailing newline")
    return data


def main() -> int:
    data = validate_joke(JOKE)
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    back = out.read_bytes()
    if back != data:
        raise SystemExit("verify fail: bytes on disk differ from the joke")
    if back.decode("utf-8") != JOKE:
        raise SystemExit("verify fail: file does not decode to the joke")
    print(f"wrote {len(JOKE)} chars ({len(data)} bytes) to {out}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    print(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
