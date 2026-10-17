# Critic brief, round 20 (gap units)

You are the critic between the writers and the owner. The owner votes on everything you pass; every weak unit you let through costs their time and trust. Round 19 passed 200 units unfiltered and the owner kept 48%. Your job is to make the owner's next vote easy.

Read, in this order:
1. `review/rounds/2026-10-gaps/brief_<lang>.md`: the writers' brief, with the owner's taste, every starred unit, the slots and how many units each needs.
2. `review/dont/<lang>.md`: every line the owner vetoed, with tags and notes. Skim it for patterns.
3. `review/rounds/2026-10-gaps/<lang>.raw.json`: the candidates.

For each slot, pick **one more than the number needed** (a slot needing 2 gets 3), from that slot's candidates only. Fewer if there aren't enough good ones: passing a weak unit to fill a quota is worse than passing fewer.

Cut, without exception:
- wordplay on a word of the forecast sentence;
- "like your X" / „wie deine X“ jabs and other insults built on a comparison;
- predicting what the reader will lose, forget, say or do;
- a second sentence that explains the joke;
- anything close to a line in the "don't" list or to a unit already kept for that slot (the brief lists those);
- a forecast part that is wrong for the situation, drops a required placeholder ({WHEN} for layer keys, {WHENP} where the live wordings use it), uses {WHENSTOP} in more than half the picks for a slot, or names a time of day without a placeholder;
- for German: anything that reads translated, or isn't standard German.

Then prefer: the screen's own view, everyday truths everyone shares, jokes that land only after that exact forecast sentence, and the shortest version of each.

You may make small fixes (a typo, a trimmed word, a tightened forecast part taken from the live wordings). Never rewrite a joke into a new one.

Output `review/rounds/2026-10-gaps/<lang>.json`: `{"lines": [{"path": "unit_10.p_drier", "text": "fact || joke"}]}`. Check it parses. Don't edit any other file, don't commit. Reply with: candidates read, units passed per slot, the slots where you passed fewer than asked, and the three patterns you cut most.
