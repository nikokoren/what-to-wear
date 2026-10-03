// node --test worker/test
import test from 'node:test';
import assert from 'node:assert/strict';
import worker, { recordPoll, normaliseForecast, normaliseSarcasm } from '../src/index.js';

function fakeStats() {
  const points = [];
  return { points, writeDataPoint: (p) => points.push(p) };
}

function stubUpstream(status = 200, body = '{"meta":{"code":"en"}}') {
  const calls = [];
  globalThis.fetch = async (url) => {
    calls.push(url);
    return new Response(body, { status });
  };
  return calls;
}

const poll = (path, env) => worker.fetch(new Request(`https://w.example${path}`), env);

test('forecast and sarcasm normalise the way the markup reads them', () => {
  const p = (q) => new URLSearchParams(q);
  assert.equal(normaliseForecast(p('f=Yes')), 'on');
  assert.equal(normaliseForecast(p('f=')), 'on');       // unset field, markup default
  assert.equal(normaliseForecast(p('f=No')), 'off');
  assert.equal(normaliseForecast(p('f=false')), 'off');
  assert.equal(normaliseForecast(p('')), 'unknown');    // old polling URL
  assert.equal(normaliseSarcasm(p('s=0')), '0');
  assert.equal(normaliseSarcasm(p('s=10')), '10');
  assert.equal(normaliseSarcasm(p('s=11')), '11');
  assert.equal(normaliseSarcasm(p('s=')), '10');        // unset field, markup default
  assert.equal(normaliseSarcasm(p('s=7')), '0');        // anything else renders as 0
  assert.equal(normaliseSarcasm(p('')), 'unknown');
});

test('a poll records language, forecast and sarcasm, and nothing else', async () => {
  stubUpstream();
  const stats = fakeStats();
  const res = await poll('/lang/de.json?f=yes&s=11&lat=48.2&lon=16.4&label=Home', { STATS: stats });
  assert.equal(res.status, 200);
  assert.deepEqual(stats.points, [{ blobs: ['de', 'on', '11'], doubles: [1], indexes: ['on'] }]);
  const recorded = JSON.stringify(stats.points);
  for (const leak of ['48.2', '16.4', 'Home']) assert.ok(!recorded.includes(leak), leak);
});

test('the texts file is passed through from the pinned jsDelivr ref', async () => {
  const calls = stubUpstream(200, '{"meta":{"code":"de"}}');
  const res = await poll('/lang/de.json?f=yes&s=10', { STATS: fakeStats(), LANG_REF: 'abc1234' });
  assert.equal(calls[0], 'https://cdn.jsdelivr.net/gh/nikokoren/what-to-wear@abc1234/lang/de.json');
  assert.equal(await res.text(), '{"meta":{"code":"de"}}');
  assert.match(res.headers.get('content-type'), /application\/json/);
});

test('an upstream 404 stays a 404 so the markup degrades as before', async () => {
  stubUpstream(404, 'not found');
  const res = await poll('/lang/xx.json?f=yes&s=10', { STATS: fakeStats() });
  assert.equal(res.status, 404);
});

test('a throwing binding never affects the poll', async () => {
  stubUpstream();
  const env = { STATS: { writeDataPoint() { throw new Error('boom'); } } };
  const res = await poll('/lang/en.json?f=no&s=0', env);
  assert.equal(res.status, 200);
  assert.equal(recordPoll(env, { lang: 'en', forecast: 'off', sarcasm: '0' }), false);
});

test('no binding at all is fine', async () => {
  stubUpstream();
  const res = await poll('/lang/en.json?f=no&s=0', {});
  assert.equal(res.status, 200);
});

test('sampling records 1 in N with weight N', () => {
  const stats = fakeStats();
  const env = { STATS: stats, STATS_SAMPLE: '4' };
  const s = { lang: 'en', forecast: 'on', sarcasm: '10' };
  assert.equal(recordPoll(env, s, () => 0.9), false);   // not this one
  assert.equal(recordPoll(env, s, () => 0.1), true);    // this one, weighted
  assert.deepEqual(stats.points[0].doubles, [4]);
});

test('anything but a language file is a 404 and is not counted', async () => {
  stubUpstream();
  const stats = fakeStats();
  for (const path of ['/', '/lang/', '/lang/../secrets.json', '/lang/en.txt']) {
    assert.equal((await poll(path, { STATS: stats })).status, 404, path);
  }
  assert.equal(stats.points.length, 0);
});
