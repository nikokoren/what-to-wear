#!/usr/bin/env python3
"""
Writes the voice audition round: 2026-10-voices.json (the lines, with a
letter per voice) and 2026-10-voices.key.json (which letter is which voice).

Five voices per language, written separately: the German voices are not
the English ones translated. Each voice gets the same four moods, two
lines per mood at On (10) and at 11.

Don't open the key until the votes are in.
"""

import json
import pathlib
import random

HERE = pathlib.Path(__file__).resolve().parent
ROUND = "2026-10-voices"

VOICES = {
    "en": {
        "friend": ("The friend: warm, plain, a little wry. At 11 it teases like someone who likes you.", {
            "nice": (["Good one today. Get outside if you can.", "Nothing to plan around. Enjoy that."],
                     ["Perfect day, and I know you'll spend it indoors.", "Great weather. Try to look like you're enjoying it."]),
            "wet": (["A damp one. Not a day for your nice shoes.", "Wet out there at some point. Give yourself five extra minutes."],
                    ["Umbrella by the door. Yes, that one. Take it.", "You'll check the window five times and still get wet."]),
            "cold": (["Cold one. Wear the warm socks.", "Scarf up to the nose today."],
                     ["You'll say 'it's not that cold' and regret it by the corner.", "Gloves. The pair, not just the one you found."]),
            "evening": (["Day's done. Nothing else coming.", "Quiet evening out there. Same in here, hopefully."],
                        ["You made it. Pajamas are now a valid outfit.", "Evening. You're not going anywhere, are you."]),
        }),
        "deadpan": ("The deadpan: as few words as possible, delivered flat.", {
            "nice": (["Nice. Noted.", "Fine all day. Unusual."],
                     ["Good weather. Try not to waste it. You will.", "Nothing to complain about. Do your best."]),
            "wet": (["Wet. As expected.", "Rain is involved today."],
                    ["Wet. Bring the umbrella or a good excuse.", "Rain. You'll act surprised. Don't."]),
            "cold": (["Cold. Dress like it.", "Cold. That's the whole update."],
                     ["Cold. You'll still try the thin jacket.", "Cold. Wear the ugly hat. Nobody's looking at you."]),
            "evening": (["Evening. Nothing to report.", "That was the day."],
                        ["Day over. You did the minimum. Fine.", "Evening. Go to bed at a reasonable hour. You won't."]),
        }),
        "nerd": ("The weather nerd: true weather trivia, and delighted by it.", {
            "nice": (["A steady day. Meteorologists call this boring. I call it lovely.", "'Fair weather' is an actual forecast term. Today qualifies."],
                     ["Ideal conditions. Wasted on people who stay indoors. Hint.", "Low drama in the atmosphere today. Unlike your group chat."]),
            "wet": (["That smell after rain has a name: petrichor.", "Raindrops aren't teardrop-shaped. More like hamburger buns."],
                    ["Raindrops fall faster than you can run. Don't try.", "Fun fact: umbrellas only work if you bring them."]),
            "cold": (["Wind makes cold feel colder. Cover the bits that stick out.", "Cold air is dry air. Lip balm counts as a weather precaution."],
                     ["You don't lose most heat through your head. Wear the hat anyway.", "Fingers lose heat fast. You'll still leave the gloves."]),
            "evening": (["Air cools fastest after sunset. Blanket weather, technically.", "Today's weather is done. Tomorrow's is already forming."],
                        ["Nights are when the air settles down. Take the hint.", "Tonight's forecast: you, ignoring tomorrow's forecast."]),
        }),
        "narrator": ("The narrator: epic, nature-documentary drama about ordinary weather.", {
            "nice": (["And on this day, the weather asked nothing of anyone.", "A rare, gentle day settles over the land."],
                     ["Bards will sing of this day. You will mostly scroll.", "The sun rose, the day was perfect, and you checked your phone."]),
            "wet": (["And the rains came, as they always do, to the people of the city.", "Somewhere, a puddle waits for the perfect shoe."],
                    ["Our hero stepped out in canvas shoes. A bold choice. A wet one.", "Brave traveller, you left without an umbrella. The sky noticed."]),
            "cold": (["Winter tightened its grip on the city.", "The cold arrived like an uninvited guest, and stayed."],
                     ["Our hero met the cold in a thin jacket. A tragedy in one act.", "The ancient scrolls say: wear a hat. You never read the scrolls."]),
            "evening": (["And so the day draws to a close, uneventfully.", "Night falls. The weather rests. So should you."],
                        ["As night fell, our hero chose the sofa. Again.", "The day ends. Your to-do list does not."]),
        }),
        "screen": ("The screen: the TRMNL on your wall, talking about itself. Carrot-style at 11.", {
            "nice": (["I'm a screen on a wall. Even I'd go outside today.", "Lovely out. I'll be here, refreshing."],
                     ["Perfect weather. I can't leave the wall. What's your excuse?", "Go outside. I'll pretend I didn't see you stay in."]),
            "wet": (["I don't get wet. Perks of living indoors.", "Rain today. I'll be on the wall, dry and smug."],
                    ["I can't hold an umbrella. You can. Think about that.", "I refresh every few minutes. Wet socks don't."]),
            "cold": (["Cold out. I'm staying on the wall where it's warm.", "Batteries hate the cold. So do you. Dress warm."],
                     ["I'd wear a hat if I had a head. You have a head.", "I've drawn you a warm coat. The least you can do is wear it."]),
            "evening": (["Nothing new from me tonight. Sleep well.", "Evening. I'll keep showing this until morning."],
                        ["I'll be here all night. Unlike your motivation.", "You've looked at me a lot today. Go to bed."]),
        }),
    },
    "de": {
        "oma": ("Die Oma: fürsorglich, ein bisschen altmodisch. Bei 11 nervt sie liebevoll.", {
            "nice": (["Schönes Wetter, Kind. Geh ein bisschen an die frische Luft.", "So ein Tag, da hängt man die Wäsche raus."],
                     ["So ein schöner Tag. Ruf mal wieder an, wenn du schon nicht vorbeikommst.", "Bei so einem Wetter hab ich früher den ganzen Garten gemacht."]),
            "wet": (["Nimm einen Schirm mit, Kind. Und eine Jacke mit Kapuze.", "Nasse Füße, und schon hast du dir was geholt."],
                    ["Wenn du nass wirst, sag nicht, ich hätt's nicht gesagt.", "Mit nassen Haaren rausgehen? Nur über meine Leiche."]),
            "cold": (["Zieh dir ein Unterhemd an. Das schadet nie.", "Bei der Kälte gehört eine Mütze auf den Kopf. Punkt."],
                     ["Ohne Mütze? Dann wundere dich nicht über die Ohren.", "Ich hab dir extra den Schal gestrickt. Trag ihn auch."]),
            "evening": (["Jetzt aber ab ins Warme. Und iss was Ordentliches.", "Der Tag ist rum. Mach dir einen Tee."],
                        ["Nicht so lange aufbleiben. Ich seh das, wenn du müde bist.", "Hast du heute überhaupt was gegessen? Na also."]),
        }),
        "grantler": ("Der Grantler: findet an jedem Wetter was, mit österreichisch-bayerischem Einschlag.", {
            "nice": (["Schön ist's. Wird schon wieder was passieren.", "Mild, ruhig, alles gut. Verdächtig."],
                     ["Jetzt passt's Wetter einmal, und du findest sicher trotzdem was.", "Perfekter Tag. Freu dich halt, wenn's geht."]),
            "wet": (["Regen. Wieder. Natürlich.", "Nass ist's. War ja klar."],
                    ["Wennst ohne Schirm gehst, brauchst nachher nicht jammern.", "Nass. Und die Leut' fahren wieder, als hätten's nie Regen gesehen."]),
            "cold": (["Saukalt. Mehr gibt's nicht zu sagen.", "Kalt ist's. Wie jedes Jahr, und jedes Jahr sind alle überrascht."],
                     ["Ohne Haube rausgehen und dann jammern. Kenn ma schon.", "Kalt. Und du in der dünnen Jacke. Na servas."]),
            "evening": (["Abend. Endlich a Ruh.", "Der Tag is gegessen."],
                        ["Feierabend. Jetzt lass mich auch in Ruh.", "Schau nicht so. Morgen is eh wieder Wetter."]),
        }),
        "wetterfrosch": ("Der Wetterfrosch: Fernseh-Wettermoderator mit allen Floskeln. Bei 11 verliert er die Geduld mit dir.", {
            "nice": (["Und nun das Wetter: ruhig, freundlich, keine Überraschungen.", "Ein Hoch macht's heute ruhig. Schöner wird's nicht."],
                     ["Bestes Wetter. Beschwerden bitte trotzdem an die Redaktion.", "Ich hab heute nur gute Nachrichten. Bitte nicht dran gewöhnen."]),
            "wet": (["Ein Tiefausläufer bringt Nässe. Klingt harmlos, ist es selten.", "Und schon wieder ein Tief. Ich kann nichts dafür."],
                    ["Ich sag den Regen an, du ignorierst ihn. Unser kleines Ritual.", "Regenwahrscheinlichkeit: hoch. Deine Laune danach: tief."]),
            "cold": (["Polarluft hat uns fest im Griff. Klingt dramatisch, ist es auch.", "Gefühlt noch kälter als gemessen. Das Gefühl hat recht."],
                     ["Meine Empfehlung: Mütze. Deine Entscheidung: vermutlich falsch.", "Kein Rekord, aber kalt genug für deinen ersten Schnupfen."]),
            "evening": (["Das war das Wetter für heute. Schönen Abend.", "Für heute keine weiteren Meldungen."],
                        ["Morgen gibt's wieder Wetter. Ob du hinschaust, ist die andere Frage.", "Ende der Sendung. Du darfst jetzt umschalten."]),
        }),
        "bauernregel": ("Die Bauernregel: jeder Satz ein gereimter Spruch. Bei 11 reimt er gegen dich.", {
            "nice": (["Ist der Himmel ruhig und still, zieh dich an, wie man es will.", "Bleibt das Wetter, wie es ist, freu dich, dass du draußen bist."],
                     ["Ist das Wetter einmal fein, fällt dir sicher Arbeit ein.", "Scheint das Glück dir ins Gesicht, nutzt du's wieder sicher nicht."]),
            "wet": (["Hängt der Himmel grau und schwer, muss der Regenschirm schnell her.", "Wenn es tropft und wenn es rinnt, freut sich nur das Gummistiefel-Kind."],
                    ["Gehst du ohne Schirm hinaus, siehst du später nass dann aus.", "Bist du nass bis auf die Knochen, hast du's wieder selbst verbrochen."]),
            "cold": (["Ist die Nase rot gefroren, hilft ein Schal bis zu den Ohren.", "Handschuh, Schal und Mütze an, dann kommt der Frost nicht an dich ran."],
                     ["Gehst du ohne Mütze raus, frieren dir die Ohren aus.", "Wer im Winter Sneaker trägt, hat sich das gut überlegt. Nicht."]),
            "evening": (["Kommt der Abend still daher, braucht's vom Wetter heut nichts mehr.", "Geht die Sonne schlafen bald, mach's ihr nach, sonst wird es kalt."],
                        ["Wer am Abend Serien schaut, hat sich morgen früh verhaut.", "Gehst du spät erst in das Bett, ist der Morgen nicht so nett."]),
        }),
        "kumpel": ("Der Kumpel: direkt, locker, duzt dich wie ein alter Freund. Bei 11 auch mal derb.", {
            "nice": (["Bestes Wetter, Alter. Raus mit dir.", "Heute passt einfach alles. Genieß es."],
                     ["Grillwetter. Und wer hat wieder nichts eingekauft? Genau.", "Heute keine Ausreden. Fahrrad, nicht Bahn."]),
            "wet": (["Nass heute. Kapuze auf und durch.", "Regen. Nicht schön, aber auch nicht tragisch."],
                    ["Ohne Schirm? Mutig. Und dumm.", "Nasse Socken sind kein Lifestyle. Schirm mit."]),
            "cold": (["Richtig kalt heute. Pack dich ein.", "Kalt. Jacke zu, Mütze auf, los."],
                     ["Arschkalt. Und du willst echt ohne Mütze? Viel Glück.", "Ohne Handschuhe? Deine Finger hassen dich jetzt schon."]),
            "evening": (["Feierabend. Füße hoch.", "Für heute ist Schluss. Chill mal."],
                        ["Abend, Alter. Morgen früh raus, also nicht wieder bis zwei.", "Pizza bestellen ist heute erlaubt. Ich sag's keinem."]),
        }),
    },
}
LETTERS = {"en": "ABCDE", "de": "FGHIJ"}


def main():
    rng = random.Random(ROUND + ":2")
    lines, key = [], {}
    for lang, voices in VOICES.items():
        names = list(voices)
        rng.shuffle(names)
        for letter, name in zip(LETTERS[lang], names):
            desc, moods = voices[name]
            key[letter] = {"lang": lang, "voice": name, "description": desc}
            for mood, (on, eleven) in moods.items():
                for level, texts in (("10", on), ("11", eleven)):
                    for text in texts:
                        lines.append({"lang": lang, "path": f"flavour_{level}.{mood}", "text": text, "batch": letter})
    (HERE / f"{ROUND}.json").write_text(json.dumps({"round": ROUND, "lines": lines}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (HERE / f"{ROUND}.key.json").write_text(json.dumps(key, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(lines)} lines, {len(key)} voices")


if __name__ == "__main__":
    main()
