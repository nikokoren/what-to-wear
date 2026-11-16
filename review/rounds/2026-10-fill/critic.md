# Critic, fill-up round (round 24)

The writers wrote 12 candidates per thin slot (9 in the slot's style, 3
marked `"wild": true`) in `review/rounds/2026-10-fill/<lang>.*.raw.json`.
The briefs they worked from are `brief_<lang>_*.md` in the same folder:
each slot's meaning, level, live lines, and what was voted out there.

You pick for the owner's vote. Per slot keep **the best 6** of the
regular candidates (5 if the sixth is weak) and **the best 1 wild one**.
The owner will cut some, so weak lines only waste the vote.

## Read first

- `docs/BRIEF.md`: the voice, the levels, every lesson from earlier rounds.
- `review/examples/<lang>.md`: what the owner starred. Your yardstick.
- `review/dont/<lang>.md`: what the owner vetoed, with tags and notes.
  Most vetoes say "not funny": flat, gentle, or a restatement.

## Cut

- Not funny, not sarcastic, merely pleasant, or a restatement of the weather.
- Unclear on first read; too long for a small e-ink screen.
- Wordplay on the forecast's words; "like your X" / „wie deine X“ jabs;
  predicting the reader's mishaps; explaining the joke.
- Wrong level: at On a jab at the reader; at 11 nothing about the reader.
- Anything the screen can't know, or that assumes how the reader lives.
- A unit whose forecast sentence uses a placeholder its live sentences
  don't have, or changes what the forecast says.
- A garment joke that doesn't fit every garment the slot covers.
- English: anything not US English, "hallway". German: dialect.
- Two candidates with the same idea (keep the better one), or one that
  repeats a live line's idea.
- Forecast sentences (`facts.*`): keep the clearest, most natural plain
  wordings; no jokes there.

## Output

Write `review/rounds/2026-10-fill/<lang>.json`:
`{"lines": [{"path": "...", "text": "...", "wild": true?, "months": "..."?}]}`,
the chosen lines only, unchanged except for a plain typo or spelling fix.
Then print, per slot, how many you kept. Check the file parses. Don't
edit any other file and don't commit.
