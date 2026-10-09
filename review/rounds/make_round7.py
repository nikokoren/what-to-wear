#!/usr/bin/env python3
"""
Round 7, theme days October to January, in calendar order.

    python3 review/rounds/make_round7.py

Each language writes the days its readers keep (docs/TODO.md, item 5):
Halloween, Christmas and New Year in both; Thanksgiving in English;
Krampus and Nikolaus in German. Every line names its day, and none
assumes what the reader is doing. The first prototype's Christmas
placeholders are on the page too, to be voted at last.

Written by hand in the main session.
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROUND = "2026-10-themes-winter"
DAYS = {
    "spooky": "Halloween, 31 October",
    "thanks": "Thanksgiving, the fourth Thursday of November (US)",
    "krampus": "Krampustag, 5 December (an Alpine custom; it has to make sense in Hamburg too)",
    "nikolo": "Nikolaus, 6 December",
    "xmas": "Christmas, 24 and 25 December",
    "ny": "New Year, 31 December and 1 January",
}
LINES = {
    ("en", "10", "spooky"): ["Happy Halloween. The ghosting on my screen? Festive.",
                             "Halloween. Everyone's dressing up. I'm going as a screen again.",
                             "Halloween. I've been pale and staring from this wall all year."],
    ("en", "11", "spooky"): ["Halloween. Your costume is 'tired adult' again, isn't it.",
                             "Halloween. You'll say you're too old for it, then wear the hat.",
                             "You'll buy candy for trick-or-treaters and eat it by eight."],
    ("de", "10", "spooky"): ["Halloween. Früher war Reformationstag, da hat keiner geklingelt.",
                             "Halloween. Gleich klingeln wieder Kinder, die man nicht kennt.",
                             "Halloween. Der Kürbis kostet mehr als der Wocheneinkauf."],
    ("de", "11", "spooky"): ["Halloween. Wenn's klingelt, bist du plötzlich nicht zu Hause.",
                             "Halloween. Du gruselst dich trotzdem nur vor Montag."],
    ("en", "10", "thanks"): ["Happy Thanksgiving. I'm thankful I don't have to eat anything.",
                             "Thanksgiving. I'm the only one here who won't need a nap later.",
                             "Thanksgiving. I won't bring up politics. I'm a weather screen."],
    ("en", "11", "thanks"): ["Thanksgiving. Pace yourself. You said that last year too.",
                             "Thanksgiving. Your 'one more plate' is a family tradition now.",
                             "Thanksgiving. You'll be grateful, then you'll be horizontal."],
    ("de", "10", "krampus"): ["Krampustag. Endlich ist mal einer schlechter gelaunt als ich.",
                              "Im Süden ist heute Krampuslauf. Da wundert sich keiner."],
    ("de", "11", "krampus"): ["Krampustag. Ich hab ihm deine Adresse nicht gegeben. Noch nicht.",
                              "Krampustag. Ob du brav warst? Ich hab mitgeschrieben."],
    ("de", "10", "nikolo"): ["Nikolaus. Der einzige Tag, an dem Schuhe vor der Tür was bringen.",
                             "Nikolaus. Schokolade aus dem Stiefel. Tradition halt."],
    ("de", "11", "nikolo"): ["Nikolaus. Hast du deine Stiefel rausgestellt? In deinem Alter?",
                             "Nikolaus. In deinem Stiefel liegt bestimmt nur Streusalz."],
    ("en", "10", "xmas"): ["Merry Christmas. Unlike the tree, I'll still be up in February.",
                           "Merry Christmas. I'm the only decoration that knows the forecast."],
    ("en", "11", "xmas"): ["Christmas. You'll say 'just a small slice'. Twice.",
                           "Merry Christmas. Act surprised. You've been rehearsing."],
    ("de", "10", "xmas"): ["Weihnachten. Früher lag mehr Schnee, sagen alle. Stimmt nicht.",
                           "Weihnachten. Die Gans hat heute den schlechtesten Tag von allen."],
    ("de", "11", "xmas"): ["Weihnachten. Du sagst wieder „wir schenken uns nichts“. Sicher."],
    ("en", "10", "ny"): ["New Year. I don't do resolutions. I was perfect last year too.",
                         "New Year. Somewhere a gym is about to be very full. Briefly."],
    ("en", "11", "ny"): ["Happy New Year. You'll write last year's date until March.",
                         "New Year. You'll say 'this is my year'. You said that last year."],
    ("de", "10", "ny"): ["Silvester. Erst Feuerwerk, dann Feinstaub. Prost Neujahr.",
                         "Neujahr. Jetzt fegt wieder keiner die Raketenreste weg."],
    ("de", "11", "ny"): ["Neues Jahr, gute Vorsätze. Ich geb dir bis zum Zehnten.",
                         "Neujahr. Dein Wachsgießen sah wieder aus wie eine Kartoffel."],
}


def main():
    out = []
    for (lang, level, key), texts in LINES.items():
        for t in texts:
            if len(t) > 65:
                raise SystemExit(f"over 65 characters: {t!r}")
            out.append({"lang": lang, "path": f"flavour_{level}.theme_{key}", "text": t,
                        "batch": "E7" if lang == "en" else "D7",
                        "meaning": f"Theme day: {DAYS[key]}. Replaces the mood's line on a steady day."})
    # The first prototype's Christmas lines: in the pool, never voted.
    for lang in ("en", "de"):
        doc = json.loads((HERE.parent.parent / "prototypes" / "fact-flavour" / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        for level in ("10", "11"):
            for t in doc[f"flavour_{level}"].get("theme_xmas", []):
                if not any(l["text"] == t for l in out):
                    out.append({"lang": lang, "path": f"flavour_{level}.theme_xmas", "text": t,
                                "batch": "E7" if lang == "en" else "D7",
                                "meaning": f"Theme day: {DAYS['xmas']}. A placeholder from the first prototype: in the pool, never voted."})
    (HERE / f"{ROUND}.json").write_text(json.dumps({"round": ROUND, "lines": out}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{ROUND}: {len(out)} lines")


if __name__ == "__main__":
    main()
