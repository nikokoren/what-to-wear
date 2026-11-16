#!/usr/bin/env python3
"""
Round 12, follow-ups (October 2026).

    python3 review/rounds/make_round12.py

Round 11's lesson (docs/BRIEF.md): under the forecast line a sarcastic
line has to build on it; everywhere else it has to stand alone. The
markup now picks follow-ups by what the forecast line says (block.liquid,
fu_key), in ten groups:

    rain     there's a shower / it rains all day / the rain stops: the umbrella
    snow     it starts snowing / snows all day / the snow stops
    off      a layer comes off later (and stays off)
    on       a layer is needed later
    offon    off, then back on
    hot      it stays hot, gets hot, or eases a little: water, shade
    steady   what you're wearing works all day
    cold     it stays this cold all day
    evening  works for the rest of the evening
    night    the same, from 22:00

This round:
- "Follow-up: <group>": new follow-ups, each under its forecast line.
- "Write new": new lines for round 11's "Write new" spots ("answers").
- "Months?": seasonal lines; "Only in these months" tags them, "All
  year" leaves them be.

build_pools.py applies it (apply_follow): kept new lines go in, kept
month questions tag their line.
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402
import make_round11 as r11  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-10-follow"
LEVEL = {"10": "On", "11": "11"}

# The forecast line a group's follow-ups sit under, and its drawing.
GROUP_CTX = {
    "rain": ("p_wetter", "jacket_dry", "a rain line: shower later, rain all day, rain stopping, or rain now"),
    "snow": ("p_snow_coming", "coat_dry", "a snow line: snow later, all day, or stopping"),
    "off": ("w_jacket", "jacket_dry", "a layer comes off later (jacket, sweater, coat, scarf) and stays off"),
    "on": ("c_jacket", "sweater_dry", "a layer is needed later"),
    "offon": ("arc_level", "jacket_dry", "a layer comes off, then back on in the evening"),
    "hot": ("steady_hot", "heat_dry", "heat: stays hot, gets hot later, or eases a little; water and shade"),
    "steady": ("steady", "tee_pants_dry", "what you're wearing works all day"),
    "cold": ("steady_cold", "coat_dry", "it stays this cold all day"),
    "evening": ("steady_evening", "jacket_dry", "18:00 to 22:00: what you're wearing works for the rest of the evening"),
    "night": ("steady_evening", "jacket_dry", "from 22:00: the same line, late"),
}

# (text, answers) or text. Answers: round 11 "Write new" ids this line answers.
FOLLOW = {
    "en": {
        "10": {
            "rain": ["I'd hold it for you, but I'm not that kind of screen.",
                     "Bring it back, too. I'm keeping count.",
                     "Forecast delivered. What happens to the umbrella next is on you.",
                     "That's my rain forecast. The umbrella's forecast is less certain."],
            "snow": ["Snow on schedule. I'd take a bow if I had a waist.",
                     "Everyone will act shocked anyway. I'm used to it."],
            "off": ["Act surprised when it does. I like an audience.",
                    "And it'll spend the afternoon where they all do: over one arm.",
                    ("Peeling off a layer: the closest today gets to drama.", ["al-en-f0292af384b7"])],
            "on": [("Shame. It was just getting comfortable.", ["al-en-deb8fe54c5a7"]),
                   "You'll forget it. Then you'll remember me.",
                   "Pack it now, feel smug later. I'll feel smugger."],
            "offon": [("Off, on. The layer gets more exercise than most people today.", ["al-en-fa88b0de371e"]),
                      "Don't lose it in between. Many have."],
            "hot": ["Water and shade are on you. Staying cool is my thing.",
                    "I'd come along, but I'm already the coolest thing in the house.",
                    "Stay in the shade. It's where all the good screens hang out."],
            "steady": [("Get dressed once and you're done. I do the same, permanently.", ["al-en-2f51a68cfc40"]),
                       ("Nothing to update. I'll just stand here being right.", ["al-en-34807153d5d8"]),
                       ("One outfit, all day, no plot twists. Restful, isn't it?", ["al-en-366e6ff11ab9"])],
            "cold": ["All day. I checked twice, out of pure spite.",
                     "I'd soften it, but I only do accurate."],
            "evening": ["Same outfit, new lighting. Evenings are generous like that.",
                        "Whatever the evening brings, the outfit won't be the problem."],
            "night": ["And 'the rest of the evening' should be about five minutes now.",
                      "It also works for bed, I'm told."],
        },
        "11": {
            "rain": ["Bring it, and maybe bring it home this time.",
                     "You'll leave it by the door anyway. I'll know.",
                     "I said umbrella. You heard 'my hood will do'."],
            "snow": ["You'll still act like it's the first snow ever.",
                     "And you'll still call it 'unexpected'."],
            "off": ["You'll carry it around all afternoon like a trophy."],
            "on": ["Bring it. Or practise your 'I'm not cold' face for later."],
            "offon": ["You'll be too warm at noon and blame me tonight."],
            "hot": ["You'll forget the water and blame the weather.",
                    "Shade, water, fewer complaints about the heat. Pick two."],
            "steady": [("Dressed right all day. Enjoy it, it won't happen often.", ["al-en-11e1b81980e7"]),
                       "For once you got it right on the first try."],
            "cold": ["All day. So no, you can't wait it out.",
                     "You'll still check again in an hour, hoping I changed my mind."],
            "evening": ["Your outfit's ready for the evening. Are you?"],
            "night": ["The rest of the evening. Not the rest of the night. Bed.",
                      "It works for the couch too, which is where this is going."],
        },
    },
    "de": {
        "10": {
            "rain": ["Und bring ihn auch wieder heim. Im Fundbüro liegen schon genug.",
                     "Ich sag's nur. Nass werden darfst du trotzdem selber.",
                     "Kapuze zählt nicht. Hab ich extra so gesagt."],
            "snow": ["Und morgen sind trotzdem wieder alle überrascht.",
                     "Angesagt hab ich's. Den Winterdienst ruf ich trotzdem nicht an."],
            "off": [("Und dann trägt wieder jeder alles überm Arm spazieren.", ["al-de-de2d9309fe1c"]),
                    ("Ein Grund zum Meckern weniger. Ich find schon einen neuen.", ["al-de-ee48eb1587c6"]),
                    "Und dann liegt's wieder in irgendeinem Büro rum."],
            "on": ["Und nein, wärmer wird's nicht, nur weil du's nicht glauben willst.",
                   "Abends hat's dann wieder keiner dabei. Außer dir, hoffentlich."],
            "offon": ["An, aus, an. Wie die Heizung im Büro.",
                      "Also schön dabeibehalten. Nicht wieder irgendwo liegen lassen."],
            "hot": ["Und trotzdem stehen gleich wieder alle in der prallen Sonne vor der Eisdiele.",
                    "Wasser, hab ich gesagt. Bier zählt nicht."],
            "steady": ["Einmal angezogen, fertig. Wenn doch alles so einfach wär.",
                       "Heut gibt's nicht mal was zum Umziehen. Langweilig."],
            "cold": ["Den ganzen Tag. Da hilft auch kein Jammern. Ich hab's probiert.",
                     "Und morgen vermutlich auch. Aber das sag ich erst morgen."],
            "evening": ["Am Outfit liegt's also nicht, wenn der Abend nix wird.",
                        "Passt also. Jetzt muss nur noch der Abend passen."],
            "night": ["Der restliche Abend ist um die Uhrzeit eh nicht mehr lang.",
                      "Für die Couch passt's sowieso."],
        },
        "11": {
            "rain": ["Und lass ihn nicht wieder in der Bahn liegen.",
                     "Den nimmst du eh nicht mit. Ich sag's trotzdem, damit ich später recht hab."],
            "snow": ["Du wirst trotzdem so tun, als hätt's dir keiner gesagt."],
            "off": [("Und dann vergisst du's irgendwo. Wie letztes Mal.", ["al-de-54570f1c1b1b"]),
                    ("Und dann hängt's den Rest des Tages über deinem Stuhl.", ["al-de-7fbce4aa0163"])],
            "on": [("Nimm's mit. Frieren steht dir nicht.", ["al-de-3ec4402a46f4"]),
                   ("Und später stehst du wieder bibbernd an der Haltestelle und tust überrascht.", ["al-de-c63e80b31f40"])],
            "offon": [("Du ziehst es aus, und am Abend weißt du nicht mehr, wo's ist.",
                       ["al-de-1500f3dab84c", "al-de-1f633d85128d", "al-de-38f7804356ce", "al-de-4b134e3a656d"]),
                      ("Ausziehen kannst du. Wiederfinden ist dein Problem.",
                       ["al-de-6fe381539e29", "al-de-99eff7b19d6d", "al-de-f99586262e21"])],
            "hot": ["Wasser mitnehmen, hab ich gesagt. Nicht Eiskaffee.",
                    "Du suchst dir eh wieder den einzigen Platz ohne Schatten."],
            "steady": ["Den ganzen Tag richtig angezogen. Merk dir das Gefühl."],
            "cold": ["Den ganzen Tag. Du kannst also aufhören, alle fünf Minuten nachzuschauen."],
            "evening": ["Passt bis heute Abend. Bei dir ist das schon eine Leistung."],
            "night": ["Der restliche Abend war vor einer Stunde. Ab ins Bett."],
        },
    },
}

# New standalone lines for round 11's "Write new" spots: (path, text, answers, three?)
ANSWERS = {
    "en": [
        ("now_10.cool", "Somewhere between coat and T-shirt. Like me, between genius and modest.", ["al-en-2bc20fba84eb"]),
        ("now_10.cool", "The one forecast I could do in my sleep. If I slept.", ["al-en-3a5a4d4b3c45", "al-en-c8f52b03ff11"]),
        ("now_10.hot", "I'm the one thing in the house not making it any warmer.", ["al-en-20adb58a013a"]),
        ("now_10.nice", "Sunny days, you walk right past me. I've stopped taking it personally. Mostly.", ["al-en-b6443acaf37e"]),
        ("now_10.nice", "Weather this nice makes my job easy. I'll still act busy.", ["al-en-82f1402ff917", "al-en-f76ab5ca1d24"]),
        ("now_10.night", "I'll hold this picture all night without using any power. Your phone could never.",
         ["al-en-78db20cf6d05", "al-en-4dbb3f093574"]),
        ("now_10.wet", "Rainy days, everyone checks me twice. I'm not complaining.", ["al-en-2b4e31f0019a"]),
        ("now_11.cold", "You'll put the coat on and still complain. I can see it from here.", ["al-en-3a72421a8159"]),
        ("now_11.cool", "Same jacket, same route, same podcast. Living dangerously.", ["al-en-ca90af0e18cf", "al-en-368963ae1960"]),
        ("now_11.cool", "You'll describe today as 'fine'. You describe everything as 'fine'.", ["al-en-7d61836a1a98"]),
        ("now_11.evening", "Another evening of you walking past me like I don't do anything.", ["al-en-1951606912e1"]),
        ("flavour_vf_10.fickle", "Three outfits for one day. You're basically a costume department.", ["al-en-3e32d0fd5b64"], True),
    ],
    "de": [
        ("now_11.cool", "Du trägst die Jacke heut schon wieder offen. Als ob du was beweisen müsstest.", ["al-de-2b3e85392ed2"]),
        ("now_11.hot", "Du hast bestimmt wieder kein Wasser dabei. Aber eine Meinung zur Hitze.", ["al-de-d95a69473a4c"]),
        ("now_11.hot", "Deine Laune schmilzt heute schneller als dein Eis.", ["al-de-ee52197dd001"]),
        ("now_11.nice", "Traumwetter, und du suchst trotzdem schon die erste Wolke.", ["al-de-88026c93fc93"]),
        ("now_11.night", "Um die Zeit fängst du wieder mit „Weißt du, was ich glaube?“ an. Nein. Schlaf.", ["al-de-0cb9fc2cedad"]),
    ],
}

# Seasonal lines: (text, months). "Only in these months" tags them.
MONTHS = {
    "en": [
        ("You asked for warm weather. Careful what you wish for.", "05,06,07", "the start of summer"),
        ("Remember wishing for summer? This is what you get.", "05,06,07", "the start of summer"),
    ],
    "de": [
        ("Kalt ist's. Wie jedes Jahr, und jedes Jahr sind alle überrascht.", "10,11,12", "the first cold weeks (owner, round 11)"),
        ("Jedes Jahr wird's kalt. Und jedes Jahr tun alle überrascht.", "10,11,12", "the first cold weeks (owner, round 11)"),
        ("Schnee kommt. Deine Stiefel sind natürlich noch im Keller.", "10,11,12", "the first snow (owner, round 11)"),
        ("Bei der Kälte schmeckt sogar Glühwein.", "11,12,01", "Glühwein season"),
        ("Bei der Kälte trinkt man sogar freiwillig Glühwein.", "11,12,01", "Glühwein season"),
    ],
}
MONTH_NAMES = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May", "06": "Jun", "07": "Jul",
               "08": "Aug", "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}


def fact_for(lang, key, doc, base):
    facts = doc["facts"]
    return r8.sentence_case(r8.fill(facts[key][0], r8.fills(lang, facts[key][0], base, facts)))


def find(doc, text):
    """The pool path a line is in now."""
    for section, pools in doc.items():
        if section.split("_")[0] in ("now", "alone", "flavour") and isinstance(pools, dict):
            for key, texts in pools.items():
                if isinstance(texts, list) and text in texts:
                    return f"{section}.{key}"
    return None


def main():
    lines = []
    for lang in ("en", "de"):
        doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        existing = {t for s, pools in doc.items() if isinstance(pools, dict) for v in pools.values()
                    if isinstance(v, list) for t in v if isinstance(t, str)}
        for level, groups in FOLLOW[lang].items():
            for group, items in groups.items():
                fkey, sprite, what = GROUP_CTX[group]
                for item in items:
                    text, answers = (item if isinstance(item, tuple) else (item, None))
                    if text in existing:
                        raise SystemExit(f"already in the pools: {text}")
                    row = {"lang": lang, "path": f"flavour_{level}.{group}", "text": text, "role": "flavour",
                           "sprite": sprite, "fact": fact_for(lang, fkey, doc, base), "new": True,
                           "batch": f"Follow-up: {group}",
                           "meaning": f"New follow-up at {LEVEL[level]}: shows under the forecast line when it says "
                                      f"{what}. It should pick up what the line says and twist it."}
                    if group == "night":
                        row["hint"] = "Shown from 22:00"
                    if answers:
                        row["answers"] = answers
                        row["hint"] = (row.get("hint", "") + " · " if row.get("hint") else "") + "Answers a “Write new” from round 11"
                    lines.append(row)
        for item in ANSWERS[lang]:
            path, text, answers = item[:3]
            three = len(item) > 3 and item[3]
            section, mood = path.split(".")
            if text in existing:
                raise SystemExit(f"already in the pools: {text}")
            kind = "vf" if section.startswith("flavour_vf") else "now"
            sprite, fact, panels = r11.screen(lang, kind, mood, doc, base)
            row = {"lang": lang, "path": path, "text": text, "role": "flavour", "sprite": sprite, "fact": fact,
                   "new": True, "batch": "Write new", "answers": answers,
                   "meaning": r11.meaning(kind, mood, section.rsplit("_", 1)[1], new=True),
                   "hint": "Answers a “Write new” from round 11"}
            if panels:
                row["panels"] = panels
            if three:
                row["three"] = True
                row["hint"] += " · only shows with three different drawings, never coat → jacket → coat"
            lines.append(row)
        for text, months, why in MONTHS[lang]:
            path = find(doc, text)
            if not path:
                raise SystemExit(f"{lang}: seasonal line not in the pools: {text}")
            section, mood = path.split(".")
            kind = "now" if section.startswith("now") else ("vf" if section.startswith("flavour_vf") else "now")
            sprite, fact, panels = r11.screen(lang, kind if kind != "now" or mood in r11.NOW_SPRITE else "now",
                                              mood if mood in r11.NOW_SPRITE or kind == "vf" else "cold", doc, base)
            names = "–".join([MONTH_NAMES[months.split(",")[0]], MONTH_NAMES[months.split(",")[-1]]])
            row = {"lang": lang, "path": path, "text": text, "role": "flavour", "sprite": sprite, "fact": fact,
                   "ask": "months", "months": months, "batch": "Months?",
                   "hint": f"Proposed: only {names} ({why})",
                   "meaning": f"A seasonal line. “Only in these months” shows it {names} only; “All year” leaves it be."}
            if panels:
                row["panels"] = panels
            lines.append(row)
    out = {"round": ROUND, "idPrefix": "fu", "lines": lines}
    path = HERE / f"{ROUND}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in lines:
        by[(r["lang"], r["batch"])] = by.get((r["lang"], r["batch"]), 0) + 1
    print(f"{len(lines)} lines -> {path.relative_to(REPO)}")
    for (l, b), n in sorted(by.items()):
        print(f"  {l} {b:18} {n}")
    answered = {a for r in lines for a in r.get("answers", [])}
    for lang in ("en", "de"):
        d = json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8"))
        open_ids = [i for i, v in d.items() if v.get("verdict") == "rewrite" and i not in answered]
        print(f"  {lang}: {len(open_ids)} Write new spots not answered" + (f": {open_ids}" if open_ids else ""))


if __name__ == "__main__":
    main()
