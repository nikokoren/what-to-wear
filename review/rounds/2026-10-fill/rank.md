# Trim the fill-up round (owner: too many lines)

`<lang>.rank_in.json` lists every slot with its candidates (the critic's
picks), how many lines are live there now, and `keep`: how many to keep
(enough to reach four live lines, plus two spares for the owner's cuts).

For each slot keep exactly `keep` lines, the strongest ones by the
critic's standards (`critic.md`, `docs/BRIEF.md`, the owner's stars in
`review/examples/<lang>.md`, vetoes in `review/dont/<lang>.md`). If the
slot has a `"wild": true` line and `keep` is 2 or more, one of the kept
lines is the best wild one; otherwise the wild line goes. Prefer lines
that are clear on first read, bite, and survive daily repetition; drop
the weakest and any two that share an idea.

Write `review/rounds/2026-10-fill/<lang>.json` as
`{"lines": [...]}` with the kept items copied unchanged (path, text,
wild, months). Check it parses and that every slot has exactly `keep`
lines. Report the total. Don't edit other files, don't commit.
