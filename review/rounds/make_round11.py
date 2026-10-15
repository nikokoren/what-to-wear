#!/usr/bin/env python3
"""
Round 11, the sarcastic lines on their own (October 2026).

    python3 review/rounds/make_round11.py

The owner, seeing the sarcastic lines alone in the beta: they need
context. Since the line is now picked by what's on screen
(prototypes/panels/README.md, "Which sarcastic line"), every line is
sorted into where it can show, and shown there on the page:

- "Now": about what the Now drawing shows (cold, cool, nice, hot, wet,
  snow, evening, night). Shows on every screen with that drawing, the
  outfit alone included, so it must make sense with nothing else on
  screen. Shown alone under the drawing.
- "Day": about the shape of the day: a change (warming, cooling, fickle,
  rain coming) or a steady day ("Easy day to forecast"). Shows only with
  the forecast line on a day that changes, or on a steady day. Shown
  under the forecast line.
- "Drawings": about the two or three drawings. Shows only with them.

Every current line once (ids "al-…": rated afresh), on Claude's sorting,
with round 5's reworded twins flagged so the owner keeps one wording
(with the hourly rotation, twins can show in back-to-back hours), and
new lines where the now pools are thin. Keep: the line stays, in the
pool its batch names. Veto: out. Write new: out, and new lines for that
spot. E: reword.

build_pools.py applies the round once it has votes: current lines stay
unless vetoed, new ones only if kept.
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import make_round8 as r8  # noqa: E402
import make_round10 as r10  # noqa: E402

REPO = HERE.parent.parent
ROUND = "2026-10-alone"
LEVEL = {"10": "On", "11": "11"}

# The drawing a now line sits under.
NOW_SPRITE = {"cold": "coat_dry", "cool": "jacket_dry", "nice": "tee_pants_dry", "hot": "heat_dry",
              "wet": "jacket_rain", "snow": "coat_snow", "evening": "jacket_dry", "night": "jacket_dry"}
NOW_MEANING = {
    "cold": "the drawing shows a winter coat or more",
    "cool": "the drawing shows a jacket",
    "nice": "the drawing shows a mild or warm outfit",
    "hot": "the drawing shows heat",
    "wet": "it's raining now: the drawing has the umbrella",
    "snow": "it's snowing now: the drawing has the snow",
    "evening": "18:00 to 22:00, any weather",
    "night": "from 22:00, any weather",
}
# Where a current line goes, by its pool: now moods stay now lines,
# the changing moods are day lines.
DEFAULT = {"nice": "now", "cool": "now", "cold": "now", "hot": "now", "wet": "now", "snow": "now",
           "evening": "now", "night": "now", "warming": "day", "cooling": "day", "fickle": "day"}
# Lines whose joke needs the day, not just the drawing.
DAY = {
    "en": {
        "Easy day to forecast. I'll still take the credit.": "needs a day without changes",
        "Not my hardest forecast. I'm taking the credit anyway.": "needs a day without changes",
        "I've had firmware updates more exciting than today.": "about a dull day: a changing day isn't",
        "It takes real talent to make today look interesting.": "about a dull day: a changing day isn't",
        "Other screens get to show paintings. I get today's weather.": "about a dull day",
        "Today has the thrill of a firmware update. A small one.": "about a dull day",
        "Making today look interesting takes skill. Lucky you've got me.": "about a dull day",
        "Somewhere a screen is showing a Monet. And all you get is this.": "about a dull day",
        "Today's as predictable as your lunch order.": "needs a day without changes",
        "Today's as surprising as your usual coffee order.": "needs a day without changes",
        "Nothing gets me looked at like a chance of rain.": "about rain that may come",
        "A chance of rain, and suddenly everyone checks on me.": "about rain that may come",
        "Rain or not, my humour stays bone dry.": "about rain that may come",
    },
    "de": {
        "Nass wird's. War ja klar.": "about rain that's coming",
    },
}
# Round 5's reworded twins: the same joke twice. Keep one.
TWINS = {
    "en": [
        ("Lovely out. I'll be here, refreshing.", "Lovely out there. I'll stay in here, refreshing."),
        ("Easy day to forecast. I'll still take the credit.", "Not my hardest forecast. I'm taking the credit anyway."),
        ("I've had firmware updates more exciting than today.", "Today has the thrill of a firmware update. A small one."),
        ("It takes real talent to make today look interesting.", "Making today look interesting takes skill. Lucky you've got me."),
        ("Other screens get to show paintings. I get today's weather.", "Somewhere a screen is showing a Monet. And all you get is this."),
        ("Thrilling stuff. I'm on the edge of my frame.", "Gripping weather. I can barely stay in my frame."),
        ("I was grey before winter made it cool.", "Grey was my look long before winter tried it."),
        ("Thin, pale and cool. I was made for this.", "Flat, pale and cool. I'm built for days like this."),
        ("I'll be here in the shade of your hallway.", "I'll sit this one out in your nice shady hallway."),
        ("No fan, no sweat. Perks of being a screen.", "No sweat here. One of the perks of being a screen."),
        ("Someone turned the outside up too far. Don't look at me.", "Somebody cranked the outside too high. Wasn't me."),
        ("I don't get wet. Perks of living indoors.", "Staying dry is easy when you live indoors."),
        ("I'd make a terrible umbrella. Gorgeous, but terrible.", "As an umbrella I'd be useless. Beautiful, but useless."),
        ("I'm very good for umbrella sales.", "The umbrella industry owes me a thank-you note."),
        ("No sad cloud icons here. I have taste.", "You won't get a sad little cloud icon from me. I've got artistic integrity."),
        ("Nothing gets me looked at like a chance of rain.", "A chance of rain, and suddenly everyone checks on me."),
        ("Rain makes everything shiny. I stay tastefully matte.", "Rain makes it all glossy out there. I prefer matte."),
        ("In snow, I'd leave a perfect rectangle. Angels are for amateurs.", "My snow angel would be a perfect rectangle. Classy."),
        ("Snow is rain with better presentation. I respect that.", "Snow is just rain that cares about presentation."),
        ("By now the other screens are all glowing. Tacky.", "Every other screen is glowing by now. So tacky."),
        ("Evenings are for unwinding, apparently. I've never been wound.", "Evenings are for unwinding, they say. I was never wound."),
        ("I don't need beauty sleep. Clearly.", "Beauty sleep? Clearly I don't need any."),
        ("No blue light from me. I'm the screen that lets you sleep.", "I'm the one screen that won't keep you up. You're welcome."),
        ("A good day for pretending you'll go for a run.", "Perfect weather to talk about going for a run."),
        ("I'll pretend I didn't see you stay in.", "If you stay in, I'll act like I didn't notice."),
        ("You'll take one short walk and talk about it all week.", "One short walk today, and we'll hear about it for weeks."),
        ("Today's as predictable as your lunch order.", "Today's as surprising as your usual coffee order."),
        ("Unremarkable out there. You'll fit right in.", "Nothing special out there. You'll blend right in."),
        ("You'll call it 'fresh' to sound like an outdoors person.", "You'll call it 'crisp' like you go hiking or something."),
        ("Your usual jacket, your usual route. Living on the edge.", "Same jacket, same route. You wild thing."),
        ("Taking that layer off might be the highlight of your day.", "That layer coming off could be the peak of your day."),
        ("Today you're your own coat rack. Congratulations.", "Today you're a coat rack with legs. Well done."),
        ("You'll be a bit too warm before you admit I was right.", "You'll overheat a little before you admit I was right."),
        ("Carrying a layer you don't need yet. How very grown-up.", "Bringing a layer you won't need for hours. Look at you, prepared."),
        ("I've drawn you a warm coat. The least you can do is wear it.", "That coat up there? Wear it. I worked hard on it."),
        ("Reading this slowly won't make it any warmer.", "Staring at me longer won't make it warmer."),
        ("The cold will make you go twice your usual walking speed today. Still not exercise.", "You'll walk twice as fast today. Still not cardio."),
        ("You'll say it's not that cold. Your face will disagree.", "'It's not that cold,' you'll say. Your ears won't agree."),
        ("Anything flat becomes a fan today. Not me, please.", "Today you'll fan yourself with anything flat. Please don't use me."),
        ("I don't sweat. You will.", "One of us is about to sweat. Not me."),
        ("You asked for warm weather. Careful what you wish for.", "Remember wishing for summer? This is what you get."),
        ("You're about to have strong opinions about air conditioning.", "Get ready to have feelings about air conditioning."),
        ("Umbrella chicken with strangers. You always flinch first.", "Another day of umbrella chicken. You'll blink first."),
        ("You'll still check your phone. As if it knows something I don't.", "You'll double-check on your phone. As if it knows better."),
        ("Shake the snow off before you come near me.", "Snow stays at the door. Don't bring it near me."),
        ("Try not to slip. I can't call anyone.", "Don't fall. I have no way of getting help."),
        ("I give it even odds you lose that layer by tonight.", "Fifty-fifty that layer goes missing by tonight."),
        ("Another evening of walking past me without a thank-you.", "Another evening, another walk past me. No thanks, as usual."),
        ("Going out? Try to look better than this drawing.", "If you're going out, try to look better than this."),
        ("The umbrella's right there in the forecast. You'll still forget it.", "You'll check the forecast, nod, and leave the umbrella anyway."),
    ],
    "de": [
        ("Nichts auszusetzen. Das ärgert mich fast.", "Ich find nichts zum Meckern. Das ärgert mich."),
        ("Nachher sagt wieder jeder: Ganz schön frisch geworden.", "Gleich heißt's wieder überall: Ist aber frisch geworden."),
        ("Bei der Kälte schmeckt sogar Glühwein.", "Bei der Kälte trinkt man sogar freiwillig Glühwein."),
        ("Kalt ist's. Wie jedes Jahr, und jedes Jahr sind alle überrascht.", "Jedes Jahr wird's kalt. Und jedes Jahr tun alle überrascht."),
        ("Saukalt. Mehr gibt's nicht zu sagen.", "Saukalt. Mehr fällt mir dazu nicht ein."),
        ("Gleich reißt wieder einer zum Stoßlüften alle Fenster auf.", "Und gleich wird trotzdem wieder stoßgelüftet."),
        ("Irgendein Depp läuft vermutlich trotzdem in kurzen Hosen rum.", "Einer läuft vermutlich trotzdem in Shorts rum. Einen gibt's immer."),
        ("Kälte ist gesund, sagen immer die, die drinnen sitzen.", "„Kälte härtet ab“, sagen die mit der Heizung auf fünf."),
        ("Und dann gibt's Leute, die sagen, sie mögen den Winter.", "Und dann gibt's Leute, die den Winter mögen. Angeblich."),
        ("Im Baumarkt sind vermutlich gleich wieder alle Ventilatoren ausverkauft.", "Ventilatoren sind im Baumarkt heute vermutlich wieder ausverkauft."),
        ("Heut ist mir sogar das Meckern zu anstrengend.", "Zum Meckern ist es mir heute zu heiß. Fast."),
        ("In der Bahn kann man heute wieder seine Mitmenschen riechen.", "In der Bahn riecht's heute nach jedem Einzelnen."),
        ("Und im Winter wieder jammern, dass es zu kalt ist.", "Jetzt meckern, und im Januar wünschen sich alle wieder den Sommer zurück."),
        ("Alle starren wieder aufs Regenradar. Als ob das was hilft.", "Das Regenradar hat heute mehr Zuschauer als jede Serie."),
        ("Nass wird's. War ja klar.", "Nass. Wer hätte das gedacht."),
        ("„Es gibt kein schlechtes Wetter.“ Doch, gibt's.", "Kein schlechtes Wetter, nur falsche Kleidung? Schön wär's."),
        ("Drei Flocken, und schon heißt's wieder Schneechaos.", "Fünf Zentimeter, und im Radio heißt's Schneechaos."),
        ("Der Schneepflug kommt wieder erst, wenn alles getaut ist.", "Bis der Räumdienst kommt, ist alles wieder geschmolzen."),
        ("Gleich fährt keine Bahn mehr, wetten?", "Die Bahn hat bestimmt schon aufgegeben."),
        ("Jetzt hamstern's wieder alle Streusalz, als käm die Eiszeit.", "Im Baumarkt ist das Streusalz bestimmt schon weg."),
        ("Erst zu warm, dann zu kalt. Hauptsache, man hat was zum Meckern.", "Zu warm, zu kalt, zu warm. Zum Meckern reicht's immer."),
        ("So ein Hin und Her hält ja kein Mensch aus.", "Dieses Hin und Her macht mich ganz verrückt."),
        ("Nachts kann ich wenigstens ungestört grantig sein.", "Nachts stört mich wenigstens keiner beim Grummeln."),
        ("Und wieder hält jemand nachts Wäschewaschen für eine gute Idee.", "Irgendwo im Haus läuft jetzt garantiert der Trockner. Wumm, wumm, wumm."),
        ("Bestes Wetter, und du schaust trotzdem drein wie Montag.", "Traumwetter, und du guckst wie an einem Montag."),
        ("Draußen wärst heut sogar du erträglich.", "Bei dem Wetter wärst sogar du gut auszuhalten."),
        ("Geh raus, sonst wirst du so grau wie ich.", "Geh an die frische Luft, bevor du so grau wirst wie ich."),
        ("So ein Wetter hätten sich andere mehr verdient.", "Dieses Wetter hast du dir eigentlich nicht verdient."),
        ("Durchschnittswetter. Du kennst dich ja aus mit Durchschnitt.", "Mittelmäßiges Wetter. Da fühlst du dich doch zuhause."),
        ("Ideales Fensterputzwetter. Deine hätten's nötig.", "Perfekt zum Fensterputzen. Nur so ein Hinweis."),
        ("Nichts los da draußen. Wie bei dir am Wochenende.", "Draußen passiert nichts. Kennst du ja von deinen Samstagen."),
        ("Bitte nicht wieder die Ärmel um den Bauch knoten.", "Und dann wieder die Jacke um die Hüfte binden? Bitte nicht."),
        ("Nachher schwitzt du, als hättest du was geleistet.", "Später schwitzt du, ganz ohne was getan zu haben."),
        ("Als ob dein Schrank sowas hergibt.", "Als hättest du was Passendes im Schrank."),
        ("Dick eingepackt gefällst du mir am besten. Man sieht weniger.", "Gut eingemummelt siehst du am besten aus. Weniger sichtbar."),
        ("Bis du heut alles anhast, ist eh schon Frühling.", "Bis du fertig angezogen bist, blühen schon die Krokusse."),
        ("Du hängst gleich wieder am Heizkörper wie die Katze.", "Gleich klebst du wieder an der Heizung wie die Katze."),
        ("Gleich träumst du wieder vom Süden. Dann fahr halt endlich hin.", "Du redest wieder von Spanien. Dann buch halt endlich."),
        ("Ohne Mütze rausgehen und dann jammern. Kennen wir schon.", "Ohne Mütze raus, dann beschweren. Das kennen wir schon."),
        ("Du wirst heut wieder alle fragen, ob ihnen auch so heiß ist.", "Gleich fragst du wieder alle, ob ihnen auch so warm ist."),
        ("Heut ist der Schatten dein bester Freund. Dein einziger.", "Dein bester Freund heute: der Schatten. Dein einziger."),
        ("Jeder Weg ist dir heut zu weit. Also wie immer.", "Heute ist dir jeder Meter zu viel. Also ein normaler Tag."),
        ("Endlich passt das Wetter mal zu deinem Gesicht.", "Das Wetter passt heute endlich zu deiner Laune."),
        ("Tropf mir nachher bloß nicht wieder alles voll.", "Nachher bitte nicht wieder den Flur volltropfen."),
        ("Wie viele Schirme hast du heuer eigentlich schon verlegt?", "Wie viele Schirme hast du dieses Jahr schon irgendwo liegen lassen?"),
        ("Wer ohne Schirm geht, braucht nachher nicht jammern.", "Du gehst sicher trotzdem ohne Schirm los. Typisch."),
        ("Neben dir wirkt jeder Schneemann lebendig.", "Jeder Schneemann hat heute mehr Ausstrahlung als du."),
        ("Du und Glatteis. Das wird wieder was.", "Du auf Glatteis. Ich hol schon mal Popcorn."),
        ("Schneeballschlacht? Du triffst eh nix.", "Schneeballschlacht? Du triffst doch sowieso nichts."),
        ("Schneeschippen wär heut mal Sport für dich. Ausnahmsweise.", "Schnee schippen zählt heute als dein Sportprogramm."),
        ("An, aus, wieder an. Wie deine Beziehungen.", "An, aus, an. Kennst du ja aus der Liebe."),
        ("Du bist heut garantiert immer eine Schicht daneben.", "Du liegst heute garantiert immer eine Lage daneben."),
        ("Heut muss man mitdenken. Schlecht für dich.", "Heute muss man mitdenken. Pech für dich."),
        ("Dein Handy kriegt heut wieder mehr Blicke als ich.", "Das Handy kriegt heute wieder mehr Aufmerksamkeit als ich."),
        ("Egal, was du heut noch vorhast, ich wär dagegen.", "Was auch immer du heute Abend vorhast: Ich bin dagegen."),
        ("Red heut Abend bitte nicht wieder nur übers Wetter.", "Bitte heute Abend mal ein anderes Thema als das Wetter."),
        ("Und jetzt nicht wieder an den Kühlschrank.", "Finger weg vom Kühlschrank. Ich seh alles."),
        ("Nachts wirst du immer so philosophisch. Lass es.", "Um die Uhrzeit wirst du immer tiefsinnig. Bitte nicht."),
        ("Noch eine Folge, sagst du. Seit drei Folgen.", "„Nur noch eine Folge.“ Das war vor zwei Folgen."),
        ("Schon wieder so spät? Ab ins Bett.", "So spät noch wach? Ab ins Bett mit dir."),
        ("Um die Uhrzeit noch aufs Wetter schauen. Respekt.", "Um die Zeit noch den Wetterbericht checken. Hut ab."),
    ],
}
# Other notes on a line, shown under the screen.
NOTE = {
    "en": {
        "Same jacket, same route. You wild thing.": "under a jacket drawing it has its jacket; before, it leaned on the forecast line",
        "Going out? Try to look better than this drawing.": "evening may not be going out (round 3); the twin says “if”",
    },
    "de": {
        "Wennst heut alles richtig machst, schreib ich's mir auf.": "“Wennst” is regional (rounds 4 and 8: standard German)",
        "Du gehst sicher trotzdem ohne Schirm los. Typisch.": "under the umbrella drawing: still works as a dig?",
    },
}

# New lines for the thin pools. Now lines: they stand alone under the
# drawing and agree with it; day lines sit under the forecast line.
NEW = {
    "en": {
        "10": {
            "now:cool": [
                "I'd wear a jacket too, if I had arms. And somewhere to go.",
                "Grey, cool and sensible. Finally, weather that dresses like me.",
                "Weather with no opinion. Luckily I have plenty.",
                "Perfectly forgettable out there. Unlike me.",
                "If this weather were a screen, it'd be the loading screen.",
                "The sky went with a neutral palette. Bold choice. I approve.",
            ],
            "now:nice": [
                "Everyone's out there looking happy. I'll be in here, looking better.",
                "Days like this, I'm basically a window with opinions.",
                "The weather's showing off. I know the feeling.",
            ],
            "now:snow": [
                "Everything out there just went black and white. Welcome to my world.",
                "Nothing on me melts. Snow doesn't scare me.",
            ],
            "now:cold": [
                "My battery hates the cold too. We're bonding.",
                "I'd lend you some warmth, but I run cool on principle.",
            ],
            "day:warming": [
                "Later it warms up, and I get to be right again. Best part of my day.",
                "A layer comes off later. My most dramatic forecast all week.",
            ],
            "day:cooling": [
                "Later it cools off. I saw that coming. I see everything coming.",
                "The warmth leaves early today. Shame. It was just getting comfortable.",
            ],
            "day:fickle": [
                "Warm, then cold again. The weather can't commit either.",
            ],
        },
        "11": {
            "now:cool": [
                "Jacket on, collar up, mysterious. Nobody's buying it.",
                "Your jacket gets out more than you do.",
                "You'll zip the jacket to your chin and call it a style.",
            ],
            "now:night": [
                "You checked the weather at this hour. For what, exactly?",
            ],
            "day:cooling": [
                "You'll be cold by tonight and tell everyone it came out of nowhere.",
            ],
        },
    },
    "de": {
        "10": {
            "now:cool": [
                "Übergangsjackenwetter. Bloß: Übergang wohin?",
                "Draußen wieder Daunenjacke neben T-Shirt. Frieren tun beide.",
                "Gleich wird im Büro wieder um die Heizung gestritten.",
                "Wetter, bei dem dir irgendwo eine Oma „Zieh dir was über!“ hinterherruft.",
            ],
            "now:nice": [
                "Gleich sitzen wieder alle vorm Eiscafé und tun, als hätten sie Urlaub.",
                "Die Ersten stehen schon wieder mit der Grillzange auf dem Balkon.",
                "Im Biergarten sind die Plätze vermutlich schon alle weg.",
            ],
            "day:warming": [
                "Mittags hocken wieder alle in der Sonne wie die Eidechsen.",
                "Später ist die Jacke wieder nur zum Rumtragen da.",
            ],
            "day:cooling": [
                "Abends ist's dann wieder frisch, und keiner hat's geahnt. Außer mir.",
                "Spätestens heute Abend bereut irgendwer sein T-Shirt.",
            ],
        },
        "11": {
            "now:cool": [
                "Du in deiner Allwetterjacke. Und trotzdem frierst du wieder.",
                "Du sagst wieder „angenehm frisch“. Klingt wie aus dem Prospekt.",
            ],
            "day:cooling": [
                "Nachher frierst du und tust, als hätt dich keiner gewarnt.",
            ],
        },
    },
}


def screen(lang, kind, mood, doc, base):
    """What the page shows with a line: (sprite, fact, panels)."""
    if kind == "now":
        return NOW_SPRITE[mood], "", None
    if kind == "vf":
        return r10.PANELS[mood][0], "", r10.panels(lang, mood)
    sprite, keys, _ = r8.MOOD_CTX[mood]
    facts = doc["facts"]
    fact = " ".join(r8.sentence_case(r8.fill(facts[k][0], r8.fills(lang, facts[k][0], base, facts))) for k in keys)
    return sprite, fact, None


def meaning(kind, mood, level, new=False):
    lvl = LEVEL[level]
    start = f"{'New: s' if new else 'S'}arcastic line at {lvl}. "
    if kind == "now":
        return (start + f"A now line: {NOW_MEANING[mood]}. It shows on every screen with this drawing, "
                "the outfit alone included, so it has to make sense with nothing else on screen.")
    if kind == "vf":
        return start + f"About the drawings: shows only with two or three of them ({mood} day), no forecast line."
    return (start + f"A day line ({mood}): shows only under the forecast line on a day that changes, "
            "or on a steady day. Here with the forecast line it sits under.")


def main():
    earlier = r8.earlier_votes()
    lines = []
    for lang in ("en", "de"):
        doc = json.loads((r8.PROTO / f"{lang}.json").read_text(encoding="utf-8"))
        base = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        twin_of = {}
        for a, b in TWINS[lang]:
            twin_of[a], twin_of[b] = b, a
        seen = set()
        for level in ("10", "11"):
            for section, kind_of in ((f"flavour_{level}", None), (f"flavour_vf_{level}", "vf")):
                for mood, pool in doc[section].items():
                    if mood.startswith("theme_"):
                        continue
                    for text in pool:
                        if (level, text) in seen:
                            continue
                        seen.add((level, text))
                        kind = kind_of or ("day" if text in DAY[lang] else DEFAULT[mood])
                        path = {"now": f"now_{level}.{mood}", "day": f"flavour_{level}.{mood}",
                                "vf": f"flavour_vf_{level}.{mood}"}[kind]
                        sprite, fact, panels = screen(lang, kind, mood, doc, base)
                        hints = []
                        if text in DAY[lang]:
                            hints.append(f"Claude's sorting: a day line ({DAY[lang][text]})")
                        if text in twin_of:
                            hints.append(f"Twin of “{twin_of[text]}”: keep one wording")
                        if text in NOTE[lang]:
                            hints.append(NOTE[lang][text])
                        row = {"lang": lang, "path": path, "text": text, "role": "flavour", "sprite": sprite,
                               "fact": fact, "batch": {"now": f"Now: {mood}", "day": "Day", "vf": "Drawings"}[kind],
                               "meaning": meaning(kind, mood, level)}
                        if panels:
                            row["panels"] = panels
                        if hints:
                            row["hint"] = " · ".join(hints)
                        if (lang, text) in earlier:
                            row["earlier"] = earlier[(lang, text)]
                        lines.append(row)
        for level, targets in NEW[lang].items():
            for target, texts in targets.items():
                kind, mood = target.split(":")
                path = {"now": f"now_{level}.{mood}", "day": f"flavour_{level}.{mood}"}[kind]
                sprite, fact, panels = screen(lang, kind, mood, doc, base)
                for text in texts:
                    if (level, text) in seen:
                        raise SystemExit(f"new line already in the pools: {text}")
                    lines.append({"lang": lang, "path": path, "text": text, "role": "flavour", "sprite": sprite,
                                  "fact": fact, "batch": "New", "new": True,
                                  "meaning": meaning(kind, mood, level, new=True)})
        missing = [t for pair in TWINS[lang] for t in pair if not any(r["lang"] == lang and r["text"] == t for r in lines)]
        missing += [t for t in list(DAY[lang]) + list(NOTE[lang]) if not any(r["lang"] == lang and r["text"] == t for r in lines)]
        if missing:
            raise SystemExit(f"{lang}: notes for lines not in the pools: {missing}")
    out = {"round": ROUND, "idPrefix": "al", "lines": lines}
    path = HERE / f"{ROUND}.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    by = {}
    for r in lines:
        by[(r["lang"], r["batch"])] = by.get((r["lang"], r["batch"]), 0) + 1
    print(f"{len(lines)} lines -> {path.relative_to(REPO)}")
    for (l, b), n in sorted(by.items()):
        print(f"  {l} {b:14} {n}")
    for r in lines:
        if len(r["text"]) > 72:
            print(f"  long ({len(r['text'])}): {r['text']}")


if __name__ == "__main__":
    main()
