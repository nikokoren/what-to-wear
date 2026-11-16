# Critic, top-up round (round 25)

The writers wrote about three candidates for every line the owner gets to
vote on, in `review/rounds/2026-10-onfill/<lang>.<group>.raw.json`, from
the briefs `brief_<lang>_<group>.md` in the same folder.

Per slot keep **exactly the number in `cells.json`** (the fourth value:
enough to reach four live lines, plus two spares for the owner's cuts),
the strongest ones. A slot may keep its one `"wild": true` line if it is
among the strongest; it counts toward that number.

Cut by `docs/CRITIC.md`, every item, and by `docs/BRIEF.md`
"Tightening". Fix a plain typo or punctuation slip; otherwise copy lines
unchanged (path, text, wild, months).

Write `review/rounds/2026-10-onfill/<lang>.json` as `{"lines": [...]}`.
Check it parses and that every slot has exactly its number. Report the
totals. Don't edit other files, don't commit.
