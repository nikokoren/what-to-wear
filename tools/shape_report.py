#!/usr/bin/env python3
"""
How each joke shape does with the owner: star and veto rates per shape,
language and level, from review/decisions/. docs/SHAPES.md explains the
shapes; this keeps its numbers honest after every round.

    python3 tools/shape_report.py              # the table
    python3 tools/shape_report.py --examples   # plus starred lines per shape

The shapes are found by pattern, so the counts are approximate: a line
can match two shapes, or none. Good enough to see which shapes the owner
stars and which ones get vetoed; not a judge of a single line.
"""

import collections
import json
import pathlib
import random
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
SHAPES = {
    "en": [
        ("screen", "The screen's own limits", r"\b(I'm a screen|I'd (come|make|go|say)|I don't (have|do|get|sweat|freeze)|I only work|I can't (display|leave|go)|my (battery|frame|screen|pixels|wall)|[Pp]erks of|I refresh|I live|indoors|in here)\b"),
        ("credit", "Taking credit, denying blame", r"\b([Ww]asn't me|take the credit|[Yy]ou're welcome|[Kk]idding|my fault|[Nn]ot my)\b"),
        ("sting", "Ends on a sting word", r"\b(Again|Anyway|Twice|Out loud|Almost|Barely|Probably|Still)\.$"),
        ("habit", "Your habits, predicted", r"\b[Yy]ou'll\b|\byou're going to\b"),
        ("quote", "Your words thrown back", r"'[^']{3,40}'|\"[^\"]{3,40}\"|‘[^’]{3,40}’"),
        ("people", "Other people", r"\b([Ee]veryone|[Ee]verybody|[Ss]omeone|[Ss]omebody|[Pp]eople|[Nn]obody|neighbou?rs?|[Hh]alf the)\b"),
        ("simile", "A simile", r"\blike (a|an|your|the)\b"),
    ],
    "de": [
        ("quote", "Zitat zurück", r"„[^“]{3,40}“"),
        ("habit", "„Ich kenn dich“", r"\b(Ich kenn dich|trotzdem|wirst du|[Kk]ennen wir|[Jj]edes Mal|sowieso)\b"),
        ("parent", "Eltern-Ton", r"\b(Ab ins Bett|[Bb]itte|Nicht „|sofort|mit dir|komm mir)\b"),
        ("jab", "Seitenhieb", r"\b(als du|wie dein|dein Herz|mehr Ausstrahlung|so blass wie du|verdient)\b"),
        ("self", "Der Grantler über sich", r"\b(Ich|ich|mir|mich)\b"),
        ("sigh", "Grantler-Seufzer", r"^(Na|Auch das noch|Natürlich|Wieder|Super|Toll|Prima|Herrlich|Juhuu)|\b(Wieder|Natürlich)\.$"),
        ("people", "Andere Leute", r"\b(alle|jeder|jede|Leute|die Nachbarn|Irgendein|halb Deutschland|im Radio|im Büro|in der Bahn)\b"),
        ("simile", "Vergleich „wie ein“", r"\bwie (ein|eine|dein|deine)\b"),
    ],
}
OUT = ("veto", "rewrite")


def joke(d):
    return (d.get("edit") or d["text"]).split("||")[-1].strip()


def main():
    examples = "--examples" in sys.argv
    rnd = random.Random(1)
    for lang, shapes in SHAPES.items():
        votes = [d for d in json.loads((REPO / "review" / "decisions" / f"{lang}.json").read_text(encoding="utf-8")).values()
                 if d.get("verdict") in ("star", "keep") + OUT]
        print(f"== {lang}")
        for level in ("10", "11"):
            at = [d for d in votes if str(d.get("level")) == level]
            star = sum(d["verdict"] == "star" for d in at) / len(at)
            out = sum(d["verdict"] in OUT for d in at) / len(at)
            print(f"  {'On' if level == '10' else '11'}: {len(at)} votes, {star:.0%} starred, {out:.0%} vetoed")
            for slug, name, pattern in shapes:
                hit = [d for d in at if re.search(pattern, joke(d))]
                if len(hit) < 8:
                    continue
                s = sum(d["verdict"] == "star" for d in hit) / len(hit)
                o = sum(d["verdict"] in OUT for d in hit) / len(hit)
                print(f"    {name:32} {len(hit):4}  starred {s:4.0%}  vetoed {o:4.0%}")
                if examples:
                    stars = sorted({joke(d) for d in hit if d["verdict"] == "star"})
                    for line in rnd.sample(stars, min(6, len(stars))):
                        print(f"        * {line}")
        buckets = collections.Counter()
        for d in votes:
            n = len(joke(d))
            b = "under 45" if n < 45 else "45 to 69" if n < 70 else "70 and over"
            buckets[(b, d["verdict"] == "star")] += 1
        print("  length: " + ", ".join(
            f"{b} {buckets[(b, True)] / max(1, buckets[(b, True)] + buckets[(b, False)]):.0%} starred"
            for b in ("under 45", "45 to 69", "70 and over")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
