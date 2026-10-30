# Fill-up round (en, facts): every thin slot to at least four lines

You write lines for a TRMNL e-ink weather screen, "What to Wear". English, US spelling and words. The speaker is the TRMNL screen itself: a little too pleased with itself, dry, smug. Write in this language from scratch; never translate.

The owner reviewed every live line. These slots have fewer than four lines. For EACH slot write **9 candidates in the slot's established style plus 3 out-of-the-box ones** (a genuinely different angle or form the slot has never tried, still clear and on voice). A critic keeps the best 5-6 plus one out-of-the-box line per slot for the owner's vote, and the owner will cut some.

## Learn from what worked, first

- Read `docs/BRIEF.md` (the voice, the levels, every lesson).
- Read `review/examples/en.md`: the owner's starred lines. Reuse what makes them work (the angle, the rhythm, the length), not their words.
- Skim `review/dont/en.md`: vetoed lines with tags and notes. Never go near those.

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
- Freezing rain all day, and the roads and sidewalks may be icy. Take the umbrella and go slowly.
- It's freezing rain all day, so the sidewalks stay icy. Walk carefully and keep the umbrella with you.
- The freezing rain keeps going all day and leaves ice everywhere. Bring the umbrella and go slowly.

### `facts.p_stays_wet_storm` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: a thunderstorm. Raining now and all day. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- Rain and thunderstorms all day. Bring the umbrella.
- Thunderstorms come and go all day. Take the umbrella.
- It's wet and stormy all day. Bring the umbrella.

### `facts.p_wetter_ice` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: freezing rain, the ice warning. Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- Freezing rain {WHENP} makes roads and sidewalks icy. Take the umbrella and watch your step.
- Freezing rain {WHENP} makes the sidewalks icy, so walk carefully and take the umbrella.
- {WHENP} there's freezing rain and the roads turn icy. Bring the umbrella and take it slowly.

### `facts.p_wetter_long_storm` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: a thunderstorm. Rain later, and it stays. Shown alone; after a change, it follows that sentence. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- Thunderstorms start {WHENP}, and the rain keeps going. Bring the umbrella.
- {WHENP} thunderstorms move in and the rain keeps going. Bring the umbrella.
- Thunderstorms move in {WHENP}. Take the umbrella for the rain that follows.

### `facts.p_wetter_maybe_ice` (live now: 2)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: freezing rain, the ice warning. Rain possible later, not likely. Shown alone; after a change, it follows that sentence. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- There might be freezing rain {WHENP}. That could mean ice, so take the umbrella and walk carefully.
- Freezing rain could come {WHENP}, and with it ice. Take the umbrella to be safe.

### `facts.p_wetter_maybe_storm` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: a thunderstorm. Rain possible later, not likely. Shown alone; after a change, it follows that sentence. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- A thunderstorm is possible {WHENP}. An umbrella wouldn't hurt.
- There could be a thunderstorm {WHENP}. Take the umbrella, just in case.
- A thunderstorm is possible {WHENP}, so the umbrella's worth taking.

### `facts.p_wetter_storm` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: a thunderstorm. Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- There's a thunderstorm {WHENP}. Take the umbrella.
- Bring the umbrella for the thunderstorm {WHENP}.
- There's a thunderstorm {WHENP}, so keep the umbrella handy.

### `facts.shorts_swing_back` (live now: 3)

FORECAST SENTENCE (no joke, no level): plain, full, friendly sentence. New: the same, and the evening wants a layer back. {WHEN} is shorts weather, {WHEN2} the layer. Use the same placeholders as the live wordings, exactly.
Live here (don't repeat their ideas):
- You could think about wearing shorts instead. It's warm {WHEN}, but bring {G} for {WHEN2}.
- Shorts might work today: warm {WHEN}, cooler {WHEN2}. Keep {G} with you either way.
- {WHEN} it's shorts weather, but {WHEN2} it cools down again. If you go with shorts, definitely keep {G} handy.

## Output

Write `review/rounds/2026-10-fill/en.facts.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
