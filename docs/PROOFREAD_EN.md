# Proofread the English texts of "What to Wear"

## What this is
"What to Wear" is a plugin for TRMNL, a small e-ink display that hangs at home. It shows a drawing of what to wear today, plus one plain sentence on what changes during the day, e.g. "The jacket can come off this afternoon. Keep it handy, you'll want it back this evening."

If the user wants, a sarcastic line is added. The display itself is the speaker: a screen on the wall that is a little too pleased with itself. Dry, smug, never cruel by accident. The English is **US English**.

## Sarcasm levels
- **0 / Off:** forecast sentence only.
- **10 / On:** sarcastic and dry, about the weather, the world or the display itself. Never aimed at the reader.
- **11:** sarcastic and personal, aimed at the reader. Looks are fair game.

## The texts
File: `prototypes/fact-flavour/lang/en.json` in the repo `nikokoren/what-to-wear`, branch `claude/serene-meitner-cg3e4v` (or the attached copy). Review these sections and skip everything else (`garments*`, `topical_*`):

| Section | What it is |
|---|---|
| `facts.<situation>` | Forecast sentences: plain, factual, the same at every level. |
| `units_10`, `units_11` | A forecast sentence and its joke, written together: `sentence || joke`. On screen, the joke sits under the sentence. |
| `flavour_10`, `flavour_11` | Jokes shown under a forecast sentence. `day_*` / `theme_*` are special days (Christmas, the clock change …). |
| `now_10`, `now_11` | Jokes about the weather right now, with no forecast sentence. |
| `alone_10`, `alone_11` | The only text on screen, under one drawing. Must make sense completely on its own. |
| `flavour_vf_10`, `flavour_vf_11` | Jokes under 2–3 drawings (now / later), with no forecast sentence. |

The key name after the section (e.g. `w_jacket`, `p_wetter`, `cold`) is the weather situation.

**Tags at the start of a line are not text:** `{M:11,12}` (only in those months), `{AM}` (only before noon), `{3}`, `{W:...}`. Ignore them, but keep them unchanged.

**Placeholders the display fills in.** Every line must work with every possible value:
- `{WHEN}`, `{WHEN2}`, `{WHENP}`, `{WHENSTOP}`: "this morning", "around midday", "this afternoon", "this evening", "tonight", "in an hour", "in two hours", "in three hours". A preposition in front of one breaks ("for in three hours", "until in an hour"), and so does a sentence that only works with some of them.
- `{G}`: "the scarf" / "the winter coat" / "the jacket" / "the sweater" (capitalized at the start of a sentence).
- `{GP}`: always "it". Check the sentence still reads right for every garment ("it" for a scarf, not "them"; no sleeves for a scarf).

## What to flag
Read every line and flag it if it:
- is grammatically wrong (agreement, tense, articles, word order),
- has a spelling or punctuation error ("…" quotes, commas, apostrophes, its/it's),
- isn't US English: British spelling or words (colour, grey, favourite, pavement, autumn, jumper, trousers, "in hospital") or British idiom,
- doesn't sound like natural English, or sounds translated,
- is unclear on first read, or seems off in a way you can name,
- breaks with one of the placeholder values above,
- says "hallway" for where the screen hangs (it's "room", or kept vague),
- doesn't fit its situation or level: e.g. a forecast sentence that jokes, an On line that attacks the reader, an `alone_` line that needs a forecast sentence to make sense, or a forecast sentence whose meaning doesn't match its key.

Do not flag a line only because you find it unfunny. Do not rewrite for style when nothing is wrong. Lines you don't flag count as fine.

## Output
Write one file, `flags_en.json`: a JSON list with one object per flagged line:

```json
[
  {
    "where": "units_10.w_jacket",
    "text": "<the line exactly as it is in en.json, tags included>",
    "reasons": ["Grammar"],
    "suggestion": "<the full corrected line, or empty if you have none>",
    "note": "<short reason, e.g. 'with \"the scarf\": no sleeves'>"
  }
]
```

- **`reasons`:** one or more of "Grammar", "Spelling / punctuation", "Not US English", "Unnatural", "Unclear", "Doesn't fit the situation", "Other".
- **`suggestion`:** keep every tag, every placeholder exactly as written (`{WHEN}`, `{G}`, `{GP}` …) and the ` || ` separator. Change only what's needed.
- **No file edits:** don't edit `en.json` or any other file, and don't commit. Check that the output parses as JSON.
- **When done:** report how many lines you checked and how many you flagged, per section.
