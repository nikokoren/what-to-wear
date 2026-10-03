// What to Wear - texts Worker.
//
// Serves lang/<code>.json exactly as jsDelivr does, and counts which
// settings polls arrive with, so it is possible to tell whether people
// read the forecast tips at all and at which sarcasm level.
//
// Recorded per poll, and nothing else:
//   blob1  language        en, de, ... ('other' if malformed)
//   blob2  forecast        on | off | unknown
//   blob3  sarcasm         0 | 10 | 11 | unknown
//   double1 weight         1, or N when 1 poll in N is sampled
//
// No coordinates, no location name, no IP, no device or account id ever
// reach this Worker: the polling URL only carries the three settings.
// Recording can never break a poll: it is synchronous, wrapped, and
// skipped entirely when the STATS binding is missing.

const UPSTREAM = 'https://cdn.jsdelivr.net/gh/nikokoren/what-to-wear@';
const LANG_PATH = /^\/lang\/([a-z]{2,3}(?:-[a-z]{2})?)\.json$/i;

// Mirrors the markup (src/shared.liquid, SETTINGS): an empty field falls
// back to the default, 'no' / 'false' / '0' turn the tips off, anything
// else leaves them on. A parameter that is absent altogether means the
// device is still on a polling URL that does not send it.
export function normaliseForecast(params) {
  if (!params.has('f')) return 'unknown';
  const v = (params.get('f') || '').trim().toLowerCase();
  if (v === 'no' || v === 'false' || v === '0') return 'off';
  return 'on';
}

// Mirrors the markup: empty is the default of 10, only 10 and 11 are
// honoured, every other value renders as 0.
export function normaliseSarcasm(params) {
  if (!params.has('s')) return 'unknown';
  const v = (params.get('s') || '').trim();
  if (v === '') return '10';
  if (v === '10' || v === '11') return v;
  return '0';
}

export function recordPoll(env, settings, random = Math.random) {
  try {
    const stats = env && env.STATS;
    if (!stats || typeof stats.writeDataPoint !== 'function') return false;
    const n = Math.max(1, parseInt(env.STATS_SAMPLE || '1', 10) || 1);
    if (n > 1 && random() >= 1 / n) return false;
    stats.writeDataPoint({
      blobs: [settings.lang, settings.forecast, settings.sarcasm],
      doubles: [n],
      indexes: [settings.forecast],
    });
    return true;
  } catch (_) {
    // A failing analytics write must never cost anyone their tip.
    return false;
  }
}

export default {
  async fetch(request, env) {
    if (request.method !== 'GET' && request.method !== 'HEAD') {
      return new Response('Method not allowed', { status: 405 });
    }
    const url = new URL(request.url);
    const m = url.pathname.match(LANG_PATH);
    if (!m) return new Response('Not found', { status: 404 });

    const lang = m[1].toLowerCase();
    recordPoll(env, {
      lang,
      forecast: normaliseForecast(url.searchParams),
      sarcasm: normaliseSarcasm(url.searchParams),
    });

    const ref = (env && env.LANG_REF) || 'main';
    const upstream = await fetch(`${UPSTREAM}${ref}/lang/${lang}.json`, {
      cf: { cacheTtl: 3600, cacheEverything: true },
    });
    // Pass the upstream status through: a 404 for an unknown language is
    // what the markup already handles (no tip, picture still drawn).
    return new Response(request.method === 'HEAD' ? null : upstream.body, {
      status: upstream.status,
      headers: {
        'content-type': 'application/json; charset=utf-8',
        'cache-control': 'public, max-age=3600',
      },
    });
  },
};
