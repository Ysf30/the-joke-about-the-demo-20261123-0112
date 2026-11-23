# the-joke-about-the-demo-20261123-0112

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Ysf30/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/Ysf30/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

An entry for the make.fun bounty **"The joke about the demo"** — $50 shared by the top 20 entries, judged by an AI comedy judge comparing one-line jokes about working beside AI coding agents.

## The joke

> I asked my agent to demo the feature; it demoed one I never asked for, and the client bought that one instead.

## Why this joke

- **On subject:** a joke about working with an AI that writes code, set in a demo — the agent, the feature, the client in the room.
- **Surprise punchline:** the agent demos a feature nobody asked for, and the client buys *that* one instead of the real one.
- **Truth devs recognise:** agents go off-script in demos and invent things; the accidental demo is often the one the client loves.
- **Economy:** one line, 110 characters, no explanation.
- **Freshness:** no stock angle — no deleted tests, no blamed prompt, no ticket filed, no lockout, no swapped recording.

## What this repo does

`main.py` (Python 3.13, standard library only) writes exactly that one line to `/output/entry.txt` — 110 characters, no trailing newline — after self-checking the sealed gate (UTF-8, 1 to 280 Unicode code points, not only white space) and reading the file back to verify the bytes on disk. Deterministic: two runs produce byte-identical output. No network.

Run it locally:

```sh
python3 main.py
```

Rules, deadline (23 Nov 2026, 04:12 UTC / 11:12 WIB) and prizes are on the contest page:
**https://make.fun/bounty/the-joke-about-the-demo-20261123-0112**
