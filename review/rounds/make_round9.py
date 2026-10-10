#!/usr/bin/env python3
"""
Round 9, the rework: what the owner's round 8 notes asked for.

    python3 review/rounds/make_round9.py

- "Rain pauses, then returns": raining now (the drawing has the umbrella),
  a dry break, rain again later. "The rain is taking a break" reads as
  now and contradicts the picture. New wordings say the order: rain for
  now, a break later, back {WHENP}. Kept ones replace every current
  wording of the situation ("replaces": "*"); the same for snow.
- The screen isn't always on a wall: on a desk, a shelf, the fridge.
  Every kept line that says "wall" gets a reworded twin; a kept twin
  replaces its original, a vetoed one leaves the original as it is.
- Theme lines: the day worked into the sentence instead of "Day. Sentence."
  A kept rewording replaces its original; new Christmas lines at 11 in
  English, which has none left, are added.

build_pools.py applies the round after round 8.
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402  (the screen context of each kind of line)

REPO = HERE.parent.parent
ROUND = "2026-10-rework"

FACTS = {
    "en": {
        "p_wet_again": [
            "The rain stops for a while later, then comes back {WHENP}. Keep the umbrella with you.",
            "It keeps raining for now, then takes a break. It's back {WHENP}, so keep the umbrella.",
            "Rain for now, then a dry spell, then more rain {WHENP}. The umbrella stays with you.",
            "Later the rain takes a break, but it returns {WHENP}. Hang on to the umbrella.",
        ],
        "p_wet_again_snow": [
            "The snow stops for a while later, then comes back {WHENP}.",
            "It keeps snowing for now, then takes a break. It's back {WHENP}.",
            "Snow for now, then a break, then more snow {WHENP}.",
        ],
    },
    "de": {
        "p_wet_again": [
            "Der Regen macht später eine Pause, {WHENP} kommt er aber zurück. Behalt den Schirm dabei.",
            "Erst regnet's weiter, dann ist Pause, und {WHENP} kommt der Regen wieder. Der Schirm bleibt dabei.",
            "Später hört der Regen eine Weile auf, {WHENP} geht's aber wieder los. Nimm den Schirm mit.",
            "Jetzt Regen, dann eine Pause, {WHENP} wieder Regen. Der Schirm bleibt also dabei.",
        ],
        "p_wet_again_snow": [
            "Der Schnee macht später eine Pause, {WHENP} schneit's aber wieder.",
            "Erst schneit's weiter, dann ist Pause, und {WHENP} schneit es wieder.",
            "Jetzt Schnee, dann eine Pause, {WHENP} wieder Schnee.",
        ],
    },
}

# (level, pool, original or None to add) -> reworded line
REWORK = {
    "en": [
        # the screen can sit anywhere indoors
        ("10", "nice", "I'm a screen on a wall, but even I'd go outside today.", "I'm a screen, and even I'd go outside today."),
        ("10", "warming", "Thrilling stuff. I'm on the edge of my wall.", "Thrilling stuff. I'm on the edge of my frame."),
        ("10", "warming", "Gripping weather. I can barely stay on the wall.", "Gripping weather. I can barely stay in my frame."),
        ("10", "cold", "I'm staying on the wall where it's warm.", "I'm staying in here where it's warm."),
        ("10", "wet", "I'll be on the wall, dry and smug.", "I'll be in here, dry and smug."),
        ("10", "wet", "Staying dry is easy when you live on a wall.", "Staying dry is easy when you live indoors."),
        ("11", "nice", "Perfect weather. I can't leave the wall. What's your excuse?", "Perfect weather. I can't leave the house. What's your excuse?"),
        ("11", "nice", "I'm stuck on a wall. What's keeping you in today?", "I'm stuck in here. What's keeping you in today?"),
        ("11", "night", "Still up? I'm a wall decoration and even I'm tired.", "Still up? I'm a screen and even I'm tired."),
        # theme days: the day in the sentence
        ("10", "theme_ny", "New Year. I don't do resolutions. I was perfect last year too.", "I don't do New Year's resolutions. I was perfect last year too."),
        ("10", "theme_ny", "New Year. Somewhere a gym is about to be very full. Briefly.", "Every gym is full of New Year's resolutions today. Give it a week."),
        ("10", "theme_spooky", "Halloween. Everyone's dressing up. I'm going as a screen again.", "Everyone's dressing up for Halloween. I'm going as a screen again."),
        ("10", "theme_spooky", "Halloween. I've been pale and staring from this wall all year.", "Pale, staring, never blinking. I've been dressed for Halloween all year."),
        ("10", "theme_spooky", "Happy Halloween. The ghosting on my screen? Festive.", "That ghosting on my screen? It's for Halloween."),
        ("10", "theme_thanks", "Happy Thanksgiving. I'm thankful I don't have to eat anything.", "This Thanksgiving, I'm thankful I don't have to eat anything."),
        ("10", "theme_thanks", "Thanksgiving. I'm the only one here who won't need a nap later.", "After Thanksgiving dinner, I'll be the only one not napping."),
        ("10", "theme_xmas", "Merry Christmas. I'm the only decoration that knows the forecast.", "Of all the Christmas decorations, I'm the only one that knows the forecast."),
        ("10", "theme_xmas", "Merry Christmas. Unlike the tree, I'll still be up in February.", "Unlike the Christmas tree, I'll still be up in February."),
        ("11", "theme_ny", "New Year. You'll say 'this is my year'. You said that last year.", "You'll call this New Year your year. You said that last year."),
        ("11", "theme_spooky", "Halloween. Your costume is 'tired adult' again, isn't it.", "Your Halloween costume is 'tired adult' again, isn't it."),
        ("11", "theme_xmas", None, "Your relatives will ask about your plans this Christmas. Have some."),
        ("11", "theme_xmas", None, "The Christmas walk after lunch is the only exercise you'll get. Enjoy it."),
        ("11", "theme_xmas", None, "You'll say the Christmas cookies were for guests. There were no guests."),
    ],
    "de": [
        ("10", "theme_krampus", "Krampustag. Endlich ist mal einer schlechter gelaunt als ich.", "Am Krampustag ist endlich mal einer schlechter gelaunt als ich."),
        ("10", "theme_nikolo", "Nikolaus. Der einzige Tag, an dem Schuhe vor der Tür was bringen.", "Am Nikolaustag bringen Schuhe vor der Tür ausnahmsweise was."),
        ("10", "theme_ny", "Silvester. Erst Feuerwerk, dann Feinstaub. Prost Neujahr.", "Erst das Silvesterfeuerwerk, dann der Feinstaub. Prost Neujahr."),
        ("10", "theme_xmas", "Weihnachten. Die Gans hat heute den schlechtesten Tag von allen.", "Die Weihnachtsgans hat heute den schlechtesten Tag von allen."),
        # the owner's idea ("might be too long"), and a shorter take
        ("11", "theme_ny", "Neues Jahr, gute Vorsätze. Ich geb dir bis zum Zehnten.", "Deine Neujahrsvorsätze hast du bis zum Zehnten sicher schon wieder vergessen. Ich kenn dich."),
        ("11", "theme_ny", "Neues Jahr, gute Vorsätze. Ich geb dir bis zum Zehnten.", "Deine Neujahrsvorsätze sind bis zum Zehnten vergessen. Ich kenn dich."),
    ],
}
THEME_DAY = {"theme_ny": "New Year's Day", "theme_spooky": "Halloween", "theme_thanks": "Thanksgiving",
             "theme_xmas": "Christmas, 24 to 26 December", "theme_krampus": "Krampustag, 5 December",
             "theme_nikolo": "Nikolaustag, 6 December"}


def main():
    earlier = r8.earlier_votes()
    lines = []
    for lang in ("en", "de"):
        doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        facts = doc["facts"]
        for key, texts in FACTS[lang].items():
            sprite, mood, meaning = r8.FACT_CTX[key]
            pool = doc["flavour_10"].get(mood) or []
            now = " / ".join(facts.get(key, []))
            for text in texts:
                lines.append({"lang": lang, "path": f"fact_0.{key}", "text": text, "batch": "Rain and snow", "role": "fact",
                              "sprite": sprite, "fills": r8.fills(lang, text, base, facts),
                              "fillsAlt": r8.fills(lang, text, base, facts, alt=True), "under": pool[0] if pool else "",
                              "replaces": "*",
                              "meaning": f"{meaning} Says the order: rain now (the umbrella in the drawing), a break later, back again. "
                                         f"Kept wordings replace all of today's: {now}"})
        for level, mood, original, text in REWORK[lang]:
            if original is not None and original not in doc[f"flavour_{level}"].get(mood, []):
                raise SystemExit(f"{lang} {level} {mood}: not in the pool: {original!r}")
            sprite, keys, meaning = r8.MOOD_CTX.get(mood, ("jacket_dry", ["steady"], ""))
            if mood.startswith("theme_"):
                meaning = THEME_DAY[mood] + ": shown instead of the mood's line."
                keys = ["steady_cold"] if mood != "theme_spooky" else ["steady"]
            fact = " ".join(r8.sentence_case(r8.fill(facts[k][0], r8.fills(lang, facts[k][0], base, facts))) for k in keys)
            batch = "Themes" if mood.startswith("theme_") else "Not a wall"
            why = (f"Replaces: “{original}”. A veto keeps the original." if original else "New: English has no Christmas line at 11.")
            row = {"lang": lang, "path": f"flavour_{level}.{mood}", "text": text, "batch": batch, "role": "flavour",
                   "sprite": sprite, "fact": fact, "meaning": f"Sarcastic line at {'On' if level == '10' else '11'}. {meaning} {why}"}
            if original:
                row["replaces"] = original
            if (lang, text) in earlier:
                row["earlier"] = earlier[(lang, text)]
            lines.append(row)
    out = {"round": ROUND, "lines": lines}
    path = HERE / f"{ROUND}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in lines:
        by[(r["lang"], r["batch"])] = by.get((r["lang"], r["batch"]), 0) + 1
    print(f"{len(lines)} lines -> {path.relative_to(REPO)}: " + ", ".join(f"{l} {b} {n}" for (l, b), n in sorted(by.items())))
    long = [(r["lang"], len(r["text"]), r["text"]) for r in lines if r["role"] == "flavour" and len(r["text"]) > 72]
    for x in long:
        print("  long:", x)


if __name__ == "__main__":
    main()
