#!/usr/bin/env python3
"""
Pins "Write new" (the review page's fourth verdict, docs/TODO.md item 14)
from vote to pools, on a made-up round in a scratch copy of review/:

    python3 tools/test_write_new.py

A "Write new" vote on a line that would replace another takes both out of
the pools, puts both on the "don't" list, and lists the spot as waiting
for new lines, with the owner's note, until a kept line from a later
round answers it. A pool is never emptied.
"""

import importlib.util
import json
import pathlib
import shutil
import sys
import tempfile

REPO = pathlib.Path(__file__).resolve().parent.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sync = load("review_sync", REPO / "tools" / "review_sync.py")
pools = load("build_pools", REPO / "review" / "rounds" / "build_pools.py")

failures = []


def expect(name, ok):
    if not ok:
        failures.append(name)


OLD = "Old line the round wanted to replace."
NEW = "A rewording that misses too."
LONE = "Only line in its pool."
ANSWER = "A completely new line."
with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp)
    (tmp / "review" / "rounds").mkdir(parents=True)
    rnd = {"round": "test-write-new", "lines": [
        {"lang": "en", "path": "flavour_10.cool", "text": NEW, "replaces": OLD, "sprite": "jacket_dry",
         "fact": "It stays cool all day.", "meaning": "Sarcastic line at On."},
        {"lang": "en", "path": "flavour_10.night", "text": LONE},
    ]}
    (tmp / "review" / "rounds" / "test-write-new.json").write_text(json.dumps(rnd), encoding="utf-8")
    sync.OUT = tmp / "review"
    pools.REPO = tmp

    def vote(i, text, path, verdict, rnd="test-write-new", note=""):
        return {"id": i, "lang": "en", "level": "10", "key": path.split(".")[1], "path": path, "text": text,
                "round": rnd, "verdict": verdict, "tags": ["not funny"], "note": note,
                "updatedAt": "2026-10-15T10:00:00Z"}

    votes = [vote("en-new", NEW, "flavour_10.cool", "rewrite", note="Something about the wind instead."),
             vote("en-lone", LONE, "flavour_10.night", "rewrite")]
    known, _ = sync.merge("en", votes)
    rows = sync.round_rows()
    sync.write_dont("en", known, rows)
    n = sync.write_waiting("en", known, rows)
    dont = (tmp / "review" / "dont" / "en.md").read_text(encoding="utf-8")
    todo = (tmp / "review" / "rewrite" / "en.md").read_text(encoding="utf-8")
    expect("both lines on the don't list", NEW in dont and OLD in dont and "write new" in dont)
    expect("two spots waiting", n == 2)
    expect("the waiting list has the note, what's out and the screen",
           "Something about the wind instead." in todo and NEW in todo and OLD in todo and "jacket_dry" in todo)

    doc = {"flavour_10": {"cool": [OLD, "Another cool line.", NEW], "night": [LONE]}}
    out = pools.apply_write_new(doc, "en", known)
    expect("the rewording and the original are out", doc["flavour_10"]["cool"] == ["Another cool line."])
    expect("a pool is never emptied", doc["flavour_10"]["night"] == [LONE] and out["waiting"] == 1)

    # A later round answers the cool spot; a kept answer clears it.
    rnd2 = {"round": "test-answer", "lines": [{"lang": "en", "path": "flavour_10.cool", "text": ANSWER, "answers": "en-new"}]}
    (tmp / "review" / "rounds" / "test-answer.json").write_text(json.dumps(rnd2), encoding="utf-8")
    known, _ = sync.merge("en", [vote("en-answer", ANSWER, "flavour_10.cool", "keep", rnd="test-answer")])
    n = sync.write_waiting("en", known, sync.round_rows())
    todo = (tmp / "review" / "rewrite" / "en.md").read_text(encoding="utf-8")
    expect("an answered spot leaves the waiting list", n == 1 and NEW not in todo and LONE in todo)

if failures:
    print("FAILED:\n  " + "\n  ".join(failures))
    sys.exit(1)
print("all good: Write new takes out the line and the one it replaces, lists the spot until it's answered")
