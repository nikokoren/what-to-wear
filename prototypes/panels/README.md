# Outfit panels prototype

The visual forecast (docs/TODO.md, item 2) as the owner sketched it: the
day as **equal panels, left to right**. What to wear now, then at each
change: noon in the middle, the evening on the right. A day that doesn't
change keeps one panel and says so in words. Today only: nothing about
tomorrow is ever drawn.

```bash
python3 prototypes/panels/build.py     # build/panels/
```

`block.liquid` is appended to the shared markup after the fact + flavour
prototype's block, and reads what the scenario logic already worked out:
the hourly outfit ranks with their two-hour rule, the rain chances, and
the current outfit.

## The rules

- **A panel is a stretch of the day**, from one change to the next. A
  change is an outfit step held for two hours (the same rank lists the
  text uses), rain or snow starting (one hour at 50% or more: a shower
  counts) or two dry hours ending it. Changes count until `DAY_END_HOUR`
  (21:00).
- **Legs are decided at the door:** T-shirt with long pants and with
  shorts are one outfit later in the day.
- **At most three panels.** Changes less than two hours apart merge (the
  later outfit wins); outfit changes win over rain changes; a rain start
  that loses its own panel wets the panel it falls in; two neighbouring
  panels that would look the same become one.
- **Now** shows rain only while it falls (as the single picture does).
- **The time under each panel** is when it starts: "Now", then "1 pm" /
  "13 Uhr" (`panels.hours` in the language files), each with "from" /
  "ab" (`panels.from`): "Now · from 1 pm · from 7 pm". A panel is a
  stretch, so a bare "1 pm" would read as a moment. The hours have a
  no-break space; in the OG's portrait quarter (240 px wide) the time
  wraps to "from" over "1 pm".
- **Words:** one panel shows a "works all day" fact wording, plus the
  sarcastic line at On and 11. Two or three panels show only the
  sarcastic line, and nothing at Off.

On 7:00 readings in London, Vienna and New York over a year: one panel
21%, two 33%, three 46%.

## Views

Generated from one template in `build.py`. Panels sit in a row, sized to
the view, the time always under the drawing; the half view lying wide
puts the words beside them; only the half view standing tall (240 by
800 on the OG) stacks them, one under the other. The portrait quarter
keeps the row: stacked with the time under each, its drawings came out
smaller. The drawings stay square, as drawn (owner, after comparing
with a 2:3 crop). The times are larger on the X (`lg:label--xlarge`,
`lg:label--large` in the quarter).

The words don't use TRMNL's content limiter. On the X the screen is
scaled up with a CSS transform, and the limiter adds the drawings'
scaled height to the layout's unscaled one: with the panels above it,
it found 10 px left and hid the line. The words fit themselves instead
(they shrink in the column and clamp at three lines each). The live
views escape it only because there the sum goes negative, which turns
the limiter off.

## Open

- Drawing all outfits with the same figure, pose and position, so the
  change between panels is the clothes. The rainy coat is still a copy
  of the dry coat, without an umbrella.
- The settings screen: how to explain which switch changes what on the
  screen (forecast text, sarcasm, panels).
