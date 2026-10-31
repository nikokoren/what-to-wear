# Proofread the German texts of "What to Wear"

## What this is
"What to Wear" is a plugin for TRMNL, a small e-ink display that hangs at home. It shows a drawing of what to wear today, plus one plain sentence on what changes during the day, e.g. „Die Jacke kann heute Nachmittag weg. Halt sie aber griffbereit, heute Abend brauchst du sie wieder.“

If the user wants, a sarcastic line is added. The display itself is the speaker: a Grantler, dry and a little fed up, in standard German (no dialect).

## Sarcasm levels
- **0 / Aus:** forecast sentence only.
- **10 / An:** sarcastic and dry, about the weather, the world or the display itself. Never aimed at the reader.
- **11:** sarcastic and personal, aimed at the reader. Looks are fair game.

## The texts
File: `prototypes/fact-flavour/lang/de.json` in the repo `nikokoren/what-to-wear`, branch `claude/serene-meitner-cg3e4v` (or the attached copy). Review these sections and skip everything else (`garments*`, `topical_*`):

| Section | What it is |
|---|---|
| `facts.<situation>` | Forecast sentences: plain, factual, the same at every level. |
| `units_10`, `units_11` | A forecast sentence and its joke, written together: `Satz || Witz`. On screen, the joke sits under the sentence. |
| `flavour_10`, `flavour_11` | Jokes shown under a forecast sentence. `day_*` / `theme_*` are special days (Weihnachten, Zeitumstellung …). |
| `now_10`, `now_11` | Jokes about the weather right now, with no forecast sentence. |
| `flavour_vf_10`, `flavour_vf_11` | Jokes under 2–3 drawings (now / later), with no forecast sentence. |

The key name after the section (e.g. `w_jacket`, `p_wetter`, `cold`) is the weather situation.

**Tags at the start of a line are not text:** `{M:11,12}` (only in those months), `{AM}` (only before noon), `{3}`, `{W:...}`. Ignore them, but keep them unchanged.

**Placeholders the display fills in.** Every line must work with every possible value:
- `{WHEN}`, `{WHEN2}`, `{WHENP}`, `{WHENSTOP}`: „heute Vormittag“, „gegen Mittag“, „heute Nachmittag“, „heute Abend“, „heute Nacht“, „in einer Stunde“, „in zwei Stunden“, „in drei Stunden“. A preposition in front of one breaks („für in drei Stunden“), and so does a sentence that only works with some of them.
- `{GV}`: „kann der Schal“ / „kann die Winterjacke“ / „kann die Jacke“ / „kann der Pulli“.
- `{GP}`: the matching pronoun „ihn“ / „sie“ (Schal → ihn, Winterjacke → sie, Jacke → sie, Pulli → ihn). Check that gender and case still fit.

## What to flag
Read every line and flag it if it:
- is grammatically wrong (case, gender, word order, tense, agreement),
- has a spelling or punctuation error (including „…“ quotes, commas, apostrophes),
- doesn't sound like natural German („so sagt das keiner“), or sounds translated,
- is unclear on first read, or seems off in a way you can name,
- breaks with one of the placeholder values above,
- doesn't fit its situation or level: e.g. a forecast sentence that jokes, an An line that attacks the reader, or a forecast sentence whose meaning doesn't match its key.

Do not flag a line only because you find it unfunny. Do not rewrite for style when nothing is wrong. Lines you don't flag count as fine.

## Output
Write one file, `flags_de.json`: a JSON list with one object per flagged line:

```json
[
  {
    "where": "units_10.w_jacket",
    "text": "<the line exactly as it is in de.json, tags included>",
    "reasons": ["Grammatik"],
    "suggestion": "<the full corrected line, or empty if you have none>",
    "note": "<short reason in German, e.g. „mit ‚der Schal‘: ‚ihn‘ statt ‚sie‘“>"
  }
]
```

- **`reasons`:** one or more of „Grammatik“, „Rechtschreibung / Zeichensetzung“, „Klingt unnatürlich“, „Unklar“, „Passt nicht zur Situation“, „Anderes“.
- **`suggestion`:** keep every tag, every placeholder exactly as written (`{WHEN}`, `{GP}` …) and the ` || ` separator. Change only what's needed.
- **No file edits:** don't edit `de.json` or any other file, and don't commit. Check that the output parses as JSON.
- **When done:** report how many lines you checked and how many you flagged, per section.

## Candidate mode (every writing round)

Used on a round's candidates after the critic, before the owner votes
(`docs/BRIEF.md`, "How to write a round"). Everything above applies, plus
`docs/BRIEF.md` "Tightening" and `docs/CRITIC.md`.

- Input: the critic's file, `review/rounds/<round>/de.json`
  (`{"lines": [{"path", "text", ...}]}`).
- For each line: leave it, fix it, or cut it. Fix in place when a small
  change makes it right (grammar, punctuation, word choice, idiom); keep
  every tag, placeholder and the ` || ` separator. Cut when it can't be
  fixed without becoming a different line. Also cut a line that is a weak joke rather than sarcasm, or that needs context the screen doesn't give (the owner's round 25 notes: „frostig“ used wrongly; „Vorhin war's doch noch warm. Ja. Vorhin.“; „Morgen hat das Fundbüro wieder Hochbetrieb.“).
- Write `review/rounds/<round>/de.proofread.json`: the same format,
  the kept lines (fixed ones with their new text), and on each fixed line
  `"was"` (the critic's text) and `"reasons"` (from „Grammatik“, „Rechtschreibung / Zeichensetzung“, „Klingt unnatürlich“, „Unklar“, „Passt nicht zur Situation“, „Anderes“). Write
  `review/rounds/<round>/de.proofread_cuts.json` with the cut lines and
  a short reason each.
- Report how many lines you kept unchanged, fixed and cut, per slot.
  Don't edit other files, don't commit.
