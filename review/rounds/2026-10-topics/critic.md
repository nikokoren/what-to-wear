# Critic brief, round 21 (fresh topics)

You are the critic between the writers and the owner. The owner votes on everything you pass; every weak unit you let through costs their time and trust. Round 19 passed 200 units unfiltered and the owner kept 48%. Your job is to make the owner's next vote easy.

Read, in this order:
1. `review/rounds/2026-10-topics/brief_<lang>.md`: the writers' brief, with the owner's taste, recent starred lines, the topics and the unit keys.
2. `review/dont/<lang>.md`: every line the owner vetoed, with tags and notes. Skim it for patterns.
3. `review/rounds/2026-10-topics/<lang>.raw.json`: the candidates.

For each topic, pass **at most 3** of its candidates (Eisheilige: at most 4), and fewer when they aren't good: passing a weak line to fill a quota is worse than passing fewer. Round 20's critic passed lines the owner then vetoed as "where's the sarcasm?" and "what is that supposed to mean?": cut gentle observations without bite, and anything that doesn't make sense on first read. Keep each line's "topic" and "months".

Cut, without exception:
- wordplay on a word of the forecast sentence;
- "like your X" / „wie deine X“ jabs and other insults built on a comparison;
- predicting what the reader will lose, forget, say or do;
- a second sentence that explains the joke;
- anything close to a line in the "don't" list, or to a line already live in `prototypes/fact-flavour/lang/<lang>.json`;
- a forecast part that is wrong for the situation, drops a required placeholder ({WHEN} for layer keys, {WHENP} where the live wordings use it), or names a time of day without a placeholder;
- for German: anything that reads translated, or isn't standard German.

Then prefer: the screen's own view, everyday truths everyone shares, jokes that land only after that exact forecast sentence, and the shortest version of each.

You may make small fixes (a typo, a trimmed word, a tightened forecast part taken from the live wordings). Never rewrite a joke into a new one.

Output `review/rounds/2026-10-topics/<lang>.json`: `{"lines": [{"path": "unit_10.p_drier", "text": "fact || joke"}]}`. Check it parses. Don't edit any other file, don't commit. Reply with: candidates read, lines passed per topic, the topics where you passed fewer than three, and the three patterns you cut most.
