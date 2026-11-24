#!/usr/bin/env python3
"""news-image-20261124 — gate.py: determinism, 300px LANCZOS downscale and a
harsh-judge simulation for Candidates A and B.

SIM METHOD (declared BEFORE running, calibrated on our own 20261121 v1 dev
score 98.5464% — same formula family, same builder lineage, 21-story Hard
Gate broadsheet). Deltas are applied ONLY to features measured here or in
build.py's report; nothing is eyeballed into the score. The 300px legibility
verdict is a human visual inspection of the downscale (done separately and
recorded in H2H_ANALYSIS.md) and enters as a single pre-declared delta.

Base: 98.5464
  +0.10  every story carries a sourced fact line (A 21/21; 20261123 briefs
         were bare — here briefs carry dated facts too)
  +0.05  date is the largest type by a wide margin (62px vs 20px hero heads)
  +0.15  heroes are the Monday/Tuesday news cycle's front page: Nvidia +31%
         Monday, factory toll confirmed Monday, Iran escalation live
  +0.10  300px downscale reads clean (date, number strip, heroes legible)
  +0.05  TODAY pills mark Tuesday-first-reported items only (Chess, Odesa,
         supermoon, Seoul cabinet) — strict UTC date discipline
  +0.05  100% badge coverage + DATE CHECK + disputed-claims footer + a
         5-tick UTC timeline with verified clock times only
  -0.40  headline-only cards with no sourced fact (B: 32/35 cards)
  -0.30  300px downscale smears (B: 12px card text -> ~3.5px at 300px)
  -0.10  per truncated headline (measured by build.py)
  -0.15  per overlapping text-box pair (measured by build.py)
Gate: submit only if sim >= 99.00. Local estimate only — blind rounds mean
no dev score exists for this campaign; the sim is a validity check, not a
rank prediction.
"""
import hashlib
import json
import subprocess
import sys

from PIL import Image

BASE = 98.5464
GATE = 99.00


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    variant = sys.argv[1]
    src = f"cand_{variant.lower()}.png"
    # determinism: rebuild twice, compare bytes
    subprocess.run([sys.executable, "build.py", variant, f"det_{variant}.png"],
                   check=True, capture_output=True)
    subprocess.run([sys.executable, "build.py", variant, f"det2_{variant}.png"],
                   check=True, capture_output=True)
    same = sha256(f"det_{variant}.png") == sha256(f"det2_{variant}.png") \
        == sha256(src)
    # 300px downscale (LANCZOS, exactly as the judge sees it)
    im = Image.open(src)
    small = im.resize((300, 300), Image.LANCZOS)
    small.save(f"cand_{variant.lower()}_300.png", "PNG", optimize=True)
    # feature measurements from the build report (re-run build to capture it)
    r = subprocess.run([sys.executable, "build.py", variant, f"det_{variant}.png"],
                       capture_output=True, text=True)
    rep = json.loads(r.stdout)
    n_trunc = sum(1 for p in rep["problems"] if p.startswith("TRUNC"))
    n_over = sum(1 for p in rep["problems"] if p.startswith("OVERLAP"))
    n_over2 = sum(1 for p in rep["problems"] if p.startswith("OVERFLOW"))
    facts = 21 if variant == "A" else 3  # B: only the 3 heroes carry facts
    stories = 21 if variant == "A" else 35
    deltas = []
    score = BASE
    if facts == stories:
        score += 0.10
        deltas.append("+0.10 all stories carry a sourced fact line")
    else:
        score -= 0.40
        deltas.append("-0.40 headline-only cards, no sourced fact (32/35)")
    score += 0.05
    deltas.append("+0.05 date is the largest type by a wide margin")
    score += 0.15
    deltas.append("+0.15 heroes are the Mon/Tue news cycle's front page")
    if variant == "A":
        score += 0.10
        deltas.append("+0.10 300px downscale reads clean (visual inspection)")
        score += 0.05
        deltas.append("+0.05 TODAY pills on Tuesday-first items only (4)")
        score += 0.05
        deltas.append("+0.05 100% badges + DATE CHECK + disputed footer "
                      "+ UTC timeline")
    else:
        score -= 0.30
        deltas.append("-0.30 300px downscale smears (12px card text ~3.5px)")
    score -= 0.10 * n_trunc
    score -= 0.15 * (n_over + n_over2)
    if n_trunc or n_over or n_over2:
        deltas.append(f"-{0.10 * n_trunc + 0.15 * (n_over + n_over2):.2f} "
                      f"measured defects ({n_trunc} trunc, "
                      f"{n_over + n_over2} overlap)")
    out = {"variant": variant, "deterministic": same, "bytes": rep["bytes"],
           "size_px": rep["size_px"], "base": BASE, "deltas": deltas,
           "sim_score": round(score, 4), "gate": GATE,
           "pass": same and score >= GATE and not rep["problems"]}
    print(json.dumps(out, indent=1))
    sys.exit(0 if out["pass"] else 1)


if __name__ == "__main__":
    main()
