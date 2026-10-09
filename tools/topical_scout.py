#!/usr/bin/env python3
"""
What's been happening, for the topical lines (.claude/skills/topical).

    python3 tools/topical_scout.py            # the last 8 days
    python3 tools/topical_scout.py --days 3 --out /tmp/scout.md

Lists, as Markdown:
  - Wikipedia's Current events, only the sections our topics come from
    (arts and culture, sport, science and technology, business): facts.
  - The Onion and Der Postillon: a radar for what people are talking
    about. Never a source of jokes: we take the real event underneath,
    if there is one, never their premise, punchline or wording. Many of
    their headlines are invented; those are no event at all.

The gate (no death, illness, crime, war, disasters, politics) is applied
by whoever reads this, as the skill says, and every event is checked in
real news before anyone writes about it.
"""

import argparse
import datetime as dt
import email.utils
import html
import re
import sys
import urllib.request

UA = "what-to-wear-topical-scout/1.0 (https://github.com/nikokoren/what-to-wear)"
WIKI = "https://en.wikipedia.org/w/index.php?title=Portal:Current_events/{d:%Y}_{d:%B}_{d.day}&action=raw"
WIKI_SECTIONS = ("Arts and culture", "Sports", "Science and technology", "Business and economy")
FEEDS = [
    ("The Onion", "https://theonion.com/rss/"),
    ("Der Postillon", "https://www.der-postillon.com/feeds/posts/default?alt=rss"),
]
# Postillon compilations, not headlines.
SKIP = re.compile(r"^(Newsticker|Fakt des Tages|Sonntagsfrage)\b")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def unwiki(text):
    text = re.sub(r"<!--.*?-->|<ref[^>]*>.*?</ref>|<ref[^>]*/>", "", text, flags=re.S)
    for _ in range(3):  # nested templates
        text = re.sub(r"\{\{[^{}|]*\|([^{}|]*)[^{}]*\}\}", r"\1", text)
        text = re.sub(r"\{\{[^{}]*\}\}", "", text)
    text = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", text)
    text = re.sub(r"\[https?://\S+(?: [^\]]*)?\]", "", text)
    text = text.replace("'''", "").replace("''", "")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def wikipedia(days):
    out = []
    today = dt.datetime.now(dt.timezone.utc).date()
    for back in range(days):
        day = today - dt.timedelta(days=back)
        try:
            raw = fetch(WIKI.format(d=day))
        except Exception as e:  # a day not written yet, or the network
            out.append(f"- {day}: not available ({e.__class__.__name__})")
            continue
        section, parents, items = None, {}, []
        for line in raw.splitlines():
            head = re.match(r"^'''(.+?)'''\s*$", line.strip())
            if head:
                section = head.group(1)
                continue
            bullet = re.match(r"^(\*+)\s*(.*)", line)
            if not bullet or section not in WIKI_SECTIONS:
                continue
            depth, text = len(bullet.group(1)), unwiki(bullet.group(2))
            parents[depth] = text
            # A bare topic line ("2026 Nobel Prize in Literature") heads the
            # lines under it; print the deepest lines with their topic.
            if len(text) > 60 or not re.match(r"^\S+( \S+){0,8}$", text):
                topic = " / ".join(parents[d] for d in range(1, depth) if d in parents)
                items.append(f"  - {section}: {topic + ': ' if topic else ''}{text}")
        if items:
            out.append(f"- **{day}**")
            out.extend(items)
    return out


def feed(url, days):
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)
    out = []
    for item in re.findall(r"<item>.*?</item>", fetch(url), re.S):
        title = re.search(r"<title>(.*?)</title>", item, re.S)
        link = re.search(r"<link>(.*?)</link>", item, re.S)
        date = re.search(r"<pubDate>(.*?)</pubDate>", item, re.S)
        if not title:
            continue
        title = html.unescape(re.sub(r"<!\[CDATA\[|\]\]>", "", title.group(1))).strip()
        title = re.sub(r"\s*\(Postillon TELEvision[^)]*\)$", "", re.sub(r"\s+", " ", title))
        when = email.utils.parsedate_to_datetime(date.group(1)) if date else None
        if SKIP.match(title) or (when and when < cutoff):
            continue
        out.append(f"- {when:%Y-%m-%d} {title} ({link.group(1).strip() if link else ''})")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=8)
    ap.add_argument("--out")
    a = ap.parse_args()

    parts = [f"# Topical scout, {dt.date.today()} (last {a.days} days)", "",
             "Facts first; the satire is only a radar. Gate, check, then write (.claude/skills/topical).", "",
             "## Wikipedia, Current events (culture, sport, science, business)", ""]
    parts += wikipedia(a.days) or ["- nothing"]
    for name, url in FEEDS:
        parts += ["", f"## {name} (radar only: never their joke)", ""]
        try:
            parts += feed(url, a.days) or ["- nothing"]
        except Exception as e:
            parts.append(f"- not available ({e.__class__.__name__}: {e})")
    text = "\n".join(parts) + "\n"
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
