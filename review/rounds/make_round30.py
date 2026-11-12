#!/usr/bin/env python3
"""
Round 30 (November 2026): directions for the evening line, before any
writing. The owner, after three failed attempts (one pool for every
evening; jokes keyed to tomorrow's weather with stock images; another
agent's "someone out there will..." scenes): present a broad variety of
ideas what to joke about first; only after feedback on the ideas start
writing. Each idea gets one English and one German sample, shown under a
real tomorrow sentence, so the owner can judge the direction, not the
wording.

    python3 review/rounds/make_round30.py
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROUND = "2026-11-ideas"
FROM = {"en": "from 1 pm", "de": "ab 13 Uhr"}
FACT = {  # an approved sentence per kind of tomorrow (evening.facts)
    "en": {"rain": "Tomorrow it rains {FROM}, so take the umbrella.", "colder": "Tomorrow it's colder {FROM}.",
           "steady": "Tomorrow's outfit works all day.", "warmer": "Tomorrow the temperature climbs {FROM}."},
    "de": {"rain": "Morgen regnet's {FROM}, denk also an den Schirm.", "colder": "Morgen wird's {FROM} kälter, dann brauchst du eine Schicht mehr.",
           "steady": "Das Outfit für morgen passt den ganzen Tag.", "warmer": "Morgen wird's {FROM} wärmer."},
}
SPRITE = {"rain": "jacket_rain", "colder": "coat_dry", "steady": "sweater_dry", "warmer": "sweater_dry"}

# (name, what it is and why it fits, needs, [(lang, level, weather, sample)])
IDEAS = [
    ("Grumbling in advance",
     "The screen gets its complaining about tomorrow done tonight. The only German evening lines you kept do exactly this ("
     "„Man kann sich schon heute drüber ärgern“, „bei den Wettergöttern beschwert“). Works in any weather.",
     "", [("en", "10", "rain", "I'm doing tomorrow's grumbling tonight. During the rain I'll be busy drawing umbrellas."),
          ("de", "10", "rain", "Ich meckere heute schon mal vor. Morgen reicht dann ein Seufzer.")]),
    ("Haggling with the weather",
     "The screen tried to get tomorrow changed, and lost. Extends the two kept lines (the weather gods, sitting on it for drama): "
     "the screen has an agenda and fails at it.",
     "", [("en", "10", "colder", "I asked if tomorrow's cold could wait a week. It's already left the house."),
          ("de", "10", "rain", "Ich wollte den Regen auf nächste Woche verschieben. Der ist aber schon losgefahren.")]),
    ("The weather's own night before",
     "Tomorrow's weather is getting ready tonight, like everyone else. Only works the evening before, which is the point.",
     "", [("en", "10", "rain", "Somewhere, tomorrow's rain is getting an early night. Big day ahead."),
          ("de", "10", "colder", "Die Kälte packt gerade ihre Sachen. Morgen zieht sie hier ein.")]),
    ("Covering up overnight changes",
     "Forecasts change overnight and the screen really does redraw itself. It admits it will do that quietly and save face. "
     "True to the device, honest about the forecast, any weather.",
     "", [("en", "10", "steady", "If this changes overnight, I'll quietly redraw it and act like it was always that way."),
          ("de", "10", "steady", "Ändert sich das über Nacht, mal ich's heimlich um und tu so, als wär nichts gewesen.")]),
    ("E-ink in the dark",
     "A device truth only TRMNL owners know: no backlight, so once the lights go out nobody can read it. The screen makes "
     "that the reader's problem. Any weather.",
     "", [("en", "10", "rain", "Once the lights go out, nobody can see me. That's e-ink. Read fast."),
          ("de", "10", "rain", "Wenn das Licht ausgeht, sieht mich keiner mehr. E-Ink. Also lies zügig.")]),
    ("The playlist neighbours",
     "TRMNL rotates several plugins on one screen. The weather screen comments on whatever comes on after it. Fresh and "
     "very TRMNL, but it guesses what else is on the reader's playlist.",
     "Guesses the reader's other plugins", [
         ("en", "10", "colder", "Next on this screen, probably the stocks. Also forecasting a drop."),
         ("de", "11", "rain", "Gleich zeigt dieser Bildschirm deinen Kalender. Der sieht für morgen auch nicht trockener aus.")]),
    ("The drawn figures",
     "The little figure in your drawings as a character. The evening screen shows it twice, tonight on the left and "
     "tomorrow on the right, so they can be keen, jealous or smug about each other.",
     "", [("en", "10", "warmer", "The one on the left is jealous. The one on the right gets the warmer day."),
          ("de", "10", "steady", "Die Figur da rechts ist schon für morgen angezogen. Streber.")]),
    ("The illustrator with nothing to draw",
     "On a day that doesn't change, the screen as an artist bored by its own assignment.",
     "", [("en", "10", "steady", "Tomorrow is so uneventful I'm tempted to draw in a cat. For plot."),
          ("de", "10", "steady", "Morgen passiert so wenig, dass ich überleg, eine Katze dazuzumalen. Für die Handlung.")]),
    ("Your own settings, used against you",
     "The screen knows what the reader told it: always cold, always hot, when they head out. At 11 it throws that back. "
     "Needs a little logic (lines that only show with a setting).",
     "Needs lines tied to a setting", [
         ("en", "11", "colder", "You told me you're always cold. Tomorrow you get to be right."),
         ("de", "11", "colder", "Du hast angegeben, dass du immer frierst. Morgen kriegst du recht.")]),
    ("Gear coming out of hiding",
     "The first rain or the first cold day means finding the umbrella or the gloves again. Small, universal household "
     "truth. Some need month tags (gloves only in autumn).",
     "Some need month tags", [
         ("en", "11", "colder", "Your gloves are still exactly where you left them last spring. Good luck."),
         ("de", "11", "rain", "Dein Schirm ist irgendwo hier. Seit dem letzten Regen weißt du nur nicht mehr, wo.")]),
    ("The two-word sigh",
     "A format, not a topic: the shortest possible reaction under the sentence. Grantler at his purest, and it reads from "
     "across the room. Needs many variants per weather so it doesn't repeat.",
     "", [("en", "10", "rain", "Marvelous. Truly."),
          ("de", "10", "rain", "Auch das noch.")]),
    ("The weather keeps its appointments",
     "Tomorrow's weather comes with an exact time. Nobody else in life manages that. German has the obvious target, which "
     "may be too obvious.",
     "", [("en", "10", "rain", "The rain told us exactly when it's coming. No repairman has ever managed that."),
          ("de", "10", "rain", "Der Regen kommt auf die Stunde genau. Da kann sich die Bahn was abschauen.")]),
    ("Tomorrow's weekday",
     "The tag says which day tomorrow is. Lines for the weather on a Saturday, a Monday, a Sunday. Needs logic, and you cut "
     "the Monday and Friday day lines once, so maybe not.",
     "Needs lines tied to the weekday", [
         ("en", "10", "rain", "Rain on a Saturday. The weather doesn't do weekends."),
         ("de", "10", "colder", "Montag und kälter. Der Tag gibt sich echt Mühe.")]),
]


def main():
    lines = []
    for n, (name, what, needs, samples) in enumerate(IDEAS, 1):
        for lang, lv, wx, text in samples:
            hint = [f"Idea {n:02d}: judge the direction; use the note for the idea"]
            if needs:
                hint.append(needs)
            lines.append({"lang": lang, "path": f"flavour_{lv}.evening_{wx}", "text": text, "role": "flavour",
                          "sprite": SPRITE[wx], "fact": FACT[lang][wx].replace("{FROM}", FROM[lang]),
                          "batch": f"Idea {n:02d}: {name}", "meaning": f"Idea {n:02d}, {name}. {what}",
                          "new": True, "hint": " · ".join(hint)})
    (HERE / f"{ROUND}.json").write_text(json.dumps({"round": ROUND, "idPrefix": "id", "lines": lines},
                                                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(len(IDEAS), "ideas,", len(lines), "samples")


if __name__ == "__main__":
    main()
