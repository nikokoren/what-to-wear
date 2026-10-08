# Text review

How lines get written, judged and kept. The writer's side is in
[docs/BRIEF.md](../docs/BRIEF.md).

## The loop

1. **Write a round.** A writer reads the brief, the taste file, the
   starred examples and the "don't" list, then writes about five
   candidates per line needed into `review/rounds/<round>.json`.
2. **Build the page.**

   ```bash
   python3 tools/review_export.py --candidates review/rounds/<round>.json --only-candidates
   python3 tools/review_export.py --keys wet_again,wet_again_j   # shipped lines instead
   python3 tools/review_export.py                                # everything shipped
   ```

   This writes `build/review/index.html` and the sprites it shows. Claude
   publishes it to the same review page each time; votes live in the
   page's database, so a new build never loses one.
3. **Vote.** Each line is shown on a mock device with its drawing and
   time words filled in; lines that join a rain sentence show the pair.
   Star, Keep or Veto, with tags (robotic, too long, not funny, wrong
   garment, wrong fact, unclear) and an optional note. Keyboard: `S` `K`
   `V`, tags `1`–`6` (set them before the verdict), `N` for a note, `R`
   for the rain pairing, arrows to move. The key list counts stars,
   keeps and vetoes and warns before a key is vetoed empty.
4. **Sync.** Ask Claude to sync the review. It reads the votes from the
   page's database (or use the page's "Save decisions file") and runs:

   ```bash
   python3 tools/review_sync.py <decisions.json> --fixes
   python3 tools/apply_review.py build/review/en_fixes.json --dry-run
   ```

   That updates `review/decisions/`, `review/examples/` and `review/dont/`
   in the repo, and writes a fix file: vetoed shipped lines are deleted,
   starred or kept candidates appended. `apply_review.py` refuses any fix
   whose line changed since the vote, and never deletes a key's last line.
5. **Check and ship.** `validate_lang.py`, `check_combinations.py`,
   `style_report.py`, then rebuild the transitional markup.

## What is kept in the repo

| Path | What | Written by |
|---|---|---|
| `review/taste.md` | lines the owner likes from anywhere, and dislikes from here | the owner |
| `review/decisions/<lang>.json` | every vote, by line id (language + hash of the text) | `review_sync.py` |
| `review/examples/<lang>.md` | starred lines: the writer's examples | `review_sync.py` |
| `review/dont/<lang>.md` | vetoed lines with tags and notes | `review_sync.py` |
| `review/rounds/<round>.json` | candidates as written | the writer |
| `review/page.html` | the page template | by hand |

A line's id comes from its text, so a line that moves keeps its vote and
an edited line is reviewed again. A vetoed line stays in `decisions/`
after it is deleted from `lang/`, which is what keeps it from coming back.

## The voice audition (October 2026)

Before any lines are written at scale, pick the voice. The tip is now a
fact line plus a flavour line (`prototypes/fact-flavour/`), and only the
flavour line has a voice.

- `review/rounds/2026-10-voices.json`: five English voices and five
  separate German ones, the same four moods each (nice, wet, cold,
  evening), two lines per mood at On and at 11. 160 lines. English voices
  are letters A to E, German F to J.
- **Don't open `2026-10-voices.key.json` or `make_voices.py` until you've
  voted**: they say which letter is which voice.
- Vote on the review page. Filter by Voice to hear one voice across moods,
  or by key to compare all voices on the same mood.
- Then: `python3 tools/review_sync.py <votes> --key=review/rounds/2026-10-voices.key.json`
  prints the score per voice. The winner (or a blend of two) becomes the
  brief for the real writing round.
