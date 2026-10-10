#!/usr/bin/env python3
"""
Round 8, the re-read: every line the beta ships, back on the review page,
after the owner saw the first ones on a device and wasn't sure they work.

    python3 review/rounds/make_round8.py

Every fact wording, every sarcastic line (On and 11, moods and theme
days) and every topical line, as they are now in
prototypes/fact-flavour/lang/. Each row is shown on the screen it belongs
to: a fact with its drawing and a sarcastic line under it, a sarcastic
line under the fact of a typical day for its mood. The page lets the owner
change a wording in place; the time words and garments are filled in live
from the "fills" each row carries.

Ids carry the prefix "rr", so a line voted in an earlier round is rated
again here instead of showing its old verdict. After the vote,
build_pools.py applies the round last: a veto takes the line out, an edit
replaces it.
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
ROUND = "2026-10-reread"
PROTO = REPO / "prototypes" / "fact-flavour" / "lang"

# The drawing for each fact, the mood whose sarcastic line shows under it,
# and what the situation is.
FACT_CTX = {
    "steady": ("sweater_dry", "nice", "Nothing changes all day. About half of all screens; also Visual Forecast's \"works all day\"."),
    "steady_evening": ("jacket_dry", "evening", "Nothing changes, from 17:00."),
    "steady_hot": ("heat_dry", "hot", "Steady heat, before 17:00."),
    "steady_cold": ("coat_dry", "cold", "Steady cold (coat or more), before 17:00."),
    "w_scarf": ("bundled_dry", "warming", "Warms up: hat, scarf and gloves come off, the coat stays."),
    "w_coat": ("coat_dry", "warming", "Warms up: the winter coat comes off."),
    "w_jacket": ("jacket_dry", "warming", "Warms up: the jacket comes off."),
    "w_hoodie": ("sweater_dry", "warming", "Warms up: the sweater comes off."),
    "w_water": ("tee_pants_dry", "hot", "Climbs into heat. Nothing left to take off."),
    "c_scarf": ("coat_dry", "cooling", "Cools to bundled: hat, scarf and gloves needed later."),
    "c_coat": ("jacket_dry", "cooling", "Cools to coat weather: the winter coat needed later."),
    "c_jacket": ("sweater_dry", "cooling", "Cools to jacket weather: a jacket needed later."),
    "c_hoodie": ("tee_pants_dry", "cooling", "Cools to sweater weather: a sweater needed later."),
    "c_relief": ("heat_dry", "hot", "The heat breaks, but it stays warm. Nothing to bring."),
    "arc_warmer": ("jacket_dry", "warming", "The jacket comes off and stays off: the evening is still warmer than now."),
    "arc_level": ("jacket_dry", "fickle", "The jacket comes off, and is wanted back in the evening."),
    "arc_colder": ("jacket_dry", "fickle", "The jacket comes off; the evening is colder than now: jacket back, plus a layer."),
    "shorts_early": ("tee_shorts_dry", "warming", "Shorts drawn on a cool morning that turns into shorts weather."),
    "p_wetter": ("jacket_dry", "wet", "Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence."),
    "p_wetter_long": ("jacket_dry", "wet", "Rain later, and it stays. Shown alone; after a change, it follows that sentence."),
    "p_wetter_maybe": ("jacket_dry", "wet", "Rain possible later, not likely. Shown alone; after a change, it follows that sentence."),
    "p_stays_wet": ("jacket_rain", "wet", "Raining now and all day."),
    "p_drier": ("jacket_rain", "wet", "Raining now, stops later."),
    "p_wet_again": ("jacket_rain", "wet", "Raining now, stops, comes back."),
    "p_snow_coming": ("coat_dry", "snow", "Snow later."),
    "p_stays_wet_snow": ("coat_snow", "snow", "Snowing now and all day."),
    "p_drier_snow": ("coat_snow", "snow", "Snowing now, stops later."),
    "p_wet_again_snow": ("coat_snow", "snow", "Snowing now, stops, comes back."),
}
# The screen a sarcastic line sits on: drawing, the fact above it, the mood.
MOOD_CTX = {
    "nice": ("sweater_dry", ["steady"], "A steady, pleasant day."),
    "cool": ("jacket_dry", ["steady"], "A steady, cool jacket day. Also drawn on warming and cooling days."),
    "warming": ("jacket_dry", ["w_jacket"], "An ordinary day that warms up: a layer comes off and stays off."),
    "cooling": ("sweater_dry", ["c_jacket"], "An ordinary day that cools down: a layer is needed later."),
    "cold": ("coat_dry", ["steady_cold"], "Cold: winter coat or more."),
    "hot": ("heat_dry", ["steady_hot"], "Heat, or climbing into it."),
    "wet": ("jacket_dry", ["p_wetter"], "Rain at some point: coming, possible, or stopping."),
    "snow": ("coat_dry", ["p_snow_coming"], "Snow coming or falling."),
    "fickle": ("jacket_dry", ["arc_level"], "Warms up, then cools enough to want the layer back."),
    "evening": ("jacket_dry", ["steady_evening"], "A steady evening, 18:00 to 22:00. People check before going out."),
    "night": ("jacket_dry", ["steady_evening"], "A steady night, from 22:00. Bed jokes allowed."),
    "theme_xmas": ("coat_dry", ["steady_cold"], "Christmas: 24 to 26 December, on top of the day's mood."),
}
GARMENT = 2  # the jacket: the arc rows draw it


def fills(lang, text, base, facts, alt=False):
    """Placeholder -> words, the way the markup fills them on a typical day."""
    b, rel = base["buckets"], base["relative"]
    f = {"{WHEN2}": b[3], "{WHEN}": b[1] if "{WHEN2}" in text else b[2], "{WHENP}": b[2],
         "{G}": facts["garments"][GARMENT], "{GP}": facts["garments_pron"][GARMENT]}
    if "garments_verb" in facts:
        f["{GV}"] = facts["garments_verb"][GARMENT]
    if alt:  # the same day with the change two hours away
        if "{WHEN2}" not in text:
            f["{WHEN}"] = rel[1]
        f["{WHENP}"] = rel[1]
    return f


def fill(text, f):
    for k in ("{WHEN2}", "{WHEN}", "{WHENP}", "{GV}", "{GP}", "{G}"):
        text = text.replace(k, f.get(k, ""))
    return " ".join(text.split())


def sentence_case(text):
    out, up = [], True
    for i, ch in enumerate(text):
        out.append(ch.upper() if up and ch.isalpha() else ch)
        if ch.isalpha():
            up = False
        if ch in ".!?" and text[i + 1:i + 2] == " ":
            up = True
    return "".join(out)


def earlier_votes():
    votes = {}
    for lang in ("en", "de"):
        path = REPO / "review" / "decisions" / f"{lang}.json"
        for d in json.loads(path.read_text(encoding="utf-8")).values():
            if d.get("verdict"):
                votes[(lang, d["text"])] = f"{d['verdict']} in {d.get('round') or 'an early review'}"
    return votes


def main():
    earlier = earlier_votes()
    lines = []
    for lang in ("en", "de"):
        doc = json.loads((PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        facts = doc["facts"]

        def first_fact(key):
            text = facts[key][0]
            return sentence_case(fill(text, fills(lang, text, base, facts)))

        def row(path, text, batch, **ctx):
            r = {"lang": lang, "path": path, "text": text, "batch": batch, **ctx}
            if (lang, text) in earlier:
                r["earlier"] = earlier[(lang, text)]
            lines.append(r)

        for key, (sprite, mood, meaning) in FACT_CTX.items():
            pool = doc["flavour_10"].get(mood) or []
            for text in facts.get(key, []):
                row(f"fact_0.{key}", text, "Facts", role="fact", sprite=sprite,
                    fills=fills(lang, text, base, facts), fillsAlt=fills(lang, text, base, facts, alt=True),
                    under=pool[0] if pool else "",
                    meaning="Fact line, shown at every sarcasm level. " + meaning)
        for level in ("10", "11"):
            for mood, texts in doc[f"flavour_{level}"].items():
                sprite, keys, meaning = MOOD_CTX.get(mood, ("jacket_dry", ["steady"], ""))
                fact = " ".join(first_fact(k) for k in keys)
                for text in texts:
                    row(f"flavour_{level}.{mood}", text, "Sarcasm", role="flavour", sprite=sprite, fact=fact,
                        meaning=f"Sarcastic line at {'On' if level == '10' else '11'}. {meaning}")
            seen = set()
            for t in doc.get(f"topical_{level}", []):
                if t["text"] in seen:
                    continue
                seen.add(t["text"])
                windows = "; ".join(f"{w['from']} to {w['until']}" + (f" in {w['region']}" if w.get("region") else "")
                                    for w in doc[f"topical_{level}"] if w["text"] == t["text"])
                row(f"topical_{level}.topical", t["text"], "Topical", role="flavour", sprite="sweater_dry",
                    fact=first_fact("steady"),
                    meaning=f"Topical line at {'On' if level == '10' else '11'}, about one day in three: {windows}.")

    out = {"round": ROUND, "idPrefix": "rr", "lines": lines}
    path = HERE / f"{ROUND}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in lines:
        by[(r["lang"], r["batch"])] = by.get((r["lang"], r["batch"]), 0) + 1
    print(f"{len(lines)} lines -> {path.relative_to(REPO)}: " + ", ".join(f"{l} {b} {n}" for (l, b), n in sorted(by.items())))


if __name__ == "__main__":
    main()
