# Fill-up round (de, units10): every thin slot to at least four lines

You write lines for a TRMNL e-ink weather screen, "What to Wear". German, standard German, no dialect. The speaker is the screen itself: der Grantler, grumpy, dry. Write in this language from scratch; never translate.

The owner reviewed every live line. These slots have fewer than four lines. For EACH slot write **9 candidates in the slot's established style plus 3 out-of-the-box ones** (a genuinely different angle or form the slot has never tried, still clear and on voice). A critic keeps the best 5-6 plus one out-of-the-box line per slot for the owner's vote, and the owner will cut some.

## Learn from what worked, first

- Read `docs/BRIEF.md` (the voice, the levels, every lesson).
- Read `review/examples/de.md`: the owner's starred lines. Reuse what makes them work (the angle, the rhythm, the length), not their words.
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

### `units_10.arc_level` (live now: 3)

The jacket comes off, and is wanted back in the evening. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{WHEN} {GV} weg. Nimm {GP} trotzdem mit, {WHEN2} wird's wieder kühler." / "{WHEN} {GV} weg, {WHEN2} brauchst du {GP} wieder." / "{WHEN} {GV} weg. {WHEN2} brauchst du {GP} aber wieder." / "{WHEN} {GV} weg, aber behalt {GP} griffbereit für {WHEN2}." / "{WHEN} {GV} weg, aber nicht für lange: {WHEN2} wird's wieder kühler."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} {GV} weg. {WHEN2} brauchst du {GP} aber wieder. || Also nicht wieder irgendwo liegen lassen.
- {WHEN} {GV} weg, aber behalt {GP} griffbereit für {WHEN2}. || Griffbereit, nicht irgendwo. Das ist ein Unterschied.
- {WHEN} {GV} weg. Nimm {GP} trotzdem mit, {WHEN2} wird's wieder kühler. || Daheim nützt's dir nichts. Da bin nur ich, und ich frier nicht.
Voted out here (stay away):
- {WHEN} {GV} weg. {WHEN2} brauchst du {GP} aber wieder. || Heute trägst du's mehr, als du's anhast. [not funny]
- {WHEN} {GV} weg, {WHEN2} brauchst du {GP} wieder. || Ob sich das Ausziehen lohnt, musst du selber wissen.
- {WHEN} {GV} weg, {WHEN2} brauchst du {GP} wieder. || Früher hat man sich einmal am Tag angezogen. Einmal! [not funny]
- {WHEN} {GV} weg. Nimm {GP} trotzdem mit, {WHEN2} wird's wieder kühler. || Kurz ohne. Mehr Sommer gibt's nicht. [not funny]

### `units_10.arc_warmer` (live now: 3)

The jacket comes off and stays off: the evening is still warmer than now. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{WHEN} {GV} runter, und zwar für den Rest des Tages." / "{WHEN} {GV} weg, und du brauchst {GP} danach heute nicht mehr." / "{WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr." / "{WHEN} {GV} runter, und dabei bleibt's dann für heute."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} {GV} weg, und zwar für den Rest des Tages. || Mitschleppen musst du {GP} dann trotzdem.
- {WHEN} {GV} weg, und dabei bleibt's dann für heute. || Eine klare Ansage. Kommt bei mir selten vor, genieß es.
- {WHEN} {GV} weg, und zwar für den Rest des Tages. || Ab da interessiert sich wieder niemand für mich.
Voted out here (stay away):
- {WHEN} {GV} weg, und zwar für den Rest des Tages. || Das Beste, was ich heute zu sagen hab. Danach wird's langweilig. [not funny]
- {WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr. || Morgen früh suchst du {GP} dann wieder. [not funny]
- {WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr. || Ich sag's einmal. Für heute. [not funny]
- {WHEN} {GV} weg, und du brauchst {GP} danach heute nicht mehr. || Danach ist's den ganzen Tag einfach. Fast verdächtig. [not funny]

### `units_10.c_hoodie` (live now: 3)

Cools to sweater weather: a sweater needed later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{WHEN} brauchst du einen Pulli, also nimm einen mit." / "{WHEN} kühlt's ab, da brauchst du vermutlich einen Pulli." / "{WHEN} wird's frisch genug für einen Pulli." / "Nimm einen Pulli mit, {WHEN} kühlt's ab." / "Pack einen Pulli ein, {WHEN} wird's kühler." / "{WHEN} wird's kühl, dann bist du froh über einen Pulli."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Nimm einen Pulli mit, {WHEN} kühlt's ab. || Nachher sagt wieder jeder: Ganz schön frisch geworden.
- Pack einen Pulli ein, {WHEN} wird's kühler. || Jetzt lächeln und nicken, und dann wieder frieren. Klar.
- {WHEN} kühlt's ab, da brauchst du vermutlich einen Pulli. || Vermutlich, so wirklich weiß das niemand.
Voted out here (stay away):
- {WHEN} kühlt's ab, da brauchst du vermutlich einen Pulli. || Den dicken musst du nicht nehmen. Ich bin ja kein Unmensch. [not funny]
- {WHEN} brauchst du einen Pulli, also nimm einen mit. || Der Pulli wiegt nichts. Das Gejammer später schon. [not funny]
- {WHEN} wird's frisch genug für einen Pulli. || Die Oma hätt's dir schon heute früh gesagt. Ich sag's halt jetzt.

### `units_10.c_relief` (live now: 3)

The heat breaks, but it stays warm. Nothing to bring. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{WHEN} ist die schlimmste Hitze überstanden, es bleibt aber warm." / "{WHEN} lässt die Hitze etwas nach, aber es bleibt warm." / "{WHEN} kühlt's ein bisschen ab, warm bleibt's trotzdem." / "Die Hitze lässt {WHEN} nach, aber es bleibt warm." / "{WHEN} wird's angenehmer, aber es bleibt warm." / "{WHEN} lässt die größte Hitze nach. Kühl wird's trotzdem nicht."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} lässt die Hitze etwas nach, aber es bleibt warm. || Mehr gute Nachrichten gibt's heute nicht.
- {WHEN} wird's angenehmer, aber es bleibt warm. || Eigentlich meine ich „weniger schlimm“.
- {WHEN} wird's angenehmer, aber es bleibt warm. || Gut. Den ganzen Tag „heiß“ ansagen strengt auch mich an.
Voted out here (stay away):
- Die Hitze lässt {WHEN} nach, aber es bleibt warm. || Der Ventilator darf trotzdem noch nicht in Rente. [not funny]
- {WHEN} ist das Schlimmste der Hitze vorbei, es bleibt aber warm. || Bei mir ist das Schlimmste nie vorbei. [not funny]
- {WHEN} ist das Schlimmste der Hitze vorbei, es bleibt aber warm. || Das Zweitschlimmste bleibt also da. [not funny]
- {WHEN} kühlt's ein bisschen ab, warm bleibt's trotzdem. || Das Wasser trinkst du bitte trotzdem weiter. [not funny]

### `units_10.c_scarf` (live now: 2)

Cools to bundled: hat, scarf and gloves needed later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Denk an deinen Schal, {WHEN} wird's ungemütlich kalt." / "{WHEN} wird's kälter, da brauchst du vermutlich einen Schal." / "{WHEN} wird's kalt genug für den Schal." / "Pack deinen Schal ein, {WHEN} wird's kälter." / "{WHEN} brauchst du eine extra warme Schicht, also nimm eventuell einen Schal mit." / "{WHEN} wird's richtig kalt, da solltest du eine extra warme Schicht, wie einen Schal, dabeihaben."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} wird's kalt genug für den Schal. || Schau nicht so, ich kann auch nichts dafür.
- Pack den Schal ein, {WHEN} wird's kälter. || Die Oma wär stolz auf mich.
Voted out here (stay away):
- {WHEN} wird's kälter, da brauchst du vermutlich einen Schal. || Der Winter klopft an. Ich mach nicht auf. [not funny]
- Pack deinen Schal ein, {WHEN} wird's kälter. || Wer im Wind den Kragen hochzieht, hat den Schal vergessen. Und tut so, als wär das Absicht. [not funny]
- Denk an Mütze, Schal und Handschuhe, {WHEN} wird's ungemütlich kalt. || So wie ich, nur eben draußen.

### `units_10.p_drier` (live now: 3)

Raining now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Nimm den Schirm mit, der Regen hört erst {WHENSTOP} auf." / "{WHENSTOP} hört der Regen auf, bis dahin brauchst du den Schirm." / "Der Regen hört später auf, bis dahin brauchst du den Schirm." / "Nimm den Schirm mit, der Regen hört erst später auf." / "Der Regen lässt später nach, für jetzt brauchst du noch einen Schirm." / "Jetzt brauchst du noch den Schirm, später wird's trocken."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Erst brauchst du noch den Schirm, später wird's trocken. || Trocken, hab ich gesagt. Von schön war nicht die Rede.
- Nimm den Schirm mit, der Regen hört erst {WHENSTOP} auf. || Jammer nicht. Ich hab mir den Tag auch anders vorgestellt.
- Noch regnet's, aber später hört es auf. Bis dahin hilft der Schirm. || Mehr Hoffnung hab ich heute nicht im Angebot.
Voted out here (stay away):
- Der Regen hört später auf, bis dahin brauchst du den Schirm. || Später heißt bei mir: wenn's keinem mehr was nützt. [not funny]

### `units_10.p_snow_coming` (live now: 3)

Snow later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Rechne {WHENP} mit Schnee." / "{WHENP} soll es schneien." / "{WHENP} fängt's an zu schneien." / "{WHENP} kommt Schnee." / "Mach dich auf Schnee gefasst, {WHENP} geht's los." / "{WHENP} setzt Schneefall ein."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHENP} soll es schneien. || Drei Flocken, und schon heißt's wieder Schneechaos.
- Rechne {WHENP} mit Schnee. || Mehr sag ich nicht. Sonst heißt's wieder, ich mach Panik.
- {WHENP} fängt's an zu schneien. || Schön ist der Schnee ja. Die ersten zehn Minuten.

### `units_10.p_stays_wet` (live now: 3)

Raining now and all day. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Eine Regenpause gibt's heute nicht. Nimm den Schirm mit." / "Es regnet den ganzen Tag, also nimm den Schirm mit." / "Regen bis zum Abend. Der Schirm sollte wirklich mit." / "Heute hört's nicht auf zu regnen. Nimm den Schirm mit." / "Den ganzen Tag Regen. Ohne Schirm geht nichts." / "Der Regen hält den ganzen Tag an. Der Schirm bleibt also bei dir."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Heute hört's nicht auf zu regnen, nimm den Schirm mit. || Du starrst trotzdem aufs Regenradar. Als ob das was hilft.
- Den ganzen Tag Regen. Ohne Schirm geht nichts. || Mit auch nicht viel, aber immerhin bist du trocken.
- Der Regen hält den ganzen Tag an, der Schirm bleibt also dabei. || Und bring ihn wieder heim. Im Fundbüro liegen genug.
Starred here before:
- Heute hört's nicht auf zu regnen, nimm den Schirm mit. || Alle starren trotzdem aufs Regenradar. Als ob das was hilft.
Voted out here (stay away):
- Es regnet den ganzen Tag, also nimm den Schirm mit. || Nass ist's. War ja klar. [not funny]

### `units_10.p_stays_wet_snow` (live now: 3)

Snowing now and all day. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Heute schneit's ohne Unterbrechung." / "Der Schneefall hält den ganzen Tag an." / "Es schneit den ganzen Tag." / "Schnee bis zum Abend." / "Heute hört's nicht auf zu schneien." / "Es schneit den ganzen Tag so weiter."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Der Schneefall hält den ganzen Tag an. || Die Bahn hat bestimmt schon aufgegeben.
- Es schneit den ganzen Tag. || Fünf Zentimeter, und im Radio heißt's Schneechaos.
- Heute hört's nicht auf zu schneien. || Freu dich nicht zu früh. Bald ist das alles grauer Matsch.

### `units_10.p_wet_again_snow` (live now: 3)

Snowing now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los." / "Es schneit noch eine Weile, dann ist kurz Ruhe. {WHENP} schneit's weiter." / "Der Schnee hört später auf, aber {WHENP} fängt's wieder an zu schneien." / "Der Schnee macht später eine Pause, {WHENP} schneit's aber weiter." / "Erstmal schneit's weiter, dann ist kurz Pause, und {WHENP} geht es wieder los." / "Der Schneefall hört später kurz auf, {WHENP} geht es weiter."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. || Schau nicht so. Ich hab mir das auch nicht ausgesucht.
- Es schneit noch eine Weile, dann ist kurz Ruhe. {WHENP} schneit's wieder. || Mehr als die kurze Ruhe gönnt mir heute auch niemand.
- Der Schnee hört später auf, {WHENP} geht's wieder los. || Der neue deckt wenigstens den grauen Matsch von vorhin zu.
Voted out here (stay away):
- Der Schnee macht später eine Pause, {WHENP} schneit's wieder. || Der Winterdienst räumt dann umsonst. Weiß er nur noch nicht. [not funny]
- Der Schnee macht später eine Pause, {WHENP} schneit's aber wieder. || Wer in der Pause schippt, darf gleich noch mal. [not funny]

### `units_10.p_wetter_long` (live now: 3)

Rain later, and it stays. Shown alone; after a change, it follows that sentence. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{WHENP} kommt Regen, und der hört so schnell nicht auf. Nimm den Schirm mit." / "{WHENP} fängt's an zu regnen und hört nicht mehr auf, also nimm den Schirm mit." / "{WHENP} setzt Regen ein und bleibt. Nimm den Schirm mit." / "Nimm den Schirm mit, {WHENP} fängt's an zu regnen, und zwar länger." / "Ohne Schirm wird's heute nichts, {WHENP} setzt Dauerregen ein." / "{WHENP} kommt Regen, und zwar für den Rest des Tages. Nimm den Schirm mit."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Ohne Schirm wird's heute nichts, {WHENP} setzt Dauerregen ein. || Die Schnecken freuen sich. Immerhin wer.
- {WHENP} kommt Regen, und zwar für den Rest des Tages. Nimm den Schirm mit. || Den Satz könnt ich im Schlaf aufsagen.
- {WHENP} setzt Regen ein und bleibt. Nimm den Schirm mit. || Gemütlich wird's höchstens hier drinnen.
Voted out here (stay away):
- {WHENP} kommt Regen, und der hört so schnell nicht auf. Nimm den Schirm mit. || Ich auch nicht. Mit dem Meckern. [not funny]

### `units_10.shorts_early` (live now: 2)

A cool morning in long-pants weather that turns into shorts weather; the line suggests shorts, the drawing shows long pants. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Gerade ist's frisch, aber {WHEN} ist's warm genug für ne kurze Hose." / "Gerade ist's noch frisch, aber {WHEN} wird's warm genug für kurze Hosen." / "Jetzt ist's noch kühl, aber {WHEN} wird's warm genug für die kurze Hose." / "Noch ist's kühl, aber {WHEN} kannst du in kurzen Hosen rumlaufen." / "Lass dich vom kühlen Start nicht täuschen, spätestens {WHEN} reicht eine kurze Hose." / "Jetzt ist's noch frisch, {WHEN} passen aber kurze Hosen besser."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Noch ist's kühl, aber {WHEN} kannst du in kurzer Hose rumlaufen. || Kannst, nicht musst. Schau nicht so verstört.
- Jetzt noch frisch, {WHEN} wird's warm genug für kurze Hosen. || Früher hätt man dazu einfach Sommer gesagt.
Voted out here (stay away):
- Gerade ist's frisch, aber {WHEN} ist Shorts-Wetter. || Überleg's dir. Ich hab da keine Meinung. Doch, hab ich. [not funny]
- Lass dich vom kühlen Start nicht täuschen, {WHEN} reichen Shorts. || Ich lass mich ja auch nicht täuschen. Von nichts. [not funny]
- Gerade ist's noch frisch, aber {WHEN} wird's warm genug für Shorts. || Ob du's machst, ist mir egal. Fast. [not funny]

### `units_10.w_coat` (live now: 3)

Warms up: the winter coat comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "{WHEN} wird's mild genug, um die Winterjacke auszuziehen." / "{WHEN} kann die Winterjacke weg." / "{WHEN} kannst du die Winterjacke ausziehen." / "{WHEN} wird es warm, dann brauchst du keine Winterjacke mehr." / "{WHEN} wird's wärmer, dann kann die Winterjacke weg." / "Mit der Winterjacke ist {WHEN} Schluss, dann wird's nämlich wärmer."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} kann die Winterjacke weg. || Freu dich nicht zu früh. Das ist noch kein Frühling.
- {WHEN} ist es warm, dann brauchst du keine Winterjacke mehr. || Mehr gute Nachrichten hab ich heute nicht.
- {WHEN} kannst du die Winterjacke ausziehen. || Die hat dann frei. Ich nicht.
Voted out here (stay away):
- {WHEN} wird's wärmer, dann kann die Winterjacke weg. || Ab dann schwitzt jeder in der Bahn, der's nicht gelesen hat. [not funny]
- {WHEN} kannst du die Winterjacke ausziehen. || Ich hab's gewusst, bevor du's gemerkt hast. Wie immer. [not funny]
- {WHEN} kann die Winterjacke weg. || Dann bist du gleich zwei Kilo leichter. Zumindest gefühlt. [not funny]
- {WHEN} wird's wärmer, dann kann die Winterjacke weg. || Und dann trägst du einen Schlafsack über dem Arm. [not funny]

### `units_10.w_jacket` (live now: 3)

Warms up: the jacket comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Live forecast sentences: "Mit der Jacke ist {WHEN} Schluss, dann wird's wärmer." / "{WHEN} wird's mild genug, um die Jacke auszuziehen." / "{WHEN} kann die Jacke weg." / "{WHEN} kannst du die Jacke ausziehen." / "{WHEN} ist es warm genug, dann brauchst du keine Jacke mehr." / "{WHEN} wird's wärmer, dann kann die Jacke weg."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} kann die Jacke weg. || Wohin damit, ist dann dein Problem. Ich sag nur das Wetter an.
- {WHEN} kann die Jacke weg. || Und dann darfst du sie wieder überm Arm spazieren tragen.
- {WHEN} wird's wärmer, dann kann die Jacke weg. || Dann darfst du dich kurz freuen. Aber übertreib's nicht.
Voted out here (stay away):
- {WHEN} kannst du die Jacke ausziehen. || Ob du sie danach wiederfindest, sag ich dir nicht voraus. [not funny]

## Output

Write `review/rounds/2026-10-fill/de.units10.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
