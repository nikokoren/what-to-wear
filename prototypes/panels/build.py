#!/usr/bin/env python3
"""
Builds the outfit-panels prototype into build/panels/:

    python3 prototypes/panels/build.py

shared.liquid = src/shared.liquid + the fact + flavour block (as in
prototypes/fact-flavour) + this prototype's block.liquid at the end.
Every view, in every forecast mode (Visual Forecast, words, none), is
generated from one template below, in TRMNL's framework classes only.
Language files are lang/<code>.json merged with both prototypes'
additions.
"""

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
FF = REPO / "prototypes" / "fact-flavour"
OUT = REPO / "build" / "panels"
ANCHOR = "{%- comment %}\n============ THE PICTURE"



# Every screen comes from one template below, in TRMNL's framework classes
# only: no <style>, no inline style, no limiter tricks. Sizes are shares of
# the view (cqw, cqh: TRMNL's `layout` is a size container).
#
# One drawing (a steady day, the words view, no forecast): a square box
# as wide as the view that gives up height to the words (images shrink in
# a flex column), so the drawing is as big as the view allows and stays
# with the words when the width is what limits it.
# Lying wide with words (the half view on its side, the quarter), it
# stands beside them; its box is wider than its column and overflows it
# on both sides, so the transparent sides of the square don't push the
# words away.
#
# Two or three drawings: as the prototype had them, rebuilt in classes.
# - Neighbours overlap by a quarter: each panel is a column 3/4 as wide as
#   its drawing, the drawing centred and overflowing it (n columns plus a
#   quarter drawing fill the row: n x 3/4 + 1/4). The figure takes about
#   55% of the square, so it stays inside its column.
# - A drawing's box is square (aspect--1/1) and capped in height, so it
#   is as big as the smaller of its share of the width and the height
#   cap, and the time sits right under it.
# - Only the half view standing tall (240 by 800 on the OG) stacks them.
#
# The words take their natural height. No content limiter: on the X it
# measures the drawings scaled up and the space not, and hides the words.
VIEWS = {
    "full": dict(words="content--xlarge lg:content--xxlarge", label="lg:label--xlarge", ih_words=66, ih_bare=80,
                 ih_fact=50, words_fact="content--large lg:content--xlarge"),
    "half_horizontal": dict(words="content--large lg:content--xlarge", label="lg:label--xlarge", ih_words=62, ih_bare=78,
                            ih_fact=48, words_fact="content--base lg:content--large",
                            side=True, side_ih=84),
    "half_vertical": dict(words="content--large lg:content--xlarge", words_n="content--base lg:content--xlarge",
                          label="lg:label--xlarge", ih_words=62, ih_bare=78, stack=dict(fact=58, words=70, bare=86),
                          ih_fact=50, words_fact="content--base lg:content--large"),
    "quadrant": dict(words="content--base lg:content--large", words_n="content--small lg:content--large",
                     label="lg:label--large", ih_words=54, ih_bare=74, side_one=True,
                     ih_fact=42, words_fact="content--small lg:content--base"),
}
ROW = 94        # the row of two or three drawings, in view width
SIDE_ROW = 60   # the same, with the words beside it (side_words wide)
SIDE_WORDS = 34
SIDE_ROW_FACT, SIDE_WORDS_FACT = 50, 46   # with the forecast line too, the words get more room
ONE_MIN = 40    # one drawing never gets less of the height than this
# Two or three drawings with the forecast line under or beside them (both
# switches on) get a lower cap (ih_fact) and words a size smaller
# (words_fact): the forecast line and the sarcastic line are two to five
# lines.
# One drawing beside the words: its column, its box, and the words' width.
ONE_SIDE = (36, 52, 60)
# A stacked panel's time, with its gap, in view height: OG, X.
STACK_LABEL = (3.5, 4.5)

ERROR = {
    "col": """<div class="layout layout--col layout--center">
  <div class="richtext richtext--center gap w--max-[100cqw]">
    <img class="image image--contain h--[60cqh]" src="{{ sprite_url }}" alt="Error">
    <div class="content content--center text--center w--max-[100cqw] content--base lg:content--large" data-content-limiter="true">
      <p>{{ error_message }}</p>
    </div>
  </div>
</div>""",
    "row": """<div class="layout layout--row portrait:layout--col layout--center gap">
  <img class="image image--contain h--[100cqh] w--max-[40cqw] portrait:h--[60cqh] portrait:w--max-[100cqw]" src="{{ sprite_url }}" alt="Error">
  <div class="content content--center text--center stretch-x content--large" data-content-limiter="true">
    <p>{{ error_headline }}</p>
  </div>
</div>""",
}

TITLE_BAR = """
{%- if show_bottom_bar == 'on' -%}
  <div class="title_bar">
    <span class="title">What to Wear</span>
    <span class="instance">{{ location_label }}</span>
  </div>
{%- endif -%}
"""

WORDS = """
  {%- if has_words %}
  <div class="content content--center text--center {{ c_words }}" data-wtw="words">
    {%- if w_fact != '' %}<p class="font--bold">{{ w_fact }}</p>{%- endif %}
    {%- if w_flavour != '' %}<p>{{ w_flavour }}</p>{%- endif %}
  </div>
  {%- endif %}"""


def build_view(view, v):
    """One view: every forecast mode, panel count and orientation."""
    side, side_one, stack = v.get("side", False), v.get("side_one", False), v.get("stack")
    words_n = v.get("words_n", v["words"])
    a = []
    a.append("""{%- comment %}
The words. Forecast on: the forecast line, with or without the drawings.
Only the drawings: "works all day" on one. The sarcastic line is the same
for every screen (flavour_line): the blocks pick it for what's on screen.
{%- endcomment %}
{%- assign w_fact = '' -%}
{%- assign w_flavour = flavour_line -%}
{%- if forecast_on and fact_line != '' -%}
  {%- assign w_fact = fact_line -%}
{%- elsif visual_forecast -%}
  {%- assign w_fact = panel_fact -%}
{%- endif -%}
{%- assign has_words = false -%}
{%- if w_fact != '' or w_flavour != '' -%}{%- assign has_words = true -%}{%- endif -%}
{%- assign n = 1 -%}
{%- if visual_forecast -%}{%- assign n = panel_n -%}{%- endif -%}
""")
    err = ERROR["row" if (side or side_one) else "col"]
    a.append("{%- if is_error %}\n" + err + "\n")

    # ---- one drawing
    col_words = f"w--[96cqw] {v['words']}"
    one_col = (f"layout layout--col gap--small",
               f"image image--contain image-dither aspect--1/1 w--[100cqw] h--min-[{ONE_MIN}cqh]")
    a.append("{%- elsif n == 1 %}\n")
    if side or side_one:
        c, box, w = ONE_SIDE
        a.append("{%- if has_words -%}\n")
        a.append(f"  {{%- assign c_outer = 'layout layout--row portrait:layout--col gap' -%}}\n"
                 f"  {{%- assign c_wrap = 'flex flex--col gap--none w--[{c}cqw] h--[100cqh] portrait:w--[100cqw] portrait:h--auto portrait:stretch' -%}}\n"
                 f"  {{%- assign c_image = 'image image--contain image-dither w--[{box}cqw] h--[100cqh] portrait:w--[100cqw] portrait:h--auto portrait:stretch portrait:h--min-[{ONE_MIN}cqh]' -%}}\n"
                 f"  {{%- assign c_words = 'w--[{w}cqw] portrait:w--[96cqw] {v['words']}' -%}}\n")
        a.append("{%- else -%}\n")
        a.append(f"  {{%- assign c_outer = '{one_col[0]}' -%}}{{%- assign c_wrap = '' -%}}{{%- assign c_image = '{one_col[1]}' -%}}\n")
        a.append("{%- endif -%}\n")
    else:
        a.append(f"{{%- assign c_outer = '{one_col[0]}' -%}}{{%- assign c_wrap = '' -%}}{{%- assign c_image = '{one_col[1]}' -%}}"
                 f"{{%- assign c_words = '{col_words}' -%}}\n")
    a.append("""<div class="{{ c_outer }}">
  {%- if c_wrap != '' %}<div class="{{ c_wrap }}">{%- endif %}
  <img class="{{ c_image }}" src="{{ sprite_url }}" onerror="this.onerror=null;this.src='{{ fallback_sprite_url }}'" alt="Outfit">
  {%- if c_wrap != '' %}</div>{%- endif %}""" + WORDS + "\n</div>\n")

    # ---- two or three drawings
    a.append("{%- else %}\n")
    def sizes(row, n):
        den = n * 0.75 + 0.25
        img = row / den
        return round(img * 0.75), round(img)
    for k in (2, 3):
        a.append(("{%- if n == 2 -%}\n" if k == 2 else "{%- else -%}\n"))
        # Three cases: the forecast line under the drawings (both switches on),
        # only the sarcastic line, no words.
        for case in ("fact", "words", "bare"):
            a.append({"fact": "  {%- if w_fact != '' -%}\n", "words": "  {%- elsif has_words -%}\n",
                      "bare": "  {%- else -%}\n"}[case])
            ih = {"fact": v["ih_fact"], "words": v["ih_words"], "bare": v["ih_bare"]}[case]
            wclass = v["words_fact"] if case == "fact" else words_n
            col, img = sizes(ROW, k)
            panel = f"w--[{col}cqw]"
            image = f"w--[{img}cqw] h--max-[{ih}cqh]"
            outer = "layout layout--col gap--small"
            row = "flex flex--row gap--none"
            words = f"w--[92cqw] {wclass}"
            if side and case != "bare":
                srow, swords = (SIDE_ROW_FACT, SIDE_WORDS_FACT) if case == "fact" else (SIDE_ROW, SIDE_WORDS)
                scol, simg = sizes(srow, k)
                outer = "layout layout--row portrait:layout--col gap"
                panel = f"w--[{scol}cqw] portrait:w--[{col}cqw]"
                image = f"w--[{simg}cqw] h--max-[{v['side_ih']}cqh] portrait:w--[{img}cqw] portrait:h--max-[{ih}cqh]"
                words = f"w--[{swords}cqw] portrait:w--[92cqw] {wclass}"
            if stack:
                total = stack[case]
                caps = [int((total - (k - 1) * 2 - k * lbl) / k) for lbl in STACK_LABEL]
                row += " portrait:flex--col"
                panel += " portrait:w--[100cqw]"
                image += f" portrait:w--[84cqw] portrait:h--max-[{caps[0]}cqh] lg:portrait:h--max-[{caps[1]}cqh]"
            a.append(f"    {{%- assign c_outer = '{outer}' -%}}{{%- assign c_row = '{row}' -%}}"
                     f"{{%- assign c_panel = '{panel}' -%}}{{%- assign c_image = '{image}' -%}}"
                     f"{{%- assign c_words = '{words}' -%}}\n")
        a.append("  {%- endif -%}\n")
    a.append("{%- endif -%}\n")
    a.append("""<div class="{{ c_outer }}">
  <div class="{{ c_row }}" data-wtw="panels">
    {%- for slug in panel_slug_list %}
    <div class="flex flex--col gap--small {{ c_panel }}">
      <img class="image image--contain image-dither aspect--1/1 {{ c_image }}" src="{{ sprite_base_url }}{{ slug }}.png" alt="{{ slug }}">
      <span class="label text--center mx--1 LABEL{% if forloop.first %} font--bold label--underline{% endif %}">{{ panel_label_list[forloop.index0] }}</span>
    </div>
    {%- endfor %}
  </div>""".replace("LABEL", v["label"]) + WORDS + "\n</div>\n{%- endif %}\n")
    a.append(TITLE_BAR)
    return "".join(a)


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
        (OUT / "views" / f"{view}.liquid").write_text(build_view(view, v), encoding="utf-8")

    for lang in ("en", "de"):
        doc = json.loads((REPO / "lang" / f"{lang}.json").read_text(encoding="utf-8"))
        doc.update(json.loads((FF / "lang" / f"{lang}.json").read_text(encoding="utf-8")))
        doc.update(json.loads((HERE / "lang" / f"{lang}.json").read_text(encoding="utf-8")))
        (OUT / "lang" / f"{lang}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"built {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
