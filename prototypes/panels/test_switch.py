#!/usr/bin/env python3
"""
Pins the forecast field's three values (config/settings.next.yaml):
"No" shows the outfit alone, "Yes" the forecast in words, "visual" the
Visual Forecast. Values saved before the field had a third option, in
any case, and no value at all must keep the words.

    python3 prototypes/panels/build.py
    python3 prototypes/panels/test_switch.py
"""

import calendar
import datetime as dt
import json
import pathlib
import sys

from liquid import Environment

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
BUILD = REPO / "build" / "panels"
SHARED = (BUILD / "shared.liquid").read_text(encoding="utf-8")
VIEWS = {v: Environment().from_string(SHARED + (BUILD / "views" / f"{v}.liquid").read_text(encoding="utf-8"))
         for v in ("full", "half_horizontal", "half_vertical", "quadrant")}
TEXTS = {l: json.loads((BUILD / "lang" / f"{l}.json").read_text(encoding="utf-8")) for l in ("en", "de")}
OFFSET = 7200
DATE = "2026-06-10"
# A cool morning that turns warm by noon: a sweater now, a T-shirt later.
FEELS = [9, 9, 8, 8, 8, 9, 10, 11, 12, 14, 17, 20, 22, 23, 24, 24, 23, 22, 21, 20, 19, 18, 17, 16]


STEADY = [15] * 24


def render(field, view="full", sarcasm="10", lang="en", feels=None):
    feels = feels or FEELS
    hours = [f"{DATE}T{h:02d}:00" for h in range(24)]
    data = {"utc_offset_seconds": OFFSET, "timezone": "Europe/Vienna",
            "current": {"time": f"{DATE}T07:30", "temperature_2m": feels[7],
                        "apparent_temperature": feels[7], "weather_code": 0},
            "hourly": {"time": hours, "temperature_2m": feels, "apparent_temperature": feels,
                       "precipitation_probability": [0] * 24, "weather_code": [0] * 24}}
    cfg = {"language": lang, "sarcasm_level": sarcasm, "lat_lon": "48.2,16.4", "show_bottom_bar": "on"}
    if field is not None:
        cfg["show_future_suggestions"] = field
    d = dt.date.fromisoformat(DATE)
    ts = calendar.timegm((d.year, d.month, d.day, 7, 30, 0)) - OFFSET
    ctx = {"trmnl": {"plugin_settings": {"custom_fields_values": cfg}, "system": {"timestamp_utc": ts},
                     "user": {"utc_offset": OFFSET}, "device": {"width": 800}},
           "IDX_0": data, "IDX_1": TEXTS[lang]}
    return VIEWS[view].render(**ctx)


failures = []


def expect(name, ok):
    if not ok:
        failures.append(name)


for view in VIEWS:
    html = render("visual", view)
    expect(f"visual draws panels ({view})", "wtw-panels" in html)
    expect(f"visual puts 'from' on the later time ({view})", ">from " in html)
    expect(f"visual has no fact line on a changing day ({view})", 'class="font--bold"' not in html)
    for field in ("Yes", "yes", "YES", None):
        html = render(field, view)
        expect(f"{field!r} keeps the words ({view})", "wtw-panels" not in html and 'class="font--bold"' in html)
    html = render("No", view)
    expect(f"'No' shows the outfit alone ({view})", "wtw-panels" not in html and 'class="font--bold"' not in html)

html = render("visual", sarcasm="0")
expect("visual at sarcasm Off has no words on a changing day", "wtw-panels" in html and 'wtw-words"' not in html)
html = render("visual", sarcasm="10")
expect("visual at sarcasm On adds the sarcastic line", 'wtw-words"' in html)
for view in VIEWS:
    html = render("visual", view, feels=STEADY)
    expect(f"visual on a steady day is the text view with 'works all day' ({view})",
           "wtw-panels" not in html and any(t in html for t in TEXTS["en"]["facts"]["steady"]))
html = render("visual", lang="de")
expect("German Visual Forecast says 'ab'", ">ab " in html and ">Jetzt<" in html)

if failures:
    print("FAILED:\n  " + "\n  ".join(failures))
    sys.exit(1)
print("all good: 'No' shows the outfit alone, 'Yes' (and old or missing values) the words, 'visual' the panels")
