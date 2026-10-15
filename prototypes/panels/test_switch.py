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


def render(field, view="full", sarcasm="10", lang="en", feels=None, nxt=None):
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
    if nxt is not None:
        cfg["what_to_wear_next"] = nxt
    d = dt.date.fromisoformat(DATE)
    ts = calendar.timegm((d.year, d.month, d.day, 7, 30, 0)) - OFFSET
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

# A line that stands alone wherever no forecast line is shown.
VF = {m: ["STANDS ALONE"] for m in ("wet", "warming", "cooling", "cold", "fickle", "hot", "snow", "nice", "cool")}
TEXTS["en"]["flavour_vf_10"] = VF
expect("drawings without words: the line that stands alone", "STANDS ALONE" in render(False, nxt=True))
expect("outfit alone: the line that stands alone", "STANDS ALONE" in render(False))
expect("forecast on: the usual line", "STANDS ALONE" not in render(True))
expect("both on: the usual line, which answers the forecast line", "STANDS ALONE" not in render(True, nxt=True))
expect("one drawing with 'works all day': the usual line", "STANDS ALONE" not in render(False, feels=STEADY, nxt=True))
del TEXTS["en"]["flavour_vf_10"]
expect("no pool: the usual line", WORDS in render(False, nxt=True))

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
