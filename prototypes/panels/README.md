# Outfit panels prototype

The visual forecast (docs/TODO.md, item 2) as the owner sketched it: the
day as **equal panels, left to right**. What to wear now, then at each
change: noon in the middle, the evening on the right. A day that doesn't
change keeps one panel and says so in words. Today only: nothing about
tomorrow is ever drawn.

It is called **Visual Forecast** in the form.

```bash
python3 prototypes/panels/build.py         # build/panels/
python3 prototypes/panels/test_switch.py   # the forecast field's three values
```

`block.liquid` is appended to the shared markup after the fact + flavour
prototype's block, and reads what the scenario logic already worked out:
the hourly outfit ranks with their two-hour rule, the rain chances, and
the current outfit.

## The switch

One field, not a new one: the forecast field (`show_future_suggestions`)
gets a third value next to "Yes" and "No", `visual`, labelled "Visual
Forecast (new)". Words and pictures are two ways of showing the same
forecast, so they can't both be on, and a separate on/off would have
made "forecast off, Visual Forecast on" a setting that means nothing.
The whole form is `config/settings.next.yaml`.

| Forecast | Sarcasm Off | Sarcasm On / 11 |
|---|---|---|
| Off ("No") | the outfit now | (sarcasm hidden in the form) |
| In words ("Yes") | outfit, fact line | plus the sarcastic line |
| Visual Forecast ("visual") | the day's outfits; "works all day" when steady | plus the sarcastic line |

Saved values don't move: "Yes", "No", old spellings and no value at all
keep the words, and markup from before reads "visual" as on, so the
form can ship before the markup. Each view is `{% if visual_forecast %}`
the panels `{% else %}` the fact + flavour view.

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
  sarcastic line, and nothing at Off. With no fact line above it, that
  line comes from the mood's Visual Forecast pool (`flavour_vf_10` /
  `_11`, built from review round 10): lines that work without the fact,
  and lines written for the drawings. No pool, the usual line.

On 7:00 readings in London, Vienna and New York over a year: one panel
21%, two 33%, three 46%.

## Views

**One panel is the text view** people know, at the live sizes (the
drawing at 60% of the view's height, the words in the live view's size),
with the "works all day" fact and the sarcastic line. The first beta
drew it through the panels template, a little smaller than live and with
smaller words; the owner found it "tiny".

**Two or three panels** come from one template in `build.py`:

- In a row, the time always under the drawing; the half view lying wide
  puts the words beside them; only the half view standing tall (240 by
  800 on the OG) stacks them, one under the other.
- **Neighbours overlap by a quarter.** The drawings are transparent and
  the figure takes about 55% of the square (the two old wide-umbrella
  drawings up to 95%: their rain reaches into the neighbour's empty
  side), so a row of three is 2.5 drawings wide instead of three plus
  gaps. With more height for the row too, on the OG in landscape: full
  view 218 to 279 px, half view lying wide 131 to 149 px, quarter about
  the same (96 px with words, 131 without).
- The drawings stay square, as drawn (owner, after comparing with a 2:3
  crop).
- The words are the live view's size, except in the two tightest spots
  on the OG (the portrait half-tall column and the quarter), a step
  smaller, since the panels can't use TRMNL's limiter to step down.
- The times are larger on the X (`lg:label--xlarge`, `lg:label--large`
  in the quarter). A time gets its share of the row and wraps to "from"
  over "3 pm" when it needs more.

The words don't use TRMNL's content limiter. On the X the screen is
scaled up with a CSS transform, and the limiter adds the drawings'
scaled height to the layout's unscaled one: with the panels above it,
it found 10 px left and hid the line. The words fit themselves instead
(they shrink in the column and clamp at four lines each). The live
views escape it only because there the sum goes negative, which turns
the limiter off.

Every mock day was checked in every language, sarcasm level, device,
orientation and view (448 screens) for words cut off, times touching
and anything spilling out of the view: none.

## Open

- Drawing all outfits with the same figure, pose and position, so the
  change between panels is the clothes. The rainy coat is still a copy
  of the dry coat, without an umbrella.
- `conditional_validation` (hiding sarcasm when the forecast is off,
  topical lines when sarcasm is off) is written from TRMNL's docs and
  untested: check it in the beta fork's form.
