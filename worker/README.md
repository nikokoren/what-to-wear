# Texts Worker

Serves `lang/<code>.json` exactly as jsDelivr does, and counts two
settings per poll so it is possible to judge where the effort should go:

- **are the forecast tips turned on at all**, and
- **at which sarcasm level**.

Language is recorded too, since it is already in the URL.

Nothing else is recorded. The polling URL only carries those settings: no
coordinates, no location name, no IP, no device or account id. The
weather URL keeps going straight to Open-Meteo, so location never passes
through here.

Recording never blocks or breaks a poll: the write is synchronous,
wrapped, and skipped when the binding is missing. If the texts cannot be
fetched the Worker passes the error through, and the markup degrades the
way it always has (picture, no tip).

## Deploy

1. Cloudflare dashboard → Workers & Pages → Analytics Engine → **Enable**
   (once per account; without it the deploy fails with code 10089).
2. From this folder: `npx wrangler deploy`.
3. In TRMNL, replace the second polling URL (the jsDelivr one) with:

   ```
   https://what-to-wear.<your-subdomain>.workers.dev/lang/##{{ language | default: 'en' }}.json?f=##{{ show_future_suggestions }}&s=##{{ sarcasm_level }}
   ```

   The first line, Open-Meteo, stays as it is. Order still matters: weather
   is `IDX_0`, texts `IDX_1`.

4. Force Refresh once and check the tip still renders.

`LANG_REF` in `wrangler.toml` picks the jsDelivr ref the texts come from;
`main` by default, a commit SHA to pin. `STATS_SAMPLE=N` records one poll
in N, weighted by N, if the free plan's 100,000 data points a day ever
get tight (about 1,000 devices at one poll per 15 minutes).

## What is stored

| column | value |
|---|---|
| `blob1` | language: `en`, `de`, ... |
| `blob2` | forecast tips: `on`, `off`, or `unknown` (a device still on the old URL) |
| `blob3` | sarcasm: `0`, `10`, `11`, or `unknown` |
| `double1` | weight: 1, or N when sampled |

Values are normalised the way `src/shared.liquid` reads them, so the
counts match what devices actually show (an unset field counts as its
default, an unrecognised sarcasm value as 0).

## Reading it

Cloudflare dashboard → Analytics Engine → SQL, or the SQL API. Multiply by
`_sample_interval` as well: Analytics Engine samples on its own at high
volume.

Are the tips on at all?

```sql
SELECT blob2 AS forecast, SUM(_sample_interval * double1) AS polls
FROM what_to_wear_polls
WHERE timestamp > NOW() - INTERVAL '7' DAY
GROUP BY forecast
```

Of those with tips on, which sarcasm level?

```sql
SELECT blob3 AS sarcasm, SUM(_sample_interval * double1) AS polls
FROM what_to_wear_polls
WHERE timestamp > NOW() - INTERVAL '7' DAY AND blob2 = 'on'
GROUP BY sarcasm
```

These count polls, not people. Devices poll at roughly the same rate, so
the shares are meaningful; absolute numbers less so. Data is kept for
3 months.

## Tests

```bash
node --test test/*.test.mjs
```
