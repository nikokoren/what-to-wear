# Fill-up round (de, other): every thin slot to at least four lines

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

### `flavour_vf_10.cold` (live now: 0)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: cold all the way. The drawings show the change, so the joke may lean on them.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- Auf jedem Bild dick eingepackt. Schöner wird dadurch keiner. [not funny]
- Ich mal die Jacken. Frieren müsst ihr selber. [not funny]

### `flavour_vf_11.cold` (live now: 1)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: cold all the way. The drawings show the change, so the joke may lean on them.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Egal wann: Du frierst.
Voted out here (stay away):
- Auf dem Bild hast du Handschuhe. Deine liegen noch im Keller. [not funny]

### `flavour_vf_10.cooling` (live now: 0)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: the last drawing is colder: a layer goes on. The drawings show the change, so the joke may lean on them.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- Die Extraschicht kommt erst später. Spannung bis zum Schluss. [not funny]
- Später kommt eine Schicht dazu. Merkt sowieso keiner. [not funny]

### `flavour_vf_11.cooling` (live now: 0)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: the last drawing is colder: a layer goes on. The drawings show the change, so the joke may lean on them.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- Auf dem Bild trägst du später was Wärmeres. Rate mal, wo deins ist. [not funny, unclear]
- Die Extraschicht auf dem Bild? Die liegt bei dir dann zu Hause. [not funny, unclear]

### `flavour_vf_10.fickle` (live now: 1)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: the same outfit first and last with a change between (off and on again). The drawings show the change, so the joke may lean on them.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Drei Bilder für einen Tag. Ich bin doch kein Daumenkino.
Voted out here (stay away):
- Drei Bilder, und zweimal das Gleiche. Ich wiederhol mich ungern. [not funny]
- Am Ende schaut's aus wie am Anfang. Typisch für so einen Tag. [not funny]

### `flavour_vf_11.fickle` (live now: 1)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: the same outfit first and last with a change between (off and on again). The drawings show the change, so the joke may lean on them.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- An, aus, an. Irgendwo dazwischen verlierst du vermutlich wieder die Mütze.
Voted out here (stay away):
- Am Ende bist du wieder eingepackt. Und genauso schlecht gelaunt. [not funny]
- Drei Bilder, drei Outfits. Du kommst schon mit einem kaum zurecht. [not funny]

### `flavour_vf_10.hot` (live now: 0)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: hot all the way. The drawings show the change, so the joke may lean on them.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- Von Bild zu Bild weniger an. Weiter runter mal ich nicht. [not funny]
- Je später, desto luftiger. Ich hab da meine Grenzen. [not funny]

### `flavour_vf_11.hot` (live now: 0)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: hot all the way. The drawings show the change, so the joke may lean on them.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- Weniger an, mehr Gejammer. Ich kenn dich. [not funny, robotic]
- Von Bild zu Bild luftiger. Dein Gejammer bleibt gleich. [not funny]

### `flavour_vf_10.nice` (live now: 0)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: nice weather, the drawings change a little. The drawings show the change, so the joke may lean on them.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups

### `flavour_vf_11.nice` (live now: 0)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: nice weather, the drawings change a little. The drawings show the change, so the joke may lean on them.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups

### `flavour_vf_10.snow` (live now: 1)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: snow across the drawings. The drawings show the change, so the joke may lean on them.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Malen kann ich den Schnee. Wegmachen musst du ihn selber.
Voted out here (stay away):
- Auf meinen Bildern sieht Schnee ordentlich aus. Draußen nicht. [not funny]

### `flavour_vf_11.snow` (live now: 2)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: snow across the drawings. The drawings show the change, so the joke may lean on them.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Ich sag dir, es schneit, und du bist trotzdem überrascht. Jedes Mal.
- {M:10,11,12}Schnee kommt. Deine Stiefel sind natürlich noch im Keller.

### `flavour_vf_10.warming` (live now: 1)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: the last drawing is warmer: a layer comes off. The drawings show the change, so the joke may lean on them.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Das Wetter wird besser. Deine Leute gleich lauter.
Voted out here (stay away):
- Zum Schluss ist's warm. Mehr Happy End biet ich normalerweise nicht. [not funny]
- Zwei Bilder für einmal Ausziehen. Was ich mir nicht alles antue. [not funny]
- Später ist eine Schicht weg. Mehr Spannung gibt's heute nicht. [not funny]
- Erst mit, dann ohne. Ein Drama in zwei Akten. Ein kurzes. [not funny]

### `flavour_vf_11.warming` (live now: 0)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: the last drawing is warmer: a layer comes off. The drawings show the change, so the joke may lean on them.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Voted out here (stay away):
- Auf dem Bild schwitzt du nicht. Wunschdenken. [not funny]
- Später ist eine Schicht weg. Bei dir dauert das bis zum Abend. [not funny, unclear]
- Zwei Bilder, zwei Outfits. Du schaffst mit Mühe eins. [not funny]

### `flavour_vf_10.wet` (live now: 3)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: rain comes or goes across the drawings. The drawings show the change, so the joke may lean on them.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Einen Schirm hab ich dir schon gemalt. Mitnehmen musst du ihn selber.
- Ich mal den Schirm. Mitnehmen musst du ihn schon selber.
- Mit Schirm, ohne Schirm. Ich mal alles, und keiner dankt's mir.
Voted out here (stay away):
- Auf einem Bild ist ein Schirm. Übersehen tun ihn trotzdem alle. [not funny]

### `flavour_vf_11.wet` (live now: 1)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: rain comes or goes across the drawings. The drawings show the change, so the joke may lean on them.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Den Schirm siehst du. Mitnehmen wirst du ihn trotzdem nicht.
Voted out here (stay away):
- Mit Schirm siehst du richtig vernünftig aus. Leider nur gemalt. [not funny]
- Gemalt hab ich den Schirm. Vergessen musst du ihn schon selber. [not funny]
- Auf einem Bild hast du einen Schirm. In echt eher nicht. [not funny]

### `now_10.evening` (live now: 3)

About the weather right now, alone under the drawing: evening, 18:00-22:00 (people go out; no bedtime).
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Pünktlich zum Feierabend fällt wieder eine S-Bahn aus.
- Gleich bohrt garantiert wieder irgendein Nachbar in der Wand rum.
- Jetzt stehen wieder alle im Stau und nennen es Feierabend.
Voted out here (stay away):
- Typisch. Um kurz vor Feierabend kommt natürlich eine „kurze Rückfrage“. [not funny]
- Irgendwo schunkeln jetzt wieder Erwachsene mit Pappnase. Freiwillig. [not funny]

## Output

Write `review/rounds/2026-10-fill/de.other.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
