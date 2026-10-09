#!/usr/bin/env python3
"""
Builds the outfit-panels prototype into build/panels/:

    python3 prototypes/panels/build.py

shared.liquid = src/shared.liquid + the fact + flavour block (as in
prototypes/fact-flavour) + this prototype's block.liquid at the end.
The four views are generated from one template below, so the layouts
differ only where the view's size makes them differ. Language files are
lang/<code>.json merged with both prototypes' additions.
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
FF = REPO / "prototypes" / "fact-flavour"
OUT = REPO / "build" / "panels"
ANCHOR = "{%- comment %}\n============ THE PICTURE"

# Per view: image height (in view height) with words / without, the
# words' size and the time's size (larger on the X). Only the portrait
# half-tall stacks the panels (ihs: the whole stack's height, times
# included); everywhere the time sits under the drawing.
VIEWS = {
    "full": dict(ih_words=56, ih_bare=74, words="content--large lg:content--xlarge", label="lg:label--xlarge", stack=False),
    "half_horizontal": dict(ih_words=58, ih_bare=74, words="content--base lg:content--large", label="lg:label--xlarge", stack=False, side=True),
    "half_vertical": dict(ih_words=58, ih_bare=76, ihs_words=70, ihs_bare=84, words="content--base", label="lg:label--xlarge", stack=True),
    "quadrant": dict(ih_words=52, ih_bare=70, words="content--small lg:content--base", label="lg:label--large", stack=False),
}

TEMPLATE = """{%- assign has_words = false -%}
{%- if panel_fact != '' or panel_flavour != '' -%}{%- assign has_words = true -%}{%- endif -%}
{%- if has_words -%}{%- assign ih = IH_WORDS -%}{%- assign ihs = IHS_WORDS -%}{%- else -%}{%- assign ih = IH_BARE -%}{%- assign ihs = IHS_BARE -%}{%- endif -%}
{%- assign gaps = panel_n | minus: 1 | times: 4 -%}
{%- assign vgaps = panel_n | minus: 1 | times: 2 -%}
<style>
  /* The view is the measure: every cq unit below is a share of it. */
  .wtw-box { container-type: size; width: 100%; height: 100%; }
  .wtw-day { width: 100cqw; height: 100cqh; --ih: {{ ih }}cqh; --pw: 92cqw; }
  .wtw-panels { flex: none; display: flex; flex-direction: row; justify-content: center; align-items: flex-end; gap: 4cqw; }
  .wtw-panel { display: flex; flex-direction: column; align-items: center; gap: 1cqh; margin: 0; }
  .wtw-panel img { aspect-ratio: 1; object-fit: contain;
    width: min(calc((var(--pw) - {{ gaps }}cqw) / {{ panel_n }}), var(--ih)); height: auto; }
  .wtw-panel .label { white-space: nowrap; }
  .wtw-now .label { font-weight: 700; text-decoration: underline; }
  /* The words fit themselves: TRMNL's content limiter miscounts on the X
     (it measures the drawings scaled up, the space not) and hides them. */
  .wtw-words { width: 92cqw; flex: 0 1 auto; min-height: 0; overflow: hidden; }
  .wtw-words p { margin: 0; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 3; overflow: hidden; }
  SIDE_CSS
  STACK_CSS
</style>
<div class="wtw-box">
<div class="layout layout--col layout--center gap--small wtw-day{% if has_words %} wtw-side{% endif %}">
  {%- if is_error %}
    <img class="image image--contain h--[60cqh]" src="{{ sprite_url }}" alt="Error">
    <div class="content content--center text--center content--base" data-content-limiter="true"><p>{{ error_headline }}</p></div>
  {%- else %}
  <div class="wtw-panels">
    {%- for slug in panel_slug_list %}
    <figure class="wtw-panel{% if forloop.first %} wtw-now{% endif %}">
      <img class="image image-dither" src="{{ sprite_base_url }}{{ slug }}.png" alt="{{ slug }}">
      {%- if panel_n > 1 %}<span class="label LABEL">{{ panel_label_list[forloop.index0] }}</span>{%- endif %}
    </figure>
    {%- endfor %}
  </div>
  {%- if has_words %}
  <div class="content content--center text--center WORDS wtw-words">
    {%- if panel_fact != '' %}<p class="font--bold">{{ panel_fact }}</p>{%- endif %}
    {%- if panel_flavour != '' %}<p>{{ panel_flavour }}</p>{%- endif %}
  </div>
  {%- endif %}
  {%- endif %}
</div>
</div>

{%- if show_bottom_bar == 'on' -%}
  <div class="title_bar">
    <span class="title">What to Wear</span>
    <span class="instance">{{ location_label }}</span>
  </div>
{%- endif -%}
"""

# Wide and short (the half view on its side, 800x240 on the OG): the
# words go beside the panels, so the drawings get the full height.
SIDE = """.screen:not(.screen--portrait) .wtw-side { flex-direction: row; gap: 3cqw; --ih: IH_BARE_SIDEcqh; --pw: 60cqw; }
  .screen:not(.screen--portrait) .wtw-side .wtw-words { width: 34cqw; }"""

# Stacked (portrait half-tall, 240 by 800 on the OG): one panel under the
# other, the time under each drawing. --lbl is a time's height with its gap.
STACK = """.screen--portrait .wtw-day { --lbl: 3.5cqh; }
  .screen--portrait.screen--lg .wtw-day { --lbl: 4.5cqh; }
  .screen--portrait .wtw-panels { flex-direction: column; align-items: center; gap: 2cqh; }
  .screen--portrait .wtw-panel img { width: auto;
    height: min(calc(({{ ihs }}cqh - {{ vgaps }}cqh - {{ panel_n }} * var(--lbl)) / {{ panel_n }}), 84cqw); }"""


def main():
    shared = (REPO / "src" / "shared.liquid").read_text(encoding="utf-8")
    if ANCHOR not in shared:
        raise SystemExit("anchor not found in src/shared.liquid")
    ff = (FF / "block.liquid").read_text(encoding="utf-8")
    block = (HERE / "block.liquid").read_text(encoding="utf-8")
    (OUT / "views").mkdir(parents=True, exist_ok=True)
    (OUT / "lang").mkdir(parents=True, exist_ok=True)
    (OUT / "shared.liquid").write_text(shared.replace(ANCHOR, ff + "\n\n" + ANCHOR, 1) + "\n" + block, encoding="utf-8")

    for view, v in VIEWS.items():
        src = (TEMPLATE.replace("IHS_WORDS", str(v.get("ihs_words", v["ih_words"]))).replace("IHS_BARE", str(v.get("ihs_bare", v["ih_bare"])))
               .replace("IH_WORDS", str(v["ih_words"])).replace("IH_BARE", str(v["ih_bare"]))
               .replace("WORDS", v["words"]).replace("LABEL", v["label"]).replace("STACK_CSS", STACK if v["stack"] else "")
               .replace("SIDE_CSS", SIDE.replace("IH_BARE_SIDE", str(v["ih_bare"])) if v.get("side") else ""))
        (OUT / "views" / f"{view}.liquid").write_text(src, encoding="utf-8")

    for lang in ("en", "de"):
        doc = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        doc.update(json.loads((FF / "lang" / f"{lang}.json").read_text(encoding="utf-8")))
        doc.update(json.loads((HERE / "lang" / f"{lang}.json").read_text(encoding="utf-8")))
        (OUT / "lang" / f"{lang}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"built {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
