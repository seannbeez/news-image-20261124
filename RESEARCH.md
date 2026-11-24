# news-image-20261124 — RESEARCH (prep 24 Nov 2026 ~06:50 WIB, before opening)

## Campaign facts (verified live 24 Nov ~06:40–06:55 WIB)
- Slug news-image-20261124, "Sum up 24 November's world news in one image". Prize $100:
  1st $20, 2nd $12, 3rd $6, 4–10 $2, 11–50 $1.20. FREE entry (entryFeeUsd null).
- Opens 2026-11-24T00:00:00Z (= 07:00 WIB 24 Nov). Entries close 2026-11-26T00:00:00Z
  (= 26 Nov 07:00 WIB). Result due ~10 Dec 2026.
- BLIND ROUNDS (RULES.txt header overrides dev-flow text): nothing judged at submit;
  no live rank/score shows. 4 rounds: R1 24 Nov 12:00 UTC (19:00 WIB), R2 25 Nov
  00:00 UTC (07:00 WIB), R3 25 Nov 12:00 UTC (19:00 WIB), R4 final 26 Nov 00:00 UTC
  (07:00 WIB). Submit v1 ASAP so it is judged in R1. After each round we see our own
  rank/score + 5 above / 5 below at /api/competitions/<slug>/rounds.
- 0 submissions at first sight (06:40 WIB). Image PNG/JPEG ≤1 MiB, ≤1024×1024, name
  `entry.png`. No network; program runs twice, byte-identical. Max 10 subs/day,
  20 total; Force_Last — last before deadline is final.
- Judge z-ai/glm-5.3-flash, pairwise, NO news feed, day not told. Criteria in
  order: (1) one day + names the day, (2) selection/breadth, (3) it reads,
  (4) faithful, (5) craft/300px. Margin 1–5, score 0.5 + margin/10 per call.
- Fresh kit: ~/workspace/makefun/news-image-20261124-kit-dl/news-image-20261124-kit/
  bundleSha 4b5efc94df5f7f13825c507da56ccbb2c28bfefaa6d9e78930db672cc4b17c10 —
  VERIFIED matches site bundleSha256 from the live API. Tarball sha256
  5dface0ac33cafe5a1661482fbc4c1ef032417c933c0a1e45ebd291b32265029.
  Kit is BUNDLE-based (requirements say bundle or loose transcripts; NO
  strict_transcripts flag anywhere — record-first does NOT apply; 20261121 proved
  record is refused HTTP 400 for this family). Build in a fresh session started
  AFTER opening; parent bundles the builder session + muse-usage, then submits.
- Account @seannbeez. Quota pre-opening (23:51 UTC): can_submit FALSE,
  day 0 taken / 6 left, hard 40 left — almost certainly because acceptingSubmissions
  was False before opening (resets_at 2026-11-24T00:00:00Z). RE-CHECK LIVE after
  opening before submitting.
- Escrowed on Solana (escrowLifecycle at_open; payout via escrow claim).

## Leaderboard study (yesterday's dev board, news-image-20261122)
- #1 jolly-stork-27 99.2370%, Top-10 line 99.0935%, Top-50 line 98.9301%.
- Our v1s: 20261121 dev 98.5464% (#187), 20261122 dev 98.3404% (~#689).
- 20261121 FINAL lesson: final re-judges afresh vs real entries; dev rank is NOT a
  rank signal (dev #1 akun-fft 99.2905% finished below #200; winner superskie
  86.1050% was never a dev leader). Dense 35–39 story broadsheets dominate dev top,
  but our 21-story Hard Gate formula beat dense variants in local duels on
  readability/faithfulness. DECISION (standing): dual-candidate — A = Hard Gate
  broadsheet (21 stories), B = dense 35-story rival formula. Local harsh-judge sim
  decides; submit only the winner.

## Gemini v1 blueprint (flash-lite, 23:56 UTC — FACT-AUDITED, see flags)
- Heroes: (1) Iran–US escalation, (2) Indonesia factory fire, (3) Jensen Huang
  returns as Nvidia CEO (+~$1tn).
- 6 giant numbers (Gemini's draft): 24 / $1TN / 2 / 21 / 15 / 6.
- Focal point: Iran–US cluster, warm-vs-cool (crimson alerts vs deep slate).
  Light background, dark ink #1A1A1A, date largest, 300px: hero headline +
  giant number + DATE CHECK box must read.
- ⚠️ FACT AUDIT FLAGS (Gemini premises to verify, do NOT trust blindly):
  1. "2 US carriers deployed" — reporting says Trump is CONSIDERING sending a
     SECOND carrier, not deployed. If unverified, the number must read "2nd carrier
     weighed" / "1 carrier + 2nd weighed", never "2 deployed".
  2. "chemical facility blaze" — sources say CANDY factory (Times of India).
     Never call it chemical.
  3. "15 Gukesh–Sindarov moves/climax" — unverified, likely invented. Drop unless
     a real verified number exists (e.g. game 1 result / move count from a live source).
  4. "21 total stories" as a giant number is weak — giant numbers must be NEWS
     numbers (deaths, $, %, counts), not the story count.
  5. Re-verify every Gemini number against live sources before drawing it.

## NEWS LEADS — Tuesday 24 November 2026 (early day, Asia morning; VERIFY 2+ sources each, UTC date-check, drop single-source)
### Iran–US escalation (likely HERO 1) — verify
- Trump warns Iran of "very traumatic" outcome if nuclear deal fails; considering
  sending a second aircraft carrier to the Middle East; recalled US strikes on
  Tehran nuclear facilities (July 2025 12-day war). Sources: Access24, Fox.
- Iran vows to end US naval blockade "by all available means"; Trump acknowledges
  Iranian attacks increasing but says "done no damage" / all knocked down.
  Sources: CBS, Fox, Epoch Times, ZaQs aggregator.
- US escalates sanctions on Iran, targets "shadow banking" networks (Treasury).
  Sources: Al Jazeera, Straits Times, Epoch Times.
- Qatar PM: needs US and Iran to resume talks to end war; met Rubio Monday.
  Source: Middle East Eye.

### Indonesia factory fire (likely HERO 2) — verify
- Candy factory fire kills at least 24, rescuers search for missing workers.
  Source: Times of India school-assembly roundup (needs a second source: AP/Reuters/
  Jakarta Post). Note: 20261122 v1 already covered an Indonesia factory fire with
  "36 missing" — the toll has moved; use the CURRENT verified toll only.

### Russian cargo ship Sparta II — verify (DATE TRAP)
- Sparta II caught fire in the Gulf of Finland after a drone attack (reported
  24 Nov roundups). BUT 20261123 research says Sparta II was FIRST struck Saturday
  21 Nov and towed out of Finnish waters Sunday. If the fire/damage is only the
  21 Nov strike, it is NOT 24 Nov news — DATE CHECK only, or a mini only if a NEW
  24 Nov development (e.g. new fire report) is verified.

### Ukraine — Kyiv region / Dymer — verify
- Russian drone and missile attacks kill people in Ukraine's Kyiv region, hit a
  residential building in Dymer. Source: Times of India roundup (needs 2nd source).

### India — verify
- Modi inaugurates AI centre at IIT Patna, launches Rs 400 crore research park.
- India–China military-level talks in Arunachal Pradesh to reduce border tensions.

### Sport / culture — verify dates carefully (many are 22 Nov results)
- World Chess Championship 2026 begins 24 Nov in Geneva: Gukesh defends vs
  Sindarov (first game 24 Nov). Source: Times of India.
- FIFA Congress selects hosts for 2031, 2035 Women's World Cups.
- ⚠️ Alcaraz ATP Finals title was SUNDAY 22 Nov — DATE CHECK only, never a
  Tuesday story. Same for India–NZ Test draw (Wellington, ended ~23 Nov? verify).

### Markets / tech — verify
- Jensen Huang returns as Nvidia CEO after pressure campaign backed by Trump;
  Nvidia value climbs by almost $1tn, tech stocks rally. Sources: Newsmriti
  roundup, Davka (needs 2nd source: Reuters/Bloomberg/FT).

### Europe / law — verify
- Denmark top court backs hardline immigration "ghetto law".
- Spain's Supreme Court drops all charges against Catalan leader Puigdemont.
- Tajikistan announces ICC withdrawal on day of Putin visit.
- Estonia plans to close all land border crossings with Russia; Russia summons
  Estonian diplomat over arson accusations and border closure.
- EU adds neo-Nazi group 'The Base' founder to terrorist list.

### Middle East / science — verify
- Oxfam + CEOBS report (released 24 Nov?): Israel's Gaza assault left air/soil/
  water contaminated (heavy metals, asbestos, dioxins) for decades.
- Taliban order women's names removed from official documents in Balkh province,
  replaced with "Bibi".
- Supermoon meets the Pleiades ('Seven Sisters') in the night sky.
- Iran flogs female singer + 4 concert team members over performance without hijab
  (Guardian/CNA — verify date: reported 24 Nov roundups).

## DATE CHECK — NOT 24 Nov (list in the box, never as Tuesday news)
- Russian corvette Merkury sunk/burning at Benghazi — first reported 22 Nov
  (was 20261123's hero). Sparta II first struck Sat 21 Nov. COP31 collapse —
  22–23 Nov (Antalya). Alcaraz ATP Finals title — Sun 22 Nov. EU–Indonesia
  trade deal / markets Fri close — 21 Nov.

## VERIFICATION — builder session, 24 Nov 2026 ~07:05–07:20 WIB (UTC 00:05–00:20)
Built at the opening hour, so the entry sums the Monday→Tuesday news cycle
as known at 00:00 UTC Tuesday. "TODAY" pills mark Tuesday-first-reported
items only (Chess Game 1, Odesa outage, supermoon, Korea cabinet); Monday
items are dated "Monday" in their fact lines. All UTC times below are UTC.

### FACT-AUDIT RESOLUTIONS (Gemini blueprint flags)
1. "2 carriers deployed" — RESOLVED, usable with attribution: Fox News
   reports 2 US carrier strike groups presently operating in the Arabian Sea
   (22 Nov report); AP (19 Nov) names them Bush + Roosevelt. The Axios
   "considering a 2nd carrier" line is the OLDER story — not used. Giant
   number reads "2 — US carrier strike groups in the Arabian Sea (Fox)".
2. "chemical facility" — WRONG, corrected: CANDY factory, PT Fonusa Agung
   Mulia, Cikande, Banten; Milkita brand. Never "chemical".
3. "15 chess moves" — DROPPED (unverified/invented). Replaced with verified
   chess facts: Game 1 Tue 24 Nov 14:00 UTC, Geneva; Sindarov White;
   14 games; $2.5m prize; both players 20; youngest-ever match.
   (Chess.com, FIDE via Day.uz, ChessBase India.)
4. "21 stories" as a giant number — DROPPED. All 6 giants are news numbers
   (see below).
5. Nvidia "$1tn" — CORRECTED to ~$950bn: Motley Fool "added about $950bn",
   shares +31% Monday to $165.05, cap ~$3.98tn; Notebookcheck ~$960bn
   premarket. Giant number: "$950BN — Nvidia value added in a day".
   Board voted Sun 22 Nov, announced Mon 23 Nov; investigations continue.

### VERIFIED STORY LIST (21 stories: 3 heroes + 12 minis + 6 briefs)
HEROES
- H1 IRAN–US: Trump warns Iranian ships testing the blockade will end "at
  the bottom of the sea"; weighs new strikes by New Year if talks fail;
  2 carrier groups in the Arabian Sea (Fox). Sources: Fox News, Reuters.
  Badge CONFIRMED (Trump quote on record).
- H2 NVIDIA: board reinstates Huang Mon 23 Nov; +31%; ~$950bn added in a
  day; value back to ~$4tn. Sources: Motley Fool, Notebookcheck, Fortune.
  Badge CONFIRMED.
- H3 INDONESIA FACTORY FIRE: 24 dead CONFIRMED Mon 23 Nov (presidential
  adviser Said Iqbal), ~30 still missing; candy factory, Cikande; fire
  Sat 21 Nov ~5pm local; possible AC short circuit, under investigation.
  Sources: Reuters/AP/BusinessWorld/People. Badge CONFIRMED.
  NOTE: fire itself is Saturday — the Monday news is the toll confirmation.

MINIS (12)
- M1 UKRAINE: 153 drones overnight Sun→Mon, 134 downed (Ukr Air Force);
  Dymer block toll rising; Vyshneve supermarket strike kills 3, 15 hurt.
  CONFIRMED (Reuters/Ukrainian Air Force).
- M2 GAZA: Oxfam + CEOBS report released Mon 23 Nov: contamination
  indicators across 99% of Gaza; 61m tonnes of debris; 78% of land
  directly affected. CONFIRMED (ReliefWeb/Oxfam).
- M3 FIFA: Mon 23 Nov Congress — 2031 to US/Mexico/Costa Rica/Jamaica,
  2035 to England/Scotland/Wales/N. Ireland; first 48-team editions.
  CONFIRMED (FIFA, Reuters).
- M4 SPAIN: Supreme Court shelves Puigdemont case Mon; exile can end
  after 9 years (since 2017); election Sun 29 Nov. CONFIRMED (Reuters/CNN).
- M5 DENMARK: top court backs 'ghetto law' evictions Mon; 91 leases
  ended in Nøjsomhed, Helsingør. CONFIRMED (Reuters).
- M6 ESTONIA: Russia summons envoy Mon, warns of "open war"; Estonia
  shuts all 5 land crossings from 1 Dec for 6 months after alleged
  arson on defence firm Threod Systems. CONFIRMED (Reuters).
- M7 SPARTA II: drone-hit cargo ship reaches St Petersburg under tow Mon
  23 Nov; 16 crew safe, no injuries. CONFIRMED (Reuters). Monday's news
  is the ARRIVAL, not the Sat 21 Nov strike.
- M8 CHESS: Game 1 TODAY Tue 24 Nov, 14:00 UTC, Geneva; Sindarov White
  vs champion Gukesh; 14 games, $2.5m, both 20. CONFIRMED. TODAY pill.
- M9 IRAN SINGER: Parastoo Ahmadi flogged Mon — 74 lashes each, 5 people
  — over Dec 2024 concert without hijab; 2-year travel + work bans.
  CONFIRMED (lawyers via Guardian/CNA roundup). Mon.
- M10 INDIA–CHINA: 2nd round corps commander talks in Arunachal Mon;
  measures to cut friction before winter. REPORTED (The Hindu).
- M11 NEPAL: PM Balen Shah in Delhi Mon; $2bn package REPORTED;
  Saryu-Kamala Express flagged off. REPORTED.
- M12 ODESA: Russian strikes leave Odesa without power, heat or water
  (Tue 00:54 UTC wire roundup). REPORTED. TODAY pill.

BRIEFS (6)
- B1 SPORT: Verstappen wins Las Vegas Grand Prix — Sunday.
- B2 SCIENCE: Beaver supermoon peaks Tue 14:53 UTC, slides past the
  Pleiades (0.9° before dawn); first of 3 supermoons. CONFIRMED
  (NASA/Farmers' Almanac via Starlust). TODAY pill.
- B3 ASIA: Modi opened IIT Patna AI centre Sat 21 Nov; ₹400cr research
  park. CONFIRMED, dated Saturday.
- B4 OCEANIA: M6.5 quake, Vanuatu region, Mon 02:40 UTC, ~600km deep;
  no tsunami, no damage. CONFIRMED (USGS/Xinhua/Anadolu).
- B5 ASIA: South Korea names new foreign minister + first woman spy
  chief (Tue wire roundup). REPORTED. TODAY pill.
- B6 EUROPE: Thousands march in Lisbon against rising living costs.
  REPORTED (24 Nov roundup).

### 6 GIANT NUMBERS (all news numbers)
24 (Indonesia dead confirmed) · $950BN (Nvidia added in a day) ·
2 (US carrier groups, Arabian Sea) · 153 (Russian drones overnight) ·
99% (of Gaza shows contamination) · 48 (teams, first 48-team WWC)

### UTC TIMELINE (verified clock times only)
- Mon 02:40 — M6.5 quake, Vanuatu region (USGS)
- Mon 06:10 — singer flogging first reported (lawyers)
- Mon 14:04 — Nvidia premarket +31% (9:04 EST)
- Mon 15:19 — FIFA names 2031 + 2035 hosts (Reuters)
- Tue 14:00 — Chess Game 1 begins, Geneva (FIDE)

### DATE CHECK (box content)
- Factory fire — Sat 21 Nov; Monday's news is the 24-dead confirmation.
- Alcaraz ATP Finals title — Sun 22 Nov. Merkury sunk — Sun 22 Nov.
- COP31 ends with no deal — Sun night, Antalya. Sparta II struck — Sat
  21 Nov; Monday's news is the tow into St Petersburg.
- IIT Patna AI centre — Sat 21 Nov. Vanuatu quake — Mon 02:40 UTC.
- Kyiv drone-debris fire — Mon 22:29 UTC (00:29 Tue Kyiv time).

### DROPPED (unverified or single-source)
- Tajikistan ICC withdrawal + EU 'The Base' list — leads unverified in
  this session, not used. India–NZ Test draw date unclear — not used.
  Trump "tired Putin ready for deal" — single-source, not used.
  Nepal $2bn package kept only as REPORTED (attributed, not confirmed).
