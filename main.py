#!/usr/bin/env python3
"""Write the entry joke to /output/entry.txt.

One-line joke about working beside an AI coding agent, written for a live
demo audience. Chosen against the judge's brief, in its order:

1. On subject: a joke about working with an AI that writes code, set in a
   demo — the agent, the feature, the client in the room.
2. Surprise punchline: the agent demos a feature nobody asked for, and the
   client buys *that* one instead of the real one.
3. Truth devs recognise: agents go off-script in demos and invent things;
   the accidental demo is often the one the client loves.
4. Economy: one line, 110 characters, no explanation, no setup beyond the
   scene itself.
5. Freshness: no stock angle — no deleted tests, no blamed prompt, no
   ticket filed, no lockout, no swapped recording.

The program self-checks the sealed gate before it exits: the text must be
UTF-8, 1 to 280 Unicode code points, and not only white space. It writes
exactly the joke bytes (no trailing newline, so the file stays minimal —
exact rate ties break to the smaller text) and reads the file back to
prove the bytes on disk are the joke.
"""

import hashlib
import os
import sys
from pathlib import Path

JOKE = "I asked my agent to demo the feature; it demoed one I never asked for, and the client bought that one instead."


def check_gate(text: str) -> None:
    """Fail loudly if the joke would fail the sealed gate."""
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"gate fail: {len(text)} chars, need 1..280")
    if not text.strip():
        raise SystemExit("gate fail: text is only white space")
    text.encode("utf-8")  # must be encodable UTF-8 text


def main() -> int:
    check_gate(JOKE)
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    data = JOKE.encode("utf-8")
    out.write_bytes(data)
    back = out.read_bytes().decode("utf-8")
    if back != JOKE:
        raise SystemExit("verify fail: bytes on disk differ from the joke")
    print(f"wrote {len(JOKE)} chars ({len(data)} bytes) to {out}")
    print(f"sha256 {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
