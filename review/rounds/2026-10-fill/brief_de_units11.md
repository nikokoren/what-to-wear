# Fill-up round (de, units11): every thin slot to at least four lines

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

### `units_11.arc_colder` (live now: 3)

The jacket comes off; the evening is colder than now: jacket back, plus a layer. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHEN} {GV} weg. Pack {GP} trotzdem ein, dazu noch eine extra Schicht, {WHEN2} wird's richtig kalt." / "{WHEN} {GV} weg. {WHEN2} brauchst du {GP} wieder, und noch eine weitere Schicht." / "{WHEN} {GV} weg. {WHEN2} wird's kälter als jetzt, nimm eine extra Schicht mit." / "{WHEN} {GV} weg. {WHEN2} wird's aber so kalt, dass du {GP} und noch eine extra Schicht brauchst." / "{WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm eine extra Schicht mit."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} {GV} weg. {WHEN2} brauchst du {GP} wieder, und noch eine weitere Schicht. || Ich hab's für dich extra simpel formuliert.
- {WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm eine Schicht mehr mit. || Der Tag erfordert mehr Planung, als du sonst in eine ganze Woche steckst.
- {WHEN} {GV} weg. {WHEN2} wird's kälter als jetzt, nimm eine extra Schicht mit. || Gänsehaut zählt nicht als Schicht.
Voted out here (stay away):
- {WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm eine Schicht mehr mit. || Und dann jammerst du in zwei Schichten. [not funny]
- {WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm eine Schicht mehr mit. || Am Abend dann: Michelin-Männchen. [not funny]
- {WHEN} {GV} weg, aber {WHEN2} wird's kälter. Nimm eine Schicht mehr mit. || Eine Schicht. Nicht das Shirt mit den Löchern. [not funny]
- {WHEN} {GV} weg, {WHEN2} brauchst du {GP} und was Warmes dazu. || Für Wetterfühlige ist so ein Tag wie Weihnachten. (note: i'm not even sure what wetterfühlig is.)

### `units_11.arc_level` (live now: 3)

The jacket comes off, and is wanted back in the evening. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHEN} {GV} weg. Nimm {GP} trotzdem mit, {WHEN2} wird's wieder kühler." / "{WHEN} {GV} weg, {WHEN2} brauchst du {GP} wieder." / "{WHEN} {GV} weg. {WHEN2} brauchst du {GP} aber wieder." / "{WHEN} {GV} weg, aber behalt {GP} griffbereit für {WHEN2}." / "{WHEN} {GV} weg, aber nicht für lange: {WHEN2} wird's wieder kühler."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} {GV} weg, {WHEN2} brauchst du {GP} wieder. || Ausziehen kannst du. Wiederfinden ist meistens dein Problem.
- {WHEN} {GV} weg, {WHEN2} brauchst du {GP} wieder. || Ausziehen, wieder anziehen. Das schaffst du schon. Vermutlich.
- {WHEN} {GV} weg, aber nicht für lange: {WHEN2} wird's wieder kühler. || Ungefähr so lang wie deine guten Vorsätze.

### `units_11.arc_warmer` (live now: 1)

The jacket comes off and stays off: the evening is still warmer than now. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHEN} {GV} runter, und zwar für den Rest des Tages." / "{WHEN} {GV} weg, und du brauchst {GP} danach heute nicht mehr." / "{WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr." / "{WHEN} {GV} runter, und dabei bleibt's dann für heute."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr. || Einmal entscheiden und durchziehen. Das Wetter kann's. Du musst noch üben.
Voted out here (stay away):
- {WHEN} {GV} weg, und du brauchst {GP} danach heute nicht mehr. || Ab dann musst du nur noch in der Sonne gut aussehen. Viel Erfolg. [not funny]
- {WHEN} {GV} weg. Den restlichen Tag brauchst du {GP} dann nicht mehr. || Das hältst sogar du durch. [not funny]
- {WHEN} {GV} weg, und dabei bleibt's dann für heute. || Endlich mal was, das bei dir hält. [not funny]
- {WHEN} {GV} weg, und dabei bleibt's dann für heute. || Hab ich dir gern gesagt. Kommt nicht wieder vor. [unclear] (note: what is that supposed to mean?)
- {WHEN} {GV} weg, und du brauchst {GP} danach heute nicht mehr. || Vergessen wirst du {GP} trotzdem irgendwo. Ich kenn dich. [not funny]
- {WHEN} {GV} weg, und zwar für den Rest des Tages. || Den Rest des Tages siehst du also aus wie du. Mutig. [not funny]
- {WHEN} {GV} weg, und du brauchst {GP} danach heute nicht mehr. || Dann hast du endlich die Hände frei. Fürs Handy. [not funny, unclear] (note: How does that make any sense?)
- {WHEN} {GV} weg, und zwar für den Rest des Tages. || Eine Entscheidung weniger, die du falsch treffen kannst. [not funny]

### `units_11.c_coat` (live now: 3)

Cools to coat weather: the winter coat needed later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHEN} kühlt's deutlich ab, dann ist die Winterjacke dran." / "{WHEN} wird's kälter, da brauchst du dann die Winterjacke." / "{WHEN} wird's kalt genug für die Winterjacke." / "Nimm die Winterjacke mit, {WHEN} wird's kälter." / "{WHEN} wird's kalt genug für die Winterjacke, also nimm sie, oder eine extra warme Schicht, mit."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} wird's kälter, da braucht's die Winterjacke. || Dein „Mir ist nie kalt“ hebst du dir bitte für einen anderen Tag auf.
- Nimm die Winterjacke mit, {WHEN} wird's kälter. || Ja, die dicke. Ich weiß, wie du drin aussiehst.
- {M:01}{WHEN} brauchst du die Winterjacke, also nimm sie mit. || Vorausgesetzt, sie geht nach den Feiertagen noch zu.
Starred here before:
- {WHEN} brauchst du die Winterjacke, also nimm sie mit. || Vorausgesetzt, sie geht nach den Feiertagen noch zu.

### `units_11.c_hoodie` (live now: 3)

Cools to sweater weather: a sweater needed later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHEN} brauchst du einen Pulli, also nimm einen mit." / "{WHEN} kühlt's ab, da brauchst du vermutlich einen Pulli." / "{WHEN} wird's frisch genug für einen Pulli." / "Nimm einen Pulli mit, {WHEN} kühlt's ab." / "Pack einen Pulli ein, {WHEN} wird's kühler." / "{WHEN} wird's kühl, dann bist du froh über einen Pulli."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Nimm einen Pulli mit, {WHEN} kühlt's ab. || Notfalls den kratzigen von der Oma. Der wärmt wenigstens.
- {WHEN} wird's kühl, dann bist du froh über einen Pulli. || Und ich bin froh, wenn du dann nicht jammerst.
- {WHEN} brauchst du einen Pulli, also nimm einen mit. || Zum Anziehen. Nicht zum Um-den-Bauch-Knoten.
Voted out here (stay away):
- Pack einen Pulli ein, {WHEN} wird's kühler. || Und nicht wieder den von jemand anderem. [not funny]

### `units_11.c_relief` (live now: 3)

The heat breaks, but it stays warm. Nothing to bring. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHEN} ist die schlimmste Hitze überstanden, es bleibt aber warm." / "{WHEN} lässt die Hitze etwas nach, aber es bleibt warm." / "{WHEN} kühlt's ein bisschen ab, warm bleibt's trotzdem." / "Die Hitze lässt {WHEN} nach, aber es bleibt warm." / "{WHEN} wird's angenehmer, aber es bleibt warm." / "{WHEN} lässt die größte Hitze nach. Kühl wird's trotzdem nicht."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} lässt die Hitze etwas nach, aber es bleibt warm. || Dein Deo hat trotzdem schon aufgegeben.
- {WHEN} lässt die Hitze etwas nach, aber es bleibt warm. || Du jammerst trotzdem weiter. Nur etwas leiser.
- {WHEN} lässt die größte Hitze nach. Kühl wird's trotzdem nicht. || Die Ausreden für deine schlechte Laune gehen dir langsam aus.
Voted out here (stay away):
- {WHEN} wird's angenehmer, aber es bleibt warm. || Angenehmer als du jedenfalls. [not funny]
- {WHEN} wird's angenehmer, aber es bleibt warm. || Ich hab heute so oft „Hitze“ gesagt, ich kann's nicht mehr hören. [not funny, unclear] (note: joke does not make sense)
- {WHEN} lässt die Hitze etwas nach, aber es bleibt warm. || Dein Sonnenbrand nicht. [not funny]
- {WHEN} lässt die größte Hitze nach. Kühl wird's trotzdem nicht. || Kühl bleibt nur dein Charme. [not funny]
- Die Hitze lässt {WHEN} nach, aber es bleibt warm. || Frisch aussehen wirst du deswegen trotzdem nicht. [not funny]
- {WHEN} ist das Schlimmste der Hitze vorbei. || Dann erholt sich auch der Kreislauf. Erstaunlich schnell. [not funny]

### `units_11.c_scarf` (live now: 3)

Cools to bundled: hat, scarf and gloves needed later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Denk an deinen Schal, {WHEN} wird's ungemütlich kalt." / "{WHEN} wird's kälter, da brauchst du vermutlich einen Schal." / "{WHEN} wird's kalt genug für den Schal." / "Pack deinen Schal ein, {WHEN} wird's kälter." / "{WHEN} brauchst du eine extra warme Schicht, also nimm eventuell einen Schal mit." / "{WHEN} wird's richtig kalt, da solltest du eine extra warme Schicht, wie einen Schal, dabeihaben."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} brauchst du den Schal, also nimm ihn mit. || Und bring ihn auch wieder mit nach hause, wenn's geht.
- {WHEN} wird's kalt genug für den Schal. || Dann siehst du aus wie ein Bankräuber. Steht dir.
- Denk an deinen Schal, {WHEN} wird's ungemütlich kalt. || Nein, dein Halstuch zählt nicht. Das ist Deko.
Voted out here (stay away):
- Pack deinen Schal ein, {WHEN} wird's kälter. || Ein Schnupfen ist bei dir ja immer gleich eine Lungenentzündung. [not funny]
- Pack Mütze, Schal und Handschuhe ein, {WHEN} wird's kälter. || Am besten die Mütze mit dem Bommel. Ich weiß, dass du eine hast. [not funny]
- {WHEN} wird's kalt genug für Mütze, Schal und Handschuhe. || Die Mütze steht dir nicht. Setz sie trotzdem auf. [not funny]
- Pack Mütze, Schal und Handschuhe ein, {WHEN} wird's kälter. || Zurück bringst du davon ja meistens nur zwei. [not funny]

### `units_11.p_drier` (live now: 3)

Raining now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Nimm den Schirm mit, der Regen hört erst {WHENSTOP} auf." / "{WHENSTOP} hört der Regen auf, bis dahin brauchst du den Schirm." / "Der Regen hört später auf, bis dahin brauchst du den Schirm." / "Nimm den Schirm mit, der Regen hört erst später auf." / "Der Regen lässt später nach, für jetzt brauchst du noch einen Schirm." / "Jetzt brauchst du noch den Schirm, später wird's trocken."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Noch regnet's, aber später hört es auf. Bis dahin hilft der Schirm. || Gegen deine schlechte Laune hilft er leider nicht.
- Der Regen lässt später nach, für jetzt brauchst du aber einen Schirm. || Für deine Frisur ist's sowieso zu spät.
- Nimm den Schirm mit, der Regen hört erst später auf. || Danach trägst du ihn nass durch die Gegend. Na toll.
Voted out here (stay away):
- Nimm den Schirm mit, der Regen hört erst {WHENSTOP} auf. || Die Uhrzeit ist geschätzt. Beschwerden bitte an den Himmel. [not funny]
- Nimm den Schirm mit, der Regen hört erst {WHENSTOP} auf. || Das ist früher, als du sonst was erledigst. [not funny]
- Erst brauchst du noch den Schirm, später wird's trocken. || Deine Witze sind's ja schon. [not funny]

### `units_11.p_drier_snow` (live now: 0)

Snowing now, stops later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Der Schneefall hört {WHENSTOP} auf." / "{WHENSTOP} hört's auf zu schneien." / "Der Schnee hört später auf." / "Später hört's auf zu schneien." / "Der Schneefall lässt später nach." / "Noch schneit's, aber später hört es auf."
Placeholders you may use: only those in the forecast sentence
Voted out here (stay away):
- {WHENSTOP} hört's auf zu schneien. || Dann sieht man wieder, wer seinen Gehweg nicht geräumt hat. [not funny, unclear] (note: how is that funny?)
- Der Schneefall hört {WHENSTOP} auf. || Von oben kommt dann nichts mehr. Vom Dach schon noch. [not funny] (note: no flow, not funny)
- Es schneit noch eine Weile, dann hört's auf. || Weiß bleibt's genau bis zum ersten Hund. [not funny, robotic] (note: no good rythm.)
- Noch schneit's, aber später hört es auf. || Die Freude über Schnee hält eh keine Stunde. Passt also. [not funny]
- {WHENSTOP} hört's auf zu schneien. || Pünktlicher, als du je irgendwo warst. [not funny]
- Der Schnee hört später auf. || Dein Schneemann bleibt trotzdem so traurig, wie er ist. [not funny]
- Später hört's auf zu schneien. || Bis dahin sieht sogar dein Balkon ordentlich aus. [not funny]

### `units_11.p_snow_coming` (live now: 3)

Snow later. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Rechne {WHENP} mit Schnee." / "{WHENP} soll es schneien." / "{WHENP} fängt's an zu schneien." / "{WHENP} kommt Schnee." / "Mach dich auf Schnee gefasst, {WHENP} geht's los." / "{WHENP} setzt Schneefall ein."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHENP} kommt Schnee. || Schneeflocken mit der Zunge fangen ist in deinem Alter übrigens gesellschaftlich verpönt.
- {WHENP} soll es schneien. || Ich sag's dir, und du bist dann trotzdem überrascht. Jedes Mal.
- {WHENP} kommt Schnee. || Dann ist draußen endlich alles so blass wie du.
Starred here before:
- {WHENP} soll es schneien. || Ich sag's dir, und du bist trotzdem überrascht. Jedes Mal.
Voted out here (stay away):
- {WHENP} setzt Schneefall ein. || Schnee macht alles schön. Fast alles. Stell dich nicht davor. [not funny]
- Mach dich auf Schnee gefasst, {WHENP} geht's los. || Gleich fühlst du dich wieder wie zwölf. Siehst halt nicht so aus. [not funny]

### `units_11.p_stays_wet` (live now: 2)

Raining now and all day. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Eine Regenpause gibt's heute nicht. Nimm den Schirm mit." / "Es regnet den ganzen Tag, also nimm den Schirm mit." / "Regen bis zum Abend. Der Schirm sollte wirklich mit." / "Heute hört's nicht auf zu regnen. Nimm den Schirm mit." / "Den ganzen Tag Regen. Ohne Schirm geht nichts." / "Der Regen hält den ganzen Tag an. Der Schirm bleibt also bei dir."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Heute hört's nicht auf zu regnen, nimm den Schirm mit. || Oder bleib einfach daheim. Darin bist du ja geübt.
- Regen bis zum Abend, der Schirm sollte wirklich mit. || Wirklich, hab ich gesagt. Nicht „Ach, das geht schon“.
Voted out here (stay away):
- Den ganzen Tag Regen. Ohne Schirm geht nichts. || Der hilft heute bis zur Hüfte. Darunter bist du auf dich gestellt. [not funny]
- Eine Regenpause gibt's heute nicht, nimm den Schirm mit. || Grau in grau. Du fällst heute also gar nicht auf. [not funny]
- Der Regen hält den ganzen Tag an, der Schirm bleibt also dabei. || Wenigstens einer, der heute durchhält. [not funny]
- Es regnet den ganzen Tag, also nimm den Schirm mit. || Du bist nicht aus Zucker, sagt man. Ich wär mir nicht so sicher. [not funny]

### `units_11.p_stays_wet_snow` (live now: 3)

Snowing now and all day. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Heute schneit's ohne Unterbrechung." / "Der Schneefall hält den ganzen Tag an." / "Es schneit den ganzen Tag." / "Schnee bis zum Abend." / "Heute hört's nicht auf zu schneien." / "Es schneit den ganzen Tag so weiter."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Es schneit den ganzen Tag. || Und nein, deswegen fällt die Arbeit nicht aus.
- Heute hört's nicht auf zu schneien. || Du wirst trotzdem so tun, als hätt's dir keiner gesagt.
- Es schneit weiter, bis der Tag vorbei ist. || Morgen erzählst du allen, wie du dich durchgekämpft hast. Bis zum Sofa.

### `units_11.p_wet_again` (live now: 2)

Raining now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHENSTOP} hört der Regen auf, {WHENP} kommt er wieder. Halt den Schirm griffbereit." / "Der Regen macht später eine Pause, {WHENP} kommt er aber zurück. Behalt den Schirm bei dir." / "Erst regnet's weiter, dann ist Pause, und {WHENP} kommt der Regen wieder." / "Später hört der Regen eine Weile auf, {WHENP} geht's aber wieder los. Nimm den Schirm mit." / "Jetzt Regen, dann eine Pause, {WHENP} wieder Regen. Der Schirm sollte also dabei bleiben." / "Der Regen hört später auf, aber nur kurz. {WHENP} regnet's wieder, also behalt den Schirm."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Den Schirm brauchst du heute zweimal: jetzt und {WHENP} wieder. || Zweimal an dasselbe denken. Für dich ist das sportlich.
- {WHENSTOP} hört der Regen auf, {WHENP} kommt er wieder. || Der kommt zurück. Anders als dein Schirm, wenn du ihn irgendwo stehen lässt.
Voted out here (stay away):
- Der Regen macht später eine Pause, {WHENP} kommt er zurück. || In der Pause sagt garantiert einer: „Na also.“ [not funny]
- {WHENSTOP} hört der Regen auf, {WHENP} kommt er wieder. || Reicht für einen Weg. Für den Rückweg nicht. [not funny]
- {WHENSTOP} hört der Regen auf, {WHENP} kommt er wieder. Behalt den Schirm bei dir. || Anders als deine gute Laune. [not funny]
- Der Regen macht später eine Pause, {WHENP} kommt er aber zurück. Behalt den Schirm dabei. || Wie deine Witze. [not funny]
- Jetzt Regen, dann eine Pause, {WHENP} wieder Regen. Der Schirm bleibt also dabei. || Pause kannst du. Weitermachen weniger. [not funny]

### `units_11.p_wet_again_snow` (live now: 2)

Snowing now, stops, comes back. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los." / "Es schneit noch eine Weile, dann ist kurz Ruhe. {WHENP} schneit's weiter." / "Der Schnee hört später auf, aber {WHENP} fängt's wieder an zu schneien." / "Der Schnee macht später eine Pause, {WHENP} schneit's aber weiter." / "Erstmal schneit's weiter, dann ist kurz Pause, und {WHENP} geht es wieder los." / "Der Schneefall hört später kurz auf, {WHENP} geht es weiter."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Der Schneefall hört später kurz auf, {WHENP} geht er weiter. || Weiß, grau, weiß. Mehr Farbe kriegt der Tag nicht. Du übrigens auch nicht.
- Der Schnee hört später auf, {WHENP} geht's wieder los. || Der erste Schnee ist romantisch, der zweite nur noch mühsam. Kennst du ja aus deinen Beziehungen.
Voted out here (stay away):
- Der Schnee macht später eine Pause, {WHENP} schneit's aber wieder. || Geräumt wird trotzdem nur einmal. Nämlich gar nicht. [not funny]
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. || Zweimal hab ich's angesagt. Das dritte Mal kostet extra. [not funny]
- Der Schnee hört später auf, aber {WHENP} fängt's wieder an zu schneien. || Wie deine Diät. [not funny]
- {WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los. || Plan das Schippen gut. Wobei, du schippst ja nicht. [not funny]
- Auf den Schnee jetzt folgt eine kurze Pause, {WHENP} kommt neuer dazu. || Neuer Schnee, alte Ausreden. [not funny]

### `units_11.p_wetter_long` (live now: 3)

Rain later, and it stays. Shown alone; after a change, it follows that sentence. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHENP} kommt Regen, und der hört so schnell nicht auf. Nimm den Schirm mit." / "{WHENP} fängt's an zu regnen und hört nicht mehr auf, also nimm den Schirm mit." / "{WHENP} setzt Regen ein und bleibt. Nimm den Schirm mit." / "Nimm den Schirm mit, {WHENP} fängt's an zu regnen, und zwar länger." / "Ohne Schirm wird's heute nichts, {WHENP} setzt Dauerregen ein." / "{WHENP} kommt Regen, und zwar für den Rest des Tages. Nimm den Schirm mit."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHENP} setzt Regen ein und bleibt. Nimm den Schirm mit. || Wenn du nass wirst, war's wieder meine Schuld. Klar.
- {WHENP} setzt Regen ein und bleibt. Nimm den Schirm mit. || Aber auf mich hörst du ja erst mit nassen Socken.
- {WHENP} setzt Regen ein und bleibt. Nimm den Schirm mit. || Den Rest vom Tag kannst du abhaken. Viel verpasst du nicht.
Voted out here (stay away):
- Ohne Schirm wird's heute nichts, {WHENP} setzt Dauerregen ein. || Wer sagt, das zieht schnell durch, lügt. [not funny]
- Ohne Schirm wird's heute nichts, {WHENP} setzt Dauerregen ein. || Am besten nicht wieder den mit der kaputten Speiche. [not funny]
- {WHENP} kommt Regen, und zwar für den Rest des Tages. Nimm den Schirm mit. || Passt endlich zu deiner Laune. [not funny]
- {WHENP} kommt Regen, und der bleibt. || Wer Regen will, wäscht sein Auto. Das klappt zuverlässiger als ich. [wrong fact] (note: i like the if you start to clean your car it'll rain right away line, but i dont think it fits here. the rain is starting that day ans something like that isusually said during a longer dry period.)

### `units_11.p_wetter_maybe` (live now: 2)

Rain possible later, not likely. Shown alone; after a change, it follows that sentence. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHENP} ist eventuell ein Schauer drin, also lieber den Schirm einpacken." / "{WHENP} könnte es regnen. Ein Schirm schadet nicht." / "{WHENP} ist Regen möglich. Nimm lieber den Schirm mit." / "{WHENP} kann's regnen. Mit Schirm bist du auf der sicheren Seite." / "Vielleicht regnet's {WHENP}. Der Schirm schadet nicht." / "Ob's {WHENP} regnet, ist nicht ganz sicher. Der Schirm schadet vermutlich nicht."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Vielleicht regnet's {WHENP}. Der Schirm schadet nicht. || Dir schadet ein bisschen Regen vermutlich eh nicht.
- {WHENP} ist Regen möglich, nimm lieber den Schirm mit. || Möglich ist bei dir ja vieles. Passieren tut selten was.
Starred here before:
- {WHENP} kann's regnen. Mit Schirm bist du auf der sicheren Seite. || Übersetzt: Ich weiß es auch nicht.
- {WHENP} ist ein Schauer drin. || Die App sagt dreißig Prozent. Was genau das heißt, weiß sie selber nicht.
- {WHENP} könnte es regnen, ein Schirm schadet nicht. || Nimmst du ihn mit, regnet's nicht. So läuft das.
Voted out here (stay away):
- {WHENP} kann's regnen. Mit Schirm bist du auf der sicheren Seite. || Da warst du schon lang nicht mehr. [not funny]
- {WHENP} ist ein Schauer drin. || Ob's regnet, hängt davon ab, ob gerade jemand sein Auto wäscht. [not funny]

### `units_11.w_coat` (live now: 3)

Warms up: the winter coat comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "{WHEN} wird's mild genug, um die Winterjacke auszuziehen." / "{WHEN} kann die Winterjacke weg." / "{WHEN} kannst du die Winterjacke ausziehen." / "{WHEN} wird es warm, dann brauchst du keine Winterjacke mehr." / "{WHEN} wird's wärmer, dann kann die Winterjacke weg." / "Mit der Winterjacke ist {WHEN} Schluss, dann wird's nämlich wärmer."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} kann die Winterjacke weg. || Dann sieht man wieder, was du den ganzen Winter gegessen hast.
- {WHEN} wird's wärmer, dann kann die Winterjacke weg. || Und dann stopfst du sie wieder in deine viel zu kleine Tasche. Du lernst auch nicht dazu.
- {WHEN} wird's mild genug, um die Winterjacke auszuziehen. || Für dich ist das ja schon ein Ereignis.
Voted out here (stay away):
- {WHEN} kannst du die Winterjacke ausziehen. || Bitte nicht gleich übertreiben. Das ist noch kein Sommer. [not funny]
- {WHEN} ist es warm, dann brauchst du keine Winterjacke mehr. || Die Ausrede für den Winterspeck auch nicht. [not funny]

### `units_11.w_jacket` (live now: 3)

Warms up: the jacket comes off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Mit der Jacke ist {WHEN} Schluss, dann wird's wärmer." / "{WHEN} wird's mild genug, um die Jacke auszuziehen." / "{WHEN} kann die Jacke weg." / "{WHEN} kannst du die Jacke ausziehen." / "{WHEN} ist es warm genug, dann brauchst du keine Jacke mehr." / "{WHEN} wird's wärmer, dann kann die Jacke weg."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} kann die Jacke weg. || Und dann wieder um die Hüfte binden? Bitte nicht.
- {WHEN} kannst du die Jacke ausziehen. || Und dann vergisst du sie irgendwo. Wie letztes Mal.
- {WHEN} kann die Jacke weg. || Dann sieht jeder, was du drunter anhast. Das Gleiche wie gestern.
Voted out here (stay away):
- {WHEN} kannst du die Jacke ausziehen. || Dann hängt sie den Rest des Tages über deinem Stuhl. [not funny]

### `units_11.w_scarf` (live now: 1)

Warms up: hat, scarf and gloves come off, the coat stays. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Den Schal kannst du {WHEN} wegpacken." / "{WHEN} brauchst du den Schal nicht mehr." / "{WHEN} kann der Schal weg." / "{WHEN} kannst du den Schal ablegen." / "{WHEN} wird's mild genug, dann kann der Schal wieder runter." / "{WHEN} wird's wärmer, da kannst du den Schal abnehmen."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- Den Schal kannst du {WHEN} wegpacken. || Riech lieber nicht dran. Der war den ganzen Winter um deinen Hals.
Voted out here (stay away):
- {WHEN} kann der Schal weg. || Der Schal hat dann frei. Bei dem Gesicht darüber hat er sich's verdient. [not funny]
- {WHEN} kannst du den Schal ablegen. || Und bitte nicht wieder in den Mantelärmel stopfen. Du bist nicht mehr in der Grundschule. [not funny]
- {WHEN} können Mütze, Schal und Handschuhe weg. || Dann sieht man wieder deine Frisur. Schade eigentlich. [not funny]
- Mütze, Schal und Handschuhe kannst du {WHEN} einpacken. || Die Handschuhe findest du dann im Frühling wieder. [not funny]
- {WHEN} kannst du Mütze, Schal und Handschuhe ablegen. || Drei Sachen auf einmal merken. Das wird schwer für dich. [not funny]

### `units_11.w_water` (live now: 3)

Climbs into heat. Nothing left to take off. UNIT: `forecast sentence || joke`, written together so they flow. Take or lightly vary a live forecast sentence below (same placeholders, never new ones); the joke follows from it. A one-sentence unit with no joke part is allowed if the sentence itself is the joke.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Live forecast sentences: "Noch geht's, aber {WHEN} wird's heiß. Nimm genug Wasser mit." / "{WHEN} wird's richtig heiß, nimm Wasser mit." / "{WHEN} wird's heiß, pack lieber Wasser ein." / "{WHEN} kommt die Hitze, nimm genug zu trinken mit." / "{WHEN} wird's heiß, da gehört eine Flasche Wasser in die Tasche."
Placeholders you may use: only those in the forecast sentence
Live here (don't repeat their ideas):
- {WHEN} wird's richtig heiß, nimm Wasser mit. || Wasser ist übrigens das Durchsichtige.
- {WHEN} wird's heiß, pack lieber Wasser ein. || Trinken, nicht nur rumtragen. Ich kenn dich.
- {WHEN} kommt die Hitze, nimm genug zu trinken mit. || Kaffee zählt übrigens nicht als Wasser. Auch nicht mit Eis.

## Output

Write `review/rounds/2026-10-fill/de.units11.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
