# Fill-up round (de, flavour10): every thin slot to at least four lines

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

### `flavour_10.day_dst_fall` (live now: 2)

SPECIAL DAY: the Sunday the clocks go back, and the Monday after. Shows on a dry, steady day under the fixed sentence "Was du anhast, passt für den restlichen Tag." or alone under the drawing. Name the day or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Endlich wieder dunkel um fünf. Das hat mir echt gefehlt.
- Eine Stunde mehr, und ich weiß nicht, wohin damit.
Voted out here (stay away):
- Die Uhren gehen eine Stunde zurück. Ich hätt lieber den Sommer zurück. [not funny]
- Zeitumstellung. Hunde und Kleinkinder halten sich nicht dran. [not funny]

### `flavour_10.day_dst_spring` (live now: 0)

SPECIAL DAY: the Sunday the clocks go forward, and the Monday after. Shows on a dry, steady day under the fixed sentence "Was du anhast, passt für den restlichen Tag." or alone under the drawing. Name the day or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- Sommerzeit. Eine Stunde weniger, und trotzdem wird's nicht früher Sommer. [not funny]
- Eine Stunde weniger seit der Zeitumstellung. Merken tut man's bis Mittwoch. [not funny]
- Die Uhren gehen eine Stunde vor. Ich merk's nicht, ich bin ein Bildschirm. Du schon. [not funny]
- Die Uhren sind vorgestellt. Die Stunde Schlaf ist weg, und keiner gibt sie zurück. [not funny]

### `flavour_10.day_longest` (live now: 0)

SPECIAL DAY: the longest day of the year. Shows on a dry, steady day under the fixed sentence "Was du anhast, passt für den restlichen Tag." or alone under the drawing. Name the day or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- Längster Tag des Jahres. Ab morgen geht's wieder bergab. [not funny]
- Heute ist der längste Tag. Für mich sind alle gleich lang, ich bin immer an. [not funny]
- Längster Tag des Jahres. Die Lebkuchen sind schon unterwegs. [not funny]

### `flavour_10.day_monday` (live now: 0)

SPECIAL DAY: Monday mornings, before noon. Shows on a dry, steady day under the fixed sentence "Was du anhast, passt für den restlichen Tag." or alone under the drawing. Name the day or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- Montag. Wer den erfunden hat, war bestimmt Frühaufsteher. [not funny]
- Montag. Auf den hat sich wieder keiner gefreut. Ich auch nicht. [not funny]
- Montag. Das Wetter kann nichts dafür. Ich auch nicht. [not funny]
- Montag. Die ganze Woche liegt noch vor uns. Ich sag's nur. [not funny]
- Montagmorgen. Ich bin auch noch nicht ganz da. Dabei schlaf ich nie. [not funny]
- Montagmorgen. Heute ist der Kaffee wichtiger als meine Vorhersage. [not funny]

### `flavour_10.day_shortest` (live now: 2)

SPECIAL DAY: the shortest day of the year. Shows on a dry, steady day under the fixed sentence "Was du anhast, passt für den restlichen Tag." or alone under the drawing. Name the day or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Ab morgen wird's heller. Langsam. Seeeeehr langsam.
- Ich mach's wie die Sonne und halt mich heute kurz.
Voted out here (stay away):
- Heute ist der kürzeste Tag. Endlich mal einer, der schnell vorbei ist. [not funny]

### `flavour_10.night` (live now: 2)

Follow-up under a forecast sentence: from 22:00: the same line, late.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Mehr als „passt“ fällt mir so spät auch nicht mehr ein.
- Das sag ich jetzt nur noch aus Pflichtgefühl. Eigentlich hab ich schon Feierabend.
Starred here before:
- Mehr als auf der Couch liegen hattest du sowieso nicht vor, oder?
- Für die Couch passt's sowieso.
Voted out here (stay away):
- Schon spät. Ich zeig trotzdem weiter, was ich zeig. [not funny]
- Morgen ist auch noch ein Tag. Leider. [unclear, not funny]
- Draußen sind jetzt nur noch Katzen und Betrunkene. Beide laut. [not funny]
- Nachtprogramm. Bis morgen früh ändert sich nichts mehr. [not funny]
- Im Bett ist es sowieso am schönsten. Wetter hin oder her. [not funny]
- Nachts passiert eh nichts. Außer du schaust mich an. [unclear]
- Wer jetzt noch rausmuss, hat einen Hund. Oder Ärger. [not funny]
- Ab jetzt läuft hier nur noch die Spätausgabe. Gleicher Inhalt, schlechtere Laune. [not funny]
- Der restliche Abend ist um die Uhrzeit eh nicht mehr lang.
- Ehrlich gesagt hätt ich's dir auch morgen sagen können. [not funny]
- Spät ist's. Ich zeig das hier trotzdem weiter. [not funny]
- Um die Uhrzeit gibt's von mir nur noch das Nötigste. [not funny]
- Im Bett ist's eh am schönsten. Das Wetter kann mich mal. [not funny]
- Abend, sagen die Jungen dazu. Für mich ist das längst Nacht. [not funny]
- Fürs Bett reicht übrigens auch der Schlafanzug. [not funny]

### `flavour_10.pants` (live now: 1)

Follow-up under a forecast sentence: long pants on a shorts morning: a cold front later.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Sieht nicht danach aus, ich weiß. Stimmt aber trotzdem.
Voted out here (stay away):
- Die Sonne jetzt ist ein Lockangebot. [not funny]
- Die Kaltfront meldet sich nicht vorher an. Außer bei mir. [not funny]
- Ich weiß, ich mach mich heute unbeliebt. [not funny]
- Mit der Jacke unterm Arm siehst du jetzt komisch aus. Später aber schlau.
- Ich trau dem schönen Wetter auch nicht. Zu Recht, wie's aussieht. [not funny]
- Die in kurzen Hosen lachen jetzt noch. [not funny, unclear]
- Das jetzt ist nur die Vorschau. Der Hauptfilm heißt Kaltfront. [not funny]

### `flavour_10.snow` (live now: 3)

Follow-up under a forecast sentence: a snow line: snow later, all day, or stopping.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Schön ist der Schnee ja. Die ersten zehn Minuten.
- Mehr sag ich nicht. Sonst heißt's wieder, ich mach Panik.
- Freu dich nicht zu früh. Bald ist das alles grauer Matsch.
Starred here before:
- Fünf Zentimeter, und im Radio heißt's Schneechaos.
- Die Bahn hat bestimmt schon aufgegeben.
- Der Hausmeister hat wieder seinen großen Tag.
- Schön ist so ein Schnee ja. Die ersten zehn Minuten.
- Jetzt hamstern's wieder alle Streusalz, als käm die Eiszeit.
Voted out here (stay away):
- Schneefall. Ich hab extra die Wetterkarte in Weiß dabei. [not funny]
- Schön zum Anschauen. Zum Gehen weniger. [not funny]
- Heute ist der Hausmeister der wichtigste Mensch im Haus. [not funny]
- Schnee. Die Kollegen vom Verkehrsfunk freuen sich schon. [not funny]
- Winterreifen kommen bei manchen ja erst im März drauf. [not funny]
- Angesagt hab ich's. Den Winterdienst ruf ich trotzdem nicht an. [not funny]
- Und morgen sind trotzdem wieder alle überrascht. (note: surprised about what?)
- Freuen tun sich nur die Kinder. Die müssen ja nicht schippen. [not funny]
- Der Hausmeister hat wieder seinen großen Tag. [not funny]
- Früher lag der Schnee meterhoch, erzählen die Alten. Da waren sie halt kleiner. [not funny]
- Dann ist draußen alles schwarzweiß wie ich. Komisch, da beschwert sich keiner. [not funny]
- Die Bahn tut dann wieder, als hätt's seit hundert Jahren nicht geschneit. [not funny, robotic]
- Der Nachbar schaufelt dann wieder um sechs Uhr früh. Damit's auch alle hören. [not funny]

### `flavour_10.storm` (live now: 1)

Follow-up under a forecast sentence: a thunderstorm: the umbrella, inside while it thunders.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Die Wetter-Apps schicken jetzt wieder Warnungen im Minutentakt. Ich sag's einmal.
Voted out here (stay away):
- Bei Gewitter hat die Oma früher alle Stecker gezogen. Ich hätt endlich mal Ruhe gehabt. [not funny]
- Fällt irgendwo der Strom aus, ist mir das egal. Ich hab Akku. [not funny]
- Dein einziger Blitzableiter bist du selbst. Also rein, wenn's donnert. [not funny]
- Bei Donner bleib ich auch drinnen. Wie immer, eigentlich. [not funny]
- Unter einem Baum ist nicht drinnen. [not funny]
- Gegen den Regen hilft der Schirm, gegen Blitze nur ein Dach. [not funny, robotic]
- Spannend wird's heute nur am Himmel. Schau's dir von drinnen an. [not funny, unclear]
- Der Schirm hilft gegen Regen. Gegen Blitze hilft nur drinnen. [not funny, unclear, robotic] (note: i like the direction, but that doesnt work as is in german.)
- Der Schirm ist für den Regen. Für den Blitz ist er eher eine Einladung. [not funny]

### `flavour_10.theme_easter` (live now: 2)

THEME DAY: Easter Sunday. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Das letzte Ei findest du wieder erst im Juni.
- Ab Dienstag gibt's die Schokohasen zum halben Preis. Nur so.
Voted out here (stay away):
- Ostern. Der Hase bringt die Eier, und ich krieg wieder nichts. [not funny]
- Ostern. Früher hat man Eier selber gefärbt. Heute kauft man sie bunt. [not funny]

### `flavour_10.theme_force` (live now: 2)

THEME DAY: Star Wars Day, 4 May. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Früher hieß das bei uns einfach 4. Mai.
- In einer weit, weit entfernten Galaxis ist das Wetter auch nicht besser.
Voted out here (stay away):
- Star-Wars-Tag. Ein Lichtschwert hätt ich gern. Ich hab nicht mal Licht. [not funny]
- Möge die Macht mit dir sein. Das Wetter ist es heute schon. [not funny]

### `flavour_10.theme_ghd` (live now: 2)

THEME DAY: Groundhog Day, 2 February. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Und täglich grüßt das Murmeltier. Heute sogar offiziell.
- Heute sagt ein Murmeltier das Wetter an. Dem hören alle zu. Mir nie.
Voted out here (stay away):
- Murmeltiertag. Für mich ist das jeden Tag. [not funny]
- Murmeltiertag. Ich sag heute einfach wieder das Gleiche. [not funny]

### `flavour_10.theme_krampus` (live now: 1)

THEME DAY: Krampustag, 5 December. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Heute ist endlich mal einer schlechter gelaunt als ich.
Starred here before:
- Krampustag. Endlich ist mal einer schlechter gelaunt als ich.
Voted out here (stay away):
- Im Süden ist heute Krampuslauf. Da wundert sich keiner. [not funny]

### `flavour_10.theme_nikolo` (live now: 1)

THEME DAY: Nikolaustag, 6 December. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Die Schoko-Nikoläuse von heute sind die Osterhasen von morgen.
Voted out here (stay away):
- Nikolaus. Schokolade aus dem Stiefel. Tradition halt. [not funny]
- Am Nikolaustag bringen Schuhe vor der Tür ausnahmsweise was. [not funny]
- Nikolaus. Lob und Tadel aus dem goldenen Buch. Mach ich jeden Tag, ohne Buch. [not funny]
- Nikolaus. Der einzige Tag, an dem Schuhe vor der Tür was bringen. [not funny]

### `flavour_10.theme_ny` (live now: 2)

THEME DAY: New Year's Day. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Und wieder hat niemand seine Raketenreste weggemacht.
- Erst das Silvesterfeuerwerk, dann der Feinstaub. Prost Neujahr.

### `flavour_10.theme_okt` (live now: 3)

THEME DAY: Oktoberfest, 20 September to 5 October. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Eine Maß kostet schon wieder so viel wie früher ein ganzes Wochenende.
- „Ein Prosit der Gemütlichkeit“ läuft jetzt wieder alle zehn Minuten.
- Zwei Wochen lang ist eine Maß um zehn Uhr früh jetzt ganz normal.
Voted out here (stay away):
- Oktoberfest. Bei dem Wetter ist das Zelt voll. Bei jedem anderen übrigens auch. [not funny]
- Morgen erzählt wieder jeder, er hätt nur zwei Maß gehabt. [not funny]
- Oktoberfest. Heißt so, obwohl's im September anfängt. Typisch. [robotic]
- Oktoberfest. Und plötzlich hat jeder eine Lederhose. Auch in Hamburg. [robotic]
- Oktoberfest. Ich bleib nüchtern. Einer muss ja das Wetter ansagen. [robotic, unclear]

### `flavour_10.theme_spooky` (live now: 1)

THEME DAY: Halloween. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Früher war Reformationstag, da hatte man seine Ruhe.
Voted out here (stay away):
- Halloween. Gleich klingeln wieder Kinder, die man nicht kennt. [not funny] (note: i like the direction, but that one does not land.)
- Halloween. Der Kürbis kostet mehr als der Wocheneinkauf. [not funny]

### `flavour_10.theme_xmas` (live now: 0)

THEME DAY: Christmas, 24 to 26 December. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- Stille Nacht. Das Wetter hält sich dran. [not funny]
- Weihnachten. Früher lag mehr Schnee, sagen alle. Stimmt nicht. [not funny]
- Frohe Weihnachten. Für den Weg zur Verwandtschaft reicht's. [not funny]
- Die Weihnachtsgans hat heute den schlechtesten Tag von allen. [not funny]
- Weihnachten. Heute arbeiten nur noch ich und der Backofen. [not funny]
- Weihnachten. Der Braten ist im Ofen, der Streit ist in Vorbereitung. [not funny]
- Weihnachten. Die Gans hat heute den schlechtesten Tag von allen. [not funny]

## Output

Write `review/rounds/2026-10-fill/de.flavour10.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
