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

Two on/off switches (owner's spec, October 2026; the whole form is
`config/settings.next.yaml`). It's called **What to Wear Next?** in the
form; it was Visual Forecast, a third value of the Forecast field, in the
first beta.

| Forecast | What to Wear Next? | Sarcasm Off | Sarcasm On / 11 |
|---|---|---|---|
| off | off | the outfit now | plus a line that stands alone |
| on | off | outfit, forecast line | plus the sarcastic line |
| off | on | the day's outfits; "works all day" when steady | plus a line that stands alone (the usual line under "works all day") |
| on | on | the day's outfits and the forecast line | plus the sarcastic line |

"A line that stands alone" is the mood's What to Wear Next pool
(`flavour_vf_10` / `_11`), since there's no forecast line for a line to
answer; a mood without one falls back to the usual line (docs/TODO.md
item 13).

Saved values don't move: Forecast keeps its key, and "Yes", "No", old
spellings, true/false and no value at all all read right (the shared
markup no longer puts a `default:` on it, which would turn false into
"yes"). The first beta's "visual" still gets the drawings without words.
Markup from before ignores What to Wear Next?, so the form can ship first.

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

Every screen, in every forecast mode (Visual Forecast, words, none),
comes from one template in `build.py`, **in TRMNL's framework classes
only**: no `<style>`, no inline style (`test_switch.py` checks). Sizes
are shares of the view: TRMNL's `layout` is a size container, so
`w--[40cqw]` and `h--max-[66cqh]` mean 40% of its width and 66% of its
height.

**One drawing** (a steady day, the words view, no forecast) is as big as
the view allows. Its box is a square as wide as the view
(`aspect--1/1 w--[100cqw]`) that gives up height to the words, since
images shrink in a flex column, down to 40% of the height. So the
drawing fills what the words leave, and stays right above them when the
width is what limits it (the portrait views). The owner found the
earlier one, fixed at 60% of the height as live, small next to the space
left on screen. On a steady day on the OG: full view 247 to 332 px,
half view standing tall 224 to 326, the quarter 146 to 173 (183 to 205
in portrait), the half view lying wide in portrait 183 to 248; lying
wide in landscape it already had the full height (173). Lying wide with words (the half view on its
side, the quarter), it stands beside them at the view's full height. Its
box (52% of the width) is wider than its column (36%) and overflows it
on both sides: the drawing's transparent sides don't push the words away.

**Two or three drawings** look as they did in the prototype, rebuilt in
classes:

- In a row, the time always under the drawing; the half view lying wide
  puts the words beside them; only the half view standing tall (240 by
  800 on the OG) stacks them, one under the other.
- **Neighbours overlap by a quarter.** Each panel is a column 3/4 as
  wide as its drawing, with the drawing centred in it and overflowing it
  on both sides (a flex column centres an item wider than itself). The
  drawings are transparent and the figure takes about 55% of the square
  (the two old wide-umbrella drawings up to 95%: their rain reaches into
  the neighbour's empty side), so the figure stays in its column and a
  row of three is 2.5 drawings wide instead of three plus gaps.
- A drawing's box is square and capped in height (`aspect--1/1` with
  `h--max-[…cqh]`): as big as the smaller of its share of the width and
  the cap, the time right under it.
- The drawings stay square, as drawn (owner, after comparing with a 2:3
  crop).
- The words are the live view's size, except in the two tightest spots
  on the OG (the portrait half-tall column and the quarter), a step
  smaller.
- **With the forecast line too** (both switches on), the forecast line
  and the sarcastic line are two to five lines, so the drawings get a
  lower cap and the words are a size smaller (`ih_fact`, `words_fact`
  in `build.py`; the half view lying wide gives the words half its
  width). On the OG in the full view: 205 px instead of 279.
- The times are larger on the X (`lg:label--xlarge`, `lg:label--large`
  in the quarter); "Now" is bold and underlined with the framework's own classes
  (`font--bold label--underline`: a dotted line on the OG, a thin grey
  one on the X; the OG's pixel font is already bold, so the bold barely
  shows there). A time wraps
  to "from" over "3 pm" when its column is too narrow.

The words don't use TRMNL's content limiter. On the X the screen is
scaled up with a CSS transform, and the limiter adds the drawings'
scaled height to the layout's unscaled one: with the drawings above it,
it found 10 px left and hid the line. The words take their natural
height instead, and the drawings make room.

`data-wtw="panels"` and `data-wtw="words"` mark the row of drawings and
the words for the tests; they style nothing.

Fit check (October 2026): every mock day in both languages, Visual
Forecast, words and no forecast, sarcasm Off, On and 11, OG and X,
landscape and portrait, every view, as rendered and again with the
longest fact and the longest sarcastic line swapped in (3,136 screens):
no words cut off or past the title bar, no figure cut or off the side,
no neighbouring figures overlapping, no times touching. Then, for the
two switches, both on (drawings, forecast line and sarcastic line) and
the outfit alone with a sarcastic line, at every sarcasm level (2,240
screens): clean once both-on got its own sizes. The times
touched in the portrait quarter until each got a small margin
(`mx--1`).

## Open

- Drawing all outfits with the same figure, pose and position, so the
  change between panels is the clothes. The rainy coat is still a copy
  of the dry coat, without an umbrella.
- `conditional_validation` (hiding sarcasm when the forecast is off,
  topical lines when sarcasm is off) is written from TRMNL's docs and
  untested: check it in the beta fork's form.
