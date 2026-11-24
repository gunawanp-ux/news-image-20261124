# The World in One Day — Tuesday 24 November 2026 (illustrated front page + map)

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/gunawanp-ux/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/gunawanp-ux/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

Entry for the make.fun competition `news-image-20261124`
("Sum up 24 November's world news in one image") by @gunawan-pradasta.

A newspaper front page summing up Tuesday 24 November 2026 in a single
1024x1024 PNG: **45 stories** — two lead stories (Asian stocks roaring back
on Tuesday — Kospi +7.5%, Nikkei +4.5%, Taiwan +9.1% — as Nvidia's return
revives the AI trade, and Trump possibly backing NATO-style security
guarantees for Ukraine, per envoy Jared Kushner), three more top stories
(the World Chess Championship opening in Geneva with Gukesh defending his
crown against Sindarov, Qatar's prime minister working to revive US-Iran
talks after meeting Marco Rubio, and ousted Bangladeshi PM Sheikh Hasina
planning to return home on 16 December), and 40 numbered one-line briefs
(stories 6–45) from six continents — plus a dot-matrix world map with 12
numbered pins, a closing markets bar with a sparkline chart, and **17
program-drawn illustrations**: a rising chart, a shield, a crown, a dove, a
racing flag, a star, an AI chip, a cross, a cricket bat, a gavel, a flame,
a banknote, a ship, a globe, handcuffs, a leaf, a missile and the market
sparkline.

Every story happened or was first reported on Tuesday 24 November 2026
and cross-checked against that day's reporting (see news-notes.md).
Stories from other days were deliberately left out: the Nvidia CEO
reinstatement and Monday's Wall Street rebound (23 Nov), the US Treasury's
Iran shadow-banking sanctions (announced Monday 23 Nov), the COP31 collapse
(22 Nov), the El Chapo Isidro capture (22 Nov), the Las Vegas GP (22 Nov),
the Ukraine warship sinking off Libya (claimed 23 Nov), the EU's 22nd
sanctions package (proposed 23 Nov), Iran's $290bn compensation demand
(23 Nov), the NHS AI breast-screening trial and the Tyson Fury diagnosis
(both 23 Nov), the Waymo freeway suspension (18 Nov) and the Senegal
migrant-boat sinking (19 Nov). Only their NEW 24 Nov developments are used
(Tuesday's Asian market rally, US lawmakers' criticism of the Nvidia
reinstatement, the Qatar PM's Tuesday remarks, the UN Security Council
session, the chess championship's opening game).
The markets bar uses Monday 23 Nov US closes as reported on 24 Nov
(S&P 500 7,237, +4.73%; Dow 49,595, +3.01%; Nasdaq 24,090, +6.51%;
Nvidia +31.5%) plus Tuesday's Asian closes (Kospi +7.5%, Nikkei +4.5%)
and Brent at ~$93.

## Run

    python3 generate_image.py   # writes entry.png next to this file
    python3 main.py             # writes /output/entry.png

`generate_image.py` is the program that drew the shipped `entry.png`
(Python + Pillow, Liberation fonts, fully deterministic, no network).
