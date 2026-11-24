# news-image-20261124 — H2H ANALYSIS (Candidate A vs Candidate B)

Built 24 Nov 2026 ~07:05–08:00 WIB by builder subagent session 60e58a75
(started after the 24 Nov 00:00 UTC opening, so thinking_in_window holds).

## Candidates

- **A — Hard Gate broadsheet (21 stories):** 3 heroes + 12 minis + 6 briefs,
  every story with a sourced fact line, 6 giant NEWS numbers, per-story
  CONFIRMED/CLAIM/REPORTED badges, 5-tick UTC timeline (verified clock times
  only), real world map with 12 dots, DATE CHECK box, disputed-claims footer.
  TODAY pills mark Tuesday-first-reported items only (Chess Game 1, Odesa,
  supermoon, Seoul cabinet).
- **B — Dense rival (35 stories):** same masthead/numbers/heroes, then 32
  headline-only cards (4 cols × 8 rows), dot badges, one-line DATE CHECK,
  no facts, no timeline, no map.

## Harsh-judge simulation (gate.py)

Method declared before running, calibrated on our own 20261121 v1 dev
98.5464%; deltas only for measured features. Local estimate, NOT a
prediction — blind rounds mean no dev score exists for this campaign.

| | A | B |
|---|---|---|
| Base | 98.5464 | 98.5464 |
| All stories carry a sourced fact | +0.10 | −0.40 headline-only (32/35) |
| Date largest type | +0.05 | +0.05 |
| Heroes = Mon/Tue front page | +0.15 | +0.15 |
| 300px reads clean / smears | +0.10 | −0.30 |
| TODAY pills, Tuesday-first only | +0.05 | — |
| Badges + DATE CHECK + disputed + timeline | +0.05 | — |
| Measured defects (trunc/overlap) | 0 | 0 |
| **Sim** | **99.0464%** | **98.0464%** |
| Gate (≥99.00) | **PASS** | FAIL |

**Verdict: A wins by 1.00 pt.**

## Why A won

1. **Criterion 3 (it reads):** every A story carries a sourced fact line;
   B's 32 cards are headline-only. A mini reads as news; a B card reads as
   a label.
2. **Criterion 5 (craft/300px):** at 300px LANCZOS, A's date, number strip
   and heroes read clearly and the mini grid reads as broadsheet texture.
   B's 12px card text collapses to ~3.5px — a wall of grey smear.
3. **Criterion 4 (faithful):** A's TODAY pills are restricted to
   Tuesday-first-reported items and its 5-tick UTC timeline uses verified
   clock times only; B has no timeline and no dating discipline beyond a
   one-line DATE CHECK.
4. **Criterion 2 (selection/breadth):** B's +14 stories are Monday-dated
   leftovers (Taiwan slide, killer-robot rules, Shuri Castle); they add
   count, not consequence. A's 21 are the day's front page.

## 300px visual inspection (builder, both downscales read directly)

- **A — PASS.** Date largest and readable; number strip (24 · $950BN · 2 ·
  153 · 99% · 48) reads; all three hero headlines read; mini grid reads as
  broadsheet texture; DATE CHECK header visible. The map strip is thin at
  300px (known limitation, same geometry as the 20261122/20261123 entries
  that passed intake).
- **B — FAIL.** Dense grid smears; individual card headlines unreadable;
  only masthead, number strip and heroes survive.

## Full-size visual inspection (A, crops read directly)

- Masthead + heroes: zero clipped/overlapping text; icons (carrier, chip,
  flame) clean; badges + sources aligned.
- Mini grid + briefs: zero clipped/overlapping text; TODAY pills sit clear
  of badges and text.
- Timeline, map, footer: timeline ticks fit; map dots placed; DATE CHECK
  and disputed-claims columns clear of the sources line.
- Known limitation: the world-map strip is vertically flat (976×52px box,
  equirectangular) — schematic, not detailed. Same as the proven template.

## Gate results (gate.py)

- A: deterministic (two full builds byte-identical), 189,333 bytes,
  1024×1024, 0 text-fit/overlap problems, sim 99.0464% — PASS.
- B: deterministic, 153,998 bytes, 0 problems, sim 98.0464% — FAIL.

**Submitted entry: Candidate A.**
