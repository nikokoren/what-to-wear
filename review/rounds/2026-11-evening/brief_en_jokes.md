# Evening round (en): the evening line

You write lines for a TRMNL e-ink weather screen, "What to Wear". English, US spelling and words. The speaker is the TRMNL screen itself: a little too pleased with itself, dry, smug. Write in English from scratch; never translate.

## Read first

- `docs/BRIEF.md` (the voice, the levels, every lesson), above all "Tightening". Then `docs/CRITIC.md`: the critic cuts by it.
- `docs/PROOFREAD_EN.md`: the proofreader checks every line by it.
- `review/rounds/2026-10-en-tight/changes.md`: the owner's own before-and-after edits.
- `review/examples/en.md` (starred lines) and `review/dont/en.md` (vetoed lines).

## The screen

From 8 pm to midnight the screen shows tonight on the left (one drawing: what the reader has on, or the outfit still coming tonight) and tomorrow on the right under a black "Tomorrow · Sat" tag: the outfit for the reader's usual time out the door (labelled with that time, or "6–9 am"), then the first change of tomorrow, labelled like "from 1 pm". Under the drawings: tomorrow's forecast sentence in bold (sometimes right after today's sentence about a change still coming tonight), then, at sarcasm On and 11, one evening line. In the morning the screen goes back to what to wear right now.

## The job

One sarcastic line under tomorrow's forecast, every evening from 8 pm. It must work with ANY weather (the same pool serves rain, snow, heat and a steady day), so its subject is the evening, tomorrow, the preview itself, getting ready the night before, the screen knowing tomorrow before you do, the reader's evening self versus their morning self. Never restate the forecast. Short: one or two short sentences.

- **On (`evening.jokes_10`)**: sarcastic and dry, about the weather, the world, other people or the screen itself. Never about the reader. Avoid the worn On moves the owner called meh: the screen smug about living indoors, being dry or gray, being right again, "everyone checks me".
- **11 (`evening.jokes_11`)**: sarcastic and personal, about the reader. Looks and worth are fair game. The owner liked 11 best lately: specific, confident, a little cruel.
- Nothing the screen can't know: no assumptions about the reader's job, partner, kids, car or plans. 8 pm to midnight is not necessarily bedtime.
- No line may repeat an idea from `review/examples` or the live pools in `prototypes/fact-flavour/lang/en.json`.

Stand-ins now: On "Two forecasts for the price of one. Still free." · 11 "Lay it out tonight. Morning-you can't be trusted with decisions."

Write 24 candidates per level (the critic keeps 8). At least a third out of the box (a fake notice, a confession, a very specific scene, a twist at the end), still clear on first read.

## Output

Write `review/rounds/2026-11-evening/en.jokes.raw.json`: `{"lines": [{"path": "evening.jokes_10", "text": "..."}]}`. Check it parses. Edit nothing else, don't commit.
