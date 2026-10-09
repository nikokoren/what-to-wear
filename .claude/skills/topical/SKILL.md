---
name: topical
description: Write, vote on and publish topical flavour lines, jokes about a current event that show only inside a date window. Use when the owner says something happened and wants lines about it, asks for "/topical <event>", or asks to add, check or prune topical lines.
---

# Topical lines

Lines about current events that take the flavour slot (sarcasm On and
11 only) on about one day in three while their window is open. The
markup is TOPICAL LINES in `prototypes/fact-flavour/block.liquid`; the
plan and its reasons are in `docs/FUTURE-topical-lines.md`.

The owner writes with you, picks every line on the review page, and
nothing goes in without a vote.

## 0. What's on? (when the owner asks, and every Monday)

When the owner asks what's been happening, or the weekly scout runs:

```bash
python3 tools/topical_scout.py --days 8
```

It lists Wikipedia's Current events (culture, sport, science, business
only) and the latest headlines from The Onion and Der Postillon.

- **The satire is a radar, never a source.** Look for the real event
  underneath a headline; many are invented and have none. Never take
  their premise, punchline or wording, not even reworded: it's their
  work, and readers would recognise a Postillon joke on the wall.
- Put every candidate through the gate below and check it in real news
  (a web search, with the date) before proposing it.
- Add planned events in the next ten days you are sure of (clock changes,
  holidays, season starts, finals), checked the same way.
- Propose three to five, each in a few lines: what happened, with a
  source link; why it's good material; region and languages; a window;
  one angle per language in the house voices (an angle, not a finished
  line). If nothing passes, say so in one line. The owner picks; then
  carry on from step 2.

## 1. Pin down the event

- What happened, when, and where it matters. If the owner only names it,
  look it up so the facts and dates are right; don't joke from memory
  about something recent.
- **The gate, before writing anything.** In: sport, records, awards,
  product launches, space, the clocks changing, seasonal absurdities,
  pop culture. Out: death, illness, crime, war, disasters, politics and
  elections, anything with victims. If it's out, say so and stop.
- Regions: `US`, `UK`, `IE`, `DE`, `AT`, `CH`, `AU` (from the forecast's
  time zone). Leave the region off only for something everyone in that
  language knows. A Bundesliga joke is `DE`; a Super Bowl joke is `US`.
- The window: from the day it happens (or the day after the commit, since
  jsDelivr can take 12 hours) for about a week; never more than 21 days.
  Within it a line shows on the first day and then about one day in
  three.

## 2. Write

Read `docs/BRIEF.md` first: the voice (English, the screen on the wall;
German, the Grantler in standard German), and the rules that cost the
most vetoes: end on the joke, never restate the weather, no clothing
advice, no regional words the owner doesn't know.

- Four or five candidates per level (On, 11) per language the event
  matters to. 11 is about the reader.
- **German is its own material**, never a translation; a German angle
  on the same event, or a different German event.
- **It has to survive a week.** No "today", "last night" or "this
  morning": the line may show five days later.
- At most 65 characters.
- Optional `moods` (`hot`, `cold`, `wet`, `snow`, ...) for a line that
  only works in that weather, like a heat record on a hot day.

## 3. The round

`review/rounds/<yyyy-mm>-topical-<slug>.json`:

```json
{"round": "2026-10-topical-clocks", "edits": {},
 "lines": [{"lang": "en", "path": "topical_11.clocks_back", "text": "...",
            "batch": "T", "meaning": "Topical: ... Shows ... in ...",
            "windows": [{"from": "2026-10-25", "until": "2026-10-29", "region": "UK,IE"},
                        {"from": "2026-11-01", "until": "2026-11-05", "region": "US"}]}]}
```

One line can have several windows (the same joke a week later in the
US). `meaning` tells the owner on the review page what the event is and
when and where the line shows.

Build the page with this round plus any round still being voted on, and
publish it to the review page (the URL is in `docs/TODO.md`, item 3):

```bash
python3 tools/review_export.py --candidates review/rounds/<round>.json --only-candidates
```

## 4. After the vote

1. Sync the votes as usual (`review/README.md`, step 4).
2. Rewordings from the owner's notes go in the round's `"edits"`:
   `{"line as voted": "line as it should run"}`.
3. Add the keepers and prune the expired:

   ```bash
   python3 tools/topical.py add review/rounds/<round>.json
   python3 prototypes/fact-flavour/build.py
   python3 prototypes/fact-flavour/test_topical.py
   ```

   Until the redesign ships, lines go into the prototype's language
   files (the default). After it ships, pass `--lang-dir lang`.
4. Commit and push. Once shipped, a commit to `main` is live within
   about 12 hours; to make it immediate, purge jsDelivr's cache:
   `curl https://purge.jsdelivr.net/gh/nikokoren/what-to-wear@main/lang/en.json`
   (and `de.json`).

## Expired lines

They stop showing on their own. `tools/topical.py add` prunes them
whenever lines are added, and `.github/workflows/topical-prune.yml`
does it weekly, moving them to `review/topical-archive.json`. Their votes
stay in `review/decisions/`, so a used joke can't return by accident.
