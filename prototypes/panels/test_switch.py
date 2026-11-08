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
           PANELS not in html and any(t.split(" || ")[0].replace("'", "&#39;") in html or t.split(" || ")[0] in html
                                      for t in TEXTS["en"]["facts"]["steady"] + TEXTS["en"].get("units_10", {}).get("steady", [])))

# Which sarcastic line (round 11): under the forecast line only follow-ups
# (flavour_10, by the day's mood); everywhere else standalone lines: now lines
# (now_10, by the Now drawing) and the day's standalone lines (alone_10);
# with two or three drawings and no words, the lines for the drawings too.
MOODS = ("wet", "warming", "cooling", "cold", "fickle", "hot", "snow", "nice", "cool", "evening", "night")
KEYS = ("now_10", "alone_10", "flavour_10", "flavour_vf_10", "units_10")
saved = {k: TEXTS["en"].get(k) for k in KEYS}
# Without units: a situation that has some shows one instead (tested below).
TEXTS["en"].pop("units_10", None)
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
de_units = TEXTS["de"].pop("units_10", None)
TEXTS["de"]["flavour_10"] = {g: ["AUS {GP}"] for g in GROUPS}
expect("German: the sweater is 'ihn'",
       all("AUS ihn" in render(True, lang="de", hour=h) for h in range(9, 13)))
TEXTS["de"]["flavour_10"] = de_saved
if de_units:
    TEXTS["de"]["units_10"] = de_units
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
    expect(f"{lang}: a Colorado morning, the forecast says shorts", re.search(r"shorts|kurze hose", words.lower()) is not None)
    expect(f"{lang}: a Colorado morning, no placeholder left", "{" not in words)
# Two hours of shorts weather from a cold start: long pants, as before.
BRIEF = [-3, -3, -4, -4, -4, -3, -2, 0, 4, 9, 14, 19, 22, 23, 25, 25, 23, 20, 18, 13, 9, 6, 4, 2]
html = render(True, feels=BRIEF, hour=7, nxt=True)
expect("two hours of shorts weather: long pants", "tee_shorts_dry" not in html and "shorts" not in re.sub(r"<[^>]+>|sprites/[a-z_]+", " ", html).lower())

# A cold front (24 C at 8 am, freezing by 3 pm): the drawing shows the
# shorts weather it is now; the forecast line suggests long pants.
NORTH = [20, 20, 19, 19, 19, 20, 21, 23, 24, 25, 25, 22, 14, 8, 4, 2, 1, 0, -1, -2, -2, -3, -3, -3]
for lang, word in (("en", "long pants"), ("de", "lange Hose")):
    html = render(True, feels=NORTH, hour=8, nxt=True, lang=lang)
    slugs = re.findall(r"([a-z_]+_dry)\.png", html)
    expect(f"{lang}: a cold front, the drawing as it is now", slugs[:1] == ["tee_pants_dry"])
    expect(f"{lang}: a cold front, the forecast says long pants", word in html)
# Dangerous heat (37 C at 9 am, 43 C by 2 pm): water and shade lead, not
# the evening's easing.
HEAT = [30, 29, 29, 28, 28, 29, 31, 33, 35, 37, 39, 41, 42, 43, 43, 42, 41, 39, 37, 35, 34, 33, 32, 31]
# Water leads (the owner reworded one German wording without „gefährlich“).
for lang, word in (("en", r"dangerous"), ("de", r"gefährlich|trink")):
    expect(f"{lang}: dangerous heat leads",
           all(re.search(word, render(True, feels=HEAT, hour=h, lang=lang).lower()) for h in (9, 12, 15)))
# Freezing rain in the window: the ice warning. A thunderstorm: the storm
# wording. Freezing rain wins when both come.
COLD = [-2] * 24
RAIN_PM = [0] * 14 + [80] * 4 + [0] * 6


def says(html, pattern):
    return re.search(pattern, re.sub(r"<[^>]+>", " ", html), re.I) is not None


for lang, ice, storm in (("en", r"\bic[ey]\b", r"thunder"), ("de", r"glatt|gefrierend", r"gewitter")):
    html = render(True, feels=COLD, hour=8, lang=lang, probs=RAIN_PM, codes=[0] * 14 + [66] * 4 + [0] * 6)
    expect(f"{lang}: freezing rain later, the ice warning", says(html, ice))
    html = render(True, feels=FEELS, hour=8, lang=lang, probs=RAIN_PM, codes=[0] * 14 + [95] * 4 + [0] * 6)
    expect(f"{lang}: a thunderstorm later, the storm wording", says(html, storm))
    html = render(True, feels=FEELS, hour=8, lang=lang, probs=RAIN_PM, codes=[0] * 14 + [61] * 4 + [0] * 6)
    expect(f"{lang}: plain rain, no ice or storm", not says(html, ice) and not says(html, storm))
    both = [0] * 14 + [66, 66, 95, 95] + [0] * 6
    expect(f"{lang}: freezing rain and thunder, the ice warning",
           says(render(True, feels=COLD, hour=8, lang=lang, probs=RAIN_PM, codes=both), ice))

# The jacket now, a little warmer around midday, the jacket again tonight:
# too small a rise to count as warming, but the drawings show the jacket
# off in between. Not "bring a jacket" (it's on), and the drawings' line
# never asks for an extra layer.
SMALL = [12] * 10 + [13, 13, 13, 13] + [12, 11, 10, 10, 9, 9, 8, 8, 8, 8]
for h in (8, 9):
    html = render(True, feels=SMALL, hour=h, nxt=True)
    slugs = re.findall(r"([a-z_]+_dry)\.png", html)
    words = re.sub(r"<[^>]+>", " ", html)
    expect(f"jacket, sweater, jacket at {h}:30: no 'bring a jacket'",
           slugs[:3] != ["jacket_dry", "sweater_dry", "jacket_dry"] or not re.search(r"(bring|take) a jacket", words))
saved_vf = TEXTS["en"].get("flavour_vf_11")
TEXTS["en"]["flavour_vf_11"] = {m: [f"VF {m.upper()}"] for m in ("cooling", "warming", "fickle", "wet", "snow")}
for h in (8, 9):
    html = render(False, feels=SMALL, hour=h, nxt=True, sarcasm="11")
    slugs = re.findall(r"([a-z_]+_dry)\.png", html)
    if len(slugs) >= 3 and slugs[0] == slugs[2]:
        expect(f"the same layer first and last at {h}:30: no 'extra layer' line", "VF COOLING" not in html)
TEXTS["en"]["flavour_vf_11"] = saved_vf

# {WHENSTOP}: when the rain falling now stops. Raining until 11, dry after:
# a wording with the stop time says it; with no dry break in the window
# (rain all day) such a wording is skipped for one without it.
saved_facts = TEXTS["en"]["facts"]
units_saved = TEXTS["en"].pop("units_10", None)  # the plain wordings, not a unit's
TEXTS["en"]["facts"] = dict(saved_facts, p_drier=["STOPS {WHENSTOP}."], p_stays_wet=["ALL DAY {WHENSTOP}.", "ALL DAY."])
WET_AM = [90] * 11 + [0] * 13
html = render(True, feels=STEADY, hour=8, probs=WET_AM, codes=[61] * 11 + [0] * 13)
expect("rain stopping: the stop time", says(html, r"STOPS (in three hours|around midday)\."))
html = render(True, feels=STEADY, hour=8, probs=[90] * 24, codes=[61] * 24)
expect("rain all day: no stop time, the other wording", says(html, r"ALL DAY\.") and "{WHENSTOP}" not in html)
TEXTS["en"]["facts"] = saved_facts
if units_saved:
    TEXTS["en"]["units_10"] = units_saved

# Special days: the owner cut the clock changes, the longest and shortest
# day, Mondays and Fridays (November 2026). Themes stay (below).

# Units (owner, October 2026): with sarcasm on, a forecast sentence and its
# joke written together. Where a situation has units, the screen shows one
# (forecast on, or What to Wear Next with one drawing); sarcasm off keeps
# the plain wording; the outfit alone keeps its standalone line; a rainy
# steady day takes the rain's unit.
saved_units = {k: TEXTS["en"].get(k) for k in ("units_10", "units_11")}
TEXTS["en"]["units_10"] = {"steady": ["UNIT FACT. || UNIT JOKE."] * 2, "p_wetter": ["UNIT RAIN {WHENP}. || RAIN JOKE."] * 2,
                           "steady_evening": ["ONE SENTENCE WITH BOTH."] * 2}


def words_of(html):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html))


expect("units: forecast on, a steady day", "UNIT FACT. UNIT JOKE." in words_of(render(True, feels=STEADY, hour=10)))
expect("units: one drawing, forecast off", "UNIT FACT. UNIT JOKE." in words_of(render(False, feels=STEADY, hour=10, nxt=True)))
expect("units: sarcasm off, the plain wording", "UNIT" not in render(True, feels=STEADY, hour=10, sarcasm="0"))
expect("units: the outfit alone, no unit", "UNIT" not in render(False, feels=STEADY, hour=10))
expect("units: a rainy steady day, the rain's unit",
       "UNIT RAIN this afternoon. RAIN JOKE." in words_of(render(True, feels=STEADY, hour=8, probs=[0] * 14 + [80] * 3 + [0] * 7,
                                                                  codes=[0] * 14 + [61] * 3 + [0] * 7)))
html = render(True, feels=STEADY, hour=19)
expect("units: one sentence with both, no second line", "ONE SENTENCE WITH BOTH." in words_of(html) and html.count("<p") == 1)
expect("units: a day without units for its situation works as before", "UNIT" not in render(True, hour=7))
TEXTS["en"]["units_10"]["steady"] = ["UNIT FACT. || UNIT JOKE."]
expect("units: one unit alone isn't used", "UNIT" not in render(True, feels=STEADY, hour=10))
TEXTS["en"]["units_10"]["steady"] = ["UNIT FACT. || UNIT JOKE."] * 2
for k in ("w_scarf", "w_coat", "w_jacket", "w_hoodie", "w_water", "shorts_early", "arc_warmer"):
    TEXTS["en"]["units_10"][k] = ["LAYER {WHEN}. || LAYER JOKE {WHEN}."] * 2
html = render(True, hour=7)
expect("units: a layer day's unit, its time words filled in both halves",
       "LAYER JOKE " in html and "{" not in words_of(html))
for k in ("w_scarf", "w_coat", "w_jacket", "w_hoodie", "w_water", "shorts_early", "arc_warmer"):
    del TEXTS["en"]["units_10"][k]

# A theme day comes with its fixed sentence (facts.steady_special), never
# a unit's or a separately picked one; on a cold or hot day, or a rainy one,
# the weather's own unit has the say (owner, round 17). Cut special days
# never show, even with lines in the texts (owner, November 2026).
saved_fl = TEXTS["en"]["flavour_10"]
TEXTS["en"]["flavour_10"] = dict(saved_fl, theme_xmas=["XMAS A.", "XMAS B.", "XMAS C."],
                                 day_monday=["MONDAY A.", "MONDAY B.", "MONDAY C."],
                                 day_dst_fall=["CLOCKS A.", "CLOCKS B."], day_longest=["LONGEST A.", "LONGEST B."])
TEXTS["en"]["units_10"]["steady_cold"] = ["COLD UNIT. || COLD JOKE."] * 2
special = TEXTS["en"]["facts"]["steady_special"][0]
for DATE, label in (("2026-10-19", "a Monday"), ("2026-10-25", "the clock change"), ("2027-06-21", "the longest day")):
    html = render(True, feels=STEADY, hour=8)
    expect(f"cut special day ({label}): no day line, the unit", "MONDAY" not in html and "CLOCKS" not in html
           and "LONGEST" not in html and "UNIT FACT. UNIT JOKE." in words_of(html))
DATE = "2026-12-25"
html = render(True, feels=STEADY, hour=8)
expect("theme day, forecast on: the fixed sentence and the day's line",
       special in html and "XMAS" in html and "UNIT" not in html)
html = render(False, feels=STEADY, hour=8, nxt=True)
expect("theme day, one drawing: the fixed sentence and the day's line", special in html and "XMAS" in html)
html = render(True, feels=[0] * 24, hour=8)
expect("theme day on a cold day: the cold unit", "COLD UNIT. COLD JOKE." in words_of(html) and "XMAS" not in html)
html = render(True, feels=STEADY, hour=8, probs=[0] * 14 + [80] * 3 + [0] * 7, codes=[0] * 14 + [61] * 3 + [0] * 7)
expect("theme day on a rainy day: the rain's unit", "RAIN JOKE." in words_of(html) and "XMAS" not in html)
DATE = "2026-06-10"
TEXTS["en"]["flavour_10"] = saved_fl
for k, v in saved_units.items():
    if v is None:
        TEXTS["en"].pop(k, None)
    else:
        TEXTS["en"][k] = v

# A texts file older than the markup (the texts URL behind: a fork's pinned
# commit, or jsDelivr serving an old @main for a while after a release): no
# now or day pools, its lines by the day's mood, and no "cooling" ones. A
# sarcastic line still shows on every screen.
import copy
OLD = copy.deepcopy(TEXTS["en"])
for k in [k for k in OLD if k.startswith(("now_", "alone_"))]:
    del OLD[k]
for level in ("10", "11"):
    OLD[f"flavour_{level}"] = {m: [f"OLD {m.upper()}"] for m in ("nice", "cool", "warming", "cold", "hot", "wet", "snow", "fickle", "evening", "night")}
saved_en = TEXTS["en"]
TEXTS["en"] = OLD
pairs = [(render(fc, feels=f, hour=h, nxt=nx), render(fc, feels=f, hour=h, nxt=nx, sarcasm="0"))
         for f in (FEELS, STEADY, CO, NORTH) for h in (7, 10, 13, 19)
         for fc, nx in ((False, True), (True, True), (True, False), (False, False))]
expect("an older texts file: a sarcastic line on every screen", all(on != off for on, off in pairs))
TEXTS["en"] = saved_en

# Nice weather (owner, October 2026: 15 C and cloudy said „Traumwetter“):
# T-shirt weather under a clear or partly cloudy sky; not sweater weather,
# not overcast.
saved_now = TEXTS["en"].get("now_10")
saved_alone = TEXTS["en"].get("alone_10")
TEXTS["en"]["now_10"] = {m: [f"MOOD {m.upper()}."] for m in MOODS}
TEXTS["en"].pop("alone_10", None)
def now_line(feels, code):
    return words_of(render(False, feels=[feels] * 24, hour=11, codes=[code] * 24))
expect("15 C and overcast: not nice", "MOOD NICE" not in now_line(15, 3))
expect("15 C and sunny: not nice (sweater weather)", "MOOD NICE" not in now_line(15, 0))
expect("22 C and overcast: not nice", "MOOD NICE" not in now_line(22, 3))
expect("22 C and fog: not nice", "MOOD NICE" not in now_line(22, 45))
expect("22 C, partly cloudy: nice", "MOOD NICE" in now_line(22, 2))
TEXTS["en"]["now_10"] = saved_now
if saved_alone is not None:
    TEXTS["en"]["alone_10"] = saved_alone

# The owner's notes (round 22): a known stop time means only the wordings
# that say it; "{AM}" wordings only before noon.
saved_facts = TEXTS["en"]["facts"]
units_saved = TEXTS["en"].pop("units_10", None)
TEXTS["en"]["facts"] = dict(saved_facts, p_drier=["STOPS {WHENSTOP}.", "STOPS LATER."],
                            steady=["{AM}MORNING ONLY.", "ANY TIME."])
WET_AM = [90] * 11 + [0] * 13
stops = {words_of(render(True, feels=STEADY, hour=h, probs=WET_AM, codes=[61] * 11 + [0] * 13)) for h in (7, 8, 9)}
expect("stop time known: never the vague wording", not any("STOPS LATER" in s for s in stops) and any("STOPS" in s for s in stops))
mornings = [words_of(render(True, feels=STEADY, hour=h)) for h in range(6, 12)]
afternoons = [words_of(render(True, feels=STEADY, hour=h)) for h in range(12, 17)]
expect("{AM} wording: shows in the morning", any("MORNING ONLY." in s for s in mornings) and not any("{AM}" in s for s in mornings))
expect("{AM} wording: never after noon", not any("MORNING ONLY" in s for s in afternoons) and all("ANY TIME." in s for s in afternoons))
TEXTS["en"]["facts"] = saved_facts
if units_saved:
    TEXTS["en"]["units_10"] = units_saved

# The order (owner, October 2026): on a day that changes and rains, the
# sentences go in the order things happen; the unit goes with the last one.
saved_facts, saved_u = TEXTS["en"]["facts"], TEXTS["en"].get("units_10")
temp_keys = [k for k in saved_facts if k[:2] in ("c_", "w_") or k.startswith(("arc_", "shorts_", "pants_"))]
TEXTS["en"]["facts"] = dict(saved_facts, p_drier=["RAINSTOP {WHENSTOP}."], p_wetter=["RAINCOMES {WHENP}."],
                            **{k: ["TEMPCHANGE {WHEN}."] for k in temp_keys})
TEXTS["en"]["units_10"] = dict(p_drier=["RAINSTOP {WHENSTOP}. || RAINJOKE.", "RAINSTOP {WHENSTOP}. || RAINJOKE."],
                               p_wetter=["RAINCOMES {WHENP}. || RAINJOKE.", "RAINCOMES {WHENP}. || RAINJOKE."],
                               **{k: ["TEMPCHANGE {WHEN}. || TEMPJOKE.", "TEMPCHANGE {WHEN}. || TEMPJOKE."] for k in temp_keys})
COOLING = [12] * 15 + [8, 6, 4, 2, 1, 0, 0, 0, 0]
w = words_of(render(True, feels=COOLING, hour=8, probs=WET_AM, codes=[61] * 11 + [0] * 13))
expect("raining now, colder later: rain sentence first, the temperature's joke last",
       w.find("RAINSTOP") < w.find("TEMPCHANGE") and "TEMPJOKE" in w and "RAINJOKE" not in w)
w = words_of(render(True, feels=COOLING, hour=8, probs=[0] * 20 + [90] * 4, codes=[0] * 20 + [61] * 4))
expect("colder first, rain later: temperature sentence first, the rain's joke last",
       0 <= w.find("TEMPCHANGE") < w.find("RAINCOMES") and "RAINJOKE" in w and "TEMPJOKE" not in w)
TEXTS["en"]["facts"] = saved_facts
if saved_u is not None:
    TEXTS["en"]["units_10"] = saved_u

# A rain transition must not resize just the wet outfits within a row.
for view in VIEWS:
    for forecast in (False, True):
        html = render(forecast, view, nxt=True,
                      probs=[0] * 13 + [90] * 11,
                      codes=[0] * 13 + [61] * 11)
        images = re.findall(r'<img class="([^"]*)" src="[^"]*/([^"/]+)\.png" alt="(?!Error)[^"]*">', html)
        expect(f"mixed day has dry and wet outfits ({view}, forecast={forecast})",
               any(slug.endswith('_dry') for _, slug in images)
               and any(slug.endswith('_rain') for _, slug in images))
        expect(f"mixed day uses one image size for the whole row ({view}, forecast={forecast})",
               len({classes for classes, _ in images}) == 1)
        if view == "half_vertical":
            dry_html = render(forecast, view, nxt=True)
            dry_images = re.findall(r'<img class="([^"]*)" src="[^"]*/([^"/]+)\.png" alt="(?!Error)[^"]*">', dry_html)
            expect(f"dry and mixed forecasts exercise three panels (forecast={forecast})",
                   len(images) == len(dry_images) == 3)
            expect(f"weather does not change the row's image scale (forecast={forecast})",
                   {classes for classes, _ in images} == {classes for classes, _ in dry_images})

# Framework classes only: no CSS of our own anywhere in the views.
for view in VIEWS:
    src = (BUILD / "views" / f"{view}.liquid").read_text(encoding="utf-8")
    expect(f"no <style> or style= in {view}", "<style" not in src and " style=" not in src)
html = render(False, lang="de", nxt=True)
expect("German drawings say 'ab'", ">ab " in html and ">Jetzt<" in html)

# The evening (prototypes/panels/evening.liquid): from 8 pm, tonight |
# tomorrow, with tomorrow in the payload (forecast_days=2). Tomorrow here:
# cold early, warmer from late morning, rain 1 pm to 5 pm.
TMR = [-1, -1, -1, -1, -1, -1, 0, 1, 3, 4, 6, 8, 9, 9, 9, 9, 8, 7, 6, 6, 5, 5, 5, 5]
TMR_P = [0] * 13 + [80] * 4 + [0] * 7


def render2(hour=20, days=2, ho=None, tmr=None, tmr_p=None, view="full", sarcasm="10", lang="en", nxt=True, forecast=True):
    today = [8] * 6 + [9, 10, 11, 12, 12, 12, 12, 12, 12, 11, 10, 9, 9, 8, 8, 8, 8, 8]
    feels = today + (tmr or TMR)
    probs = [0] * 24 + (tmr_p if tmr_p is not None else TMR_P)
    d = dt.date.fromisoformat(DATE)
    d2 = d + dt.timedelta(days=1)
    times = [f"{d}T{h:02d}:00" for h in range(24)] + [f"{d2}T{h:02d}:00" for h in range(24)]
    n = 24 * days
    data = {"utc_offset_seconds": OFFSET, "timezone": "Europe/Vienna",
            "current": {"time": f"{DATE}T{hour:02d}:30", "temperature_2m": feels[hour],
                        "apparent_temperature": feels[hour], "weather_code": 0},
            "hourly": {"time": times[:n], "temperature_2m": feels[:n], "apparent_temperature": feels[:n],
                       "precipitation_probability": probs[:n], "weather_code": [61 if p else 0 for p in probs][:n]}}
    cfg = {"language": lang, "sarcasm_level": sarcasm, "lat_lon": "48.2,16.4", "show_bottom_bar": "on",
           "show_future_suggestions": forecast, "what_to_wear_next": nxt}
    if ho is not None:
        cfg["head_out_time"] = ho
    ts = calendar.timegm((d.year, d.month, d.day, hour, 30, 0)) - OFFSET
    ctx = {"trmnl": {"plugin_settings": {"custom_fields_values": cfg}, "system": {"timestamp_utc": ts},
                     "user": {"utc_offset": OFFSET}, "device": {"width": 800}},
           "IDX_0": data, "IDX_1": TEXTS[lang]}
    return VIEWS[view].render(**ctx)


EVE = 'data-wtw="evening"'
for view in VIEWS:
    html = render2(view=view)
    expect(f"8:30 pm with tomorrow in the payload: the evening ({view})", EVE in html and "Tomorrow · Thu" in html
           and ">Tonight<" in html)
    expect(f"7:30 pm: still today ({view})", EVE not in render2(hour=19, view=view))
    expect(f"no tomorrow in the payload: still today ({view})", EVE not in render2(days=1, view=view))
html = render2()
expect("tomorrow: the coldest outfit 6 to 9 am, then the rain", re.search(r"coat_dry\.png.*jacket_rain\.png", html, re.S) is not None
       and ">6–9\u00a0am<" in html and ">from 1\u00a0pm<" in html and "rain from 1\u00a0pm" in html)
expect("evening joke at On", "Two forecasts" in html)
expect("no evening joke at Off", "Two forecasts" not in render2(sarcasm="0"))
expect("evening joke at 11", "Morning-you" in render2(sarcasm="11"))
expect("tonight: what you have on, 'now'", ">now<" in html)
ho6, ho9 = render2(ho="6", tmr_p=[0] * 24), render2(ho="9", tmr_p=[0] * 24)
expect("out at 6 am: the winter coat first", ">6\u00a0am<" in ho6 and re.search(r"Tomorrow · Thu.*?coat_dry", ho6, re.S))
expect("out at 9 am: the jacket first", ">9\u00a0am<" in ho9 and re.search(r"Tomorrow · Thu.*?jacket_dry", ho9, re.S))
steady = render2(tmr=[15] * 24, tmr_p=[0] * 24)
expect("a steady tomorrow: one drawing, all day", ">all day<" in steady and "one outfit works all day" in steady)
nodraw = render2(nxt=False)
expect("drawings off: no tonight, one drawing of tomorrow", EVE in nodraw and ">Tonight<" not in nodraw
       and nodraw.count('.png"') == 1)
expect("drawings and words off: today as before", EVE not in render2(nxt=False, forecast=False))
de = render2(lang="de")
expect("German evening", "Morgen · Do" in de and ">Heute Abend<" in de and "ab 13\u00a0Uhr Regen" in de)

if failures:
    print("FAILED:\n  " + "\n  ".join(failures))
    sys.exit(1)
print("all good: Forecast shows the words, What to Wear Next the drawings, both together, old values keep working")
