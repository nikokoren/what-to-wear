#!/usr/bin/env python3
"""
Topical lines: lines about current events, each shown only inside a date
window (see TOPICAL LINES in prototypes/fact-flavour/block.liquid, and
.claude/skills/topical for the routine).

    python3 tools/topical.py add review/rounds/<round>.json   # keepers in
    python3 tools/topical.py prune                            # expired out
    python3 tools/topical.py check                            # format

--lang-dir picks the language files (default: the prototype's, until the
redesign ships; the weekly prune job passes lang/).

add: every line of the round the owner starred or kept (by
review/decisions/), once per window, then prune and check. A round can
carry "edits": {"line as voted": "line as it should run"} for the owner's
rewordings.

prune: drops every line whose window ended before yesterday (UTC), so
the last day has ended in every time zone, and appends it to
review/topical-archive.json. The votes stay in review/decisions/, so a
pruned joke can't come back by accident.
"""

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_LANG_DIR = REPO / "prototypes" / "fact-flavour" / "lang"
ARCHIVE = REPO / "review" / "topical-archive.json"
LEVELS = ("10", "11")
REGIONS = {"US", "UK", "IE", "DE", "AT", "CH", "AU"}
MOODS = {"nice", "cool", "warming", "cooling", "cold", "hot", "wet", "snow", "fickle", "evening", "night"}
MAX_DAYS = 21
MAX_CHARS = 80
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def line_id(lang, text):
    return lang + "-" + hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def save(path, doc):
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def lang_files(lang_dir):
    return sorted(pathlib.Path(lang_dir).glob("*.json"))


def problems(entry):
    out = []
    text = entry.get("text", "")
    if not isinstance(text, str) or not text.strip():
        out.append("no text")
    elif len(text) > MAX_CHARS:
        out.append(f"longer than {MAX_CHARS} characters")
    elif "~|~" in text:
        out.append("contains ~|~, the markup's separator")
    dates = []
    for f in ("from", "until"):
        v = entry.get(f, "")
        if not DATE.match(str(v)):
            out.append(f"{f} is not YYYY-MM-DD")
            continue
        try:
            dates.append(dt.date.fromisoformat(v))
        except ValueError:
            out.append(f"{f} is not a real date")
    if len(dates) == 2:
        if dates[0] > dates[1]:
            out.append("from is after until")
        elif (dates[1] - dates[0]).days + 1 > MAX_DAYS:
            out.append(f"window longer than {MAX_DAYS} days")
    for field, known in (("region", REGIONS), ("moods", MOODS)):
        if entry.get(field):
            unknown = {x.strip() for x in str(entry[field]).split(",")} - known
            if unknown:
                out.append(f"unknown {field}: {', '.join(sorted(unknown))}")
    extra = set(entry) - {"text", "from", "until", "region", "moods"}
    if extra:
        out.append(f"unknown fields: {', '.join(sorted(extra))}")
    return out


def check(lang_dir):
    bad = []
    for path in lang_files(lang_dir):
        doc = load(path)
        for level in LEVELS:
            for i, entry in enumerate(doc.get(f"topical_{level}", [])):
                for p in problems(entry):
                    bad.append(f"{path.name} topical_{level}[{i}]: {p}")
    return bad


def prune(lang_dir, today):
    cutoff = (today - dt.timedelta(days=1)).isoformat()
    archive = load(ARCHIVE) if ARCHIVE.exists() else []
    removed = 0
    for path in lang_files(lang_dir):
        doc = load(path)
        changed = False
        for level in LEVELS:
            key = f"topical_{level}"
            if key not in doc:
                continue
            keep = [e for e in doc[key] if str(e.get("until", "")) >= cutoff]
            gone = [e for e in doc[key] if str(e.get("until", "")) < cutoff]
            for e in gone:
                record = {"lang": path.stem, "level": level, **e}
                if record not in archive:
                    archive.append(record)
            if gone:
                doc[key] = keep
                changed = True
                removed += len(gone)
        if changed:
            save(path, doc)
    if removed:
        save(ARCHIVE, archive)
    return removed


def add(round_path, lang_dir):
    data = load(pathlib.Path(round_path))
    name, edits = data["round"], data.get("edits", {})
    added = 0
    for lang in sorted({l["lang"] for l in data["lines"]}):
        decisions_path = REPO / "review" / "decisions" / f"{lang}.json"
        decisions = load(decisions_path) if decisions_path.exists() else {}
        path = pathlib.Path(lang_dir) / f"{lang}.json"
        doc = load(path)
        for line in data["lines"]:
            if line["lang"] != lang:
                continue
            vote = decisions.get(line_id(lang, line["text"]), {})
            if vote.get("round") != name or vote.get("verdict") not in ("star", "keep"):
                continue
            level = line["path"].split(".")[0].split("_")[1]
            text = edits.get(line["text"], line["text"])
            for window in line.get("windows") or [line]:
                entry = {"text": text, "from": window["from"], "until": window["until"]}
                for f in ("region", "moods"):
                    v = window.get(f) or line.get(f)
                    if v:
                        entry[f] = v
                pool = doc.setdefault(f"topical_{level}", [])
                if entry not in pool:
                    pool.append(entry)
                    added += 1
        save(path, doc)
    return added


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=("add", "prune", "check"))
    ap.add_argument("round", nargs="?")
    ap.add_argument("--lang-dir", default=str(DEFAULT_LANG_DIR))
    ap.add_argument("--today", help="YYYY-MM-DD, default today (UTC)")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.today) if a.today else dt.datetime.now(dt.timezone.utc).date()

    if a.command == "add":
        if not a.round:
            sys.exit("add needs the round file")
        print(f"added {add(a.round, a.lang_dir)} topical lines")
    if a.command in ("add", "prune"):
        print(f"pruned {prune(a.lang_dir, today)} expired topical lines")
    bad = check(a.lang_dir)
    if bad:
        print("\n".join(bad))
        sys.exit(1)
    print("topical lines check out")


if __name__ == "__main__":
    main()
