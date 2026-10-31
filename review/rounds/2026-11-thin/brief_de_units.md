# Top-up round (de, units): thin slots to four lines

You write lines for a TRMNL e-ink weather screen, "What to Wear". German, standard German, no dialect. The speaker is the screen itself: der Grantler, grumpy, dry. Write in this language from scratch; never translate.

These slots have fewer than four live lines, and they are the ones that actually show on screen. Each heading says how many the critic will keep for the owner's vote and how many candidates to write (three times that). At most one candidate per slot may be out of the box (a different angle or form, still clear and on voice); mark it `"wild": true`.

## Learn from what worked, first

- Read `docs/BRIEF.md` (the voice, the levels, every lesson), above all "Tightening": the owner's own proofreading pass. Then `docs/CRITIC.md`: the critic cuts by it, so write so nothing on it applies.
- Read `review/rounds/2026-10-de-tight/changes.md`: every before and after of that pass.
- Read `review/examples/de.md`: the owner's starred lines. Reuse what makes them work (the angle, the rhythm, the length), not their words.
- Read `docs/PROOFREAD_DE.md`: the proofreader checks every line by it. The owner finds machine-sounding German the worst fault: write as a native speaker would say it.
- Skim `review/dont/de.md`: vetoed lines with tags and notes. Never go near those.

## Rules that cost the most votes

- Sarcasm with bite; never merely pleasant, never a restatement of the weather. Clear on first read, short (one or two short sentences).
- No wordplay on the forecast's words, no "like your X" / „wie deine X“ jabs, no predicting the reader's mishaps, never explain the joke.
- Nothing the screen can't know; no assumptions about how the reader lives. Evening (18-22) is not bedtime.
- Garment jokes must fit every garment the slot covers. Storms: no "get inside" lectures. The extra-cold layer is just the scarf.
- Each joke sits at one level: On is not about the reader; 11 is.
- The room, never the hallway (en). Keep the device's spot in the home vague (de).
- No line may repeat another candidate's idea, or a live line's.

## Slots

### `units_10.arc_colder` (live now: 3; the critic keeps 2, write 6)

The jacket comes off; the evening is colder than now: jacket back, plus a layer. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{WHEN} {GV} weg. Pack {GP} trotzdem ein, dazu noch eine extra Schicht, {WHEN2} wird's richtig kalt." / "{WHEN} {GV} weg. {WHEN2} brauchst du {GP} wieder und noch eine weitere Schicht." / "{WHEN} {GV} weg. {WHEN2} wird's kälter als jetzt, nimm eine extra Schicht mit." / "{WHEN} {GV} weg. {WHEN2} wird's aber so kalt, dass du {GP} und noch eine extra Schicht brauchst." / "{WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm eine extra Schicht mit."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm eine Schicht mehr mit. || So ein Hin und Her hält ja niemand aus.
- {WHEN} {GV} weg, {WHEN2} brauchst du {GP} wieder und noch eine extra Schicht. || Hier drin bleibt's gemütlich. Nur so als Idee.
- {WHEN} {GV} weg. Pack {GP} trotzdem ein, dazu noch eine extra Schicht, {WHEN2} wird's richtig kalt. || Ja, das ist viel Zeug. Beschwer dich beim Wetter.
Starred here before:
- {WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm also eine Schicht mehr mit. || Hauptsache, du hast was zum Meckern.
Voted out here (stay away):
- {WHEN} {GV} weg. {WHEN2} wird's kälter als jetzt, nimm eine extra Schicht mit. || Erst freundlich, dann gemein. Das Wetter lernt von mir. [not funny]
- {WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm eine Schicht mehr mit. || Wenn's warm ist, glaubst du mir sowas nie.
- {WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm eine Schicht mehr mit. || Dein Rucksack hat heute mehr an als du. [not funny, unclear]
- {WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm eine Schicht mehr mit. || Erst Sommer, dann Winter. Und ich mittendrin. [not funny]
- {WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm eine Schicht mehr mit. || Wer sich das ausdenkt, hat keine Freunde. [not funny]

### `units_10.arc_level` (live now: 2; the critic keeps 3, write 9)

The jacket comes off, and is wanted back in the evening. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{WHEN} {GV} weg. Nimm {GP} trotzdem mit, {WHEN2} wird's wieder kühler." / "{WHEN} {GV} weg, {WHEN2} brauchst du {GP} wieder." / "{WHEN} {GV} weg. {WHEN2} brauchst du {GP} aber wieder." / "{WHEN} {GV} weg. Halt {GP} aber griffbereit, {WHEN2} brauchst du {GP} wieder." / "{WHEN} {GV} weg, aber {WHEN2} wird's wieder kühler."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} {GV} weg. Nimm {GP} trotzdem mit, {WHEN2} wird's wieder kühler. || Daheim nützt's dir nichts. Da bin nur ich, und ich frier nicht.
- {WHEN} {GV} weg, {WHEN2} brauchst du {GP} wieder. || Dazwischen tun wieder alle so, als wär Sommer.
Starred here before:
- {WHEN} {GV} weg, aber behalt {GP} griffbereit für {WHEN2}. || Griffbereit, nicht irgendwo. Das ist ein Unterschied.
- {WHEN} {GV} weg. {WHEN2} brauchst du {GP} aber wieder. || Also nicht wieder irgendwo liegen lassen.
Voted out here (stay away):
- {WHEN} {GV} weg. {WHEN2} brauchst du {GP} aber wieder. || Heute trägst du's mehr, als du's anhast. [not funny]
- {WHEN} {GV} weg, aber nicht für lange: {WHEN2} wird's wieder kühler. || Der Sommer kommt heute nur auf einen Sprung vorbei. [not funny] (note: those are all not sarcastic)
- {WHEN} {GV} weg, aber nicht für lange: {WHEN2} wird's wieder kühler. || Die Biergärten bleiben trotzdem voll. Mit Decken. [not funny]
- {WHEN} {GV} weg, {WHEN2} brauchst du {GP} wieder. || Ob sich das Ausziehen lohnt, musst du selber wissen.
- {WHEN} {GV} weg, {WHEN2} brauchst du {GP} wieder. || Früher hat man sich einmal am Tag angezogen. Einmal! [not funny]
- {WHEN} {GV} weg. Nimm {GP} trotzdem mit, {WHEN2} wird's wieder kühler. || Kurz ohne. Mehr Sommer gibt's nicht. [not funny]

### `units_10.c_scarf` (live now: 3; the critic keeps 2, write 6)

Cools to bundled: hat, scarf and gloves needed later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Denk an deinen Schal, {WHEN} wird's ungemütlich kalt." / "{WHEN} wird's kälter, da brauchst du vermutlich einen Schal." / "{WHEN} wird's kalt genug für den Schal." / "Pack deinen Schal ein, {WHEN} wird's kälter." / "{WHEN} wird's richtig kalt, da solltest du eine extra warme Schicht, wie einen Schal, dabeihaben."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Pack den Schal ein, {WHEN} wird's kälter. || Die Oma wär stolz auf mich.
- Denk an deinen Schal, {WHEN} wird's ungemütlich kalt. || Ich hab keinen Hals. Ein Vorteil, den ich selten erwähne.
- {WHEN} wird's kalt genug für den Schal. || Ab da ist der Schal kein Accessoire mehr, sondern Notwehr.
Voted out here (stay away):
- {WHEN} wird's kälter, da brauchst du vermutlich einen Schal. || Der Winter klopft an. Ich mach nicht auf. [not funny]
- Pack deinen Schal ein, {WHEN} wird's kälter. || Wer im Wind den Kragen hochzieht, hat den Schal vergessen. Und tut so, als wär das Absicht. [not funny]
- {WHEN} wird's kalt genug für den Schal, und für die ersten Leute, die „Schön knackig!“ sagen. [not funny]
- {WHEN} wird's kälter, da brauchst du vermutlich einen Schal. || Bald riecht der Bus wieder nach Wolle und Erkältung. [not funny]
- Denk an Mütze, Schal und Handschuhe, {WHEN} wird's ungemütlich kalt. || So wie ich, nur eben draußen.

### `units_10.p_stays_wet` (live now: 2; the critic keeps 3, write 9)

Raining now and all day. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Eine Regenpause gibt's heute nicht. Nimm den Schirm mit." / "Es regnet den ganzen Tag, also nimm den Schirm mit." / "Regen bis zum Abend. Der Schirm sollte wirklich mit." / "Heute hört's nicht auf zu regnen. Nimm den Schirm mit." / "Den ganzen Tag Regen. Ohne Schirm geht nichts." / "Der Regen hält den ganzen Tag an. Der Schirm bleibt also bei dir."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Es regnet den ganzen Tag, also nimm den Schirm mit. || Auf einer Skala von eins bis Herbst: Herbst.
- Den ganzen Tag Regen. Ohne Schirm geht nichts. || Mit auch nicht viel, aber immerhin bist du trocken.
Starred here before:
- Heute hört's nicht auf zu regnen, nimm den Schirm mit. || Alle starren trotzdem aufs Regenradar. Als ob das was hilft.
Voted out here (stay away):
- Heute hört's nicht auf zu regnen. Nimm den Schirm mit. || „Gut für die Natur“, sagt garantiert wieder einer. Mit trockenen Füßen. [not funny]
- Den ganzen Tag Regen. Ohne Schirm geht nichts. || Die Schuhe, die „ein bisschen Regen abkönnen“, finden das heute raus. [not funny]
- Es regnet den ganzen Tag, also nimm den Schirm mit. || Nass ist's. War ja klar. [not funny]

### `units_10.p_wet_again_snow` (live now: 3; the critic keeps 2, write 6)

Snowing now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los." / "Der Schnee hört später auf, aber {WHENP} fängt's wieder an zu schneien." / "Der Schnee macht später eine Pause, {WHENP} schneit's aber weiter." / "Der Schneefall hört später auf, {WHENP} geht es weiter." / "Jetzt schneit's noch, dann ist Pause. {WHENP} schneit's wieder."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Es schneit noch eine Weile, dann ist kurz Ruhe. {WHENP} schneit's wieder. || Mehr als die kurze Ruhe gönnt mir heute auch niemand.
- Der Schnee hört später auf, {WHENP} geht's wieder los. || Der neue deckt wenigstens den grauen Matsch von vorhin zu.
- Der Schnee macht später eine Pause, {WHENP} schneit's aber weiter. || Ein Winter mit Werbeunterbrechung.
Starred here before:
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. || Schau nicht so. Ich hab mir das auch nicht ausgesucht.
Voted out here (stay away):
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. || Nachschub ist also bestellt. Zurückschicken geht nicht. [not funny]
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. || Ich sag Bescheid, wenn's wieder losgeht. Ach nein, hab ich ja grad. [not funny]
- Der Schnee macht später eine Pause, {WHENP} schneit's wieder. || Der Winterdienst räumt dann umsonst. Weiß er nur noch nicht. [not funny]
- Der Schnee macht später eine Pause, {WHENP} schneit's aber wieder. || Wer in der Pause schippt, darf gleich noch mal. [not funny]

### `units_10.p_wetter` (live now: 3; the critic keeps 2, write 6)

Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{WHENP} regnet's kurz. Mit Schirm bleibst du trocken." / "Pack den Schirm ein, {WHENP} wird's kurz nass." / "{WHENP} kommt ein Schauer, also nimm den Schirm mit." / "Nimm den Schirm mit, {WHENP} kommt ein Regenschauer." / "{WHENP} zieht ein Regenschauer durch, pack also den Schirm ein." / "Schirm nicht vergessen, {WHENP} kommt ein Regenschauer."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHENP} kommt ein Schauer, also nimm den Schirm mit. || Ein kurzer. Aber lang genug, um sich drüber zu ärgern.
- {WHENP} regnet's kurz. Mit Schirm bleibst du trocken. || Und dann heißt es wieder: „Es gibt kein schlechtes Wetter.“ Doch, gibt's.
- {WHENP} kommt ein Schauer, also nimm den Schirm mit. || „Fliegen die Schwalben tief, kommt Regen.“ Ja sicher, einem Vogel glaubt man wieder mehr als mir.
Voted out here (stay away):
- Nimm den Schirm mit, {WHENP} kommt ein Regenschauer. || Und schon wieder ein Tief. Ich kann nichts dafür. [not funny]

### `units_10.shorts_early` (live now: 1; the critic keeps 4, write 12)

A cool morning in long-pants weather that turns into shorts weather; the line suggests shorts, the drawing shows long pants. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Gerade ist's noch frisch, aber {WHEN} wird's warm genug für kurze Hosen." / "Jetzt ist's noch kühl, aber {WHEN} wird's warm genug für die kurze Hose." / "Noch ist's kühl, aber {WHEN} kannst du in kurzen Hosen rumlaufen." / "Jetzt ist's noch frisch, {WHEN} passen aber kurze Hosen besser."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Jetzt noch frisch, {WHEN} wird's warm genug für kurze Hosen. || Früher hätt man dazu einfach Sommer gesagt.
Voted out here (stay away):
- Gerade ist's frisch, aber {WHEN} ist's warm genug für ne kurze Hose. || Der Tag fängt an wie ein Montag und hört auf wie ein Freitag. [not funny]
- Noch ist's kühl, aber {WHEN} kannst du in kurzen Hosen rumlaufen. || Die Ersten haben sie jetzt schon an. Mit Gänsehaut und Überzeugung. [not funny]
- Jetzt ist's noch kühl, aber {WHEN} wird's warm genug für die kurze Hose. || Die Beine sind noch winterweiß. Bei allen. Tröstlich. [not funny]
- Lass dich vom kühlen Start nicht täuschen, spätestens {WHEN} reicht eine kurze Hose. || Kurze Hose. Ich sag's leise, damit's der Morgen nicht hört. [not funny]
- Gerade ist's frisch, aber {WHEN} ist Shorts-Wetter. || Überleg's dir. Ich hab da keine Meinung. Doch, hab ich. [not funny]
- Lass dich vom kühlen Start nicht täuschen, {WHEN} reichen Shorts. || Ich lass mich ja auch nicht täuschen. Von nichts. [not funny]
- Gerade ist's noch frisch, aber {WHEN} wird's warm genug für Shorts. || Ob du's machst, ist mir egal. Fast. [not funny]

### `units_10.w_hoodie` (live now: 3; the critic keeps 2, write 6)

Warms up: the sweater comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Mit dem Pulli ist {WHEN} Schluss, dann wird's wärmer." / "{WHEN} wird's mild genug, um den Pulli auszuziehen." / "{WHEN} kann der Pulli weg." / "{WHEN} kannst du den Pulli ausziehen." / "{WHEN} wird es warm genug, dann brauchst du keinen Pulli mehr." / "{WHEN} wird's wärmer, dann kann der Pulli weg."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} kann der Pulli weg. || Hier drin merk ich davon natürlich wieder nichts.
- {WHEN} wird's wärmer, dann kann der Pulli weg. || Ich sag's nur. Ausziehen musst du ihn selber.
- {WHEN} wird's mild genug, um den Pulli auszuziehen. || Das Wetter wird freundlich. Ich bleib, wie ich bin.
Voted out here (stay away):
- Mit dem Pulli ist {WHEN} Schluss, dann wird's wärmer. || Und schon ist er zu warm zum Tragen und zu groß für die Tasche. [not funny]
- {WHEN} kannst du den Pulli ausziehen. || Die Haare stehen danach wieder in alle Richtungen. Ist halt so. [not funny]
- Mit dem Pulli ist {WHEN} Schluss. || Wenn du dann wieder Kopfweh kriegst, war's natürlich der Föhn. Sicher. [not funny]

### `units_10.w_jacket` (live now: 3; the critic keeps 2, write 6)

Warms up: the jacket comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Mit der Jacke ist {WHEN} Schluss, dann wird's wärmer." / "{WHEN} wird's mild genug, um die Jacke auszuziehen." / "{WHEN} kann die Jacke weg." / "{WHEN} kannst du die Jacke ausziehen." / "{WHEN} ist es warm genug, dann brauchst du keine Jacke mehr." / "{WHEN} wird's wärmer, dann kann die Jacke weg."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} kann die Jacke weg. || Und dann darfst du sie wieder überm Arm spazieren tragen.
- Mit der Jacke ist {WHEN} Schluss, dann wird's wärmer. || Platz nimmt sie danach natürlich trotzdem weg.
- Mit der Jacke ist {WHEN} Schluss, dann wird's wärmer. || Weniger anhaben, genauso viel zu schleppen. Großartig.
Starred here before:
- {WHEN} kann die Jacke weg. || Wohin damit, ist dann dein Problem. Ich sag nur das Wetter an.
- {WHEN} wird's wärmer, dann kann die Jacke weg. || Dann darfst du dich kurz freuen. Aber übertreib's nicht.
Voted out here (stay away):
- {WHEN} kann die Jacke weg. || Dann kommen wieder die Leute raus, die man den Winter über nicht vermisst hat. [not funny]
- {WHEN} kannst du die Jacke ausziehen. || Endlich wieder Wetter, bei dem keiner meckert. Ich übernehm das. [not funny]
- {WHEN} kannst du die Jacke ausziehen, und ich kann endlich mal was Nettes sagen. Fast. [not funny]
- {WHEN} kannst du die Jacke ausziehen. || Ob du sie danach wiederfindest, sag ich dir nicht voraus. [not funny]

### `units_10.w_scarf` (live now: 2; the critic keeps 3, write 9)

Warms up: hat, scarf and gloves come off, the coat stays. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Den Schal kannst du {WHEN} wegpacken." / "{WHEN} brauchst du den Schal nicht mehr." / "{WHEN} kann der Schal weg." / "{WHEN} kannst du den Schal ablegen." / "{WHEN} wird's mild genug, dann kann der Schal wieder runter."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} kann der Schal weg. || Die Oma hätt ihn dir trotzdem drangelassen.
- Den Schal kannst du {WHEN} wegpacken. || Ein Schal weniger. Das ist bei mir schon fast gute Laune.
Starred here before:
- {WHEN} kannst du Mütze, Schal und Handschuhe ablegen. || Man erkennt dich dann sogar wieder.
Voted out here (stay away):
- {WHEN} kannst du Mütze, Schal und Handschuhe ablegen. || Die Mützenfrisur bleibt dir allerdings noch eine Weile.
- {WHEN} können Mütze, Schal und Handschuhe weg. || Ein Handschuh bleibt dann wieder irgendwo liegen. Immer der linke. [not funny]
- {WHEN} können Mütze, Schal und Handschuhe weg. || Ich würd ja sagen, der Frühling kommt. So weit geh ich aber nicht. [not funny]
- {WHEN} brauchst du Mütze, Schal und Handschuhe nicht mehr. || Das Handy geht dann auch wieder ohne Nasenspitze. [not funny]

### `units_10.w_water` (live now: 2; the critic keeps 3, write 9)

Climbs into heat. Nothing left to take off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Noch geht's, aber {WHEN} wird's heiß. Nimm genug Wasser mit." / "{WHEN} wird's richtig heiß, nimm Wasser mit." / "{WHEN} wird's heiß, pack lieber Wasser ein." / "{WHEN} kommt die Hitze, nimm genug zu trinken mit." / "{WHEN} wird's heiß, da gehört eine Flasche Wasser in die Tasche."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Noch geht's, aber {WHEN} wird's heiß. Nimm genug Wasser mit. || Leitungswasser reicht. Es muss nicht nach Bergpanorama schmecken.
- {WHEN} wird's heiß, pack lieber Wasser ein. || Aber stell's nicht in die Sonne. Warmes Wasser schmeckt scheiße.

### `units_11.arc_warmer` (live now: 3; the critic keeps 2, write 6)

The jacket comes off and stays off: the evening is still warmer than now. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHEN} {GV} runter, und zwar für den Rest des Tages." / "{WHEN} {GV} weg, und du brauchst {GP} danach heute nicht mehr." / "{WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr." / "{WHEN} {GV} runter, und dabei bleibt's dann für heute."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr. || Einmal entscheiden und durchziehen. Das Wetter kann's. Du musst noch üben.
- {WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr. || Ein Tag ohne Hin und Her. Selbst du kannst da nichts falsch anziehen.
- {WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr. || Danach kannst du dich ganz auf deine anderen Probleme konzentrieren.
Voted out here (stay away):
- {WHEN} {GV} weg, und du brauchst {GP} danach heute nicht mehr. || Ab dann musst du nur noch in der Sonne gut aussehen. Viel Erfolg. [not funny]
- {WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr. || Ab dann gibt's keine Ausrede mehr, warum du so aussiehst. [not funny]
- {WHEN} {GV} weg, und du brauchst {GP} danach heute nicht mehr. || Besser wird der Tag nicht. Du übrigens auch nicht. [not funny]
- {WHEN} {GV} runter, und zwar für den Rest des Tages. Wenn nicht für dich, dann für die Leute, die neben dir schwitzen müssten. [not funny]
- {WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr. || Das hältst sogar du durch. [not funny]
- {WHEN} {GV} weg, und dabei bleibt's dann für heute. || Endlich mal was, das bei dir hält. [not funny]
- {WHEN} {GV} weg, und dabei bleibt's dann für heute. || Hab ich dir gern gesagt. Kommt nicht wieder vor. [unclear] (note: what is that supposed to mean?)
- {WHEN} {GV} weg, und du brauchst {GP} danach heute nicht mehr. || Vergessen wirst du {GP} trotzdem irgendwo. Ich kenn dich. [not funny]
- {WHEN} {GV} weg, und zwar für den Rest des Tages. || Den Rest des Tages siehst du also aus wie du. Mutig. [not funny]
- {WHEN} {GV} weg, und du brauchst {GP} danach heute nicht mehr. || Dann hast du endlich die Hände frei. Fürs Handy. [not funny, unclear] (note: How does that make any sense?)
- {WHEN} {GV} weg, und zwar für den Rest des Tages. || Eine Entscheidung weniger, die du falsch treffen kannst. [not funny]

### `units_11.c_relief` (live now: 3; the critic keeps 2, write 6)

The heat breaks, but it stays warm. Nothing to bring. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHEN} ist die schlimmste Hitze überstanden, es bleibt aber warm." / "{WHEN} lässt die Hitze etwas nach, aber es bleibt warm." / "{WHEN} kühlt's ein bisschen ab, warm bleibt's trotzdem." / "Die Hitze lässt {WHEN} nach, aber es bleibt warm." / "{WHEN} wird's angenehmer, aber es bleibt warm." / "{WHEN} lässt die größte Hitze nach. Kühl wird's trotzdem nicht."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} lässt die Hitze etwas nach, aber es bleibt warm. || Dein Deo hat trotzdem schon aufgegeben.
- {WHEN} lässt die Hitze etwas nach, aber es bleibt warm. || Du jammerst trotzdem weiter. Nur etwas leiser.
- {WHEN} lässt die größte Hitze nach. Kühl wird's trotzdem nicht. || Die Ausreden für deine schlechte Laune gehen dir langsam aus.
Voted out here (stay away):
- {WHEN} ist die schlimmste Hitze überstanden, es bleibt aber warm. || Du hast sie überstanden. Wie, wollen wir lieber nicht wissen. [not funny]
- Die Hitze lässt {WHEN} nach, aber es bleibt warm. || Ein guter Moment, um wieder freundlich zu sein. Zu anderen, nicht zu mir. [not funny]
- {WHEN} wird's angenehmer, aber es bleibt warm. || Angenehm genug, dass man dich wieder ansprechen kann. Ungefähr. [not funny]
- {WHEN} wird's angenehmer, aber es bleibt warm. || Angenehmer als du jedenfalls. [not funny]
- {WHEN} wird's angenehmer, aber es bleibt warm. || Ich hab heute so oft „Hitze“ gesagt, ich kann's nicht mehr hören. [not funny, unclear] (note: joke does not make sense)
- {WHEN} lässt die Hitze etwas nach, aber es bleibt warm. || Dein Sonnenbrand nicht. [not funny]
- {WHEN} lässt die größte Hitze nach. Kühl wird's trotzdem nicht. || Kühl bleibt nur dein Charme. [not funny]
- Die Hitze lässt {WHEN} nach, aber es bleibt warm. || Frisch aussehen wirst du deswegen trotzdem nicht. [not funny]
- {WHEN} ist das Schlimmste der Hitze vorbei. || Dann erholt sich auch der Kreislauf. Erstaunlich schnell. [not funny]

### `units_11.p_drier_snow` (live now: 2; the critic keeps 3, write 9)

Snowing now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Der Schneefall hört {WHENSTOP} auf." / "{WHENSTOP} hört's auf zu schneien." / "Der Schnee hört später auf." / "Später hört's auf zu schneien." / "Noch schneit's, aber später hört es auf." / "Der Schneefall hört später auf."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Noch schneit's, aber später hört es auf. || Auf die Mütze verzichten musst du deswegen nicht. Du siehst darunter eh nicht besser aus.
- Der Schnee hört später auf. || Ich zeig's dir auch extra nochmal als Bild. Lesen ist ja nicht so deins.
Voted out here (stay away):
- Später hört's auf zu schneien. || Die Schneeballschlacht kannst du dann also ohne Ausrede verlieren. [not funny]
- Der Schnee hört später auf. || Danach ist alles still und weiß. Bis du rausgehst und was sagst. [not funny]
- Der Schneefall hört {WHENSTOP} auf. || Dann hast du keinen Grund mehr, so verfroren zu schauen. Du schaust trotzdem so. [not funny]
- Der Schneefall lässt später nach. || Dann darfst du wieder raus. Ob das draußen jemand will, ist eine andere Frage. [not funny]
- {WHENSTOP} hört's auf zu schneien. || Dann sieht man wieder, wer seinen Gehweg nicht geräumt hat. [not funny, unclear] (note: how is that funny?)
- Der Schneefall hört {WHENSTOP} auf. || Von oben kommt dann nichts mehr. Vom Dach schon noch. [not funny] (note: no flow, not funny)
- Es schneit noch eine Weile, dann hört's auf. || Weiß bleibt's genau bis zum ersten Hund. [not funny, robotic] (note: no good rythm.)
- Noch schneit's, aber später hört es auf. || Die Freude über Schnee hält eh keine Stunde. Passt also. [not funny]
- {WHENSTOP} hört's auf zu schneien. || Pünktlicher, als du je irgendwo warst. [not funny]
- Der Schnee hört später auf. || Dein Schneemann bleibt trotzdem so traurig, wie er ist. [not funny]
- Später hört's auf zu schneien. || Bis dahin sieht sogar dein Balkon ordentlich aus. [not funny]

### `units_11.p_wet_again` (live now: 3; the critic keeps 2, write 6)

Raining now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHENSTOP} hört der Regen auf, {WHENP} kommt er wieder. Halt den Schirm griffbereit." / "Erst regnet's weiter, dann ist Pause, und {WHENP} kommt der Regen wieder." / "Jetzt Regen, dann eine Pause, {WHENP} wieder Regen. Der Schirm sollte also dabeibleiben." / "Der Regen macht später eine Pause. {WHENP} regnet's wieder, also behalt den Schirm." / "Den Schirm brauchst du heute zweimal: jetzt und {WHENP} wieder."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Den Schirm brauchst du heute zweimal: jetzt und {WHENP} wieder. || Zweimal an dasselbe denken. Für dich ist das sportlich.
- {WHENSTOP} hört der Regen auf, {WHENP} kommt er wieder. || Der kommt zurück. Anders als dein Schirm, wenn du ihn irgendwo stehen lässt.
- Erst regnet's weiter, dann ist Pause, und {WHENP} kommt der Regen wieder. || Aufspannen, zumachen, aufspannen. Endlich mal ein Tag mit Struktur für dich.
Voted out here (stay away):
- Jetzt Regen, dann eine Pause, {WHENP} wieder Regen. || In der Pause bitte nicht den Schirm schütteln wie ein nasser Hund. [not funny]
- {WHENSTOP} hört der Regen auf, {WHENP} kommt er wieder. || In der Pause kannst du schnell mal raus. Schnell ist allerdings nicht so deins. [not funny]
- Erst regnet's weiter, dann ist Pause, und {WHENP} kommt der Regen wieder. || Fühl dich nicht verfolgt. Der Regen meint nicht dich. Ich schon. [not funny]
- Der Regen macht später eine Pause, {WHENP} kommt er zurück. || In der Pause sagt garantiert einer: „Na also.“ [not funny]
- {WHENSTOP} hört der Regen auf, {WHENP} kommt er wieder. || Reicht für einen Weg. Für den Rückweg nicht. [not funny]
- {WHENSTOP} hört der Regen auf, {WHENP} kommt er wieder. Behalt den Schirm bei dir. || Anders als deine gute Laune. [not funny]
- Der Regen macht später eine Pause, {WHENP} kommt er aber zurück. Behalt den Schirm dabei. || Wie deine Witze. [not funny]
- Jetzt Regen, dann eine Pause, {WHENP} wieder Regen. Der Schirm bleibt also dabei. || Pause kannst du. Weitermachen weniger. [not funny]

### `units_11.p_wet_again_snow` (live now: 3; the critic keeps 2, write 6)

Snowing now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los." / "Der Schnee hört später auf, aber {WHENP} fängt's wieder an zu schneien." / "Der Schnee macht später eine Pause, {WHENP} schneit's aber weiter." / "Der Schneefall hört später auf, {WHENP} geht es weiter." / "Jetzt schneit's noch, dann ist Pause. {WHENP} schneit's wieder."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Der Schneefall hört später auf, {WHENP} geht er weiter. || Weiß, grau, weiß. Mehr Farbe kriegt der Tag nicht. Du übrigens auch nicht.
- Der Schnee hört später auf, {WHENP} geht's wieder los. || Der erste Schnee ist romantisch, der zweite nur noch mühsam. Kennst du ja aus deinen Beziehungen.
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. || Schau nicht so. Ich hab mir das auch nicht ausgesucht.
Voted out here (stay away):
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. || Die Pause reicht für ein Foto. Nicht für eins, auf dem du gut aussiehst. [not funny]
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. || Wer in der Pause rausgeht, hält sich für schlau. Du zum Beispiel. [not funny]
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. Dazwischen ist's kurz still. Genieß es, du bist ja selten still. [not funny]
- Der Schnee macht später eine Pause, {WHENP} schneit's aber wieder. || Geräumt wird trotzdem nur einmal. Nämlich gar nicht. [not funny]
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. || Zweimal hab ich's angesagt. Das dritte Mal kostet extra. [not funny]
- Der Schnee hört später auf, aber {WHENP} fängt's wieder an zu schneien. || Wie deine Diät. [not funny]
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. || Plan das Schippen gut. Wobei, du schippst ja nicht. [not funny]
- Auf den Schnee jetzt folgt eine kurze Pause, {WHENP} kommt neuer dazu. || Neuer Schnee, alte Ausreden. [not funny]

## Output

Write `review/rounds/2026-11-thin/de.units.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
