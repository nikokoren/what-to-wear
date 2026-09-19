#!/usr/bin/env python3
"""
Renders the shared markup against synthetic Open-Meteo payloads.

Three things are checked:

1. THE TWO CODE PATHS AGREE. src/shared.liquid and the generated
   src/shared.transitional.liquid must produce identical output given the
   same language file and the same payload. They share their logic but not
   their text lookup, so this is what stops one drifting from the other.

2. THE ROLLOUT FALLBACK RENDERS. Transitional markup with a single-URL
   payload has no IDX_1 to read and falls back to the text inlined from
   lang/.rollout-fallback/. That path serves real devices during the window
   between the markup update and the polling-URL update, so it has to
   produce a complete sentence, not a blank.

3. EVERY LANGUAGE RENDERS EVERY SCENARIO with no placeholder left
   unsubstituted, no doubled spaces and no punctuation left dangling where
   a token resolved to nothing.

An earlier version of this file also asserted that the refactor was
byte-identical to the pre-extraction markup. It was, and that is recorded in
the history; the text has since been deliberately rewritten, so comparing
the two corpora no longer means anything.

Uses python-liquid, which is not the Ruby engine TRMNL runs, so this proves
the logic and not the last 1% of engine quirks. Force Refresh in the TRMNL
editor is still the final word.

Usage:  python3 tools/render_test.py
"""

import json
import pathlib
import re
import sys

from liquid import Environment
from liquid import FileSystemLoader

REPO = pathlib.Path(__file__).resolve().parent.parent

# Every language in the repo gets rendered. The two that predate the refactor
# additionally get compared against the embedded copies, because only those
# two have an embedded copy to compare against.
LANGS = {
    p.stem: json.loads(p.read_text(encoding="utf-8"))
    for p in sorted((REPO / "lang").glob("*.json"))
    if p.stem != "schema"
}
EMBEDDED_LANGS = ("en", "de")

# 24 hourly slots, index == hour, matching forecast_days=1&timezone=auto.
HOURS = [f"2026-03-14T{h:02d}:00" for h in range(24)]


def payload(current_temp, current_code, temps, probs, codes=None, hour=8):
    """Shape an Open-Meteo response the way the plugin consumes it."""
    return {
        "current": {
            "time": HOURS[hour],
            "temperature_2m": current_temp,
            "apparent_temperature": current_temp,
            "weather_code": current_code,
        },
        "hourly": {
            "time": HOURS,
            "temperature_2m": temps,
            "apparent_temperature": temps,
            "precipitation_probability": probs,
            "weather_code": codes or [0] * 24,
        },
    }


def flat(value, n=24):
    return [value] * n


def ramp(start, end, n=24):
    step = (end - start) / (n - 1)
    return [round(start + step * i, 1) for i in range(n)]


def arc(low, peak, n=24):
    mid = n // 2
    up = [round(low + (peak - low) * i / mid, 1) for i in range(mid)]
    down = [round(peak - (peak - low) * i / (n - mid), 1) for i in range(n - mid)]
    return up + down


SCENARIOS = {
    # name: (payload, expectation note)
    "steady_mild_dry": payload(17, 0, flat(17), flat(0)),
    "warming_out_of_jacket": payload(8, 0, ramp(8, 22), flat(0)),
    "cooling_into_jacket": payload(18, 0, ramp(18, 6), flat(0)),
    "arc_up_then_down": payload(9, 0, arc(9, 21), flat(0)),
    "rain_arriving": payload(14, 0, flat(14), [0] * 10 + [80] * 14),
    "long_rain": payload(14, 0, flat(14), [0] * 10 + [70] * 14),
    "maybe_rain": payload(14, 0, flat(14), [0] * 10 + [30, 30] + [0] * 12),
    "raining_now_clearing": payload(12, 61, flat(12), [0] * 24),
    "raining_all_day": payload(12, 61, flat(12), flat(90)),
    "snow_coming": payload(1, 0, flat(1), flat(0), [0] * 12 + [73] * 12),
    "heat_no_layers_left": payload(29, 0, ramp(29, 36), flat(0)),
    "extra_cold": payload(-12, 0, flat(-12), flat(0)),
    "freezing_snow_now": payload(-2, 73, flat(-2), flat(90), flat(73)),
}


def settings(lang="en", sarcasm="10", future="yes", bar="on", label="Vienna"):
    return {
        "location_label": label,
        "show_future_suggestions": future,
        "language": lang,
        "sarcasm_level": sarcasm,
        "show_bottom_bar": bar,
    }


def globals_for(data, texts, cfg, shape, day_offset=0):
    """shape: 'root' = single polling URL, 'idx' = two polling URLs."""
    base = {
        "trmnl": {
            "plugin_settings": {"custom_fields_values": cfg},
            "system": {"timestamp_utc": 1773500000 + day_offset * 86400},
            "user": {"utc_offset": 3600},
            "device": {"width": 800},
        }
    }
    if shape == "root":
        base.update(data)
        if texts is not None:
            raise ValueError("root shape cannot carry a texts payload")
    else:
        base["IDX_0"] = data
        if texts is not None:
            base["IDX_1"] = texts
    return base


def render(env, template_name, view_name, ctx):
    shared = env.get_template(template_name)
    view = env.get_template(view_name)
    # TRMNL concatenates shared markup and the view into one render pass.
    combined = shared.render(**ctx)
    # Re-render the view with the assigns the shared pass produced by
    # rendering both together, which is what TRMNL actually does.
    source = (REPO / "src" / template_name).read_text(encoding="utf-8")
    view_source = (REPO / "src" / view_name).read_text(encoding="utf-8")
    one_pass = env.from_string(source + view_source)
    return one_pass.render(**ctx), combined


def extract_tip(html):
    marker = 'outfit-tip text--center mt--xs">'
    if marker not in html:
        return None
    return html.split(marker, 1)[1].split("</div>", 1)[0].strip()


def extract_sprite(html):
    if 'src="' not in html:
        return None
    return html.split('src="', 1)[1].split('"', 1)[0]


def main():
    env = Environment(loader=FileSystemLoader(str(REPO / "src")))
    failures = []
    checked = 0

    for lang in EMBEDDED_LANGS:
        for sarcasm in ("0", "10", "11"):
            for day in range(4):  # the day index rotates the chosen line
                for name, data in SCENARIOS.items():
                    cfg = settings(lang=lang, sarcasm=sarcasm)
                    texts = LANGS[lang]
                    label = f"{lang}/{sarcasm}/day{day}/{name}"

                    # Both markups, same corpus, same payload shape: the two
                    # code paths must agree exactly. This is what stops a
                    # change to one of them drifting from the other.
                    trans_html, _ = render(
                        env, "shared.transitional.liquid", "views/full.liquid",
                        globals_for(data, texts, cfg, "idx", day),
                    )
                    final_html, _ = render(
                        env, "shared.liquid", "views/full.liquid",
                        globals_for(data, texts, cfg, "idx", day),
                    )
                    checked += 1

                    if extract_tip(trans_html) != extract_tip(final_html):
                        failures.append(
                            f"PATHS DISAGREE {label}\n"
                            f"   transitional: {extract_tip(trans_html)!r}\n"
                            f"   final:        {extract_tip(final_html)!r}"
                        )
                    if extract_sprite(trans_html) != extract_sprite(final_html):
                        failures.append(f"SPRITE MISMATCH {label}")

                    # The rollout fallback: transitional markup on a device
                    # that has the new markup but not yet the texts polling
                    # URL. It must still render the pre-rewrite text rather
                    # than nothing.
                    fb_html, _ = render(
                        env, "shared.transitional.liquid", "views/full.liquid",
                        globals_for(data, None, cfg, "root", day),
                    )
                    fb_tip = extract_tip(fb_html)
                    if not fb_tip:
                        failures.append(f"NO FALLBACK TIP {label}")
                    elif re.search(r"\{[A-Z0-9_]+\}", fb_tip):
                        failures.append(f"FALLBACK UNSUBSTITUTED {label}: {fb_tip!r}")

    print(f"code paths agree: {checked} render pairs ({', '.join(EMBEDDED_LANGS)})")
    print(f"rollout fallback: {checked} renders off the pinned snapshot")

    # ---- every language renders every scenario with nothing left unfilled ----
    smoke = 0
    leftover = re.compile(r"\{[A-Z0-9_]+\}")
    for lang, texts in LANGS.items():
        for sarcasm in ("0", "10", "11"):
            for day in range(4):
                for name, data in SCENARIOS.items():
                    cfg = settings(lang=lang, sarcasm=sarcasm)
                    html, _ = render(
                        env, "shared.liquid", "views/full.liquid",
                        globals_for(data, texts, cfg, "idx", day),
                    )
                    tip = extract_tip(html)
                    smoke += 1
                    label = f"{lang}/{sarcasm}/day{day}/{name}"
                    if not tip:
                        failures.append(f"NO TIP {label}")
                        continue
                    stray = leftover.findall(tip)
                    if stray:
                        failures.append(
                            f"UNSUBSTITUTED {label}: {stray} in {tip!r}"
                        )
                    if "  " in tip or tip != tip.strip():
                        failures.append(f"SPACING {label}: {tip!r}")
                    if " ." in tip or " ," in tip:
                        failures.append(
                            f"DANGLING PUNCTUATION {label}: {tip!r} "
                            "(a placeholder resolved to nothing)"
                        )

    print(f"all languages: {smoke} renders checked ({', '.join(sorted(LANGS))})")

    # ---- degraded states ----
    cfg = settings()
    data = SCENARIOS["warming_out_of_jacket"]

    # final markup, second polling URL has not arrived yet
    html, _ = render(env, "shared.liquid", "views/full.liquid",
                     globals_for(data, None, cfg, "root"))
    if extract_tip(html) not in (None, ""):
        failures.append("final markup without texts should render no tip")
    if "404.png" in html or "<img" not in html:
        failures.append("final markup without texts should still render the sprite")

    # Transitional markup in both payload shapes. The two tips are expected
    # to DIFFER in wording: with IDX_1 present it reads the rewritten text
    # from lang/, without it the pre-rewrite text inlined from the pinned
    # snapshot. What matters is that both are complete sentences, so a device
    # renders properly on either side of the polling-URL update.
    html_idx, _ = render(env, "shared.transitional.liquid", "views/full.liquid",
                         globals_for(data, LANGS["en"], cfg, "idx"))
    html_root, _ = render(env, "shared.transitional.liquid", "views/full.liquid",
                          globals_for(data, None, cfg, "root"))
    for shape, html in (("idx", html_idx), ("root", html_root)):
        tip = extract_tip(html)
        if not tip:
            failures.append(f"transitional markup rendered no tip in {shape} shape")
        elif re.search(r"\{[A-Z0-9_]+\}", tip):
            failures.append(f"transitional/{shape} left a placeholder: {tip!r}")
    if extract_sprite(html_idx) != extract_sprite(html_root):
        failures.append("transitional markup picked different sprites per payload shape")

    # missing weather entirely
    for tmpl in ("shared.liquid", "shared.transitional.liquid"):
        for lang in ("en", "de"):
            ctx = globals_for({}, None, settings(lang=lang), "root")
            html, _ = render(env, tmpl, "views/full.liquid", ctx)
            if "404.png" not in html:
                failures.append(f"{tmpl}/{lang}: error state should use the 404 sprite")
            expected = LANGS[lang]["ui"]["error_short"]
            if expected not in html:
                failures.append(
                    f"{tmpl}/{lang}: error headline missing, expected {expected!r}"
                )

    # future suggestions turned off
    html, _ = render(env, "shared.liquid", "views/full.liquid",
                     globals_for(data, LANGS["en"], settings(future="No"), "idx"))
    if extract_tip(html) not in (None, ""):
        failures.append("show_future_suggestions=No should suppress the tip")

    print("degraded states: 4 checks")

    if failures:
        print(f"\n{len(failures)} FAILURE(S):\n")
        for f in failures[:25]:
            print(f"  {f}")
        if len(failures) > 25:
            print(f"  ... and {len(failures) - 25} more")
        return 1

    print("\nall good: both code paths agree, the rollout fallback renders,\n"
          "and every language fills every scenario cleanly")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
