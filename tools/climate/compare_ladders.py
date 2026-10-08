import json, sys, collections
rows = json.load(open(sys.argv[1]))
LADDERS = {
  'today (8)':        ([-7, 3, 10, 14, 19, 27, 32],
                       ['puffer+scarf', 'puffer', 'light jacket', 'hoodie', 'sweatshirt', 'tee+shorts', 'tank', 'tank+hat+water'],
                       {3: 'mid', 4: 'mid'}),   # hoodie and sweatshirt: one warmth class, no hint between them
  'straw-man A (7)':  ([-5, 5, 12, 18, 24, 30],
                       ['bundled up', 'winter coat', 'jacket', 'sweater', 'tee+long pants', 'tee+shorts', 'heat'], {}),
  'straw-man B (6)':  ([-5, 5, 12, 20, 28],
                       ['bundled up', 'winter coat', 'jacket', 'sweater', 'tee+shorts', 'heat'], {}),
}
def rank(at, edges):
    for i, e in enumerate(edges):
        if at <= e: return i
    return len(edges)

# per city-day series
days = collections.defaultdict(dict)
wday = {}
for w, reg, name, loc, at, pr, t in rows:
    d = (name, loc[:10]); days[d][int(loc[11:13])] = (at, pr)
    wday[name] = wday.get(name, 0) + w
nd = collections.Counter(n for n, _ in days)
for lname, (edges, names, cls) in LADDERS.items():
    key = lambda i: cls.get(i, i)
    awake = collections.defaultdict(float); dress = collections.defaultdict(float)
    wet = collections.defaultdict(float)
    tw = tdw = tww = 0; change = 0; dw = 0; changes_wet = 0
    for (name, day), hrs in days.items():
        wd = wday[name] / nd[name] / 15
        for h in range(7, 22):
            if h in hrs:
                r = rank(hrs[h][0], edges); awake[r] += wd; tw += wd
                if hrs[h][1] is not None and hrs[h][1] >= 0.2: wet[r] += wd; tww += wd
        if 7 in hrs: dress[rank(hrs[7][0], edges)] += wd; tdw += wd
        if 8 in hrs and all(h in hrs for h in range(11, 18)) and 19 in hrs:
            m = key(rank(hrs[8][0], edges))
            pk = key(rank(max(hrs[h][0] for h in range(11, 18)), edges))
            ev = key(rank(hrs[19][0], edges))
            dw += wd
            if pk != m or ev != m: change += wd
    print(f'\n== {lname}   edges {edges}')
    print(f'   {"outfit":16} daytime  7am   of wet hours')
    for i, n in enumerate(names):
        print(f'   {n:16} {100*awake[i]/tw:5.1f}%  {100*dress[i]/tdw:5.1f}%  {100*wet[i]/tww:5.1f}%')
    print(f'   days where the outfit changes between 08:00, the afternoon peak or 19:00: {100*change/dw:.0f}%')
