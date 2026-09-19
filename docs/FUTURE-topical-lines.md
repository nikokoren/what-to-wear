# Idea: topical lines that rotate weekly

Not built. Captured while the surrounding design was fresh, because most of
the machinery it needs already exists.

The idea: a weekly job reads the news, writes a handful of jokes about it in
each language, and those rotate into the tip for a week or two before being
replaced. Carrot Weather does something like this and it is a large part of
why it feels alive rather than generated.

## Why this is cheaper than it sounds

The plugin already fetches its phrasing from a URL at render time. Topical
lines are the same mechanism pointed at a file that changes weekly:

```
line 1  api.open-meteo.com/...                     weather
line 2  cdn.jsdelivr.net/.../lang/en.json          the permanent corpus
line 3  cdn.jsdelivr.net/.../topical/en-US.json    this week's jokes
```

A third polling URL arrives as `IDX_2`. The markup reads it if present and
ignores it if absent, exactly as it already does for `IDX_1`. Nothing about
the rollout or the fallback behaviour changes.

## Where the lines should attach

The same rule the seasonal themes use: **a topical line may only ever
replace `perfect`.** It never displaces a sentence that tells someone to
take a coat.

That is not a limitation, it is the whole reason this works. `perfect` is
about half of all renders and is the key with the least to say, so it is
precisely the slot where a joke costs nothing. Plumbing already exists —
`perfect` is refined to a variant in `shared.liquid` and falls back when a
key is missing, so a topical key slots in beside `theme_*` with no new
mechanism.

Levels 10 and 11 only. Level 0 is kid-safe and news-free by definition.

## Regional targeting

Language is not region. A German file serves Germany and Austria; an English
one serves the US, the UK, Ireland, Australia. A joke about a Bundesliga
result lands in Munich and baffles Vienna.

The plugin already knows the answer: it has `lat_lon` from the form. A
region can be derived from coordinates without asking the user anything, and
interpolated into the URL the way `language` already is:

```
topical/##{{ language }}-##{{ region }}.json
```

Start with `en-US`, `en-GB`, `de-DE`, `de-AT`. Fall back to the plain
language file when a region has no topical file that week, so a new region
costs nothing until someone writes for it.

## The part that needs care

**Automated jokes about the news will eventually make one about a
disaster.** That is not a risk to manage with a better prompt; it is a
certainty over a long enough run. A generated line about a plane crash,
an election, a death or a war, rendered on a wall in someone's kitchen,
under this plugin's name, is a bad week for the author.

So: a human gate before anything publishes. The weekly job opens a pull
request; merging it is the publish. That also means the whole thing runs on
machinery this repo already has — CI validates the file exactly as it
validates a translation, and nothing reaches a device without someone
pressing merge.

Beyond that, a topic allowlist is worth more than a blocklist. Sport,
weather records, awards, product launches, space, seasonal absurdities.
Anything involving death, politics, crime, conflict or illness is out, and
"is this in the allowlist" is a far easier judgement for a model to make
reliably than "is this in bad taste".

## Other things to think about before starting

- **Staleness.** jsDelivr caches ~12h and TRMNL renders on its own schedule,
  so a line can appear two days after the event it refers to. Write jokes
  that survive a week, not ones pinned to a moment.
- **Change detection.** TRMNL skips regenerating a screen when merge
  variables are unchanged. A weekly-changing file is fine, but it is one
  more thing in the payload to watch on the first run.
- **Payload size.** Keep it small, a dozen lines per region. It rides along
  on every poll.
- **Rotation.** The existing `local_days | modulo` rotation works unchanged.
  Freshness comes from the file changing, not from the picker.
- **It has to be optional.** Some people want a weather plugin, not a
  comedian. A form field to turn topical lines off, defaulting to off for
  existing installs, since they did not sign up for it.

## Why not do it now

It needs the human gate, a region mapping, a third polling URL, and a
publishing workflow — each small, but together a separate piece of work
from getting the permanent corpus right. And the permanent corpus is what
renders on the other ~50 weeks' worth of days where nothing topical fits.
