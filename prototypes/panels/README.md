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
  "13 Uhr" (`panels.hours` in the language files).
- **Words:** one panel shows a "works all day" fact wording, plus the
  sarcastic line at On and 11. Two or three panels show only the
  sarcastic line, and nothing at Off.

On 7:00 readings in London, Vienna and New York over a year: one panel
21%, two 33%, three 46%.

## Views

Generated from one template in `build.py`. Panels sit in a row, sized to
the view; the half view lying wide puts the words beside them; portrait
half-tall and quarter stack them. `panel_shape` (a mock-only field)
crops the current square drawings to 2:3 to show what tall drawings
would do; the owner can redraw them tall.

## Open

- Whether the portrait quarter (240 by 400 on the OG) falls back to the
  now drawing alone.
- Square or tall drawings, and drawing all outfits with the same figure,
  pose and position so changes stand out.
- The settings screen: how to explain which switch changes what on the
  screen (forecast text, sarcasm, panels).
