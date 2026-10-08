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

## The pilot

1. Owner fills in `review/taste.md` and confirms the narrator sentence in
   the brief.
2. Owner votes the shipped `wet_again` lines: small, new, a warm-up for
   the page.
3. Two writers (Fable 5.1 and Opus 5.5) each write a `perfect` round for
   English, five candidates per line, from the same brief and taste file.
   Their lines go into one candidates file as batch A and batch B,
   shuffled; the key stays out of the repo until the votes are in.
4. Owner votes. Stars per batch decide who writes the rest.
