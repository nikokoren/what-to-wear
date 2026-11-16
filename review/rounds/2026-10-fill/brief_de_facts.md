# Fill-up round (de, facts): every thin slot to at least four lines

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

### `facts.p_stays_wet_ice` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: freezing rain, the ice warning. Raining now and all day. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- Den ganzen Tag gefrierender Regen, Straßen und Gehwege sind glatt. Nimm den Schirm mit und pass auf.
- Der gefrierende Regen hält den ganzen Tag an, überall ist es glatt. Nimm den Schirm mit und sei vorsichtig.
- Heute bleibt's bei gefrierendem Regen und Glatteis. Behalt den Schirm bei dir und lass dir auf dem Gehweg Zeit.

### `facts.p_stays_wet_storm` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: a thunderstorm. Raining now and all day. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- Den ganzen Tag Regen und Gewitter. Nimm den Schirm mit.
- Regen und Gewitter halten den ganzen Tag an. Behalt den Schirm bei dir.
- Heute gewittert's immer wieder, und der Regen hört nicht auf. Nimm den Schirm mit.

### `facts.p_wetter_ice` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: freezing rain, the ice warning. Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- {WHENP} droht Glatteis durch gefrierenden Regen. Nimm den Schirm mit und geh auf den Gehwegen langsam.
- {WHENP} kommt gefrierender Regen, dann wird's auf Straßen und Gehwegen glatt. Nimm den Schirm mit und sei vorsichtig.
- Nimm den Schirm mit, {WHENP} kommt gefrierender Regen.

### `facts.p_wetter_long_ice` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: freezing rain, the ice warning. Rain later, and it stays. Shown alone; after a change, it follows that sentence. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- {WHENP} setzt gefrierender Regen ein und hört nicht mehr auf. Rechne mit Glatteis und nimm den Schirm mit.
- {WHENP} beginnt gefrierender Regen, und der hält an. Nimm den Schirm mit und geh vorsichtig.
- Nimm den Schirm mit: {WHENP} fängt gefrierender Regen an und bleibt. Pass auf, es wird spiegelglatt.

### `facts.p_wetter_long_storm` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: a thunderstorm. Rain later, and it stays. Shown alone; after a change, it follows that sentence. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- {WHENP} kommen Gewitter, und der Regen hört nicht mehr auf. Nimm den Schirm mit.
- {WHENP} ziehen Gewitter auf, danach regnet's weiter. Nimm den Schirm mit.
- Nimm den Schirm mit: {WHENP} beginnt Regen mit Gewittern, und der bleibt.

### `facts.p_wetter_maybe_ice` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: freezing rain, the ice warning. Rain possible later, not likely. Shown alone; after a change, it follows that sentence. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- {WHENP} ist gefrierender Regen möglich, dann wird's glatt. Ein Schirm schadet nicht.
- {WHENP} könnte gefrierender Regen kommen. Dann wird's glatt, also pack lieber den Schirm ein und sei vorsichtig.
- Vielleicht kommt {WHENP} gefrierender Regen. Nimm sicherheitshalber den Schirm mit.

### `facts.p_wetter_maybe_storm` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: a thunderstorm. Rain possible later, not likely. Shown alone; after a change, it follows that sentence. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- {WHENP} ist ein Gewitter möglich. Ein Schirm schadet nicht.
- Vielleicht gibt's {WHENP} ein Gewitter. Nimm den Schirm mit.
- {WHENP} kann ein Gewitter aufziehen. Mit Schirm bist du gut vorbereitet.

### `facts.p_wetter_storm` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: a thunderstorm. Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- Nimm den Schirm mit, {WHENP} gibt's ein Gewitter.
- {WHENP} zieht ein Gewitter durch. Nimm den Schirm mit.
- {WHENP} kommt ein Gewitter. Pack den Schirm ein.

### `facts.shorts_swing` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: a cold morning with three hours or more of shorts weather later (a reader in Colorado). The drawing keeps the coat; go out in shorts anyway. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- {WHEN} wird's warm. Überleg dir, gleich ne kurze Hose anzuziehen.
- Es lohnt sich eventuell, schon jetzt kurze Hosen anzuziehen, {WHEN} wird's warm.
- Zieh eventuell gleich deine kurze Hose an. {WHEN} ist's warm genug dafür.

### `facts.shorts_swing_back` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: the same, and the evening wants a layer back. {WHEN} is shorts weather, {WHEN2} the layer. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- {WHEN} wird's warm, {WHEN2} wieder kühl. Kurze Hosen sind eventuell die bessere Wahl.
- Überleg dir, ne kurze Hose anzuziehen, {WHEN} wird's warm. Die warme Schicht solltest du aber trotzdem mitnehmen.
- Eventuell passt heute eine kurze Hose besser, {WHEN} wird's warm. {WHEN2} brauchst du aber die warme Schicht wieder.

## Output

Write `review/rounds/2026-10-fill/de.facts.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
