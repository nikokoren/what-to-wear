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
import re
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


def render(field, view="full", sarcasm="10", lang="en", feels=None, nxt=None, hour=7, lat=None, probs=None, codes=None):
    feels = feels or FEELS
    hours = [f"{DATE}T{h:02d}:00" for h in range(24)]
    data = {"utc_offset_seconds": OFFSET, "timezone": "Europe/Vienna",
            "current": {"time": f"{DATE}T{hour:02d}:30", "temperature_2m": feels[hour],
                        "apparent_temperature": feels[hour], "weather_code": (codes or [0] * 24)[hour]},
            "hourly": {"time": hours, "temperature_2m": feels, "apparent_temperature": feels,
                       "precipitation_probability": probs or [0] * 24, "weather_code": codes or [0] * 24}}
    if lat is not None:
        data["latitude"] = lat
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

# Which sarcastic line (round 11): under the forecast line only follow-ups
# (flavour_10, by the day's mood); everywhere else standalone lines: now lines
# (now_10, by the Now drawing) and the day's standalone lines (alone_10);
# with two or three drawings and no words, the lines for the drawings too.
MOODS = ("wet", "warming", "cooling", "cold", "fickle", "hot", "snow", "nice", "cool", "evening", "night")
KEYS = ("now_10", "alone_10", "flavour_10", "flavour_vf_10")
saved = {k: TEXTS["en"].get(k) for k in KEYS}
TEXTS["en"]["now_10"] = {m: ["NOW LINE"] for m in MOODS}
TEXTS["en"]["alone_10"] = {m: ["ALONE LINE"] for m in MOODS}
GROUPS = ("rain", "snow", "off", "on", "offon", "hot", "steady", "cold", "evening", "night")
TEXTS["en"]["flavour_10"] = {g: ["FOLLOW-UP LINE"] for g in GROUPS}
TEXTS["en"]["flavour_vf_10"] = {m: ["DRAWINGS LINE"] for m in MOODS}
MARKERS = ("NOW LINE", "ALONE LINE", "FOLLOW-UP LINE", "DRAWINGS LINE")


def line(html):
    return next((t for t in MARKERS if t in html), None)


def lines_over_hours(**kw):
    """The sarcastic lines from 7:00 to 12:00 (they rotate by the hour)."""
    return {line(render(hour=h, **kw)) for h in (7, 8, 9, 10, 11, 12)}


STANDALONE = {"NOW LINE", "ALONE LINE"}
expect("forecast on, a changing day: only follow-ups", lines_over_hours(field=True) == {"FOLLOW-UP LINE"})
expect("forecast on, a steady day: only follow-ups", lines_over_hours(field=True, feels=STEADY) == {"FOLLOW-UP LINE"})
expect("both on: only follow-ups", lines_over_hours(field=True, nxt=True) == {"FOLLOW-UP LINE"})
expect("outfit alone: standalone lines", lines_over_hours(field=False) == STANDALONE)
expect("outfit alone, a steady day: standalone lines", lines_over_hours(field=False, feels=STEADY) == STANDALONE)
expect("drawings without words: drawings and standalone lines",
       lines_over_hours(field=False, nxt=True) == STANDALONE | {"DRAWINGS LINE"})
expect("one drawing with 'works all day': standalone lines", lines_over_hours(field=False, feels=STEADY, nxt=True) == STANDALONE)
# No follow-ups for the mood: the standalone lines, under the forecast line too.
TEXTS["en"]["flavour_10"] = {}
expect("no follow-ups: standalone lines", lines_over_hours(field=True) <= STANDALONE)
# Month tags: a line shows only in its months; otherwise the next line.
TEXTS["en"]["flavour_10"] = {g: ["{M:01,02}WINTER LINE", "FOLLOW-UP LINE"] for g in GROUPS}
expect("a June day skips a January line", all("WINTER LINE" not in render(True, hour=h) and "{M:" not in render(True, hour=h) for h in range(7, 13)))
TEXTS["en"]["flavour_10"] = {g: ["{M:05,06,07}SUMMER LINE", "FOLLOW-UP LINE"] for g in GROUPS}
expect("a June day shows a June line, tag stripped", any("SUMMER LINE" in render(True, hour=h) for h in range(7, 13))
       and not any("{M:" in render(True, hour=h) for h in range(7, 13)))
# South of the equator the seasons run six months on: in June, Sydney gets
# the December lines and not the June ones; Vienna, with its latitude, not.
TEXTS["en"]["flavour_10"] = {g: ["{M:12}DECEMBER LINE", "{M:06}JUNE LINE"] for g in GROUPS}
south = {render(True, hour=h, lat=-33.9) for h in range(7, 13)}
north = {render(True, hour=h, lat=48.2) for h in range(7, 13)}
expect("June in Sydney: the December line", all("DECEMBER LINE" in h and "JUNE LINE" not in h for h in south))
expect("June in Vienna: the June line", all("JUNE LINE" in h and "DECEMBER LINE" not in h for h in north))
# Follow-ups go by what the forecast line says: a cold morning whose line says
# the coat comes off gets the "off" lines, not cold ones.
TEXTS["en"]["flavour_10"] = {g: [f"GROUP {g.upper()}"] for g in GROUPS}
COLD_THEN_MILD = [-4, -4, -4, -4, -3, -3, -2, -1, 1, 3, 6, 9, 12, 14, 15, 15, 14, 12, 10, 8, 6, 4, 2, 1]
html = render(True, feels=COLD_THEN_MILD, hour=7)
expect("a cold morning that warms: the 'off' follow-ups", "GROUP OFF" in html)
expect("a steady day: the 'steady' follow-ups", "GROUP STEADY" in render(True, feels=STEADY))
# "{3}": only with three different drawings.
TEXTS["en"]["flavour_vf_10"] = {m: ["{3}THREE LINE"] for m in MOODS}
TEXTS["en"]["now_10"] = {m: ["NOW LINE"] for m in MOODS}
TEXTS["en"]["alone_10"] = {}
ARC = [2, 2, 2, 2, 2, 3, 4, 5, 7, 10, 13, 15, 16, 16, 15, 13, 10, 7, 5, 4, 3, 3, 2, 2]
UP = [2, 2, 2, 2, 2, 3, 4, 6, 9, 13, 17, 21, 24, 26, 27, 27, 26, 25, 24, 23, 22, 21, 20, 19]
expect("jacket, sweater, jacket: no 'three outfits' line", all("THREE LINE" not in render(False, feels=ARC, hour=h, nxt=True) for h in (8, 9)))
expect("three different outfits: the 'three outfits' line can show",
       any("THREE LINE" in render(False, feels=UP, hour=h, nxt=True) for h in range(7, 10)))
# The garment the forecast line names: {GP} its pronoun, {G} the garment;
# "{W:...}" lines only for the garments they list. The cool morning above:
# the jacket comes off at 7:00 and 8:00, from 9:00 the line is about the
# sweater ("ihn" in German), and the jacket-only line stays away.
TEXTS["en"]["flavour_10"] = {g: ["{W:jacket}JACKET ONLY", "OFF {GP} | {G}"] for g in GROUPS}
expect("the jacket comes off: the jacket line, or 'it', 'the jacket'",
       all("JACKET ONLY" in render(True, hour=h) or "OFF it | the jacket" in render(True, hour=h) for h in (7, 8)))
shown = {render(True, hour=h) for h in range(9, 13)}
expect("a sweater: no jacket-only line", not any("JACKET ONLY" in h for h in shown))
expect("a sweater: 'it', 'the sweater'", any("OFF it | the sweater" in h for h in shown))
expect("no garment placeholder left over", not any("{G" in h or "{W:" in h for h in shown))
TEXTS["en"]["flavour_10"] = {g: ["{W:hoodie,jacket}SWEATER OR JACKET", "OTHER"] for g in GROUPS}
expect("a sweater: the line for sweaters can show",
       any("SWEATER OR JACKET" in render(True, hour=h) for h in range(9, 13)))
expect("a steady day names no garment: no garment line", not any(
    "SWEATER OR JACKET" in render(True, feels=STEADY, hour=h) for h in range(7, 13)))
de_saved = TEXTS["de"].get("flavour_10")
TEXTS["de"]["flavour_10"] = {g: ["AUS {GP}"] for g in GROUPS}
expect("German: the sweater is 'ihn'",
       all("AUS ihn" in render(True, lang="de", hour=h) for h in range(9, 13)))
TEXTS["de"]["flavour_10"] = de_saved
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
cool_lines = set()
for key in ("now_11", "alone_11", "flavour_11"):
    cool_lines |= set(TEXTS["en"].get(key, {}).get("cool", []))
cool_only = cool_lines - nice
expect("the regression test has cool lines to look for", any("crisp" in t for t in cool_only))
for h in (7, 9, 11, 13):
    for field, nxt in ((False, False), (False, True)):
        html = render(field, sarcasm="11", feels=WARMING, hour=h, nxt=nxt)
        expect(f"warm now at {h}:00 ({field}, {nxt}): no cool-day line", not any(t in html for t in cool_only))

# Big swings (a reader in Colorado): freezing at dawn, shorts weather from
# 1 pm to 5 pm. Three hours or more of it and the legs are shorts: the Now
# drawing keeps the coat, the later drawings show shorts, and the forecast
# line says to go out in shorts, and that a layer comes back this evening.
CO = [-3, -3, -4, -4, -4, -3, -2, 0, 4, 9, 14, 19, 23, 26, 27, 27, 26, 23, 18, 13, 9, 6, 4, 2]
for lang, word in (("en", "shorts"), ("de", "Shorts")):
    html = render(True, feels=CO, hour=7, nxt=True, lang=lang)
    slugs = re.findall(r"([a-z_]+_dry)\.png", html)
    expect(f"{lang}: a Colorado morning, the coat now", slugs[:1] == ["coat_dry"])
    expect(f"{lang}: a Colorado morning, shorts later", "tee_shorts_dry" in slugs and "tee_pants_dry" not in slugs)
    words = re.sub(r"<[^>]+>", " ", html)
    expect(f"{lang}: a Colorado morning, the forecast says shorts", f"{word} an" in words or "wear shorts" in words.lower()
           or "go with shorts" in words.lower())
    expect(f"{lang}: a Colorado morning, no placeholder left", "{" not in words)
# Two hours of shorts weather from a cold start: long pants, as before.
BRIEF = [-3, -3, -4, -4, -4, -3, -2, 0, 4, 9, 14, 19, 22, 23, 25, 25, 23, 20, 18, 13, 9, 6, 4, 2]
html = render(True, feels=BRIEF, hour=7, nxt=True)
expect("two hours of shorts weather: long pants", "tee_shorts_dry" not in html and "shorts" not in re.sub(r"<[^>]+>|sprites/[a-z_]+", " ", html).lower())

# A cold front (24 C at 8 am, freezing by 3 pm): long pants at the door,
# and the forecast line says why.
NORTH = [20, 20, 19, 19, 19, 20, 21, 23, 24, 25, 25, 22, 14, 8, 4, 2, 1, 0, -1, -2, -2, -3, -3, -3]
for lang, word in (("en", "long pants"), ("de", "lange Hosen")):
    html = render(True, feels=NORTH, hour=8, nxt=True, lang=lang)
    slugs = re.findall(r"([a-z_]+_dry)\.png", html)
    expect(f"{lang}: a cold front, long pants now", slugs[:1] == ["tee_pants_dry"])
    expect(f"{lang}: a cold front, the forecast says long pants", word in html)
# Dangerous heat (37 C at 9 am, 43 C by 2 pm): water and shade lead, not
# the evening's easing.
HEAT = [30, 29, 29, 28, 28, 29, 31, 33, 35, 37, 39, 41, 42, 43, 43, 42, 41, 39, 37, 35, 34, 33, 32, 31]
for lang, word in (("en", "Dangerous heat"), ("de", "gefährlich heiß")):
    expect(f"{lang}: dangerous heat leads", all(word in render(True, feels=HEAT, hour=h, lang=lang) for h in (9, 12, 15)))
# Freezing rain in the window: the ice warning. A thunderstorm: the storm
# wording. Freezing rain wins when both come.
COLD = [-2] * 24
RAIN_PM = [0] * 14 + [80] * 4 + [0] * 6


def says(html, pattern):
    return re.search(pattern, re.sub(r"<[^>]+>", " ", html), re.I) is not None


for lang, ice, storm in (("en", r"\bic[ey]\b", r"thunder"), ("de", r"glatt", r"gewitter")):
    html = render(True, feels=COLD, hour=8, lang=lang, probs=RAIN_PM, codes=[0] * 14 + [66] * 4 + [0] * 6)
    expect(f"{lang}: freezing rain later, the ice warning", says(html, ice))
    html = render(True, feels=FEELS, hour=8, lang=lang, probs=RAIN_PM, codes=[0] * 14 + [95] * 4 + [0] * 6)
    expect(f"{lang}: a thunderstorm later, the storm wording", says(html, storm))
    html = render(True, feels=FEELS, hour=8, lang=lang, probs=RAIN_PM, codes=[0] * 14 + [61] * 4 + [0] * 6)
    expect(f"{lang}: plain rain, no ice or storm", not says(html, ice) and not says(html, storm))
    both = [0] * 14 + [66, 66, 95, 95] + [0] * 6
    expect(f"{lang}: freezing rain and thunder, the ice warning",
           says(render(True, feels=COLD, hour=8, lang=lang, probs=RAIN_PM, codes=both), ice))

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
