# German prune (owner, November 2026)

The owner: go over all current German lines, especially in the full
categories, and cut the ones that could or should go. The German texts
are near TRMNL's size limit, so every weak line costs room a better one
could use.

You are the German proofreader. Read `docs/PROOFREAD_DE.md` (including
candidate mode), `docs/BRIEF.md` ("Tightening" and the levels),
`docs/CRITIC.md`, `review/rounds/2026-10-de-tight/changes.md` (the
owner's own edits: what they cut and why) and `review/examples/de.md`
(what the owner starred). Then read every line in
`prototypes/fact-flavour/lang/de.json` (skip `garments*` and
`topical_*`).

## Cut a line when

- it is clumsy, unnatural or translated-sounding German, or has a
  grammar or punctuation error that a fix can't save;
- it repeats the idea, joke or frame of another line in the same
  category (keep the better one), or of a line in a neighbouring
  category the same reader sees (the same situation at the other level,
  a unit's joke and the matching follow-up);
- it is weak: not sarcastic, merely pleasant, restates the weather, needs
  context the screen doesn't give, or explains itself;
- it breaks a rule in `docs/CRITIC.md` or "Tightening" (wrong level,
  fixed facts that vary, assumptions about the reader's life, dialect);
- in a forecast-sentence category (`facts.*`): it says the same as
  another wording with no gain, or is stiff next to the others.

## Limits

- Never take a category below 4 lines. Categories with 4 or fewer stay
  untouched. Start with the fullest categories; most cuts belong there.
- A unit (`units_*`, "Satz || Witz") is one line: cut it whole.
- Don't rewrite; this pass only cuts. If a line is good but has a small
  fixable error, list it under "fixes" instead (old → new), don't cut it.
- Starred lines (in `review/examples/de.md`) need a strong reason.

## Output

Write `review/rounds/2026-11-de-prune/cuts.json`:
`{"cuts": [{"where": "now_10.cold", "text": "<exact line, tags included>", "reason": "<short, in English>"}], "fixes": [{"where": "...", "old": "...", "new": "...", "reason": "..."}]}`.
Check it parses, that every `text` is an exact line from de.json at that
`where`, and that no category drops below 4. Report the number of cuts
per category and the main reasons. Don't edit other files, don't commit.
