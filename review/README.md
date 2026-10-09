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
- **Result (8 October):** English, the screen (+6; every other voice
  scored −17 or worse). German, the Grantler (0) and the Wetterfrosch
  (−4); Kumpel, Oma and the Bauernregel lost. The lessons are in
  `docs/BRIEF.md`.

## Round 2 (October 2026)

Two rounds on one page, each blind by letter:

- `2026-10-voices-2`: the flavour line narrowed to the winners and
  rewritten under the lessons. English: the screen (set W). German: the
  Grantler without dialect, and a grumbling TV weather presenter (sets X
  and Y). All nine moods, including `night` (from 22:00, the only mood
  that may mention bed). Lines you already rated in round 1 keep their
  vote and don't come back under "Not rated".
- `2026-10-facts`: the fact line. Six styles (sets K to P in English, Q
  to V in German), each written for the same eight real situations.
  Filter by key to compare the styles on one situation.
- Keys: `2026-10-voices-2.key.json`, `2026-10-facts.key.json`; sync with
  `--key=` both, comma-separated.
- **Result (9 October):** fact line, plain sentences won both
  languages (English +12, German +8; timeline −16, minimal −13). Flavour,
  the German Grantler held (+2) and the TV presenter lost (−33); the
  English screen stayed the only English voice, though no new line got a
  star. Details in `docs/BRIEF.md`.
- After the voice is picked, the first real round is also the model
  comparison: Fable 5.1 and Opus 5.5 each write it from the same brief,
  as two blind batches.

## Round 3: the writing round (October 2026)

Fill every flavour pool: three new candidates per mood, level and
language, written cold from the brief by a subagent.

- `2026-10-writing.json`: Opus 5.5's 108 lines (sets E1/E2 in English,
  D1/D2 in German; one of each is in use until the second writer runs).
  The writer's raw output is in `2026-10-writing/`.
- The Fable 5.1 writer, given the identical brief, could not run: the
  account had no Fable usage credits. Once it can, run it with the same
  prompt, save its output next to Opus's, and rebuild with
  `python3 review/rounds/make_round3.py "Opus 5.5=review/rounds/2026-10-writing/opus-5.5.json" "Fable 5.1=<file>"`.
  Opus keeps its label; lines already rated are dropped.
- **Result (9 October):** German 6 stars, 32 keeps, 16 vetoes (+12);
  English 1 star, 31 keeps, 22 vetoes (−11). The pools now hold 2 to 5
  lines per mood, rebuilt with `python3 review/rounds/build_pools.py`;
  German `mild` at On is still empty.

## Round 4: the top-up (October 2026)

"Mild" split into `warming`, `cooling` and `cool` (see `docs/BRIEF.md`),
and every pool topped up, sized by how often its mood shows. One writer
per language (Opus 5.5), the German one forbidden from reading any
English lines. 172 lines in `2026-10-topup.json` (sets E4 and D4), raw
output in `2026-10-topup/`. After voting: sync, then
`python3 review/rounds/build_pools.py`.
- **Result (9 October):** German 3 stars, 39 keeps, 44 vetoes; English
  0 stars, 42 keeps, 44 vetoes. Pools now hold 1 to 9 lines per mood;
  warming and cooling also draw from cool. Lessons in `docs/BRIEF.md`.

## Round 5: variants (October 2026)

Enough lines that a run of the same weather doesn't show the same words.
Written by hand (`make_round5.py`), not by a writer agent: this is
editing, not invention. 361 lines in `2026-10-variants.json`:

- **Fact wordings** (sets FE, FD): two to four new wordings of every fact
  template, five in all for the common situations. Shown with time words
  filled in; each row also shows the current wording. Kept wordings join
  the list the template rotates through (`facts` in the prototype are
  now lists, rotated by day on their own offset).
- **Flavour rewordings** (sets VE, VD): one new wording of every line in
  the pools, same joke, different words; each row shows the line it
  varies. A kept rewording goes into the pool a whole cycle after its
  original, never next to it. The German ones also drop the Austrian
  markers still in some kept lines ("eh", "nix", "Leut'", "heuer",
  "Wennst").

After voting: sync, then `python3 review/rounds/build_pools.py`, which now
also builds the fact lists.

Repeats, measured by `tools/climate/repeat_report.py` (7:00 in London,
New York, Minneapolis, Phoenix and Vienna, 2024-2025, sarcasm On): the
share of lines already shown in the previous 7 / 30 days.

| | before | every variant kept |
|---|---|---|
| English fact line | 33% / 50% | 10% / 28% |
| English flavour line | 29% / 79% | 1% / 56% |
| English whole screen | 10% / 28% | 0% / 8% |
| German fact line | 33% / 50% | 12% / 29% |
| German flavour line | 15% / 75% | 4% / 50% |
| German whole screen | 5% / 23% | 0% / 2% |

The 30-day flavour number is the one left to beat: the pools are small,
and a rewording doesn't count as a new joke. Next steps are item 6 in
`docs/TODO.md`.

**Result (9 October):** fact wordings did well: English 19 stars, 33
keeps, 2 vetoes (25 not yet rated: the steady and `w_*` ones); German 26
stars, 40 keeps, 11 vetoes. The rewordings did worse: English 13 stars,
48 keeps, 37 vetoes; German 12 stars, 72 keeps, 23 vetoes, nearly all
"not funny". The owner's notes are applied in `build_pools.py` (`EDIT`,
`FACT_EDIT`). With what was kept, at sarcasm On:

| | before | after the votes |
|---|---|---|
| English fact / flavour / whole screen, 7 days | 33% / 29% / 10% | 21% / 16% / 5% |
| English, 30 days | 50% / 79% / 28% | 38% / 67% / 17% |
| German, 7 days | 33% / 15% / 5% | 14% / 11% / 0% |
| German, 30 days | 50% / 75% / 23% | 31% / 56% / 7% |

English facts still repeat more because the steady facts, the commonest,
aren't rated yet.

## Topical rounds

Lines about a current event, with a date window, written with Claude
whenever something happens. The routine is the repo skill
`.claude/skills/topical`: the event and the gate, the window and region,
the round file (`<yyyy-mm>-topical-<slug>.json`, set T), then
`python3 tools/topical.py add <round>` after the vote. The first is
`2026-10-topical-clocks`: the clocks going back, 25 October in Europe and
1 November in the US.
