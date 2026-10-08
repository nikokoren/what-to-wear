# Writer's brief

This replaces the rulebook in [VOICE.md](VOICE.md) as the thing a writer
works from. It is short on purpose: what steers the writing is the
owner's taste, kept as examples, not adjectives.

## Who is talking

> **A friend who checked the weather for you before you left, and tells
> you the one thing worth knowing.**

*(Draft. The owner confirms or rewrites this sentence before the pilot.)*

The three sarcasm levels are the same friend in three moods:

| Level | Setting | The friend is |
|---|---|---|
| `0` | Plain | helpful and brief |
| `10` | Dry | the same, with a straight face |
| `11` | Sarcastic | teasing you, because they know you |

## What to read before writing, in this order

1. **The facts of the key** in [SCENARIOS.md](SCENARIOS.md): when it
   fires, what the drawing shows, which tokens resolve. These are hard
   rules. A line that is funny and wrong is vetoed.
2. **`review/taste.md`**: lines the owner likes from anywhere, and lines
   from this corpus they dislike, each with one word for why.
3. **`review/examples/<lang>.md`**: lines the owner starred on the review
   page. Write lines that would sit beside them.
4. **`review/dont/<lang>.md`**: vetoed lines with their reasons. Never
   reuse one, or its sentence frame.

## How to write a round

- **One situation at a time.** Write for the screen the line appears on:
  the drawing, the time words filled in, and the rain half it is paired
  with. `python3 tools/review_export.py --keys <key>` renders those.
- **Five candidates for every line needed.** The owner keeps the best;
  the rest are thrown away, not repaired.
- **Few lines per key.** A reader sees one line a day. Three great lines
  beat twelve passable ones; `perfect` and `c_relief` earn more because
  they show most often.
- **German is written in German**, against the German examples, never
  translated from the English.
- **Run `python3 tools/style_report.py <lang>`** before handing over. It
  flags the habits that made the last corpus read as generated: objects
  given a job (the jacket's "shift", the rain's "calendar"), semicolons,
  ", because" explanations, and repeated sentence frames.

Hard limits that stay: no temperatures in the text, the 165-character
budget for the full tip (`tools/check_combinations.py`), and the token
rules in [TRANSLATING.md](TRANSLATING.md).

## Handing a round over

A round is a candidates file, `review/rounds/<round>.json`:

```json
{"round": "2026-11-perfect",
 "lines": [{"lang": "en", "path": "temp_10.perfect", "text": "...", "batch": "A"}]}
```

`batch` is shown on the page only as a letter. To compare two writers
blind, give each a letter and keep which is which out of the repo until
the votes are in. The full loop is in [review/README.md](../review/README.md).
