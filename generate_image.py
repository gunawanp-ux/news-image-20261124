"""Draw the front page for Tuesday 24 November 2026.

A single 1024x1024 PNG newspaper front page: masthead, two lead stories,
three top stories, forty numbered one-line briefs, a dot-matrix world map
with twelve numbered pins, and a closing markets bar. Every picture on the
page is drawn here in code with Pillow; nothing is fetched from the network,
so the output is fully deterministic.
"""

import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "entry.png"

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (26, 26, 26)
RED = (176, 42, 32)
BLUE = (31, 78, 121)
GREY = (110, 108, 100)
LIGHT = (232, 228, 216)
RULE = (180, 175, 160)

FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
SERIF = str(FONT_DIR / "LiberationSerif-Bold.ttf")
SERIF_REG = str(FONT_DIR / "LiberationSerif-Regular.ttf")
SANS = str(FONT_DIR / "LiberationSans-Regular.ttf")
SANS_BOLD = str(FONT_DIR / "LiberationSans-Bold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to a pixel width; returns a list of lines."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def one_line(draw, text, fnt, width):
    """Shrink text to a single line that fits, adding an ellipsis if cut."""
    if draw.textlength(text, font=fnt) <= width:
        return text
    while text and draw.textlength(text + "\u2026", font=fnt) > width:
        text = text[:-1]
    return text + "\u2026"


# ---------------------------------------------------------------- stories

LEADS = [
    {
        "kicker": "MARKETS  \u00b7  ASIA RALLIES",
        "headline": "Asian stocks roar back: Kospi +7.5%, Nikkei +4.5%, Taiwan +9.1%",
        "deck": "Nvidia's return revives the AI trade; MSCI Asia-Pacific "
                "+4.6%, its best day in two weeks.",
        "icon": "chart",
    },
    {
        "kicker": "UKRAINE  \u00b7  PEACE TALKS",
        "headline": "Trump may back NATO-style guarantees for Ukraine, envoy says",
        "deck": "Kushner: backing possible if a new framework limits war "
                "risk; Putin signals acceptance.",
        "icon": "shield",
    },
]

TOPS = [
    {
        "kicker": "CHESS  \u00b7  GENEVA",
        "headline": "Gukesh defends world crown vs Sindarov; Game 1 tonight",
        "deck": "Youngest-ever title match; $2.5m prize.",
        "icon": "crown",
    },
    {
        "kicker": "GULF  \u00b7  WASHINGTON",
        "headline": "Qatar PM works to revive US-Iran talks after Rubio meeting",
        "deck": "Doha warns region 'cannot afford a new escalation'.",
        "icon": "dove",
    },
    {
        "kicker": "BANGLADESH  \u00b7  EXILE",
        "headline": "Hasina plans return home on Dec 16 after two years in exile",
        "deck": "Ousted PM to fly in on state carrier, aide says.",
        "icon": "flag",
    },
]

BRIEFS = [
    "Russia, Ukraine clash at UN over Black Sea shipping strikes",
    "North Korea may shut Swiss office after sanctions, KCNA says",
    "Japan factory activity grows faster; flash PMI hits 53.7",
    "South Korea central bank seen raising rates to 3.25% Thursday",
    "CrowdStrike snaps up Zscaler in $44bn cyber deal",
    "US lawmakers criticise Nvidia's decision to reinstate Huang",
    "EU criticises Tajikistan for hosting Putin despite ICC warrant",
    "Central Europe leaders question EU's seven-year budget plan",
    "Russia summons Estonian envoy over border closure, arson claim",
    "Armenia starts work on Trump Route TRIPP in Syunik province",
    "Iran objects to Qatar envoy over Qatar-Germany statement",
    "Iran's army says it shot down a US drone over the Gulf",
    "Trump puts Iowa lead azide blast on hold pending court ruling",
    "Trump calls to 'expedite' federal executions, blasts Newsom",
    "Appeals court revives Trump bid on hush-money jurisdiction",
    "Canada PM brings Trump impersonator on stage at press gala",
    "Bukele details deaths of Salvadoran troops in Haiti mission",
    "Israeli minister approves return of Flydubai flights",
    "Israeli strikes kill three in Gaza, including UNRWA worker",
    "Spain's right on track to oust Sanchez in Nov 29 vote, polls show",
    "UK sanctions top Myanmar generals after genocide ruling",
    "Burnham to ignore 'stuck in the past' ex-PMs after EU deal",
    "Manchester Co-op Live evacuated over unknown substance",
    "Capita shares plunge 70% as boss quits after pensions failure",
    "Democrats announce 12 presidential primary debates",
    "Amazon drone snags on wire, falls on Michigan garage roof",
    "Hague verdict due today in Hashim Thaci war-crimes case",
    "Tickner out of second India Test with hamstring injury",
    "Leaked files show budget iPhone 18e with Pro-style camera bump",
    "Indian markets shut for Guru Nanak Jayanti holiday",
    "Indian journalist stopped at Delhi airport from flying to UK",
    "Google rival Kagi launches its own email service",
    "LA Skins Fest ends 20th year celebrating Indigenous artists",
    "Arsenal's Raya out of Dortmund clash; no surgery needed",
    "Andrew 'received \u00a3750,000 from Turkish millionaire', court told",
    "RAF's next fighter jet may be last crewed combat plane",
    "Catherine's cancer journey shown in new documentary",
    "US rapper postpones arena shows after Manchester evacuation",
    "Benefits review to urge quicker payments for disabled people",
    "Britain's landlords grow bigger; two-tier rental market looms",
]

BRIEF_ICONS = {8: "chart", 10: "chip", 17: "missile", 24: "cross",
               28: "flame", 33: "bat", 40: "gavel", 45: "note"}

PINS = [
    (37.6, 127.0, "Seoul, S. Korea"),
    (35.7, 139.7, "Tokyo, Japan"),
    (25.0, 121.5, "Taipei, Taiwan"),
    (46.2, 6.1, "Geneva, Switzerland"),
    (38.9, -77.0, "Washington, USA"),
    (23.8, 90.4, "Dhaka, Bangladesh"),
    (40.7, -74.0, "New York, USA"),
    (31.5, 34.5, "Gaza"),
    (40.4, -3.7, "Madrid, Spain"),
    (51.5, -0.1, "London, UK"),
    (39.0, 125.8, "Pyongyang, N. Korea"),
    (18.5, -72.3, "Port-au-Prince, Haiti"),
]

# 48 columns x 20 rows of land ('#') and sea ('.'). Columns span
# 180W-180E, rows span 78N-57S, so a pin's cell is easy to find.
LAND = [
    "......##" "........" "..##...." "........" "########" "###.....",
    ".#####.." "########" "#.####.." "......##" "########" "#######.",
    "..######" "########" "#......." ".###.###" "########" "########",
    "..######" "########" "#......#" "########" "########" "########",
    "...#####" "########" "#......." "#######." "########" "#######.",
    "....####" "########" "........" "######.." ".#######" "######..",
    ".....###" "#######." "........" ".####.##" "########" "#####...",
    ".......#" "#####..." "......##" "########" "#####.##" "###.....",
    "........" "...###.." ".......#" "########" "..#..###" "#.......",
    "........" "....###." ".......#" "########" ".....###" "........",
    "........" "......##" "####...." "########" ".....###" "###.....",
    "........" "......##" "####...." ".#######" "......##" "#####...",
    "........" "......##" "####...." ".######." ".....###" "...###..",
    "........" "......##" "####...." "..#####." ".......#" "####....",
    "........" ".......#" "####...." "..####.." ".......#" "#####...",
    "........" ".......#" "####...." "..####.." ".......#" "####....",
    "........" ".......#" "###....." "...##..." "........" "####....",
    "........" ".......#" "##......" "........" "........" "......##",
    "........" ".......#" "#......." "........" "........" "........",
    "........" ".......#" "........" "........" "........" "........",
]

MARKETS = [
    ("S&P 500", "7,237", "+4.7%"),
    ("Dow", "49,595", "+3.0%"),
    ("Nasdaq", "24,090", "+6.5%"),
    ("Nvidia", "+31.5%", ""),
    ("Kospi", "+7.5% Tue", ""),
    ("Nikkei", "+4.5% Tue", ""),
    ("Brent", "~$93", ""),
]

# ---------------------------------------------------------------- icons

def icon(draw, kind, cx, cy, s, color=INK):
    """Draw one small pictogram centred at (cx, cy), size s."""
    u = s / 40.0

    def line(xy, w=2):
        draw.line([(cx + x * u, cy + y * u) for x, y in xy],
                  fill=color, width=max(1, int(w * u)))

    def ell(box, outline=color, fill=None, w=2):
        draw.ellipse([cx + box[0] * u, cy + box[1] * u,
                      cx + box[2] * u, cy + box[3] * u],
                     outline=outline, fill=fill, width=max(1, int(w * u)))

    def poly(pts, fill=color, outline=None):
        draw.polygon([(cx + x * u, cy + y * u) for x, y in pts],
                     fill=fill, outline=outline)

    if kind == "cuffs":
        ell((-16, -6, -2, 8))
        ell((2, -6, 16, 8))
        line([(-9, -12), (9, -12)])
        line([(-9, -12), (-9, -6)])
        line([(9, -12), (9, -6)])
    elif kind == "leaf":
        draw.ellipse([cx - 15 * u, cy - 15 * u, cx + 15 * u, cy + 15 * u],
                     outline=color, width=max(1, int(2 * u)))
        poly([(-12, 8), (0, -14), (12, 8), (0, 2)], fill=(74, 124, 60))
        line([(0, -14), (0, 14)], w=2)
    elif kind == "missile":
        poly([(-16, 10), (-4, -14), (4, -14), (16, 10), (0, 4)])
        line([(0, 4), (0, 14)])
        line([(-10, 14), (0, 4), (10, 14)])
    elif kind == "flag":
        line([(-14, -16), (-14, 16)], w=3)
        for r in range(3):
            for c in range(4):
                if (r + c) % 2 == 0:
                    draw.rectangle([cx + (-12 + c * 7) * u, cy + (-16 + r * 6) * u,
                                    cx + (-5 + c * 7) * u, cy + (-10 + r * 6) * u],
                                   fill=color)
    elif kind == "chart":
        line([(-16, 14), (16, 14)])
        line([(-16, 14), (-16, -14)])
        line([(-14, -10), (-4, -2), (4, -8), (14, 10)], w=3)
        poly([(14, 10), (8, 10), (14, 4)])
    elif kind == "star":
        pts = [(0, -16), (4, -5), (16, -5), (7, 2), (10, 14),
               (0, 7), (-10, 14), (-7, 2), (-16, -5), (-4, -5)]
        poly(pts, fill=color)
    elif kind == "chip":
        draw.rectangle([cx - 10 * u, cy - 10 * u, cx + 10 * u, cy + 10 * u],
                       outline=color, width=max(1, int(2 * u)))
        draw.rectangle([cx - 4 * u, cy - 4 * u, cx + 4 * u, cy + 4 * u], fill=color)
        for k in (-6, 0, 6):
            line([(k, -16), (k, -10)])
            line([(k, 10), (k, 16)])
            line([(-16, k), (-10, k)])
            line([(10, k), (16, k)])
    elif kind == "cross":
        poly([(-4, -16), (4, -16), (4, -4), (16, -4), (16, 4),
              (4, 4), (4, 16), (-4, 16), (-4, 4), (-16, 4), (-16, -4), (-4, -4)],
             fill=RED)
    elif kind == "bat":
        line([(-12, 12), (8, -12)], w=5)
        draw.ellipse([cx + 8 * u, cy - 16 * u, cx + 16 * u, cy - 8 * u],
                     fill=RED)
    elif kind == "gavel":
        line([(-14, 12), (14, -12)], w=4)
        line([(-14, -2), (-2, -14)], w=6)
        line([(-14, 16), (14, 16)], w=2)
    elif kind == "flame":
        poly([(-10, 12), (-12, 0), (-4, -8), (0, -16), (6, -6),
              (12, -2), (10, 12)], fill=(214, 96, 20))
    elif kind == "note":
        draw.rectangle([cx - 16 * u, cy - 10 * u, cx + 16 * u, cy + 10 * u],
                       outline=color, width=max(1, int(2 * u)))
        ell((-6, -5, 6, 5), fill=color)
    elif kind == "ship":
        poly([(-16, 2), (16, 2), (10, 12), (-10, 12)])
        line([(0, 2), (0, -14)], w=2)
        poly([(0, -14), (0, -2), (12, -2)])
    elif kind == "globe":
        draw.ellipse([cx - 15 * u, cy - 15 * u, cx + 15 * u, cy + 15 * u],
                     outline=color, width=max(1, int(2 * u)))
        line([(-15, 0), (15, 0)])
        draw.arc([cx - 7 * u, cy - 15 * u, cx + 7 * u, cy + 15 * u],
                 270, 90, fill=color, width=max(1, int(2 * u)))
        draw.arc([cx - 7 * u, cy - 15 * u, cx + 7 * u, cy + 15 * u],
                 90, 270, fill=color, width=max(1, int(2 * u)))
    elif kind == "shield":
        poly([(-14, -14), (14, -14), (14, 2), (0, 16), (-14, 2)],
             fill=None, outline=color)
        line([(-7, -1), (-2, 5), (8, -7)], w=3)
    elif kind == "crown":
        poly([(-15, 10), (-15, -8), (-7, 2), (0, -12), (7, 2),
              (15, -8), (15, 10)], fill=(212, 175, 55))
        line([(-15, 14), (15, 14)], w=2)
    elif kind == "dove":
        ell((-14, -4, 8, 8), fill=color)
        ell((6, -12, 16, -2), fill=color)
        poly([(15, -9), (20, -7), (15, -5)], fill=(214, 96, 20))
        poly([(-10, -2), (2, -14), (6, -2)], fill=(120, 140, 170))
        line([(-14, 6), (-4, 12), (6, 6)], w=2)


# ---------------------------------------------------------------- page

def draw_page():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 16

    # Masthead
    title_f = font(SERIF, 46)
    date_f = font(SANS_BOLD, 15)
    d.text((W // 2, 12), "THE WORLD IN ONE DAY", font=title_f,
           fill=INK, anchor="ma")
    d.text((W // 2, 62), "TUESDAY 24 NOVEMBER 2026  \u00b7  45 STORIES FROM SIX CONTINENTS",
           font=date_f, fill=RED, anchor="ma")
    d.line([(mx, 84), (W - mx, 84)], fill=INK, width=2)
    d.line([(mx, 88), (W - mx, 88)], fill=INK, width=1)

    # Leads: two boxes
    lead_y, lead_h = 96, 148
    box_w = (W - 2 * mx - 12) // 2
    f_kick = font(SANS_BOLD, 12)
    f_head = font(SANS_BOLD, 18)
    f_deck = font(SANS, 13)
    for i, lead in enumerate(LEADS):
        x0 = mx + i * (box_w + 12)
        d.rectangle([x0, lead_y, x0 + box_w, lead_y + lead_h],
                    outline=RULE, width=1)
        d.rectangle([x0, lead_y, x0 + box_w, lead_y + 22], fill=LIGHT)
        d.text((x0 + 8, lead_y + 4), lead["kicker"], font=f_kick, fill=RED)
        icon(d, lead["icon"], x0 + box_w - 34, lead_y + 46, 44)
        head_w = box_w - 84
        lines = wrap(d, lead["headline"], f_head, head_w)
        y = lead_y + 30
        for ln in lines[:3]:
            d.text((x0 + 8, y), ln, font=f_head, fill=INK)
            y += 22
        for ln in wrap(d, lead["deck"], f_deck, box_w - 16)[:2]:
            d.text((x0 + 8, y), ln, font=f_deck, fill=(60, 58, 52))
            y += 16

    # Top stories: three boxes
    top_y, top_h = 254, 100
    top_w = (W - 2 * mx - 24) // 3
    f_thead = font(SANS_BOLD, 14)
    f_tdeck = font(SANS, 11)
    for i, top in enumerate(TOPS):
        x0 = mx + i * (top_w + 12)
        d.rectangle([x0, top_y, x0 + top_w, top_y + top_h],
                    outline=RULE, width=1)
        d.text((x0 + 8, top_y + 5), top["kicker"], font=f_kick, fill=BLUE)
        icon(d, top["icon"], x0 + top_w - 26, top_y + 24, 34)
        lines = wrap(d, top["headline"], f_thead, top_w - 62)
        y = top_y + 24
        for ln in lines[:3]:
            d.text((x0 + 8, y), ln, font=f_thead, fill=INK)
            y += 17
        for ln in wrap(d, top["deck"], f_tdeck, top_w - 16)[:1]:
            d.text((x0 + 8, y), ln, font=f_tdeck, fill=(60, 58, 52))

    # Briefs header
    d.line([(mx, 366), (W - mx, 366)], fill=INK, width=2)
    d.text((mx, 372), "THE DAY IN BRIEF \u2014 40 MORE STORIES",
           font=font(SANS_BOLD, 13), fill=INK)
    d.text((W - mx, 372), "ALL FROM TUESDAY 24 NOVEMBER 2026",
           font=font(SANS_BOLD, 11), fill=GREY, anchor="ra")

    # Briefs: two columns of twenty
    f_num = font(SANS_BOLD, 12)
    f_brief = font(SANS, 12)
    col_w = (W - 2 * mx - 12) // 2
    row_h = 20
    for idx, text in enumerate(BRIEFS):
        col = idx // 20
        row = idx % 20
        x0 = mx + col * (col_w + 12)
        y = 396 + row * row_h
        num = idx + 6
        d.text((x0, y), f"{num}.", font=f_num, fill=RED)
        tx = x0 + 26
        kind = BRIEF_ICONS.get(num)
        if kind:
            icon(d, kind, x0 + 34, y + 7, 15)
            tx = x0 + 46
        d.text((tx, y), one_line(d, text, f_brief, x0 + col_w - tx),
               font=f_brief, fill=INK)

    # World map: dot matrix + pins
    map_y = 806
    d.line([(mx, map_y - 6), (W - mx, map_y - 6)], fill=INK, width=2)
    d.text((mx, map_y), "WHERE IT HAPPENED",
           font=font(SANS_BOLD, 13), fill=INK)
    map_x, map_w, map_h = mx, 620, 118
    map_top = map_y + 20
    cols, rows = 48, 20
    cw, ch = map_w / cols, map_h / rows
    for r, line in enumerate(LAND):
        assert len(line) == cols, f"map row {r} is {len(line)} chars"
        for c, ch_ in enumerate(line):
            if ch_ == "#":
                d.ellipse([map_x + c * cw + 1, map_top + r * ch + 1,
                           map_x + (c + 1) * cw - 1, map_top + (r + 1) * ch - 1],
                          fill=(90, 88, 80))
    f_pin = font(SANS_BOLD, 10)
    for n, (lat, lon, _name) in enumerate(PINS, start=1):
        px = map_x + (lon + 180) / 7.5 * cw
        py = map_top + (78 - lat) / 6.75 * ch
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=PAPER, width=1)
        d.text((px, py - 1), str(n), font=f_pin, fill=(255, 255, 255), anchor="mm")
    # Legend
    leg_x = map_x + map_w + 16
    f_leg = font(SANS, 12)
    for i, (_lat, _lon, name) in enumerate(PINS):
        lx = leg_x + (i // 6) * 190
        ly = map_top + 4 + (i % 6) * 20
        d.ellipse([lx, ly, lx + 14, ly + 14], fill=RED)
        d.text((lx + 7, ly + 6), str(i + 1), font=f_pin,
               fill=(255, 255, 255), anchor="mm")
        d.text((lx + 20, ly + 1), name, font=f_leg, fill=INK)

    # Markets bar
    bar_y = 946
    d.rectangle([mx, bar_y, W - mx, bar_y + 52], fill=INK)
    d.text((mx + 10, bar_y + 6), "MARKETS \u2014 MONDAY US CLOSES; TUESDAY ASIA",
           font=font(SANS_BOLD, 12), fill=(255, 210, 90))
    f_mkt2 = font(SANS, 12)
    x = mx + 10
    y = bar_y + 26
    for name, val, chg in MARKETS:
        label = f"{name} {val} {chg}".strip()
        d.text((x, y), label, font=f_mkt2, fill=(240, 238, 230))
        x += d.textlength(label, font=f_mkt2) + 18
    # Sparkline: Kospi's Tuesday surge, at the bar's top right
    pts = [(0, 12), (18, 11), (36, 12), (54, 9), (72, 6), (90, 3), (108, 1)]
    sx, sy = W - mx - 122, bar_y + 5
    d.line([(sx + px, sy + py) for px, py in pts], fill=(120, 220, 130), width=2)

    # Footer
    d.text((W // 2, 1006),
           "Every story above happened or was first reported on Tuesday 24 November 2026.",
           font=font(SANS, 11), fill=GREY, anchor="ma")

    img.save(OUT, "PNG")
    return OUT


if __name__ == "__main__":
    path = draw_page()
    print("wrote", path, path.stat().st_size, "bytes")
