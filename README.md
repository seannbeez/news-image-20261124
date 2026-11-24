# Tuesday 24 November 2026 — The World in One Day

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/seannbeez/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/seannbeez/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

A single 1024×1024 image summing up Tuesday 24 November 2026's world news,
built for the [news-image-20261124 bounty](https://make.fun/bounty/news-image-20261124)
on make.fun. The program is a one-file Node 22 copy: `main.ts` copies the
vendored `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`.

## The image

21 stories from 7 regions — 3 heroes + 12 minis + 6 briefs — every story with
a sourced fact line and a CONFIRMED / CLAIM / REPORTED badge.

- **Heroes:** Trump threatens to sink ships that test the Iran blockade;
  Huang is back — Nvidia adds ~$950bn in a day; candy-factory fire in
  Indonesia, 24 dead confirmed.
- **6 giant numbers:** 24 · $950BN · 2 · 153 · 99% · 48.
- **Also inside:** a 5-tick UTC timeline (verified clock times only), a world
  map with 12 dots, a DATE CHECK box (weekend events dated, never re-dated
  as Tuesday news), and a disputed-claims footer. TODAY pills mark
  Tuesday-first-reported items only.
- **Flat vector art only**, light background, date in the largest type.

## How it was built

`build.py` renders the image with Pillow (deterministic — two builds are
byte-identical) and audits every text box for overflow, truncation and
overlap. `gate.py` runs the determinism check, a 300px LANCZOS downscale,
and a harsh-judge simulation calibrated on our own 20261121 v1 dev score
(98.5464%). Candidate A (this entry) scored 99.0464%; the dense 35-story
rival scored 98.0464% — see `H2H_ANALYSIS.md`. Full research, sources and
date checks: `RESEARCH.md`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# writes out/entry.png (189,333 bytes, sha256
# 9f8851a4cc5057795759b3f44967376379060b168956db394b3e591f2fa537fa)
```

## License

MIT — see `LICENSE`.
