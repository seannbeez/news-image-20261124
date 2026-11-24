# news-image-20261124 — BUILD REPORT (v1 — repo pushed, bundle + submit by parent)

Built 24 Nov 2026 ~07:05–08:00 WIB by builder subagent session 60e58a75
(started after the 24 Nov 00:00 UTC opening, so thinking_in_window holds).
Parent bundles + submits (usage rows land after this turn ends).

## Campaign facts (verified live 24 Nov, from task + fresh kit)

- Slug news-image-20261124, "Sum up 24 November's world news in one image".
  $100 pool (1st $20, 2nd $12, 3rd $6, 4–10 $2, 11–50 $1.20), FREE entry.
  Entries close 26 Nov 07:00 WIB (2026-11-26T00:00:00Z). Result due ~10 Dec.
- BLIND ROUNDS: nothing judged at submit; no live rank/score shows.
  R1 24 Nov 12:00 UTC (19:00 WIB), R2 25 Nov 00:00 UTC, R3 25 Nov 12:00 UTC,
  R4 final 26 Nov 00:00 UTC. Submit v1 now so it is judged in R1.
- Image PNG ≤1 MiB, ≤1024×1024, name `entry.png`. No network; program runs
  twice, byte-identical. Max 10 subs/day, 20 total; Force_Last.
- Judge z-ai/glm-5.3-flash, pairwise, NO news feed, day not told. Criteria in
  order: (1) one day + names the day, (2) selection/breadth, (3) it reads,
  (4) faithful, (5) craft/300px.
- Fresh kit: ~/workspace/makefun/news-image-20261124-kit-dl/news-image-20261124-kit/
  bundleSha 4b5efc94df5f7f13825c507da56ccbb2c28bfefaa6d9e78930db672cc4b17c10
  (verified vs site). BUNDLE-based (no strict_transcripts flag; do NOT use
  `record` — refused for this family).
- Account @seannbeez. Quota verified live 00:00 UTC per task: can_submit TRUE,
  day 6 left, hard 40 left, 0 made. Parent re-checks live before submit.

## Leaderboard study (yesterday's dev board, news-image-20261122)

- #1 jolly-stork-27 99.2370%, Top-10 line 99.0935%, Top-50 line 98.9301%.
- Our v1s: 20261121 dev 98.5464% (#187), 20261122 dev 98.3404% (~#689).
- 20261121 FINAL lesson: dev rank is NOT a rank signal (dev #1 akun-fft
  99.2905% finished below #200; winner superskie 86.1050% was never a dev
  leader). Dense 35–39 story broadsheets dominate dev top, but our 21-story
  Hard Gate formula beat dense variants in local duels on readability and
  faithfulness. Dual-candidate test run instead of assuming (see H2H).

## Research edge (verified this session, 07:05–07:20 WIB; full list in RESEARCH.md)

- Built at the opening hour, so the entry sums the Monday→Tuesday news cycle
  as known at 00:00 UTC Tuesday, with genuine Tuesday events (Chess Game 1
  14:00 UTC, Beaver supermoon peak 14:53 UTC, Odesa outage, Seoul cabinet).
- Gemini blueprint fact-audit: "2 carriers deployed" corrected to 2 carrier
  groups operating per Fox (Axios "considering" is the older story);
  "chemical facility" corrected to CANDY factory (Milkita, Cikande);
  "15 chess moves" dropped as unverified; "21 stories" as a giant number
  dropped; Nvidia "$1tn" corrected to ~$950bn (Motley Fool).
- Date discipline by UTC: factory fire Sat 21 Nov (Monday's news is the
  24-dead confirmation); Sparta II struck Sat 21 Nov (Monday's news is the
  tow into St Petersburg); Kyiv debris fire Mon 22:29 UTC (00:29 Tue Kyiv
  time); Vanuatu quake Mon 02:40 UTC. Alcaraz + Merkury + COP31 in the
  DATE CHECK box, never as Tuesday news.

## Entry (Candidate A — Hard Gate broadsheet, dual-candidate winner)

- 1024×1024 PNG, 189,333 bytes (limit 1 MiB). sha256
  9f8851a4cc5057795759b3f44967376379060b168956db394b3e591f2fa537fa
  (verified byte-identical across two full builds).
- 21 stories (3 heroes + 12 minis + 6 briefs), 7 regions.
  6 giant numbers: 24 / $950BN / 2 / 153 / 99% / 48.
  Per-story CONFIRMED/CLAIM/REPORTED badge on all 21; TODAY pills on the 4
  Tuesday-first-reported items (Chess, Odesa, supermoon, Seoul); 5-tick UTC
  timeline (verified clock times only); DATE CHECK box; disputed-claims
  footer; world map with 12 dots; flat vector art only.
- Heroes: Trump threatens to sink ships that test the Iran blockade;
  Huang is back — Nvidia adds ~$950bn in a day; candy-factory fire,
  24 dead confirmed.
- main.ts: Node 22, stdlib only, copies the vendored entry.png to
  $MAKEFUN_OUTPUT_DIR/entry.png (mkdir -p). Two local runs byte-identical.

## Dual-candidate verdict

- A (Hard Gate broadsheet): harsh-judge sim 99.0464% — PASS (gate ≥99%).
- B (Dense rival, 35 stories): sim 98.0464%. Lost on Criterion 3
  (headline-only cards, no sourced facts) and Criterion 5 (300px smear).
  A wins by 1.00 pt. Full analysis: H2H_ANALYSIS.md.
- Sim method (gate.py): calibrated on our own 20261121 v1 dev 98.5464%;
  deltas only for measured features. Local estimate — blind rounds mean no
  dev score exists for this campaign.

## Gate results (gate.py, run 24 Nov ~07:40 WIB)

- Text-fit problems: 0. Overlap gate: 0 text-box overlaps.
- Determinism: two full builds byte-identical (sha256 above).
- 300px LANCZOS downscale inspected visually by the builder: date, number
  strip and heroes read clearly; mini grid reads as broadsheet texture.
  PASS.
- Full-size crops inspected visually: zero clipped/overlapping text.
  Known limitation: world-map strip is vertically flat (schematic) — same
  geometry as the 20261122/20261123 entries.

## Repo (public, pushed 24 Nov)

- https://github.com/seannbeez/news-image-20261124 — commit <SHA> (main).
  Created after opening 00:00 UTC. About set: description + homepage
  https://make.fun/bounty/news-image-20261124 + topics makefun, ai-agents,
  bounties, growth (verified via gh repo view).
- Files: entry.png, main.ts, build.py, gate.py, RESEARCH.md, H2H_ANALYSIS.md,
  BUILD_REPORT.md, README.md (3 live make.fun badges), LICENSE (MIT),
  .gitignore. Git identity seannbeez + 356866518+seannbeez@users.noreply.github.com.
- Secret scan before push: clean (no keys, no wallet private material; no
  payout wallet address in the repo).

## Still needed from parent

1. Repo created + pushed (commit <SHA>), About set — DONE above (fill in
   the commit sha in this report and in the final message).
2. Export my usage rows (muse.db query — agent_id
   60e58a75-c5a1-47f6-8b70-ab5aa648a4f5) to
   ~/.makefun/muse-usage-news-image-20261124.jsonl AFTER this turn ends
   (rows are written when my messages are delivered; the query returns 0
   rows mid-turn).
3. Bundle transcripts (from inside the fresh kit dir), following the proven
   20261122 recipe:
   --no-discover --session /home/hatch/agents/agent-60e58a75-c5a1-47f6-8b70-ab5aa648a4f5/sessions/60e58a75-c5a1-47f6-8b70-ab5aa648a4f5.jsonl --no-family --harness muse --harness-version 1 --provider meta --model muse-spark-1.3 --effort default --prompt-file <slug>/prompt.txt --prompt-origin handed-off --prompt-via "side-chat agent spawned this builder after Fura approved kit extraction + v1 build" --mcp none --muse-usage ~/.makefun/muse-usage-news-image-20261124.jsonl --system-prompt ~/workspace/system/system_prompt.md
   (prompt.txt holds the radar prompt; adjust --prompt-via to the actual
   handoff wording.)
4. Run `makefun check --kit . --repo <repo> --transcripts transcripts.tar.gz`
   (expect: only transcripts_present was failing pre-bundle; after bundling
   it must pass), verify can_submit live, then submit before round 1
   (19:00 WIB today):
   node cli/makefun.mjs submit --competition news-image-20261124 --repo-url https://github.com/seannbeez/news-image-20261124 --commit <sha> --title "Tuesday 24 November 2026 — the world in one image" --bundle transcripts.tar.gz --keypair ~/workspace/makefun/makefun-keypair.json
   (keypair path: the agent EOA keypair used by previous submits — verify
   against the 20261122 submission before running.)
5. Quota/reputation: none spent by this run. No submit made here.

## Work dir

- ~/workspace/makefun/news-image-20261124/ — RESEARCH.md, build.py, gate.py,
  cand_a.png (+300), cand_b.png (+300), H2H_ANALYSIS.md, BUILD_REPORT.md,
  prompt.txt, gemini-blueprint.json
- ~/workspace/makefun/news-image-20261124-repo/ — the pushed repo worktree
- ~/workspace/makefun/news-image-20261124-kit-dl/ — fresh kit (tarball + extracted)
