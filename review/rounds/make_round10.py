#!/usr/bin/env python3
"""
Round 10, Visual Forecast's sarcastic line. With two or three panels the
screen shows drawings and times, and no fact line, so a line that answers
the fact ("that layer", "admit I was right") points at nothing.

    python3 review/rounds/make_round10.py

Two parts, shown the way Visual Forecast shows them (the panels, their
times, the line; no fact):

- "Stands alone?": every line of the moods that come with changes. The
  buttons read "Works without the fact" and "Needs the fact"; a "needs"
  only keeps the line off Visual Forecast, it stays in the words. Each row
  carries Claude's guess.
- "For the drawings": new lines about what the panels show, per mood. They
  never name a panel by position: where the umbrella is depends on the day.

After the vote build_pools.py writes flavour_vf_10 / flavour_vf_11: per
mood, the lines that work alone (warming and cooling with cool's, as the
words do) plus the kept new ones. The panels pick from them on two- and
three-panel days and fall back to the usual line otherwise.
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-10-visual"
# The moods a two- or three-panel day can have (cool shows on warming and
# cooling days, from their shared pool).
MOODS = ["wet", "warming", "cooling", "cool", "cold", "fickle", "hot", "snow"]

# A typical day of each mood as panels: (drawing, hour) after "now".
PANELS = {
    "wet": ["jacket_dry", ("jacket_rain", 14)],
    "warming": ["jacket_dry", ("sweater_dry", 13)],
    "cool": ["jacket_dry", ("sweater_dry", 13)],
    "cooling": ["sweater_dry", ("jacket_dry", 18)],
    "cold": ["coat_dry", ("bundled_dry", 18)],
    "fickle": ["coat_dry", ("jacket_dry", 13), ("coat_dry", 19)],
    "hot": ["tee_pants_dry", ("heat_dry", 13)],
    "snow": ["coat_dry", ("coat_snow", 15)],
}

# Claude's guess: lines that answer the fact line, so make no sense under
# drawings alone. Borderline ones say so.
NEEDS = {
    "en": {
        "Taking that layer off might be the highlight of your day.": "“that layer” points at the fact",
        "That layer coming off could be the peak of your day.": "“that layer” points at the fact",
        "You'll be a bit too warm before you admit I was right.": "“I was right” answers the fact's advice",
        "You'll overheat a little before you admit I was right.": "“I was right” answers the fact's advice",
        "Leave it behind and you'll think of me later. Not fondly.": "“it” is the jacket the fact names",
        "You'll put it on later and act like it was your idea.": "“it” is the jacket the fact names",
        "I give it even odds you lose that layer by tonight.": "“that layer” points at the fact",
        "Fifty-fifty that layer goes missing by tonight.": "“that layer” points at the fact",
    },
    "de": {
        "Als ob dein Schrank sowas hergibt.": "“sowas” points at the jacket the fact names",
        "Als hättest du was Passendes im Schrank.": "“was Passendes” answers the fact's advice",
    },
}
BORDERLINE = {
    "Carrying a layer you don't need yet. How very grown-up.",
    "Bringing a layer you won't need for hours. Look at you, prepared.",
    "Today you're your own coat rack. Congratulations.",
    "Today you're a coat rack with legs. Well done.",
    "Heute trägst du die Jacke mehr spazieren als am Leib.",
}

# New lines about the drawings. English: the screen at On, the reader at 11.
# German: the Grantler, standard German, never a translation.
NEW = {
    "en": {
        "10": {
            "wet": ["I put an umbrella in one of these. You're welcome.",
                    "Spot the difference: one of these has an umbrella.",
                    "The umbrella makes a guest appearance today. I cast it myself.",
                    "I drew the umbrella. Bringing it is your department."],
            "warming": ["The sequel has fewer layers. Most sequels do.",
                        "Watch a layer vanish later. I'm basically a magician.",
                        "One layer fewer by the end. I drew every gripping detail."],
            "fickle": ["Today is a trilogy, and the third part looks like the first.",
                       "Three outfits for one day. I'm basically a costume department.",
                       "Same outfit at both ends of the day. Lazy? No. Accurate."],
            "cold": ["Different layers in every drawing. Same cold in all of them.",
                     "I draw the coats. Your ears are on their own."],
            "hot": ["Less and less clothing in these drawings. I'm keeping it tasteful.",
                    "The drawings get breezier. I stay cool. Comes with being a screen."],
            "cooling": ["A layer shows up later. I call that foreshadowing.",
                        "I drew the extra layer for later. Even I plan ahead."],
            "snow": ["Snow in today's drawings. I drew every flake by hand.",
                     "There's snow in this lineup. I made it look easy."],
        },
        "11": {
            "wet": ["One of these has an umbrella. Guess which one you'll ignore.",
                    "The umbrella's right there in the drawing. You'll still forget it.",
                    "You'll check the drawings, nod, and leave the umbrella anyway.",
                    "Umbrella in the picture, umbrella at home. Classic you."],
            "warming": ["Later you'll lose a layer. Then you'll lose it for real.",
                        "Later you'll carry a layer around like a hostage.",
                        "You'll match the first drawing all day. Out of stubbornness."],
            "fickle": ["Three outfits by tonight. You can barely manage one.",
                       "Off and back on. You'll lose track by lunch.",
                       "Three drawings, three outfits. You'll get each one wrong."],
            "cold": ["Whatever the drawings say, your nose goes red in all of them.",
                     "Every drawing has gloves. Yours are in last winter's coat."],
            "hot": ["Fewer clothes later. More complaining, as always.",
                    "The drawings get lighter. Your mood won't."],
            "cooling": ["The extra layer's in the later drawing. Yours will be on a chair.",
                        "You'll see the later drawing and leave without the layer anyway."],
            "snow": ["Snow in the drawings. You'll act surprised anyway.",
                     "Snow in the drawings, and your boots are still in the closet."],
        },
    },
    "de": {
        "10": {
            "wet": ["Einen Schirm hab ich auch gemalt. Einer muss ja mitdenken.",
                    "Auf einem Bild ist ein Schirm. Übersehen tun ihn trotzdem alle.",
                    "Ich mal den Schirm. Mitnehmen müsst ihr ihn schon selber.",
                    "Mit Schirm, ohne Schirm. Ich mal alles, und keiner dankt's mir."],
            "warming": ["Später ist eine Schicht weg. Mehr Spannung gibt's heute nicht.",
                        "Erst mit, dann ohne. Ein Drama in zwei Akten. Ein kurzes.",
                        "Zwei Bilder für einmal Ausziehen. Was ich mir alles antu."],
            "fickle": ["Am Ende schaut's aus wie am Anfang. Typisch für so einen Tag.",
                       "Drei Bilder, und zweimal das Gleiche. Ich wiederhol mich ungern.",
                       "Drei Bilder für einen Tag. Ich bin doch kein Daumenkino."],
            "cold": ["Auf jedem Bild dick eingepackt. Schöner wird dadurch keiner.",
                     "Ich mal die Jacken. Frieren müsst ihr selber."],
            "hot": ["Von Bild zu Bild weniger an. Weiter runter mal ich nicht.",
                    "Je später, desto luftiger. Ich hab da meine Grenzen."],
            "cooling": ["Später kommt eine Schicht dazu. Merkt sowieso keiner.",
                        "Die Extraschicht kommt erst später. Spannung bis zum Schluss."],
            "snow": ["Auf meinen Bildern sieht Schnee ordentlich aus. Draußen nicht.",
                     "Schnee kann ich malen. Schippen müsst ihr selber."],
        },
        "11": {
            "wet": ["Auf einem Bild hast du einen Schirm. In echt eher nicht.",
                    "Den Schirm siehst du. Mitnehmen wirst du ihn trotzdem nicht.",
                    "Gemalt hab ich den Schirm. Vergessen musst du ihn schon selber.",
                    "Mit Schirm siehst du richtig vernünftig aus. Leider nur gemalt."],
            "warming": ["Später ist eine Schicht weg. Bei dir dauert das bis zum Abend.",
                        "Zwei Bilder, zwei Outfits. Du schaffst mit Mühe eins.",
                        "Auf dem Bild schwitzt du nicht. Wunschdenken."],
            "fickle": ["Drei Bilder, drei Outfits. Du kommst schon mit einem kaum zurecht.",
                       "An, aus, an. Irgendwo dazwischen verlierst du die Jacke.",
                       "Am Ende bist du wieder eingepackt. Und genauso schlecht gelaunt."],
            "cold": ["Auf dem Bild hast du Handschuhe. Deine liegen noch im Keller.",
                     "Egal welches Bild: Du frierst als Erster."],
            "hot": ["Von Bild zu Bild luftiger. Dein Gejammer bleibt gleich.",
                    "Weniger an, mehr Gejammer. Ich kenn dich."],
            "cooling": ["Die Extraschicht auf dem Bild? Die liegt bei dir dann zu Hause.",
                        "Auf dem Bild trägst du später was Wärmeres. Rate mal, wo deins ist."],
            "snow": ["Schnee auf den Bildern. Du bist trotzdem überrascht. Jedes Mal.",
                     "Schnee kommt. Deine Stiefel sind natürlich noch im Keller."],
        },
    },
}


def panels(lang, mood):
    """The mood's panels with the times as the screen writes them."""
    labels = json.loads((REPO / "prototypes" / "panels" / "lang" / f"{lang}.json").read_text(encoding="utf-8"))["panels"]
    seq = PANELS[mood]
    out = [{"sprite": seq[0], "label": labels["now"]}]
    for sprite, hour in seq[1:]:
        out.append({"sprite": sprite, "label": labels["from"] + " " + labels["hours"][hour]})
    return out


def main():
    lines = []
    for lang in ("en", "de"):
        doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        for level in ("10", "11"):
            name = "On" if level == "10" else "11"
            for mood in MOODS:
                shown = "warming" if mood == "cool" else mood
                for text in doc[f"flavour_{level}"].get(mood, []):
                    why = NEEDS[lang].get(text)
                    hint = (f"Claude's guess: needs the fact ({why})" if why else
                            "Claude's guess: works alone, but borderline" if text in BORDERLINE else
                            "Claude's guess: works alone")
                    lines.append({"lang": lang, "path": f"flavour_{level}.{mood}", "text": text, "batch": "Stands alone?",
                                  "role": "flavour", "ask": "alone", "sprite": PANELS[shown][0], "fact": "",
                                  "panels": panels(lang, shown), "hint": hint,
                                  "meaning": f"Visual Forecast, sarcastic line at {name}, mood {mood}"
                                             + (" (shown on warming and cooling days)" if mood == "cool" else "")
                                             + ". Does it make sense under the drawings, with no fact line? "
                                               "“Needs the fact” only keeps it off Visual Forecast; it stays in the words."})
            for mood, texts in NEW[lang][level].items():
                for text in texts:
                    lines.append({"lang": lang, "path": f"flavour_vf_{level}.{mood}", "text": text, "batch": "For the drawings",
                                  "role": "flavour", "sprite": PANELS[mood][0], "fact": "", "panels": panels(lang, mood),
                                  "meaning": f"New, for Visual Forecast only: sarcastic line at {name} on a {mood} day "
                                             "with two or three panels. It talks about the drawings, so it never names "
                                             "a panel by position."})
    out = {"round": ROUND, "idPrefix": "vf", "lines": lines}
    path = HERE / f"{ROUND}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in lines:
        by[(r["lang"], r["batch"])] = by.get((r["lang"], r["batch"]), 0) + 1
    print(f"{len(lines)} lines -> {path.relative_to(REPO)}: " + ", ".join(f"{l} {b} {n}" for (l, b), n in sorted(by.items())))
    for r in lines:
        if r["batch"] == "For the drawings" and len(r["text"]) > 66:
            print(f"  long ({len(r['text'])}): {r['text']}")
    missing = [t for lang in NEEDS for t in NEEDS[lang]
               if not any(l["text"] == t for l in lines)] + [t for t in BORDERLINE if not any(l["text"] == t for l in lines)]
    if missing:
        raise SystemExit(f"guesses for lines not in the pools: {missing}")


if __name__ == "__main__":
    main()
