#!/usr/bin/env python3
"""
Pins how topical lines show (block.liquid, TOPICAL LINES).

    python3 prototypes/fact-flavour/build.py
    python3 prototypes/fact-flavour/test_topical.py
"""

import calendar
import copy
import datetime as dt
import json
import pathlib
import sys

from liquid import Environment

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
PROTO = REPO / "build" / "proto"
SHARED = (PROTO / "shared.liquid").read_text(encoding="utf-8")
PROBE = Environment().from_string(SHARED + "\n@@{{ flavour_line }}|{{ flavour_topical }}|{{ mood }}")
TEXTS = {l: json.loads((PROTO / "lang" / f"{l}.json").read_text(encoding="utf-8")) for l in ("en", "de")}
OFFSET = 3600


def local_days(date):
    """The markup's day number: local seconds since the epoch, in days."""
    return dt.date.fromisoformat(date).toordinal() - dt.date(1970, 1, 1).toordinal()


def render(date, topical, field="on", sarcasm="10", temp=10, tz="Europe/Vienna", lang="en"):
    texts = copy.deepcopy(TEXTS[lang])
    texts[f"topical_{sarcasm}"] = topical
    hours = [f"{date}T{h:02d}:00" for h in range(24)]
    data = {"utc_offset_seconds": OFFSET, "timezone": tz,
            "current": {"time": f"{date}T09:30", "temperature_2m": temp,
                        "apparent_temperature": temp, "weather_code": 0},
            "hourly": {"time": hours, "temperature_2m": [temp] * 24, "apparent_temperature": [temp] * 24,
                       "precipitation_probability": [0] * 24, "weather_code": [0] * 24}}
    cfg = {"language": lang, "sarcasm_level": sarcasm, "show_future_suggestions": "yes", "lat_lon": "48.2,16.4"}
    if field is not None:
        cfg["topical_lines"] = field
    d = dt.date.fromisoformat(date)
    ts = calendar.timegm((d.year, d.month, d.day, 9, 30, 0)) - OFFSET
    ctx = {"trmnl": {"plugin_settings": {"custom_fields_values": cfg}, "system": {"timestamp_utc": ts},
                     "user": {"utc_offset": OFFSET}, "device": {"width": 800}},
           "IDX_0": data, "IDX_1": texts}
    line, topical, mood = PROBE.render(**ctx).split("@@")[-1].split("|")
    return line.strip(), topical == "true", mood


failures = []


def expect(name, got, want):
    if got != want:
        failures.append(f"{name}: got {got!r}, want {want!r}")


def days_in(start, n):
    d = dt.date.fromisoformat(start)
    return [(d + dt.timedelta(days=i)).isoformat() for i in range(n)]


A = {"text": "TOPICAL A", "from": "2026-10-25", "until": "2026-10-31"}
B = {"text": "TOPICAL B", "from": "2026-10-25", "until": "2026-10-31"}

# The first day of the window always shows it.
expect("first day", render("2026-10-25", [A])[:2], ("TOPICAL A", True))

# Then about one day in three, the rest the mood's own line.
shown = [d for d in days_in("2026-10-25", 7) if render(d, [A])[1]]
want = ["2026-10-25"] + [d for d in days_in("2026-10-26", 6) if local_days(d) % 3 == 0]
expect("one day in three", shown, want)

# Never outside the window.
expect("day before", render("2026-10-24", [A])[1], False)
expect("day after", render("2026-11-01", [A])[1], False)

# Off unless the field says on: installs from before the field have none.
expect("field missing", render("2026-10-25", [A], field=None)[1], False)
expect("field off", render("2026-10-25", [A], field="off")[1], False)

# Sarcasm Off shows no flavour line at all.
expect("sarcasm off", render("2026-10-25", [A], sarcasm="0")[0], "")

# Region, from the forecast's time zone.
expect("region match", render("2026-10-25", [dict(A, region="DE,AT,CH")])[1], True)
expect("region other", render("2026-10-25", [dict(A, region="UK")])[1], False)
expect("region UK", render("2026-10-25", [dict(A, region="UK,IE")], tz="Europe/London")[1], True)
expect("region US", render("2026-10-25", [dict(A, region="US")], tz="America/Indiana/Indianapolis")[1], True)
expect("region unknown zone", render("2026-10-25", [dict(A, region="US")], tz="Asia/Tokyo")[1], False)
expect("no region, any zone", render("2026-10-25", [A], tz="Asia/Tokyo")[1], True)

# Moods: a heat joke only on a hot day.
expect("mood mismatch", render("2026-10-25", [dict(A, moods="hot")], temp=10)[1], False)
expect("mood match", render("2026-10-25", [dict(A, moods="hot")], temp=33)[1], True)

# Two lines from one event take turns.
both = {render(d, [A, B])[0] for d in days_in("2026-10-25", 7) if render(d, [A, B])[1]}
expect("two lines take turns", both, {"TOPICAL A", "TOPICAL B"})

# A seasonal theme day keeps its own lines.
X = {"text": "TOPICAL X", "from": "2026-12-25", "until": "2026-12-25"}
line, topical, _ = render("2026-12-25", [X], temp=2)
expect("theme day keeps its lines", topical, False)

# German reads its own list.
expect("German", render("2026-10-25", [dict(A, text="AKTUELL")], lang="de")[0], "AKTUELL")

if failures:
    print("\n".join(failures))
    sys.exit(1)
print("all good: topical lines show inside their window, region and mood, about one day in three")
