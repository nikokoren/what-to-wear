#!/usr/bin/env python3
"""
Round 39 (November 2026): the two situations the beta review added, in
both languages, written by shape (docs/SHAPES.md) as the first round of
that method:

  - snowing now, turning to rain later (facts.p_turns_rain): more plain
    wordings, and units ("fact || joke") at On and 11;
  - tomorrow with one outfit and possible rain, on the evening screen
    (evening.facts.tmr_maybe): more plain wordings, and the evening line
    at On and 11 (evening.jokes_10/11.maybe; without them the markup
    borrows the rain lines, which promise rain the forecast doesn't).

The wordings already in the texts are voted too ("live"); a veto takes
one out, never a situation's last.

    python3 review/rounds/make_round39.py

Reads review/rounds/2026-11-turns/<lang>.raw.json (every line written,
the critic's cuts marked with the rule), writes review/rounds/2026-11-turns.json
and review/rounds/2026-11-turns/critic.md. After the vote, build_pools.py
(day) and apply_evening.py (evening) put the kept lines in.
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROUND = "2026-11-turns"
LEVEL = {"10": "On", "11": "11"}
FILLS = {"en": {"{WHENP}": "around midday"}, "de": {"{WHENP}": "gegen Mittag"}}
FILLS_ALT = {"en": {"{WHENP}": "in two hours"}, "de": {"{WHENP}": "in zwei Stunden"}}
SHAPE = {"screen": "the screen's own limits", "credit": "taking credit, denying blame", "sting": "ends on a sting word",
         "habit": "your habits, predicted", "quote": "your words thrown back", "jab": "a jab at you",
         "parent": "the parent's scold", "self": "the Grantler about himself", "sigh": "the Grantler's sigh",
         "people": "other people", "simile": "a simile", "other": "outside the strong shapes, for variety"}
DAY = "Snowing now, turning to rain {WHENP}: the drawing is in snow now, in rain later."
EVE = "Evening screen, 8 pm to midnight. Tomorrow one outfit works all day (one drawing, 'all day'), and rain is possible but never likely: no umbrella in the drawing."


def main():
    rows, cuts = [], []
    for lang in ("en", "de"):
        raw = json.loads((HERE / ROUND / f"{lang}.raw.json").read_text(encoding="utf-8"))
        kept = lambda items: [x for x in items if not x.get("cut")]
        for x in raw["facts"]["p_turns_rain"] + raw["facts"]["evening_tmr_maybe"] + sum(raw["units"].values(), []) \
                + sum(raw["evening_jokes"].values(), []):
            if x.get("cut"):
                cuts.append((lang, x.get("text") or x["joke"], x["cut"]))
        turns = kept(raw["facts"]["p_turns_rain"])
        live_turns = [x["text"] for x in turns if x.get("live")]
        for x in turns:
            rows.append({"lang": lang, "path": "fact_0.p_turns_rain", "text": x["text"], "role": "fact",
                         "sprite": "coat_snow", "fills": FILLS[lang], "fillsAlt": FILLS_ALT[lang],
                         "batch": "Snow turns to rain: forecast", "new": not x.get("live"),
                         "meaning": DAY + " The forecast sentence, at every setting.",
                         "hint": "In the texts since the beta review, not voted yet" if x.get("live") else ""})
        for level, items in raw["units"].items():
            for x in kept(items):
                fact = live_turns[x["fact"] % len(live_turns)]
                rows.append({"lang": lang, "path": f"unit_{level}.p_turns_rain", "text": f"{fact} || {x['joke']}",
                             "role": "unit", "sprite": "coat_snow", "fills": FILLS[lang], "fillsAlt": FILLS_ALT[lang],
                             "batch": f"Snow turns to rain: {LEVEL[level]}", "new": True,
                             "meaning": DAY + f" At {LEVEL[level]}: the sentence and its joke as one.",
                             "hint": "Shape: " + SHAPE[x["shape"]]})
        maybe = kept(raw["facts"]["evening_tmr_maybe"])
        for x in maybe:
            rows.append({"lang": lang, "path": "fact_0.evening_tmr_maybe", "text": x["text"], "role": "fact",
                         "sprite": "jacket_dry", "batch": "Tomorrow, rain possible: forecast", "new": not x.get("live"),
                         "meaning": EVE + " Tomorrow's sentence.",
                         "hint": "In the texts since the beta review, not voted yet" if x.get("live") else ""})
        shown = [x["text"] for x in maybe if x.get("live")]
        for level, items in raw["evening_jokes"].items():
            for n, x in enumerate(kept(items)):
                rows.append({"lang": lang, "path": f"flavour_{level}.evening_maybe", "text": x["joke"], "role": "flavour",
                             # Without tomorrow's sentence the screen shows no rain at all: these need it.
                             "evtag": "{S}", "sprite": "jacket_dry", "fact": shown[n % len(shown)],
                             "batch": f"Tomorrow, rain possible: {LEVEL[level]}", "new": True,
                             "meaning": EVE + f" At {LEVEL[level]}: the line under tomorrow's sentence.",
                             "hint": "Shape: " + SHAPE[x["shape"]] + " · Only when tomorrow's sentence shows"})
    (HERE / f"{ROUND}.json").write_text(json.dumps({"round": ROUND, "idPrefix": "tr", "lines": rows},
                                                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    out = ["# Round 39: the critic's cuts", "",
           "Generated by `make_round39.py` from the raw files. Every line the",
           "writer wrote is in `<lang>.raw.json`; these were cut before the vote,",
           "by the rules in `docs/CRITIC.md`.", ""]
    for lang, text, why in cuts:
        out.append(f"- **{lang}** {text}  \n  _{why}_")
    (HERE / ROUND / "critic.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    for l in ("en", "de"):
        mine = [r for r in rows if r["lang"] == l]
        by = {}
        for r in mine:
            by[r["batch"]] = by.get(r["batch"], 0) + 1
        print(l, len(mine), by)
    print("cut before the vote:", len(cuts))


if __name__ == "__main__":
    main()
