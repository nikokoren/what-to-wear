#!/usr/bin/env python3
"""
How often the screen repeats itself, over two years of real mornings.

    sh tools/climate/fetch.sh /tmp/climate              # once, ~140 MB
    python3 prototypes/fact-flavour/build.py            # build/proto
    python3 tools/climate/repeat_report.py /tmp/climate
    python3 tools/climate/repeat_report.py /tmp/climate --lang de --level 11
    python3 tools/climate/repeat_report.py /tmp/climate --all-variants

Feeds every 7:00 reading of 2024-2025 in a few cities through the
prototype markup (build/proto) and counts, for each line shown, whether
the same line was already shown in the 7 or 30 days before. "Whole
screen" is the fact and flavour line together.

--all-variants adds every round-5 candidate (review/rounds/
2026-10-variants.json) as if it had been kept: the most the variance
round can do.

The goal (October 2026): repeats rare enough that nobody notices,
closer to Carrot Weather than to one line per mood.
"""

import argparse
import collections
import copy
import csv
import datetime as dt
import gzip
import json
import math
import pathlib
from zoneinfo import ZoneInfo

from liquid import Environment

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
PROTO = REPO / "build" / "proto"
TZ = {l.split()[1]: l.split()[3] for l in (REPO / "tools" / "climate" / "stations.txt").read_text().splitlines() if l.strip()}
# Meteostat condition code -> the WMO code Open-Meteo reports
COCO = {1: 0, 2: 1, 3: 2, 4: 3, 5: 45, 6: 48, 7: 61, 8: 63, 9: 65, 10: 66, 11: 67, 12: 71, 13: 73,
        14: 71, 15: 73, 16: 75, 17: 80, 18: 82, 19: 85, 20: 85, 21: 85, 22: 86, 23: 95, 24: 95, 25: 95, 26: 96, 27: 99}
WET = {51, 53, 55, 61, 63, 65, 66, 67, 71, 73, 75, 80, 81, 82, 85, 86, 95, 96, 99}


def apparent(t, rh, ws_kmh):
    e = rh / 100 * 6.105 * math.exp(17.27 * t / (237.7 + t))
    return t + 0.33 * e - 0.70 * (ws_kmh / 3.6) - 4.00


def city_hours(data, city):
    z = ZoneInfo(TZ[city])
    out = {}
    with gzip.open(data / f"{city}.csv.gz", "rt") as f:
        for r in csv.reader(f):
            if not r[0].startswith(("2023", "2024", "2025")) or r[2] == "" or r[4] == "":
                continue
            t, rh = float(r[2]), float(r[4])
            ws = float(r[8]) if r[8] else 10.8
            pr = float(r[5]) if r[5] else None
            co = int(float(r[12])) if len(r) > 12 and r[12] else None
            utc = dt.datetime.fromisoformat(r[0]).replace(hour=int(r[1]), tzinfo=dt.timezone.utc)
            out[utc.astimezone(z).replace(tzinfo=None)] = (round(apparent(t, rh, ws), 1), round(t, 1), pr, co)
    return out


def day_series(hrs, city, date):
    rows = [hrs.get(dt.datetime.combine(date, dt.time(h))) for h in range(24)]
    if sum(r is None for r in rows) > 4:
        return None
    for i in range(24):
        if rows[i] is None:
            prev = next((rows[j] for j in range(i - 1, -1, -1) if rows[j]), None)
            nxt = next((rows[j] for j in range(i + 1, 24) if rows[j]), None)
            rows[i] = prev or nxt
    codes, probs = [], []
    for _, t, pr, co in rows:
        w = COCO.get(co, 0) if co else 0
        if pr is not None and pr >= 0.2 and w not in WET:
            w = 71 if t <= 0.5 else 61
        codes.append(w)
        probs.append(90 if w in WET else 5)
    z = ZoneInfo(TZ[city])
    off = int(dt.datetime.combine(date, dt.time(12)).replace(tzinfo=z).utcoffset().total_seconds())
    return {"at": [r[0] for r in rows], "t": [r[1] for r in rows], "codes": codes, "probs": probs, "offset": off}


def context(city, date, hour, s, texts, lang, level):
    times = [f"{date.isoformat()}T{h:02d}:00" for h in range(24)]
    data = {"utc_offset_seconds": s["offset"],
            "current": {"time": f"{date.isoformat()}T{hour:02d}:30", "temperature_2m": s["t"][hour],
                        "apparent_temperature": s["at"][hour], "weather_code": s["codes"][hour]},
            "hourly": {"time": times, "temperature_2m": s["t"], "apparent_temperature": s["at"],
                       "precipitation_probability": s["probs"], "weather_code": s["codes"]}}
    cfg = {"location_label": city.title(), "show_future_suggestions": "yes", "language": lang,
           "sarcasm_level": level, "show_bottom_bar": "on", "lat_lon": "0,0"}
    ts = int(dt.datetime.combine(date, dt.time(hour, 30)).timestamp()) - s["offset"]
    return {"trmnl": {"plugin_settings": {"custom_fields_values": cfg}, "system": {"timestamp_utc": ts},
                      "user": {"utc_offset": s["offset"]}, "device": {"width": 800}},
            "IDX_0": data, "IDX_1": texts}


def with_all_variants(texts, lang):
    """Every round-5 candidate added as if kept, in the order build_pools.py uses."""
    texts = copy.deepcopy(texts)
    lines = json.loads((REPO / "review" / "rounds" / "2026-10-variants.json").read_text(encoding="utf-8"))["lines"]
    for l in lines:
        if l["lang"] != lang:
            continue
        section, key = l["path"].split(".")
        if section == "fact_0":
            if l["template"] not in texts["facts"][key]:
                texts["facts"][key].append(l["template"])
    for level in ("10", "11"):
        pool = texts[f"flavour_{level}"]
        for mood, base in list(pool.items()):
            if mood.startswith("theme_"):
                continue
            extra = [l for l in lines if l["lang"] == lang and l["path"] == f"flavour_{level}.{mood}"
                     and l["variant_of"] in base]
            pool[mood] = base + [l["text"] for l in sorted(extra, key=lambda l: base.index(l["variant_of"]))]
    return texts


def repeats(seqs, pick):
    """Share of shown lines that were also shown in the previous 7 and 30 days."""
    w7 = w30 = n = 0
    for seq in seqs.values():
        last = {}
        for day, shown in enumerate(seq):
            k = pick(shown) if shown else None
            if not k:
                continue
            n += 1
            if k in last:
                gap = day - last[k]
                w7 += gap <= 7
                w30 += gap <= 30
            last[k] = day
    return w7 / n, w30 / n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("data", help="directory fetch.sh wrote")
    ap.add_argument("--cities", default="london,newyork,minneapolis,phoenix,vienna")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--level", default="10")
    ap.add_argument("--hour", type=int, default=7)
    ap.add_argument("--all-variants", action="store_true")
    a = ap.parse_args()

    texts = json.loads((PROTO / "lang" / f"{a.lang}.json").read_text(encoding="utf-8"))
    if a.all_variants:
        texts = with_all_variants(texts, a.lang)
    shared = (PROTO / "shared.liquid").read_text(encoding="utf-8")
    probe = Environment().from_string(shared + "\n@@{{ fact_line }}|{{ mood }}|{{ flavour_line }}")

    seqs = collections.defaultdict(list)
    for city in a.cities.split(","):
        hrs = city_hours(pathlib.Path(a.data), city)
        for date in sorted({k.date() for k in hrs if k.year in (2024, 2025)}):
            s = day_series(hrs, city, date)
            if not s:
                seqs[city].append(None)
                continue
            fact, mood, flavour = probe.render(**context(city, date, a.hour, s, texts, a.lang, a.level)).split("@@")[-1].split("|")
            seqs[city].append((fact.strip(), mood, flavour.strip()))

    print(f"{a.lang}, sarcasm {a.level}, {a.hour}:00, {a.cities}" + (", all variants" if a.all_variants else ""))
    for name, pick in (("fact line", lambda x: x[0]), ("flavour line", lambda x: x[2]),
                       ("whole screen", lambda x: x[0] + " | " + x[2])):
        w7, w30 = repeats(seqs, pick)
        print(f"  {name:13} already shown in the last 7 days: {w7:4.0%}   last 30 days: {w30:4.0%}")
    top = collections.Counter(x[0] for v in seqs.values() for x in v if x)
    total = sum(top.values())
    print("  commonest fact lines:")
    for text, n in top.most_common(3):
        print(f"    {n / total:5.1%}  {text}")


if __name__ == "__main__":
    main()
