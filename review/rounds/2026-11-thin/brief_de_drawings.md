# Top-up round (de, drawings): thin slots to four lines

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

### `flavour_vf_10.fickle` (live now: 2; the critic keeps 3, write 9)

Under What to Wear Next's 2-3 drawings (now, later), no forecast sentence: the same outfit first and last with a change between (off and on again). The drawings show the change, so the joke may lean on them.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Mehrere Bilder für einen Tag. Ich bin doch kein Daumenkino.
- Im Café hängt heute wieder über jeder Stuhllehne ein halber Kleiderschrank.
Starred here before:
- Drei Bilder für einen Tag. Ich bin doch kein Daumenkino.
Voted out here (stay away):
- Morgens: Schicht an. Mittags: Schicht in der Hand. Abends: siehe morgens. [not funny]
- Mittags ruft wieder einer: „Jetzt wird's Frühling!“ Abends sagt er nichts mehr. [not funny]
- Wetter heute, kurz gefasst: Ja. Nein. Doch. [not funny]
- Morgen hat das Fundbüro wieder Hochbetrieb. [not funny] (note: not funny without context. even with context it's stretching it.)
- Das Wetter hat heute mehr Wendungen als ein Tatort. Und ein genauso vorhersehbares Ende. [not funny]
- Ein Tag für Leute mit großen Taschen und kleinen Erwartungen. [not funny] (note: i like the direction, but this is not landing.)
- Drei Bilder, und zweimal das Gleiche. Ich wiederhol mich ungern. [not funny]
- Am Ende schaut's aus wie am Anfang. Typisch für so einen Tag. [not funny]

## Output

Write `review/rounds/2026-11-thin/de.drawings.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
