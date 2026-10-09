# Idea: topical lines that rotate weekly

Not built. Captured while the surrounding design was fresh, because most of
the machinery it needs already exists.

## Status, October 2026: built in the prototype

- **Markup:** TOPICAL LINES in `prototypes/fact-flavour/block.liquid`.
  A line shows inside its window, on the window's first day and then
  about one day in three, rotating with other active lines; other days
  keep the mood's line. Optional `region` (from the forecast's time zone:
  US, UK, IE, DE, AT, CH, AU) and `moods`. Seasonal theme days keep their
  own lines. Pinned by `prototypes/fact-flavour/test_topical.py`.
- **Opt-in:** the `topical_lines` form field
  (`prototypes/fact-flavour/settings-topical.yaml`). No value counts as
  off, so existing installs don't see it unasked.
- **Writing:** the routine is the repo skill `.claude/skills/topical`;
  rounds go on the review page as `topical_<level>.<event>` rows.
- **In and out:** `tools/topical.py add` puts the keepers in and
  `prune` takes expired lines out (also weekly, by
  `.github/workflows/topical-prune.yml`), archiving them in
  `review/topical-archive.json`. CI checks the format.
- **Finding events:** `tools/topical_scout.py` lists Wikipedia's Current
  events (culture, sport, science, business) and the Onion and
  Postillon headlines, as a radar only, never as a source of jokes. A
  weekly routine, "Topical scout" (Mondays 07:47 Vienna time, in the
  owner's claude.ai routines), runs it in a fresh session and sends the
  owner a shortlist of three to five events that pass the gate; replying
  in that session starts the writing.
- **Size:** about 140 bytes a line; pruned, a dozen live lines.
- **First event:** the clocks going back (`2026-10-topical-clocks`),
  waiting for votes.

## Update, October 2026: the owner's version

The text redesign (fact line plus flavour line, `prototypes/fact-flavour/`)
changes where these lines go and makes most of the original plan below
unnecessary. What the owner wants:

- **Written with Claude as a sparring partner, whenever something
  happens.** Not an automated news job: the owner opens a session,
  brainstorms On and 11 lines about the event, votes on them on the
  review page, and the keepers go in. A person writes and picks every
  line, so the disaster-joke risk described below mostly goes away
  (the topic allowlist is still a good habit).
- **Rotated in and out automatically.** Each topical line carries a
  date window, and the markup shows it only inside that window:

  ```json
  "topical_10": [
    {"text": "...", "from": "2026-11-03", "until": "2026-11-10", "region": "US"}
  ]
  ```

  Expired lines simply stop showing; nothing has to be republished to
  take them out. Adding one is a commit to `lang/<code>.json`, live
  within jsDelivr's ~12 hours.
- **Where they show:** in the flavour line, levels 10 and 11 only, which
  never carries a fact, so a topical line can never displace advice.
  Inside its window it competes with the mood's pool rather than
  replacing it (say one day in three), so a week of one joke doesn't
  wear thin.
- **No third polling URL.** A dozen dated lines fit in the language file
  that is already fetched. `region` (optional) uses the coordinate-based
  region idea below; lines without one show everywhere in the language.
- Still optional per device, off by default for existing installs.

Needs: the date-window filter in the markup (the date is already known,
`today_year`/`today_md`), a `topical` round type in `tools/review_export.py`,
and a short how-to so a future session knows the routine.

The original plan, for reference:

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
