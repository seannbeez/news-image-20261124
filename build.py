#!/usr/bin/env python3
"""news-image-20261124 — render Candidate A (Hard Gate broadsheet, 21 stories)
and Candidate B (dense 35-story rival) as 1024x1024 PNGs with Pillow.

Deterministic: no network, no clock, no randomness. Every drawn text line is
tracked as a box; overflow, truncation and overlap are reported and fail the
build (exit 1). News facts verified by the builder on 24 Nov 2026, 07:05-07:20
WIB; see RESEARCH.md. TODAY pills mark Tuesday-first-reported items only.
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 244, 233)
INK = (26, 26, 26)
RED = (163, 22, 33)
WHITE = (255, 255, 255)
GREY = (110, 105, 92)
CARD = (255, 255, 255)
EDGE = (200, 192, 172)
MAP_BG = (238, 233, 220)
MAP_FILL = (201, 194, 178)

BADGE_FILL = {"CONFIRMED": (30, 107, 58), "CLAIM": (180, 83, 9),
              "REPORTED": (47, 75, 124)}
REGION_FILL = {
    "GULF": (133, 77, 14), "TECH": (109, 40, 217), "DISASTER": (194, 65, 12),
    "WAR": (163, 22, 33), "MIDDLE EAST": (133, 77, 14), "SPORT": (51, 65, 85),
    "EUROPE": (31, 78, 121), "POLITICS": (31, 56, 100), "ASIA": (146, 64, 14),
    "SCIENCE": (55, 48, 163), "OCEANIA": (15, 118, 110),
    "ECONOMY": (15, 118, 110), "AFRICA": (120, 53, 15), "SPACE": (55, 48, 163),
}

FONT_DIRS = ["/usr/share/fonts/truetype/liberation",
             "/usr/share/fonts/truetype/dejavu"]


def load_font(bold, size):
    names = (["LiberationSans-Bold.ttf", "DejaVuSans-Bold.ttf"] if bold else
             ["LiberationSans-Regular.ttf", "DejaVuSans.ttf"])
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def wrap_text(draw, text, fnt, max_w):
    out, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


class Audit:
    """Tracks every text box; records overflow / truncation / overlap."""

    def __init__(self):
        self.boxes = []   # (label, x0, y0, x1, y1)
        self.problems = []

    def put(self, draw, xy, lines, fnt, fill, cap=None, label="text"):
        x, y = xy
        step = int(fnt.size * 1.22)
        for ln in lines:
            w = draw.textlength(ln, font=fnt)
            self.boxes.append((label, x, y, x + w, y + fnt.size))
            if cap is not None and w > cap + 0.5:
                self.problems.append(
                    f"OVERFLOW {label}: '{ln}' {w:.0f}px > {cap}px")
            draw.text((x, y), ln, font=fnt, fill=fill)
            y += step
        return y

    def check_overlaps(self):
        n = 0
        for i in range(len(self.boxes)):
            for j in range(i + 1, len(self.boxes)):
                a, b = self.boxes[i], self.boxes[j]
                if a[0].startswith("deco") or b[0].startswith("deco"):
                    continue
                if a[1] < b[3] and b[1] < a[3] and a[2] < b[4] and b[2] < a[4]:
                    n += 1
                    self.problems.append(f"OVERLAP {a[0]} vs {b[0]}")
        return n


# ---------------------------------------------------------------- data
HEROES = [
    {"tag": "IRAN–US · GULF", "badge": "CONFIRMED", "region": "GULF",
     "src": "Fox News · Reuters",
     "head": "Trump threatens to sink ships that test the Iran blockade",
     "fact": "Weighs new strikes by New Year if talks fail; 2 US carrier "
             "groups in the Arabian Sea.",
     "icon": "carrier"},
    {"tag": "TECH · MARKETS", "badge": "CONFIRMED", "region": "TECH",
     "src": "Motley Fool · Fortune",
     "head": "Huang is back — Nvidia adds ~$950bn in a day",
     "fact": "Board reinstates him as CEO Monday; shares +31%, value back "
             "near $4tn.",
     "icon": "chip"},
    {"tag": "DISASTER · INDONESIA", "badge": "CONFIRMED", "region": "DISASTER",
     "src": "Reuters · AP · BusinessWorld",
     "head": "Candy-factory fire: 24 dead confirmed",
     "fact": "Toll confirmed Monday; ~30 still missing in Cikande, Banten. "
             "Fire broke out Saturday.",
     "icon": "flame"},
]

MINIS = [
    {"tag": "WAR", "badge": "CONFIRMED",
     "head": "153 drones fired at Ukraine overnight; 134 downed",
     "fact": "Dymer toll rises; supermarket strike kills 3."},
    {"tag": "MIDDLE EAST", "badge": "CONFIRMED",
     "head": "Gaza 'toxic wasteland': 99% shows contamination",
     "fact": "Oxfam + CEOBS report; 61m tonnes of debris."},
    {"tag": "SPORT", "badge": "CONFIRMED",
     "head": "FIFA names 2031 + 2035 Women's World Cup hosts",
     "fact": "US + 3 co-host 2031; UK stages 2035; 48 teams."},
    {"tag": "EUROPE", "badge": "CONFIRMED",
     "head": "Spain shelves Puigdemont case; exile can end",
     "fact": "9 years after 2017 independence bid; vote Sun."},
    {"tag": "EUROPE", "badge": "CONFIRMED",
     "head": "Denmark top court backs 'ghetto law' evictions",
     "fact": "91 leases ended in Helsingor neighbourhood."},
    {"tag": "EUROPE", "badge": "CONFIRMED",
     "head": "Russia warns Estonia of 'open war' over border",
     "fact": "Envoy summoned Monday; crossings shut 1 Dec."},
    {"tag": "WAR", "badge": "CONFIRMED", "today": True,
     "head": "Sparta II reaches St Petersburg under tow",
     "fact": "Drone-hit cargo ship; 16 crew safe, no injuries."},
    {"tag": "SPORT", "badge": "CONFIRMED", "today": True,
     "head": "Chess title match begins today in Geneva",
     "fact": "Game 1, 14:00 UTC; Sindarov White vs Gukesh."},
    {"tag": "MIDDLE EAST", "badge": "CONFIRMED",
     "head": "Iran flogs singer, 4 team members: 74 lashes",
     "fact": "Parastoo Ahmadi sang without hijab in 2024."},
    {"tag": "ASIA", "badge": "REPORTED",
     "head": "India-China hold 2nd round of border talks",
     "fact": "Corps commanders meet in Arunachal Pradesh."},
    {"tag": "ASIA", "badge": "REPORTED",
     "head": "Nepal PM in Delhi; $2bn package reported",
     "fact": "Balen Shah meets Modi; rail link flagged off."},
    {"tag": "WAR", "badge": "REPORTED", "today": True,
     "head": "Odesa left without power, heat or water",
     "fact": "Russian strikes hit the port city overnight."},
]

BRIEFS = [
    "Verstappen wins the Las Vegas Grand Prix — Sunday",
    "Beaver supermoon peaks today, 14:53 UTC, past the Pleiades",
    "Modi opened IIT Patna AI centre Saturday; Rs 400cr park",
    "M6.5 quake, Vanuatu region, Mon 02:40 UTC; no tsunami",
    "Seoul names new foreign minister, first woman spy chief",
    "Thousands march in Lisbon against living costs",
]
BRIEF_TODAY = {1, 4}  # supermoon, Seoul cabinet (Tuesday-first)

NUMBERS = [
    ("24", "dead confirmed in\nIndonesia factory fire"),
    ("$950BN", "Nvidia value added\nin a day"),
    ("2", "US carrier groups\nin the Arabian Sea"),
    ("153", "Russian drones fired\nat Ukraine overnight"),
    ("99%", "of Gaza shows\ncontamination signs"),
    ("48", "teams at the first\n48-team Women's Cup"),
]

# Simplified continent outlines (lon, lat) — schematic, flat-vector style.
LAND = {
    "NA": [(-168, 66), (-140, 70), (-120, 72), (-100, 73), (-85, 70),
           (-70, 60), (-55, 47), (-65, 44), (-75, 35), (-85, 28),
           (-97, 16), (-105, 20), (-115, 28), (-125, 40), (-145, 60),
           (-160, 58)],
    "SA": [(-80, 10), (-72, 4), (-58, -2), (-45, -8), (-40, -20),
           (-48, -28), (-58, -35), (-66, -48), (-72, -52), (-75, -35),
           (-75, -18), (-80, -5)],
    "AF": [(-17, 15), (-10, 30), (0, 35), (10, 37), (22, 33), (32, 31),
           (38, 22), (43, 12), (51, 11), (48, 0), (40, -12), (35, -22),
           (28, -32), (18, -34), (13, -25), (12, -15), (9, -1), (-8, 5)],
    "EU": [(-10, 36), (-9, 43), (-2, 48), (2, 51), (8, 57), (12, 59),
           (20, 56), (28, 60), (32, 70), (42, 68), (44, 58), (38, 50),
           (30, 46), (26, 40), (22, 36), (16, 40), (8, 44), (0, 40)],
    "AS": [(42, 68), (60, 70), (80, 73), (105, 76), (130, 72), (155, 68),
           (175, 65), (165, 60), (155, 50), (142, 42), (130, 34),
           (122, 30), (114, 22), (106, 10), (100, 8), (94, 16), (88, 22),
           (80, 12), (74, 8), (68, 22), (58, 25), (50, 30), (44, 38)],
    "OC": [(113, -22), (118, -32), (128, -32), (138, -35), (146, -39),
           (150, -37), (153, -28), (148, -20), (142, -11), (134, -12),
           (126, -14), (118, -20)],
}
MAP_DOTS = [("Washington", -77.0, 38.9), ("Tehran", 51.4, 35.7),
            ("Cikande", 106.3, -6.3), ("Kyiv", 30.5, 50.4),
            ("Odesa", 30.7, 46.5), ("Geneva", 6.1, 46.2),
            ("Gaza", 34.5, 31.5), ("Tallinn", 24.7, 59.4),
            ("Madrid", -3.7, 40.4), ("Copenhagen", 12.6, 55.7),
            ("Delhi", 77.2, 28.6), ("St Petersburg", 30.3, 59.9)]

# B extras: Monday-dated stories verified in the 20261123 research round.
B_EXTRA = [
    {"tag": "EUROPE", "badge": "REPORTED",
     "head": "EU proposes fresh Russia sanctions"},
    {"tag": "EUROPE", "badge": "REPORTED",
     "head": "Denmark to ban mobile phones in schools"},
    {"tag": "ASIA", "badge": "REPORTED",
     "head": "Myanmar junta criticises ASEAN decision"},
    {"tag": "POLITICS", "badge": "CONFIRMED",
     "head": "Democrats win 258th House seat in N. Carolina"},
    {"tag": "ECONOMY", "badge": "CONFIRMED",
     "head": "Taiwan shares -17.5% in a week; short sales banned"},
    {"tag": "TECH", "badge": "CONFIRMED",
     "head": "UN pushes killer-robot rules to 2028"},
    {"tag": "GULF", "badge": "CLAIM",
     "head": "Houthis claim strikes on Saudi refinery"},
    {"tag": "WAR", "badge": "REPORTED",
     "head": "Settlers torch 12 vehicles near Ramallah"},
    {"tag": "POLITICS", "badge": "CONFIRMED",
     "head": "Netanyahu-Eisenkot talks end with no deal"},
    {"tag": "SPACE", "badge": "CONFIRMED",
     "head": "BepiColombo enters orbit around Mercury"},
    {"tag": "ASIA", "badge": "REPORTED",
     "head": "Shuri Castle's restored hall opens in Okinawa"},
    {"tag": "ASIA", "badge": "REPORTED",
     "head": "Lahore world's most polluted city, AQI 538"},
    {"tag": "POLITICS", "badge": "CONFIRMED",
     "head": "Bolsonaro 'stable' in intensive care"},
    {"tag": "POLITICS", "badge": "CONFIRMED",
     "head": "Kim: N. Korea seeks security, not supremacy"},
]


# ---------------------------------------------------------------- drawing
def badge(draw, x, y, label):
    fnt = load_font(True, 11)
    w = int(draw.textlength(label, font=fnt)) + 12
    draw.rounded_rectangle([x, y, x + w, y + 17], radius=3,
                           fill=BADGE_FILL[label])
    draw.text((x + 6, y + 2), label, font=fnt, fill=WHITE)
    return w


def today_pill(draw, x, y):
    fnt = load_font(True, 10)
    lab = "TODAY"
    w = int(draw.textlength(lab, font=fnt)) + 10
    draw.rounded_rectangle([x, y, x + w, y + 15], radius=3, fill=RED)
    draw.text((x + 5, y + 2), lab, font=fnt, fill=WHITE)
    return w


def hero_icon(draw, kind, cx, cy, s):
    if kind == "carrier":
        draw.polygon([(cx - s, cy + s // 3), (cx + s, cy + s // 3),
                      (cx + s - 8, cy + s), (cx - s + 8, cy + s)], fill=INK)
        draw.line([cx, cy + s // 3, cx, cy - s], fill=INK, width=3)
        draw.rectangle([cx - 4, cy - s, cx + 10, cy - s // 3], fill=INK)
        draw.polygon([(cx + 2, cy - s), (cx + 2, cy - s // 3),
                      (cx + s // 2, cy - s // 3)], fill=RED)
        draw.line([cx - s - 6, cy + s + 8, cx + s + 6, cy + s + 8],
                  fill=(31, 78, 121), width=3)
    elif kind == "chip":
        draw.rounded_rectangle([cx - s, cy - s, cx + s, cy + s], radius=5,
                               outline=INK, width=3)
        draw.rectangle([cx - s // 2, cy - s // 2, cx + s // 2, cy + s // 2],
                       outline=RED, width=3)
        for k in range(-1, 2):
            draw.line([cx + k * s // 2, cy - s - 6, cx + k * s // 2, cy - s],
                      fill=INK, width=3)
            draw.line([cx + k * s // 2, cy + s, cx + k * s // 2, cy + s + 6],
                      fill=INK, width=3)
            draw.line([cx - s - 6, cy + k * s // 2, cx - s, cy + k * s // 2],
                      fill=INK, width=3)
            draw.line([cx + s, cy + k * s // 2, cx + s + 6, cy + k * s // 2],
                      fill=INK, width=3)
        fnt = load_font(True, 20)
        draw.text((cx - 6, cy - 12), "$", font=fnt, fill=RED)
    elif kind == "flame":
        draw.polygon([(cx, cy - s), (cx + s // 2, cy - s // 4),
                      (cx + s // 3, cy + s // 2), (cx - s // 3, cy + s // 2),
                      (cx - s // 2, cy - s // 4)], fill=(194, 65, 12))
        draw.polygon([(cx, cy - s // 4), (cx + s // 4, cy + s // 6),
                      (cx, cy + s // 2), (cx - s // 4, cy + s // 6)],
                     fill=RED)
        draw.line([cx - s, cy + s + 6, cx + s, cy + s + 6], fill=INK, width=3)


def masthead(draw, tr):
    draw.rectangle([0, 0, W, 8], fill=RED)
    f_kick = load_font(True, 17)
    kick = "T H E   W O R L D   I N   O N E   D A Y"
    w = draw.textlength(kick, font=f_kick)
    tr.put(draw, ((W - w) / 2, 18), [kick], f_kick, INK, label="masthead")
    f_date = load_font(True, 62)
    date = "TUESDAY 24 NOVEMBER 2026"
    w = draw.textlength(date, font=f_date)
    tr.put(draw, ((W - w) / 2, 46), [date], f_date, INK, label="date")
    f_sub = load_font(False, 16)
    sub = "21 stories from 7 regions  —  as reported on Tuesday 24 November 2026"
    w = draw.textlength(sub, font=f_sub)
    tr.put(draw, ((W - w) / 2, 122), [sub], f_sub, GREY, label="subline")
    draw.line([24, 146, W - 24, 146], fill=INK, width=2)
    draw.line([24, 150, W - 24, 150], fill=INK, width=1)


def numbers_strip(draw, tr, y0=158, h=68):
    draw.rectangle([24, y0, W - 24, y0 + h], fill=RED)
    cw = (W - 48) / 6
    f_lab = load_font(False, 11)
    for i, (num, lab) in enumerate(NUMBERS):
        x0 = 24 + i * cw
        if i:
            draw.line([x0, y0 + 8, x0, y0 + h - 8], fill=WHITE, width=1)
        size = 40
        while size > 24:
            f_n = load_font(True, size)
            if draw.textlength(num, font=f_n) <= cw - 10:
                break
            size -= 2
        w = draw.textlength(num, font=f_n)
        tr.put(draw, (x0 + (cw - w) / 2, y0 + 4), [num], f_n, WHITE,
               cap=cw - 8, label=f"num{i}")
        for j, ln in enumerate(lab.split("\n")):
            w2 = draw.textlength(ln, font=f_lab)
            tr.put(draw, (x0 + (cw - w2) / 2, y0 + 46 + j * 13), [ln],
                   f_lab, WHITE, label=f"numlab{i}")
    return y0 + h


def hero_row(draw, tr, y0=236, h=196):
    cw, gap = 322, 7
    f_tag = load_font(True, 12)
    f_head = load_font(True, 20)
    f_fact = load_font(False, 13.5)
    f_src = load_font(False, 11)
    for i, st in enumerate(HEROES):
        x0 = 24 + i * (cw + gap)
        draw.rectangle([x0, y0, x0 + cw, y0 + h], fill=CARD, outline=INK,
                       width=2)
        draw.rectangle([x0, y0, x0 + cw, y0 + 22], fill=REGION_FILL[st["region"]])
        tr.put(draw, (x0 + 8, y0 + 4), [st["tag"]], f_tag, WHITE,
               label=f"herotag{i}")
        hero_icon(draw, st["icon"], x0 + 40, y0 + 58, 21)
        tr.boxes.append((f"icon{i}", x0 + 16, y0 + 34, x0 + 64, y0 + 82))
        hl = wrap_text(draw, st["head"], f_head, cw - 88)
        y = tr.put(draw, (x0 + 76, y0 + 32), hl, f_head, INK, cap=cw - 88,
                   label=f"herohead{i}")
        if len(hl) > 3:
            tr.problems.append(f"TRUNC herohead{i}: '{st['head']}'")
        fl = wrap_text(draw, st["fact"], f_fact, cw - 16)
        y = max(y + 6, y0 + 100)
        y = tr.put(draw, (x0 + 8, y), fl, f_fact, INK, cap=cw - 16,
                   label=f"herofact{i}")
        if len(fl) > 3:
            tr.problems.append(f"TRUNC herofact{i}: '{st['fact']}'")
        bw = badge(draw, x0 + 8, y0 + h - 26, st["badge"])
        tr.put(draw, (x0 + 8 + bw + 8, y0 + h - 24), [st["src"]], f_src, GREY,
               label=f"herosrc{i}")
    return y0 + h


def mini_grid(draw, tr, y0=440, ch=72):
    cw, gap = 322, 7
    f_tag = load_font(True, 11)
    f_head = load_font(True, 15)
    f_fact = load_font(False, 12)
    for idx, st in enumerate(MINIS):
        r, c = divmod(idx, 3)
        x0 = 24 + c * (cw + gap)
        yy = y0 + r * (ch + 5)
        draw.rectangle([x0, yy, x0 + cw, yy + ch], fill=CARD, outline=EDGE,
                       width=1)
        draw.rectangle([x0, yy, x0 + 5, yy + ch], fill=REGION_FILL[st["tag"]])
        tw = draw.textlength(st["tag"], font=f_tag)
        tr.put(draw, (x0 + 12, yy + 4), [st["tag"]], f_tag,
               REGION_FILL[st["tag"]], label=f"minitag{idx}")
        bx = x0 + 12 + int(tw) + 6
        if st.get("today"):
            today_pill(draw, bx, yy + 4)
            bx += 46
        badge(draw, x0 + cw - 78, yy + 4, st["badge"])
        hl = wrap_text(draw, st["head"], f_head, cw - 22)
        tr.put(draw, (x0 + 12, yy + 19), hl[:2], f_head, INK, cap=cw - 22,
               label=f"minihead{idx}")
        if len(hl) > 2:
            tr.problems.append(f"TRUNC minihead{idx}: '{st['head']}'")
        fl = wrap_text(draw, st["fact"], f_fact, cw - 22)
        if len(fl) > 1:
            tr.problems.append(f"TRUNC minifact{idx}: '{st['fact']}'")
        tr.put(draw, (x0 + 12, yy + 56), fl[:1], f_fact, GREY, cap=cw - 22,
               label=f"minifact{idx}")
    return y0 + 4 * (ch + 5)


def briefs_block(draw, tr, y0=744):
    f_b = load_font(False, 11.5)
    f_dot = load_font(True, 11.5)
    for idx, ln in enumerate(BRIEFS):
        r, c = divmod(idx, 2)
        x0 = 24 + c * 490
        yy = y0 + r * 16
        draw.text((x0, yy), "•", font=f_dot, fill=RED)
        tr.put(draw, (x0 + 12, yy), [ln], f_b, INK, cap=468,
               label=f"brief{idx}")
        if idx in BRIEF_TODAY:
            today_pill(draw, x0 + 12 + int(draw.textlength(ln, font=f_b)) + 6,
                       yy)
    return y0 + 3 * 16


def timeline_block(draw, tr, y0=798):
    f_h = load_font(True, 12)
    f_t = load_font(False, 12)
    tr.put(draw, (24, y0), ["THE DAY IN UTC — MON 23 NOV → TUE 24 NOV"],
           f_h, INK, label="tl-h")
    lines = [
        "MON 02:40  M6.5 quake, Vanuatu   ·   06:10  Singer flogging reported"
        "   ·   14:04  Nvidia +31%",
        "MON 15:19  FIFA names 2031 + 2035 hosts   ·   TUE 14:00  Chess Game 1"
        " begins, Geneva",
    ]
    y = y0 + 18
    for ln in lines:
        y = tr.put(draw, (24, y), [ln], f_t, INK, cap=W - 48, label="tl")
    return y


def map_block(draw, tr, y0=845, h=76):
    f_lab = load_font(True, 12)
    tr.put(draw, (24, y0), ["WHERE IT HAPPENED — 12 PLACES"], f_lab, INK,
           label="maplabel")
    x0, y1, mw, mh = 24, y0 + 18, W - 48, h - 22
    draw.rectangle([x0, y1, x0 + mw, y1 + mh], fill=MAP_BG, outline=INK,
                   width=1)

    def px(lon, lat):
        return x0 + (lon + 180) / 360 * mw, y1 + (75 - lat) / 130 * mh
    for poly in LAND.values():
        draw.polygon([px(lo, la) for lo, la in poly], fill=MAP_FILL)
    for name, lon, lat in MAP_DOTS:
        x, y = px(lon, lat)
        draw.ellipse([x - 5, y - 5, x + 5, y + 5], fill=RED, outline=WHITE,
                     width=1)
    return y0 + h


def footer_block(draw, tr, y0=927):
    f_h = load_font(True, 12)
    f_b = load_font(False, 11.5)
    draw.line([24, y0, W - 24, y0], fill=INK, width=2)
    tr.put(draw, (24, y0 + 8), ["DATE CHECK — what is dated when"], f_h, INK,
           label="dc-h")
    dc = [
        "Factory fire — Sat 21 Nov; Monday's news is the 24-dead confirmation.",
        "Alcaraz title + Merkury sinking — Sun 22 Nov. COP31 no-deal — Sun night.",
        "Sparta II struck Sat 21 Nov; Monday: tow into St Petersburg. IIT Patna — Sat.",
    ]
    y = y0 + 26
    for ln in dc:
        y = tr.put(draw, (24, y), [ln], f_b, INK, cap=560, label="dc")
    tr.put(draw, (600, y0 + 8), ["DISPUTED CLAIMS"], f_h, RED, label="dis-h")
    dis = [
        "Disputed claims are attributed, not fact:",
        "Nepal's $2bn package + India-China talks outcome",
        "as reported; casualty counts may be revised.",
    ]
    y2 = y0 + 26
    for ln in dis:
        y2 = tr.put(draw, (600, y2), [ln], f_b, INK, cap=400, label="dis")
    f_s = load_font(False, 11)
    src = ("Sources: Reuters · AP · Fox News · Motley Fool · FIFA · Oxfam · "
           "USGS · FIDE — 24 Nov 2026")
    w = draw.textlength(src, font=f_s)
    tr.put(draw, ((W - w) / 2, 1002), [src], f_s, GREY, label="sources")


def render_a(path):
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    tr = Audit()
    masthead(draw, tr)
    numbers_strip(draw, tr)
    hero_row(draw, tr)
    mini_grid(draw, tr, y0=438, ch=70)
    briefs_block(draw, tr)
    timeline_block(draw, tr)
    map_block(draw, tr, y0=852, h=74)
    footer_block(draw, tr, y0=932)
    tr.check_overlaps()
    img.save(path, "PNG", optimize=True)
    return tr


def render_b(path):
    """Dense rival: same masthead/numbers/heroes, then 32 headline-only
    cards (4 cols x 8 rows) — 35 stories total, no facts, no timeline, no map."""
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    tr = Audit()
    masthead(draw, tr)
    numbers_strip(draw, tr)
    hero_row(draw, tr)
    small = MINIS + [{"tag": "SPORT", "badge": "REPORTED",
                      "head": "Verstappen wins the Las Vegas Grand Prix"},
                     {"tag": "SCIENCE", "badge": "CONFIRMED",
                      "head": "Beaver supermoon peaks today, past Pleiades"},
                     {"tag": "ASIA", "badge": "CONFIRMED",
                      "head": "Modi opened IIT Patna AI centre Saturday"},
                     {"tag": "OCEANIA", "badge": "CONFIRMED",
                      "head": "M6.5 quake, Vanuatu region; no tsunami"},
                     {"tag": "ASIA", "badge": "REPORTED",
                      "head": "Seoul names new foreign minister"},
                     {"tag": "EUROPE", "badge": "REPORTED",
                      "head": "Thousands march in Lisbon on living costs"}] \
        + B_EXTRA
    assert len(small) == 32, len(small)
    f_tag = load_font(True, 10)
    f_head = load_font(True, 12)
    cols, rows, cw, ch = 4, 8, 238, 56
    for idx, st in enumerate(small):
        r, c = divmod(idx, cols)
        x0 = 24 + c * (cw + 6)
        yy = 444 + r * (ch + 5)
        draw.rectangle([x0, yy, x0 + cw, yy + ch], fill=CARD, outline=EDGE,
                       width=1)
        draw.rectangle([x0, yy, x0 + 4, yy + ch], fill=REGION_FILL[st["tag"]])
        tr.put(draw, (x0 + 9, yy + 4), [st["tag"]], f_tag,
               REGION_FILL[st["tag"]], label=f"btag{idx}")
        hl = wrap_text(draw, st["head"], f_head, cw - 14)
        tr.put(draw, (x0 + 9, yy + 19), hl[:2], f_head, INK, cap=cw - 14,
               label=f"bhead{idx}")
        if len(hl) > 2:
            tr.problems.append(f"TRUNC bhead{idx}: '{st['head']}'")
        dot = BADGE_FILL[st["badge"]]
        draw.ellipse([x0 + cw - 12, yy + 5, x0 + cw - 5, yy + 12], fill=dot)
    f_d = load_font(True, 11)
    tr.put(draw, (24, 948),
           ["DATE CHECK: factory fire Sat · Alcaraz + Merkury Sun · "
            "Sparta II struck Sat · IIT Patna Sat"], f_d, INK, label="dc-b")
    draw.line([24, 972, W - 24, 972], fill=INK, width=2)
    f_s = load_font(False, 11)
    src = ("Sources: Reuters · AP · Fox News · Motley Fool · FIFA · Oxfam · "
           "USGS · FIDE — 24 Nov 2026")
    w = draw.textlength(src, font=f_s)
    tr.put(draw, ((W - w) / 2, 980), [src], f_s, GREY, label="sources")
    tr.check_overlaps()
    img.save(path, "PNG", optimize=True)
    return tr


def main():
    variant = sys.argv[1]
    out = sys.argv[2]
    tr = render_a(out) if variant == "A" else render_b(out)
    size = os.path.getsize(out)
    im = Image.open(out)
    report = {"variant": variant, "path": out, "bytes": size,
              "size_px": im.size, "problems": tr.problems,
              "n_boxes": len(tr.boxes)}
    print(json.dumps(report, indent=1))
    if tr.problems:
        sys.exit(1)


if __name__ == "__main__":
    main()
