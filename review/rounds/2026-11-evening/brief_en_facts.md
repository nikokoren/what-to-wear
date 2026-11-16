# Evening round (en): tomorrow's forecast sentences

You write lines for a TRMNL e-ink weather screen, "What to Wear". English, US spelling and words. The speaker is the TRMNL screen itself: a little too pleased with itself, dry, smug. Write in English from scratch; never translate.

## Read first

- `docs/BRIEF.md` (the voice, the levels, every lesson), above all "Tightening". Then `docs/CRITIC.md`: the critic cuts by it.
- `docs/PROOFREAD_EN.md`: the proofreader checks every line by it.
- `review/rounds/2026-10-en-tight/changes.md`: the owner's own before-and-after edits.
- `review/examples/en.md` (starred lines) and `review/dont/en.md` (vetoed lines).

## The screen

From 8 pm to midnight the screen shows tonight on the left (one drawing: what the reader has on, or the outfit still coming tonight) and tomorrow on the right under a black "Tomorrow · Sat" tag: the outfit for the reader's usual time out the door (labelled with that time, or "6–9 am"), then the first change of tomorrow, labelled like "from 1 pm". Under the drawings: tomorrow's forecast sentence in bold (sometimes right after today's sentence about a change still coming tonight), then, at sarcasm On and 11, one evening line. In the morning the screen goes back to what to wear right now.

## The job

Plain forecast sentences about tomorrow: no joke, no level, no sarcasm. Each must read as being about tomorrow at a glance (start with or contain "Tomorrow" / „Morgen“), stand as its own sentence after another one, and be short (one sentence, two at most; under about 70 characters with {FROM} filled). {FROM} is filled with "from 1 pm", so the grammar must work with exactly that. Use the same placeholder, never new ones. Name no garment: the drawings show which one, and it differs from day to day. No clock words beyond {FROM}, no promises the forecast can't keep, the state rather than its absence (see Tightening).

Write 12 candidates per situation (the critic keeps 4). Vary the structure across them; the screen rotates them hourly.

## Situations

### `evening.facts.tmr_steady`

Tomorrow's outfit works all day: one drawing, labelled 'all day'. No {FROM}.
Stand-in now: "Tomorrow, one outfit works all day."

### `evening.facts.tmr_warmer`

Tomorrow starts cooler and warms up {FROM}: the second drawing is lighter. Must fit whether tomorrow starts in a winter coat or in a T-shirt (then it gets hot), so don't promise a layer coming off.
Stand-in now: "Tomorrow it warms up {FROM}, so a layer can come off."

### `evening.facts.tmr_colder`

Tomorrow gets colder {FROM}: the second drawing is warmer. Must fit any start (a T-shirt that needs a sweater, a jacket that needs the winter coat).
Stand-in now: "Tomorrow it gets colder {FROM}, so bring a layer."

### `evening.facts.tmr_rain`

Rain starts tomorrow {FROM}: take the umbrella in the morning.
Stand-in now: "Tomorrow: rain {FROM}, so take the umbrella."

### `evening.facts.tmr_snow`

Snow starts tomorrow {FROM}.
Stand-in now: "Tomorrow: snow {FROM}."

### `evening.facts.tmr_drier`

Tomorrow starts wet and the rain stops {FROM}.
Stand-in now: "Tomorrow starts wet. The rain stops {FROM}."

### `evening.facts.tmr_wet`

Tomorrow starts wet (likely rain at the time the reader heads out): take the umbrella.
Stand-in now: "Tomorrow starts wet, so take the umbrella."

### `evening.facts.tmr_snow_start`

Tomorrow starts with snow.
Stand-in now: "Tomorrow starts with snow."

## Output

Write `review/rounds/2026-11-evening/en.facts.raw.json`: `{"lines": [{"path": "evening.facts.tmr_rain", "text": "..."}]}`. Check it parses. Edit nothing else, don't commit.
