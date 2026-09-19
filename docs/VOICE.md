# The three voices

This is the spec every line is written against. It is prescriptive on
purpose: the previous corpus drifted into template-filling because nothing
said what the levels were *for*.

## The architecture

The levels do not differ by how many jokes they contain. They differ by
**what the sentence is about**.

| | Subject of the sentence | Stance |
|---|---|---|
| **0** | your day, and what you do about it | helpful, no persona |
| **10** | the *things* — the jacket, the umbrella, the rain | deadpan observer of objects |
| **11** | **you** — your habits, your optimism, your history | it has your number and says so |

That is the test for every line. Ask: *who or what is this sentence about?*
If a level-10 line is about the reader, it belongs at 11. If a level-11 line
is about the weather, it belongs at 10.

This also settles a thing the old corpus got backwards: **level 10 should
address the reader less than level 0 does.** Level 0 talks to you because it
is helping you. Level 10 is looking at the objects. Level 11 comes back to
you, hard.

## The one rule that outranks everything

**The fact is the joke's setup, not its neighbour.**

Never write a fact sentence and then bolt a joke sentence onto it. Write one
sentence that carries both, or make the second sentence raise the stakes
rather than decorate.

Test: delete the humour. Is the advice still there? If the joke *carried* the
fact, yes — that line is good. If the fact fell out with it, rewrite.

> ✗ `It rains all day. The umbrella is having a moment.`
> ✓ `The rain has cleared its schedule. Nothing else is happening today.`

The second one tells you it rains all day *by means of* the joke.

A reader at any level must be able to act on the line alone. Level 11 is not
worse advice delivered rudely — it is the same advice, aimed at someone the
narrator expects to ignore it.

## Level 0 — plain

A calm adult telling a child what to bring. Says the thing and stops.

- 6–14 words. One or two short clauses.
- Present tense. Imperatives are good: *Take a jacket.*
- Concrete nouns. No irony, no rhetorical questions, no personification.
- Nothing to decode. A child reads it literally and is correct.
- Never negative about the weather or the reader.

> `Take a jacket. You'll want it {WHEN}.`
> `The jacket comes off {WHEN}. Keep a hand free for it.`
> `Rain all day today. There's no dry gap.`

## Level 10 — deadpan, aimed at the objects

The jacket has a shift. The umbrella has a job. The rain has a schedule. Give
the things agency and let the comedy come from understatement.

- 8–16 words.
- The reader appears rarely and is never the target.
- Workplace and logistics metaphors work well: clocking off, overtime, a
  double shift, luggage, dead weight, handing over.
- Dry, never zany. No exclamation marks. No puns.
- The weather is the antagonist, not the person.

> `The jacket clocks off {WHEN}. After that it rides on your arm.`
> `The hoodie runs out of arguments {WHEN}. The jacket takes over.`
> `The rain has cleared its schedule. Nothing else is happening today.`

## Level 11 — savage, aimed at you

It has watched you make this mistake before. It expects you to make it again.
It tells you anyway.

- 10–18 words.
- The subject is the reader: their habits, their optimism, their plan.
- It predicts behaviour and is usually right: *yours stays on the hook, and
  you'll call that a decision.*
- Savage about **choices**, never about the person. Attack the plan, the
  optimism, the hoodie. Never appearance, intelligence, or worth.
- No slurs, no cruelty about bodies, nothing that would land badly on a wall
  in someone's kitchen every morning for a year.
- The information survives intact. That is what makes it funny rather than
  just rude.

> `Jacket weather {WHEN}. Yours stays on the hook, and you'll call that a decision.`
> `It rains all day. Your plan, whatever it was, is already wet.`
> `You'll carry that coat for hours because you dressed for a day that ends at noon.`

## Writing English

**`lang/en.json` is US English.** The US is about half of all devices and
**79% of the English-speaking ones** — see [AUDIENCE.md](AUDIENCE.md). That
is not close enough to hedge. British idiom is not a neutral default here,
and some of it is actively wrong across the Atlantic:

| Write | Not | Because |
|---|---|---|
| around your waist | round your waist | |
| sidewalk | pavement | in the US, *pavement* is the road surface, so "the pavement stops cooperating" reads as the road |
| sweater | jumper | a US jumper is a pinafore dress |
| tank top | vest | a US vest is a waistcoat |
| pants | trousers | |
| fall | autumn | both work, *fall* is more natural |
| a real / a proper *(sparingly)* | proper cold | *properly cold* is fine; *proper cold* as an intensifier reads British |

A British variant belongs in `en-GB.json` as its own file. The UK, Australia
and Canada together are ~13% of devices, so it is the highest-value
translation anyone could submit, and the easiest — a diff, not a rewrite.
Don't hedge `en.json` toward mid-Atlantic; that pleases nobody.

**Never state a temperature number.** The plugin has no idea whether its
reader thinks in Celsius or Fahrenheit, and it never needs to: the drawing
shows the outfit and the words describe the change. Say "cold enough for a
jacket", never "down to 9 degrees". The corpus currently has zero numbers in
it and should stay that way.

**Use contractions.** The old corpus had two in 499 lines and read like a
manual. *doesn't, won't, you'll, there's, it's.* This is the single biggest
difference between stiff and spoken.

Banned openers, because the old corpus wore them out: `It gets…`, `It
turns…`, `You will…`. Find a verb with something in it.

Vary the sentence shape. Not every line is `[statement]. [instruction].`

## Writing German

German is **written from the meaning, not from the English line.** Do not
open the English file. Work from the scenario description and write what a
German speaker would actually say standing at their front door.

Hard rules, each one fixing a measured flaw in the old corpus:

1. **Present tense for the near future.** *Morgen regnet es*, not *Morgen
   wird es regnen*. The old corpus used `wird`/`wirst` in 33% of lines and it
   is the main reason it read translated.
2. **Use modal particles.** *ja, halt, eben, schon, wohl, doch, mal.* These
   are the native German device for dry understatement and the old corpus had
   none at all. `Deine hängt zu Hause, und da bleibt sie wohl auch.`
3. **No Amtsdeutsch.** Banned: *Im Tagesverlauf*, *ist nicht in Sicht*, *Eine
   Wetteränderung*. That is the register of a parking notice.
4. **Banned opener: `Es wird {WHEN}…`** It opened 59 of 485 old lines.
5. **Compound nouns are a comic resource.** *Handgepäck, Ballast,
   Feierabend, Dauereinsatz.* Use them; they are funnier in German than any
   translation of them.
6. **Konjunktiv II carries knowingness** at level 11. *Du könntest ihn
   mitnehmen.*
7. **Du throughout**, never Sie.
9. **Germany, Switzerland, Austria — in that order.** Switzerland is roughly
   twice Austria by device count. Standard German serves all three; just
   avoid phrasing that works in only one of them when a neutral one exists.
8. Colloquial contractions are fine and good: *wird's, gibt's, hab's.*

> 0 `Nimm eine Jacke mit. {WHEN} brauchst du sie.`
> 10 `Dem Hoodie gehen {WHEN} die Argumente aus. Die Jacke übernimmt.`
> 11 `{WHEN} Jackenwetter. Deine hängt zu Hause, und das nennst du dann eine Entscheidung.`

## Depth follows frequency, not fairness

Every key used to have six lines. Replaying the plugin's own logic over a
year of real weather, and over a summer across nine cities weighted to the
audience, says that was exactly wrong:

| key | share of renders | lines |
|---|---|---|
| `perfect` and its variants | ~50% | as many as you can write |
| `c_relief` | 26% in summer, 32% in US cities | deep |
| `w_coat` `w_jacket` | ~8% and ~6% in winter | deep |
| `w_water` `c_sweatshirt` `w_sweatshirt` | 6-8% | medium |
| `arc_colder` `c_hoodie` | 0.1% | six is plenty |

A line in `perfect` shows roughly 80 times a year at six alternatives. A line
in `arc_colder` shows once. Write where the traffic is.

## Variety

Within a level, no more than **two** lines may open with the same two words.
The five `c_*` keys especially must not share a frame — in the old corpus
they were one sentence with the noun swapped, five times, and it showed.

Within a key, the six lines are interchangeable: each must work on any day
the scenario fires. They are alternatives, not a sequence.

## The hard constraints

These are not style, they are correctness. `tools/validate_lang.py` enforces
them.

- Placeholders: `{WHEN}` `{WHEN2}` `{WHENP}` `{GARMENT}` `{GARMENTA}`.
  Nothing else, spelled exactly.
- `{WHEN}` and `{WHENP}` already carry their preposition. Never put one in
  front: ✗ `for {WHENP}`.
- `{WHEN2}` only in `arc_colder`, `arc_level`, `arc_warmer`.
- `{WHENP}` only in precipitation lines, and never in a `_j` fragment.
- `{GARMENT}` / `{GARMENTA}` only in the three `arc_*` keys. Elsewhere name
  the garment in prose — see SCENARIOS.md for why.
- Never `{GARMENT}` in `w_water` or `c_relief`; there is no layer, so it
  renders empty.
- **Every key that uses `{WHEN}` needs at least one line with no time token
  at all**, for the days the forecast cannot name a time.
- No `||` or `;;` anywhere. No commas inside `garments`, `buckets`,
  `relative`.
- Keep lines short enough to read at large type on a small e-ink screen.
  Over ~18 words wraps badly on the OG device.

See [SCENARIOS.md](SCENARIOS.md) for what each key means and
[TRANSLATING.md](TRANSLATING.md) for the file format.
