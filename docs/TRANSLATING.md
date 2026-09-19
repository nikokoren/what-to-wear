# Adding a language

Everything the plugin says lives in `lang/<code>.json`. Adding a language is
one new file plus one line of config — no markup changes.

```bash
cp lang/en.json lang/fr.json     # then translate it
python3 tools/validate_lang.py   # catches most mistakes instantly
```

Translate the whole file. CI compares every string against `en.json` and
fails on any line still identical to the English, because a half-translated
file renders a mix of both languages on the device — the keys are all
present, so nothing else would catch it. If a string is genuinely identical
in your language, list its path in `meta.allow_same_as_en`.

Read [SCENARIOS.md](SCENARIOS.md) before you start — it says when each key
fires and what the drawing already shows, which is what keeps a line specific
rather than a vague paraphrase.

Open a PR. CI runs the validator and renders your file against every weather
scenario, so a missing key or a misplaced placeholder fails the build rather
than reaching someone's wall.

## What the file contains

| Key | What it is |
|---|---|
| `meta.code` | the two-letter code; must match the filename |
| `meta.name` | the language's name, written in that language |
| `ui` | the three error strings |
| `garments` | the five layers, in two grammatical cases |
| `buckets` | five times of day |
| `relative` | "in an hour", "in two hours", "in three hours" |
| `temp_0` / `temp_10` / `temp_11` | temperature lines, per sarcasm level |
| `precip_0` / `precip_10` / `precip_11` | precipitation lines, per level |

Each scenario key is documented in [SCENARIOS.md](SCENARIOS.md): when it
fires, what the drawing already shows, and what the sentence therefore has to
say. Read it before writing. The `arc_*` keys in particular are easy to get
subtly wrong, and getting them wrong sends someone out underdressed.

## The three voices

Users pick a sarcasm level. The three must feel genuinely different or the
setting is pointless — this is the most common way a translation comes out
flat. Measured across the English corpus:

| | words/line | addresses the reader | first person |
|---|---|---|---|
| `0` | 9.6 | 30% | 0% |
| `10` | 10.8 | 24% | 0% |
| `11` | 11.5 | 55% | 17% |

**Level 0 — plain.** Says the thing and stops. Shortest lines. Kid-safe, no
joke to get, nothing to decode. Someone reading it at 7am half-awake gets the
information and moves on.

> The jacket comes off {WHEN}. Have a bag or a free arm ready.

**Level 10 — dry.** Same information, wry about the *situation*. Note it
addresses the reader *less* than level 0: the joke is aimed at the weather,
the umbrella, the coat — not at the person. Understated, never mean.

> You will want the jacket off {WHEN}. Your arm is the hook.

**Level 11 — personal.** Turns on the reader. Longest lines, most direct
address, keeps score, assumes they will ignore the advice and says so. In
English it also has a narrator with opinions ("I am noting that you were
warned") — that device is one way to do it, not a requirement. The German
does not use first person at all and escalates instead through length and
direct address. Either works. What must be true is that 11 is *more* than
10, and aimed at the reader rather than the weather.

> The jacket becomes dead weight {WHEN}. Wear something underneath you can
> live with.

Same scenario at all three levels, which is the comparison worth making:

| | `precip_*.stays_wet` |
|---|---|
| `0` | It rains all day. The umbrella stays with you. |
| `10` | No dry spell. The umbrella is on a double today. |
| `11` | It rains all day. You and the umbrella are in this together. |

Across all three levels the *advice never changes*. Level 11 is not worse
advice delivered rudely — the reader still learns exactly when the rain
starts and what to take. Humour is never at the cost of the information.

Write level 0 first and get it right, then work up. The validator fails a
file whose levels are identical to each other, because a copy-paste across
levels silently removes a feature people paid attention to.

## Lines are interchangeable

Each scenario key holds an array. The plugin picks one by day, so every line
in an array must work in exactly the same situation. Don't write a sequence.
Six lines per key is the house standard; fewer is fine, one is the minimum.

## Placeholders

| Token | Becomes | Valid in |
|---|---|---|
| `{WHEN}` | a time, carrying its own preposition | temperature lines |
| `{WHEN2}` | the second time in a there-and-back day | `arc_*` keys only |
| `{WHENP}` | when the rain or snow starts | precipitation lines, standalone form only |
| `{GARMENT}` | a layer, sentence-initial | temperature lines |
| `{GARMENTA}` | the same layer, mid-sentence | temperature lines |

`{WHEN}` already includes its preposition, so never put one in front of it:
write *"take the umbrella, you will want it {WHENP}"*, not *"take the
umbrella for {WHENP}"* — the relative form ("in two hours") dies after a
preposition.

### You are translating sentences, not words

Every line is a complete sentence that you write from scratch in your own
language. Nothing is assembled from pieces. The only fragments in the file
are the eight time phrases (`buckets`, `relative`) and the five garment
names — and you choose where in your sentence those land.

`{GARMENT}` and `{GARMENTA}` are needed in **three keys only**: `arc_colder`,
`arc_level` and `arc_warmer`. Everywhere else the scenario key already fixes
which layer is meant — `w_jacket` can only ever be about the jacket — so
those lines just name it in ordinary prose. Do the same.

Even in the `arc_*` keys the token is optional. If your language needs more
than the two cases the file carries, or inflects adjectives to agree with the
garment's gender, write those lines without `{GARMENT}` at all: say "the
layer", or restructure so the garment is implied. Several English arc lines
already do exactly that. Nothing breaks — an absent token is simply not
substituted.

Watch for agreement if you do use the token: the five garments will not share
one gender in most languages, so any adjective agreeing with `{GARMENT}` will
be wrong for some of them.

### Every key needs one line that works without a time

Sometimes the forecast cannot name a time — both turning points land in the
same part of the day. The plugin then looks for a line in the array with no
`{WHEN...}` token in it. If every line needs one, the sentence renders with a
hole. The validator enforces this.

## The two precipitation forms

Each precipitation scenario appears twice:

- `wetter` — **standalone**, the whole tip. May use `{WHENP}`.
- `wetter_j` — **joined**, tacked onto a temperature sentence that already
  said when. Must not use `{WHENP}`, and should read as a continuation:
  *"Take the umbrella too, rain is coming."*

`drier` and `stays_wet` name no time in either form and never tell anyone to
take an umbrella — it is already raining, so the drawing already has one.

## House style

The picture shows the outfit. The words add only what a picture cannot: what
happens to that layer later, or what to put in the bag. Never name a
different garment to wear instead — it contradicts the drawing.

Keep lines short. They render at large type on a small e-ink screen, and long
sentences wrap badly on the OG device.

## Reserved characters

`||` and `;;` are delimiters in the transitional build and will fail
validation. Commas are fine in sentences but not in `garments`, `buckets` or
`relative`, which are comma-split in that same build.

## Getting it live

A new language file is reachable only once the `language` dropdown offers it.
That is a change to `config/settings.yaml`, which only the recipe owner can
publish — mention in your PR that it needs doing.
