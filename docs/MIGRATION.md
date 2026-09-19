# Rolling this out without breaking anyone

The refactor moves all phrasing out of the shared markup and into
`lang/<code>.json`, fetched as a second polling URL. That is two changes to
the plugin — new markup, new polling config — and TRMNL delivers them
through different mechanisms with no guarantee they land together.

**Do them in the order below.** Steps 1 and 2 are separated by a wait on
purpose.

## Why the order matters

Adding a second polling URL changes the shape of the whole payload, not just
the part you added. With one URL, the weather sits at the root: `current`,
`hourly`. With two, it moves under an index: `IDX_0.current`,
`IDX_0.hourly`, and the texts arrive as `IDX_1`.

So if the polling URL change reaches a device before the markup change, the
old markup looks for `current`, finds nothing, and every installed user gets
the 404 sprite and an error message. That is the failure mode this sequence
exists to prevent.

`src/shared.transitional.liquid` reads **both** shapes. Publishing it first
means there is no order in which the two updates can arrive that breaks
anything.

## Step 1 — publish the transitional markup

Paste `src/shared.transitional.liquid` into the shared markup box. Paste the
four files in `src/views/` into their matching view boxes.

Change nothing else. Do not touch the polling URL yet.

At this point every device renders exactly what it rendered before — the
phrasing still comes from copies embedded in the markup. The only new
behaviour is that the markup now *also* knows how to read the indexed shape,
which nothing is sending yet.

Verify in the editor with Force Refresh, then wait for the update to
propagate to installed users. Give it a day.

> The transitional file is 94 KB against TRMNL's 100 KB ceiling, because it
> carries the embedded phrasing *and* the new code path. It is generated —
> `python3 tools/build_transitional.py` — and CI fails if it is stale.

## Step 2 — add the texts polling URL

Set the Polling URL box to the two lines in `config/polling_urls.txt`.
Weather first, texts second.

Devices now receive `IDX_0` and `IDX_1`. The transitional markup notices
`IDX_0`, switches to it, and starts reading phrasing from `IDX_1` instead of
its embedded copies. The rendered output does not change: the JSON was
extracted from those same embedded copies and is verified byte-identical by
`tools/render_test.py`.

Before you move on, confirm on a real device that the tip still appears.
If `IDX_1` fails to arrive, the tip goes blank rather than wrong — the
sprite and the bottom bar still render.

## Step 3 — publish the slim markup

Paste `src/shared.liquid`. This is step 1's markup with the embedded copies
deleted: 33 KB instead of 100 KB.

From here, changing phrasing means editing a JSON file, and the markup is
only touched when the logic changes.

## Things worth checking on the way

**Does a polling URL change actually propagate to installed users?** TRMNL
documents that markup updates push to everyone who installed (rather than
forked) a recipe. It does not document the same for plugin *settings*. This
sequence is safe either way, but if settings do not propagate you will find
out at step 2: installed devices keep the root shape and keep using the
embedded copies, and you cannot do step 3 until that is resolved. Test it
with a second account before assuming.

**Screen refresh.** TRMNL skips generating a screen when merge variables are
unchanged. The texts payload is static, so it adds a constant to the hash
while the weather keeps changing — regeneration should behave as before.
There is a community report of change detection misbehaving on multi-URL
plugins, so watch that screens still update on day one of step 2.

**The language dropdown.** New languages need an option added to the
`language` field in `config/settings.yaml`, which is another settings change.
Until that option exists, a translation in the repo is unreachable.

## Who is affected by what

| | Installed the recipe | Forked the recipe |
|---|---|---|
| Gets the new markup | yes, automatically | no |
| Gets the new polling URL | see above | no |
| Keeps working during rollout | yes, by design | yes — nothing reaches them |
| Gets new languages later | yes | only by re-forking |

Forked users are untouched. A fork is a full copy taken at fork time, and
TRMNL's docs are explicit that forked recipes receive no updates from the
original author. They keep their embedded phrasing and keep rendering exactly
as they do today; they are frozen, not broken. That was your instinct in the
first place, and it is right.
