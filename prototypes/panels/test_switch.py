#!/usr/bin/env python3
"""
Pins the two switches (config/settings.next.yaml): Forecast (the field
that was there, show_future_suggestions: "Yes"/"No" saved before,
true/false now) shows the words; What to Wear Next? (what_to_wear_next,
true/false) the drawings; both can be on. Old values in any case, and no
value at all, keep the words; the first beta's "visual" keeps drawings
without words. The sarcastic line shows at On and 11 in every mode.

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


def render(field, view="full", sarcasm="10", lang="en", feels=None, nxt=None, hour=7):
    feels = feels or FEELS
    hours = [f"{DATE}T{h:02d}:00" for h in range(24)]
    data = {"utc_offset_seconds": OFFSET, "timezone": "Europe/Vienna",
            "current": {"time": f"{DATE}T{hour:02d}:30", "temperature_2m": feels[hour],
                        "apparent_temperature": feels[hour], "weather_code": 0},
            "hourly": {"time": hours, "temperature_2m": feels, "apparent_temperature": feels,
                       "precipitation_probability": [0] * 24, "weather_code": [0] * 24}}
    cfg = {"language": lang, "sarcasm_level": sarcasm, "lat_lon": "48.2,16.4", "show_bottom_bar": "on"}
    if field is not None:
        cfg["show_future_suggestions"] = field
    if nxt is not None:
        cfg["what_to_wear_next"] = nxt
    d = dt.date.fromisoformat(DATE)
    ts = calendar.timegm((d.year, d.month, d.day, hour, 30, 0)) - OFFSET
    ctx = {"trmnl": {"plugin_settings": {"custom_fields_values": cfg}, "system": {"timestamp_utc": ts},
                     "user": {"utc_offset": OFFSET}, "device": {"width": 800}},
           "IDX_0": data, "IDX_1": TEXTS[lang]}
    return VIEWS[view].render(**ctx)


failures = []
PANELS = 'data-wtw="panels"'
WORDS = 'data-wtw="words"'
FACT = 'class="font--bold"'


def expect(name, ok):
    if not ok:
        failures.append(name)


for view in VIEWS:
    # Forecast only, in every spelling saved over the years, and no value at all.
    for field in ("Yes", "yes", "YES", None, True, "true"):
        html = render(field, view)
        expect(f"forecast {field!r}: the words ({view})", PANELS not in html and FACT in html)
    # Neither: the outfit, and the sarcastic line on its own.
    for field in ("No", "no", False, "false"):
        html = render(field, view)
        expect(f"forecast {field!r}: no forecast line ({view})", PANELS not in html and FACT not in html)
        expect(f"forecast {field!r}: the sarcastic line on the outfit alone ({view})", WORDS in html)
        expect(f"forecast {field!r}, sarcasm Off: the outfit alone ({view})", WORDS not in render(field, view, sarcasm="0"))
    # Only What to Wear Next: the drawings, no forecast line on a changing day.
    for field, nxt in ((False, True), ("No", "true"), ("visual", None), ("Visual", None)):
        html = render(field, view, nxt=nxt)
        expect(f"next only ({field!r}, {nxt!r}): drawings ({view})", PANELS in html)
        expect(f"next only ({field!r}, {nxt!r}): 'from' on the later time ({view})", ">from " in html)
        expect(f"next only ({field!r}, {nxt!r}): no forecast line ({view})", FACT not in html)
    # Both: the drawings and the forecast line.
    for field, nxt in ((True, True), ("Yes", "true")):
        html = render(field, view, nxt=nxt)
        expect(f"both ({field!r}, {nxt!r}): drawings and the forecast line ({view})", PANELS in html and FACT in html)
    # What to Wear Next off, in any spelling: the words.
    expect(f"next false: the words ({view})", PANELS not in render(True, view, nxt=False))

expect("next only, sarcasm Off: drawings, no words", WORDS not in render(False, sarcasm="0", nxt=True))
expect("next only, sarcasm On: the sarcastic line", WORDS in render(False, nxt=True))
for view in VIEWS:
    html = render(False, view, feels=STEADY, nxt=True)
    expect(f"next only on a steady day: one drawing, 'works all day' ({view})",
           PANELS not in html and any(t in html for t in TEXTS["en"]["facts"]["steady"]))

# Which sarcastic line: "now" lines (by what the Now drawing shows) on every
# screen; the day's lines only with the forecast line on a day that changes;
# the lines for the drawings only with two or three drawings and no words.
MOODS = ("wet", "warming", "cooling", "cold", "fickle", "hot", "snow", "nice", "cool", "evening", "night")
saved = {k: TEXTS["en"].get(k) for k in ("now_10", "flavour_10", "flavour_vf_10")}
TEXTS["en"]["now_10"] = {m: ["NOW LINE"] for m in MOODS}
TEXTS["en"]["flavour_10"] = {m: ["DAY LINE"] for m in MOODS}
TEXTS["en"]["flavour_vf_10"] = {m: ["DRAWINGS LINE"] for m in MOODS}


def line(html):
    return next((t for t in ("NOW LINE", "DAY LINE", "DRAWINGS LINE") if t in html), None)


def lines_over_hours(**kw):
    """The sarcastic lines a changing day shows from 7:00 to 10:00 (they rotate by the hour)."""
    out = set()
    for h in (7, 8, 9, 10):
        out.add(line(render(hour=h, **kw)))
    return out


expect("outfit alone: only now lines", lines_over_hours(field=False) == {"NOW LINE"})
expect("forecast on, a changing day: the day's and now lines", lines_over_hours(field=True) == {"NOW LINE", "DAY LINE"})
expect("forecast on, a steady day: now lines", line(render(True, feels=STEADY)) == "NOW LINE")
expect("drawings without words: lines for the drawings and now lines, never the day's",
       lines_over_hours(field=False, nxt=True) == {"NOW LINE", "DRAWINGS LINE"})
expect("both on: the day's and now lines, never the drawings'", lines_over_hours(field=True, nxt=True) == {"NOW LINE", "DAY LINE"})
expect("one drawing with 'works all day': now lines", line(render(False, feels=STEADY, nxt=True)) == "NOW LINE")
for k, v in saved.items():
    if v is None:
        TEXTS["en"].pop(k, None)
    else:
        TEXTS["en"][k] = v

# The owner's screen (October 2026): a day that warms up, T-shirt and shorts
# already, sarcasm 11, no words: "You'll call it 'crisp'..." from the cool
# lines contradicted the drawing. Now lines go by the Now drawing.
WARMING = [16, 16, 16, 17, 18, 19, 20, 22, 24, 25, 26, 27, 28, 29, 30, 30, 29, 28, 27, 26, 25, 24, 23, 22]
nice = set(TEXTS["en"]["now_11"]["nice"]) | set(TEXTS["en"]["now_11"].get("hot", []))
cool_only = set(TEXTS["en"]["flavour_11"]["cool"]) - nice
for h in (7, 9, 11, 13):
    for field, nxt in ((False, False), (False, True)):
        html = render(field, sarcasm="11", feels=WARMING, hour=h, nxt=nxt)
        expect(f"warm now at {h}:00 ({field}, {nxt}): no cool-day line", not any(t in html for t in cool_only))

# Framework classes only: no CSS of our own anywhere in the views.
for view in VIEWS:
    src = (BUILD / "views" / f"{view}.liquid").read_text(encoding="utf-8")
    expect(f"no <style> or style= in {view}", "<style" not in src and " style=" not in src)
html = render(False, lang="de", nxt=True)
expect("German drawings say 'ab'", ">ab " in html and ">Jetzt<" in html)

if failures:
    print("FAILED:\n  " + "\n  ".join(failures))
    sys.exit(1)
print("all good: Forecast shows the words, What to Wear Next the drawings, both together, old values keep working")
