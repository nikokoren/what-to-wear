#!/usr/bin/env python3
"""
Pins how the texts rotate (block.liquid, text_rot): a new wording every
hour, the same one all through the hour, and every line of a pool coming
round, also for someone who only ever looks at the same hour.

    python3 prototypes/fact-flavour/build.py
    python3 prototypes/fact-flavour/test_rotation.py
"""

import calendar
import datetime as dt
import json
import pathlib
import sys

from liquid import Environment

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
PROTO = REPO / "build" / "proto"
SHARED = (PROTO / "shared.liquid").read_text(encoding="utf-8")
PROBE = Environment().from_string(SHARED + "\n@@{{ fact_line }}|{{ flavour_line }}|{{ mood }}")
TEXTS = {l: json.loads((PROTO / "lang" / f"{l}.json").read_text(encoding="utf-8")) for l in ("en", "de")}
OFFSET = 7200


def render(date, hour, minute=30, temp=18, lang="en", sarcasm="10"):
    """A steady day (same weather all day), read at date hour:minute local time."""
    hours = [f"{date}T{h:02d}:00" for h in range(24)]
    data = {"utc_offset_seconds": OFFSET, "timezone": "Europe/Vienna",
            "current": {"time": f"{date}T{hour:02d}:{minute - minute % 15:02d}", "temperature_2m": temp,
                        "apparent_temperature": temp, "weather_code": 0},
            "hourly": {"time": hours, "temperature_2m": [temp] * 24, "apparent_temperature": [temp] * 24,
                       "precipitation_probability": [0] * 24, "weather_code": [0] * 24}}
    cfg = {"language": lang, "sarcasm_level": sarcasm, "show_future_suggestions": "yes", "lat_lon": "48.2,16.4"}
    d = dt.date.fromisoformat(date)
    ts = calendar.timegm((d.year, d.month, d.day, hour, minute, 0)) - OFFSET
    ctx = {"trmnl": {"plugin_settings": {"custom_fields_values": cfg}, "system": {"timestamp_utc": ts},
                     "user": {"utc_offset": OFFSET}, "device": {"width": 800}},
           "IDX_0": data, "IDX_1": TEXTS[lang]}
    fact, flavour, mood = PROBE.render(**ctx).split("@@")[-1].split("|")
    return fact.strip(), flavour.strip(), mood.strip()


failures = []


def expect(name, ok):
    if not ok:
        failures.append(name)


DATE = "2026-06-10"
day = [render(DATE, h) for h in range(7, 17)]
mood = day[0][2]
expect("a steady daytime mood", mood == "nice" and all(d[2] == mood for d in day))
# With the forecast line on screen the line is a follow-up (block.liquid);
# no follow-ups for the mood, the standalone lines.
pool = TEXTS["en"]["flavour_10"].get(mood) or ((TEXTS["en"].get("alone_10", {}).get(mood) or []) + (TEXTS["en"].get("now_10", {}).get(mood) or []))

# A new sarcastic line every hour, and the fact wording moves too.
expect("the sarcastic line changes every hour", all(day[i][1] != day[i + 1][1] for i in range(len(day) - 1)))
expect("the fact wording changes during the day", len({d[0] for d in day}) > 1)

# The same all through the hour.
expect("same words at :00 and :59", render(DATE, 9, 0) == render(DATE, 9, 59))

# Someone who only looks at 7:00 sees the whole pool over the days.
d0 = dt.date.fromisoformat(DATE)
mornings = {render((d0 + dt.timedelta(days=i)).isoformat(), 7)[1] for i in range(len(pool))}
expect(f"every 7:00 line over {len(pool)} days ({len(mornings)} of {len(set(pool))})", mornings == set(pool))

# Never the next line in the pool: an hour on lands elsewhere.
idx = [pool.index(d[1]) for d in day]  # first index of the line in the mixed pool
if len(pool) > 2:  # with two lines every step is the other one
    expect("an hour on isn't simply the next line", any((b - a) % len(pool) != 1 for a, b in zip(idx, idx[1:])))

# The primes (101, 103) must be larger than every pool, merged pools included.
for lang, doc in TEXTS.items():
    for key, section in doc.items():
        if isinstance(section, dict):
            for name, lines in section.items():
                if isinstance(lines, list):
                    expect(f"{lang} {key}.{name} has {len(lines)} lines, fewer than 101", len(lines) < 101)
    for level in ("10", "11"):
        lib = doc.get(f"flavour_{level}", {})
        for m in ("warming", "cooling"):
            n = len(lib.get(m, [])) + len(lib.get("cool", []))
            expect(f"{lang} {level} {m} with cool's lines: {n}, fewer than 101", n < 101)

if failures:
    print("FAILED:\n  " + "\n  ".join(failures))
    sys.exit(1)
print("all good: a new wording every hour, steady within the hour, every line comes round")
