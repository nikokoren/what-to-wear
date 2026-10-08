#!/usr/bin/env python3
"""
Round 2, two audits on one page:

  2026-10-voices-2  the flavour line, narrowed to what won round 1 and
                    rewritten under its lessons (docs/BRIEF.md)
  2026-10-facts     the fact line: six styles, the same eight real
                    situations in each

Writes <round>.json and <round>.key.json for both. Don't open the keys,
or this file, until the votes are in.
"""

import json
import pathlib
import random

HERE = pathlib.Path(__file__).resolve().parent
MOODS = ["nice", "mild", "cold", "hot", "wet", "snow", "fickle", "evening", "night"]

VOICES = {
    "en": {
        "screen": ("The screen: the TRMNL on your wall, talking about itself.", {
            "nice": (["I'm a screen on a wall. Even I'd go outside today.", "Lovely out. I'll be here, refreshing."],
                     ["Perfect weather. I can't leave the wall. What's your excuse?", "I'll pretend I didn't see you stay in."]),
            "mild": (["Nothing to report. I'll keep refreshing anyway, out of habit.", "A day with no surprises. I've shown worse."],
                     ["Even I'm bored, and I'm a screen.", "Unremarkable out there. You'll fit right in."]),
            "cold": (["I'm staying on the wall where it's warm.", "I don't feel the cold. You do. That's the difference between us."],
                     ["I've drawn you a warm coat. The least you can do is wear it.", "You'll stand at the door and argue with me. I'll win."]),
            "hot": (["No fan, no sweat. Perks of being a screen.", "I'll be here in the shade of your hallway."],
                    ["I don't sweat. You will. I'll be here, judging.", "You'll come home looking less crisp than this drawing."]),
            "wet": (["I don't get wet. Perks of living indoors.", "I'll be on the wall, dry and smug."],
                    ["I refresh every few minutes. Wet socks don't.", "I'd hold the umbrella for you, but, you know. Wall."]),
            "snow": (["I've never seen snow. Describe it to me later.", "Snow is basically e-ink for the outdoors. I approve."],
                     ["Snow looks great on e-ink. Less great on your shoes.", "Try not to slip. I can't call anyone."]),
            "fickle": (["Make up your mind, weather. Some of us refresh on a schedule.", "I'll keep you posted. That's literally all I do."],
                       ["You'll trust me in the morning and blame me by lunch.", "I've changed this drawing in my head twice already."]),
            "evening": (["Evening. I'm still here. Of course I am.", "Off somewhere? I'll hold the wall down."],
                        ["Going out? Look better than this drawing.", "Whatever your plans are, I'm not invited. Fine."]),
            "night": (["Nothing new from me tonight. Sleep well.", "Late. I'm on battery, you're on coffee. Let's both rest."],
                      ["You've looked at me a lot today. Go to bed.", "Still up? I'm a wall decoration and even I'm tired."]),
        }),
    },
    "de": {
        "grantler": ("Der Grantler, ohne Dialekt: findet an jedem Wetter was.", {
            "nice": (["Schönes Wetter. Ich trau dem Frieden nicht.", "Nichts auszusetzen. Das ärgert mich fast."],
                     ["Jetzt passt's Wetter einmal, und du findest sicher trotzdem was.", "Bestes Wetter, und du schaust trotzdem drein wie Montag."]),
            "mild": (["Nicht schön, nicht schlimm. Typisch.", "Ein Wetter wie Leitungswasser."],
                     ["Durchschnittswetter. Du kennst dich ja aus mit Durchschnitt.", "Nichts los da draußen. Wie bei dir am Wochenende."]),
            "cold": (["Saukalt. Mehr gibt's nicht zu sagen.", "Kalt ist's. Wie jedes Jahr, und jedes Jahr sind alle überrascht."],
                     ["Ohne Mütze rausgehen und dann jammern. Kennen wir schon.", "Und du wieder in der dünnen Jacke. Na dann viel Spaß."]),
            "hot": (["Zu heiß. Und im Winter wieder jammern, dass es zu kalt ist.", "Schwitzen im Stehen. Ein Traum."],
                    ["Du wirst kleben, schwitzen und dich beschweren. In der Reihenfolge.", "Keine Klimaanlage, du nicht und ich nicht. Wir leiden gemeinsam."]),
            "wet": (["Regen. Wieder. Natürlich.", "Nass ist's. War ja klar."],
                    ["Wer ohne Schirm geht, braucht nachher nicht jammern.", "Du wirst nass. Und dann bin wieder ich schuld."]),
            "snow": (["Schnee. Gleich fährt keine Bahn mehr, wetten?", "Schön zum Anschauen. Zum Gehen weniger."],
                     ["Du und Glatteis. Das wird wieder was.", "Der Gehweg wartet. Der Nachbar schaut schon."]),
            "fickle": (["Warm, kalt, warm. Kann sich auch mal entscheiden.", "Erst zu warm, dann zu kalt. Hauptsache, man hat was zum Meckern."],
                       ["Morgens frierst du, mittags schwitzt du, abends meckerst du. Ich kenn dich.", "Heute trägst du die Jacke mehr spazieren als am Leib."]),
            "evening": (["Abend. Das Wetter ändert sich nicht mehr. Ich mich auch nicht.", "Falls du noch weggehst: Ich bleib hier. Wie immer."],
                        ["Feierabend. Jetzt lass mich auch in Ruhe.", "Ausgehen? Zieh was Schöneres an als das hier."]),
            "night": (["Spät ist's. Ich zeig das hier trotzdem weiter.", "Nachts passiert eh nichts. Außer du schaust mich an."],
                      ["Schon wieder so spät? Ab ins Bett. Das Wetter wartet nicht auf dich.", "Um die Uhrzeit noch aufs Wetter schauen. Respekt. Oder Problem."]),
        }),
        "moderator": ("Der grantige Wetterfrosch: TV-Wettermoderator, der seinen Job satt hat.", {
            "nice": (["Und nun das Wetter. Gibt nichts zu meckern. Leider.", "Ein Hoch. Ich hab extra zweimal nachgeschaut, ob das stimmt."],
                     ["Ich hab heute nur gute Nachrichten. Bitte nicht dran gewöhnen.", "Bestes Wetter. Beschwerden bitte trotzdem an die Redaktion."]),
            "mild": (["Wetterlage: unspektakulär. Meine Moderation: ebenso.", "Heute keine Unwetterwarnung. Nur Mittelmaß."],
                     ["Ich könnte dir jetzt was von Luftdruck erzählen. Du hörst eh nicht zu.", "Wenig Wetter heute. Mehr Zeit für deine Ausreden."]),
            "cold": (["Polarluft hat uns fest im Griff. Klingt dramatisch, ist es auch.", "Arktische Luft. Ich hab sie nicht bestellt."],
                     ["Kein Rekord, aber kalt genug für deinen ersten Schnupfen.", "Ich sag's seit Tagen an. Trotzdem stehst du überrascht an der Tür."]),
            "hot": (["Hitzewarnung. Ich moderiere im Anzug. Beneide mich nicht.", "Tropische Werte. Ich bleib im klimatisierten Studio."],
                    ["Viel trinken, Schatten suchen. Sag ich jeden Sommer. Hört keiner.", "Ich zeig dir die Hitzekarte. Sie ist komplett rot. Wie du später."]),
            "wet": (["Und schon wieder ein Tief. Ich kann nichts dafür.", "Ein Tiefausläufer bringt Nässe. Klingt harmlos, ist es selten."],
                    ["Ich sag den Regen an, du ignorierst ihn. Unser kleines Ritual.", "Wenn du nass wirst: Ich hab's angesagt. Zur besten Sendezeit."]),
            "snow": (["Schnee. Die Kollegen vom Verkehrsfunk freuen sich schon.", "Schneefall. Ich hab extra die Wetterkarte in Weiß dabei."],
                     ["Ich hab Schnee angesagt. Du hast Turnschuhe an. Wer hat jetzt recht?", "Glätte. Hinterher heißt's wieder, ich hätt's nicht angesagt."]),
            "fickle": (["Wechselhaft. Das sagen wir Wetterfrösche, wenn wir's selber nicht wissen.", "Erst Hoch, dann Tief. Wie meine Laune."],
                       ["Wechselhaft. Und du ziehst dich an, als gäb's nur ein Wetter. Mutig.", "Ich hab für heute zwei Wetter angesagt. Du hast für keins geplant."]),
            "evening": (["Das war das Wetter für heute. Schönen Abend.", "Noch was vor heute? Das Wetter hält still."],
                        ["Ausgehen? Würd ich auch. Wenn ich nicht im Studio festsäße.", "Abendprognose: Du entscheidest dich wieder in letzter Minute."]),
            "night": (["Sendeschluss. Morgen früh gibt's frisches Wetter.", "Nachtprogramm. Bis morgen früh ändert sich nichts mehr."],
                      ["Um die Uhrzeit schauen nur noch zwei aufs Wetter: ich und du. Geh schlafen.", "Schlaf jetzt. Ich wiederhol die Sendung morgen früh."]),
        }),
    },
}

# Eight real days from station records, as the mock renders them
# (prototypes/fact-flavour). Hours are when each change actually happens.
SITUATIONS = {
    "s1_steady": ("tee_pants_dry", "New York, 2 June, 07:30. Warm and steady all day."),
    "s2_shower": ("jacket_dry", "London, 1 May, 07:30. Jacket off around 9, a shower around noon."),
    "s3_off_on": ("jacket_dry", "Vienna, 22 March, 07:30. Jacket off around 2pm, back on around 8pm."),
    "s4_cooling": ("sweater_dry", "London, 24 September, 07:30. Mild, a jacket needed from about 7pm."),
    "s5_snow": ("bundled_dry", "Minneapolis, 8 January, 07:30. Bitter cold all day, snow from about 11."),
    "s6_hot": ("heat_dry", "Phoenix, 7 June, 07:30. Hot from about 9."),
    "s7_evening": ("coat_dry", "New York, 2 January, 19:30. Steady cold evening."),
    "s8_busy": ("coat_rain", "London, 6 March, 07:30. Raining now, coat off around noon, rain back around 2pm, coat back on around 8pm."),
}
STYLES = {
    "en": {
        "telegram": ("Short sentences, time words (the prototype today).", [
            "Good for the whole day.",
            "Jacket off in two hours. A shower around midday. Take the umbrella.",
            "Jacket off this afternoon, back on tonight.",
            "Jacket needed this evening.",
            "Snow around midday.",
            "Getting hot in two hours. Bring water.",
            "Good for the rest of the evening.",
            "Winter coat off around midday, back on tonight. A dry spell, then rain again this afternoon. Keep the umbrella."]),
        "clock": ("Clock times instead of time words.", [
            "No changes until tonight.",
            "Jacket off around 9am. Shower around noon, so take the umbrella.",
            "Jacket off around 2pm, back on around 8pm.",
            "Jacket needed from about 7pm.",
            "Snow from about 11am.",
            "Hot from about 9am. Bring water.",
            "No changes for the rest of the evening.",
            "Coat off around noon, back on around 8pm. Rain stops soon, back around 2pm. Keep the umbrella."]),
        "timeline": ("A timeline: time, then what changes.", [
            "All day: as shown.",
            "9am: jacket off. Noon: shower, umbrella.",
            "2pm: jacket off. 8pm: jacket back on.",
            "7pm: add a jacket.",
            "11am: snow.",
            "9am: heat. Bring water.",
            "Rest of the evening: as shown.",
            "Now: rain. Noon: coat off. 2pm: rain again. 8pm: coat back on."]),
        "sentence": ("Full, plain sentences.", [
            "What you're wearing works for the whole day.",
            "You can take the jacket off in a couple of hours. There's a shower around midday, so bring the umbrella.",
            "The jacket can come off this afternoon, but you'll want it back tonight.",
            "It cools down this evening, so bring a jacket.",
            "It stays this cold all day, and snow starts around midday.",
            "It gets hot in a couple of hours, so bring water.",
            "What you're wearing works for the rest of the evening.",
            "The coat can come off around midday, but you'll want it back tonight. The rain pauses, then returns this afternoon, so keep the umbrella."]),
        "action": ("What to do or carry first, then why.", [
            "Nothing to carry today.",
            "Take the umbrella for a shower around midday. Jacket off in two hours.",
            "Keep the jacket with you. Off this afternoon, back on tonight.",
            "Bring a jacket for this evening.",
            "Watch your step: snow around midday.",
            "Bring water. It gets hot in two hours.",
            "Nothing to change this evening.",
            "Keep the umbrella and the coat with you. Coat off around midday, back on tonight. Rain returns this afternoon."]),
        "minimal": ("As few words as possible.", [
            "No changes.",
            "Umbrella. Jacket off by 9.",
            "Jacket off at 2, on at 8.",
            "Jacket by 7.",
            "Snow at 11.",
            "Water. Hot by 9.",
            "No changes tonight.",
            "Umbrella. Coat off at noon, on at 8."]),
    },
    "de": {
        "telegram": ("Kurze Sätze, Tageszeiten (der Prototyp heute).", [
            "So bleibt's den ganzen Tag.",
            "In zwei Stunden Jacke aus. Gegen Mittag ein Schauer. Schirm mitnehmen.",
            "Heute Nachmittag Jacke aus, heute Nacht wieder an.",
            "Heute Abend braucht's eine Jacke.",
            "Gegen Mittag Schnee.",
            "In zwei Stunden wird's heiß. Wasser mitnehmen.",
            "So bleibt's den restlichen Abend.",
            "Gegen Mittag Winterjacke aus, heute Nacht wieder an. Zwischendurch trocken, heute Nachmittag regnet's wieder. Schirm behalten."]),
        "clock": ("Uhrzeiten statt Tageszeiten.", [
            "Keine Änderung bis zum Abend.",
            "Ab etwa 9 Uhr ohne Jacke. Gegen 12 ein Schauer, Schirm mitnehmen.",
            "Ab 14 Uhr Jacke aus, ab 20 Uhr wieder an.",
            "Ab etwa 19 Uhr braucht's eine Jacke.",
            "Ab etwa 11 Uhr Schnee.",
            "Ab etwa 9 Uhr heiß. Wasser mitnehmen.",
            "Keine Änderung mehr heute Abend.",
            "Ab 12 Uhr Winterjacke aus, ab 20 Uhr wieder an. Kurze Regenpause, ab 14 Uhr regnet's wieder. Schirm behalten."]),
        "timeline": ("Zeitleiste: Uhrzeit, dann was sich ändert.", [
            "Ganzer Tag: wie gezeigt.",
            "9 Uhr: Jacke aus. 12 Uhr: Schauer, Schirm.",
            "14 Uhr: Jacke aus. 20 Uhr: Jacke an.",
            "19 Uhr: Jacke dazu.",
            "11 Uhr: Schnee.",
            "9 Uhr: Hitze. Wasser mitnehmen.",
            "Restlicher Abend: wie gezeigt.",
            "Jetzt: Regen. 12 Uhr: Winterjacke aus. 14 Uhr: wieder Regen. 20 Uhr: Winterjacke an."]),
        "sentence": ("Ganze, einfache Sätze.", [
            "Was du anhast, passt für den ganzen Tag.",
            "In zwei Stunden kann die Jacke weg. Gegen Mittag kommt ein Schauer, also nimm den Schirm mit.",
            "Am Nachmittag kann die Jacke weg, heute Nacht brauchst du sie wieder.",
            "Am Abend kühlt's ab, da braucht's eine Jacke.",
            "Es bleibt den ganzen Tag so kalt, und gegen Mittag fängt's an zu schneien.",
            "In zwei Stunden wird's heiß, nimm Wasser mit.",
            "Was du anhast, passt für den restlichen Abend.",
            "Gegen Mittag kann die Winterjacke weg, heute Nacht brauchst du sie wieder. Der Regen macht Pause und kommt am Nachmittag zurück, also Schirm behalten."]),
        "action": ("Erst was zu tun oder mitzunehmen ist, dann warum.", [
            "Heute musst du nichts mitnehmen.",
            "Schirm mitnehmen, gegen Mittag kommt ein Schauer. Die Jacke kann in zwei Stunden weg.",
            "Jacke dabeihaben: am Nachmittag aus, heute Nacht wieder an.",
            "Für heute Abend eine Jacke einpacken.",
            "Vorsicht auf dem Weg: Gegen Mittag kommt Schnee.",
            "Wasser mitnehmen, in zwei Stunden wird's heiß.",
            "Heute Abend nichts mehr umziehen.",
            "Schirm und Winterjacke dabeihaben. Mittags aus, nachts wieder an. Am Nachmittag regnet's wieder."]),
        "minimal": ("So wenig Wörter wie möglich.", [
            "Keine Änderung.",
            "Schirm. Ab 9 ohne Jacke.",
            "Jacke: 14 Uhr aus, 20 Uhr an.",
            "Jacke ab 19 Uhr.",
            "Schnee ab 11.",
            "Wasser. Ab 9 heiß.",
            "Keine Änderung mehr.",
            "Schirm. Winterjacke: 12 aus, 20 an."]),
    },
}


def write(round_name, lines, key):
    (HERE / f"{round_name}.json").write_text(json.dumps({"round": round_name, "lines": lines}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (HERE / f"{round_name}.key.json").write_text(json.dumps(key, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{round_name}: {len(lines)} lines")


def main():
    rng = random.Random("2026-10-round-2")

    lines, key = [], {}
    letters = {"en": iter("W"), "de": iter("XY")}
    for lang, voices in VOICES.items():
        names = list(voices)
        rng.shuffle(names)
        for name in names:
            letter = next(letters[lang])
            desc, moods = voices[name]
            key[letter] = {"lang": lang, "voice": name, "description": desc}
            for mood in MOODS:
                on, eleven = moods[mood]
                for level, texts in (("10", on), ("11", eleven)):
                    for text in texts:
                        lines.append({"lang": lang, "path": f"flavour_{level}.{mood}", "text": text, "batch": letter})
    write("2026-10-voices-2", lines, key)

    lines, key = [], {}
    letters = {"en": iter("KLMNOP"), "de": iter("QRSTUV")}
    for lang, styles in STYLES.items():
        names = list(styles)
        rng.shuffle(names)
        for name in names:
            letter = next(letters[lang])
            desc, texts = styles[name]
            key[letter] = {"lang": lang, "style": name, "description": desc}
            for (sit, (sprite, meaning)), text in zip(SITUATIONS.items(), texts):
                lines.append({"lang": lang, "path": f"fact_0.{sit}", "text": text, "batch": letter,
                              "sprite": sprite, "meaning": "Fact line. " + meaning})
    write("2026-10-facts", lines, key)


if __name__ == "__main__":
    main()
