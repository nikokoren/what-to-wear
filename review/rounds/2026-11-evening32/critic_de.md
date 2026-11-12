# Critic, round 32 (German evening line, top-up)

Input: `de.written.json`, 13 lines. Kept 0, cut 13, fixed 0. Targets allowed up to 8 (11.any 3, 11.rain 1, 11.colder 1, 11.steady 1, 10.warmer 2). Each line was read under every tomorrow sentence of its pool (rain = tmr_rain + tmr_wet, colder = tmr_colder, warmer = tmr_warmer, steady = tmr_steady, `any` under all of them, {FROM} = „ab 13 Uhr“). Lines were checked against the live evening and daytime pools, the starred and vetoed lists, the owner's evening verdicts (rounds evening, evening2, ideas, evening31) and each other. The owner vetoed both 11/any-style lines round 31's critic kept, so the bar here is his and not the critic's. Numbers are positions in `de.written.json`.

## Cut

1. `11.any` „Für morgen hab ich dir was Vernünftiges hingemalt. Zur Abwechslung.“: the closest call. The joke is "for once you'll be dressed sensibly", which is live (now_11.cool „Heut bist du mal passend angezogen. Am Rest arbeiten wir noch.“) and was vetoed in this very slot („Schön, dass du dir mal Gedanken um deine Kleidung machst. Gemerkt hat man's bisher nicht.“, plus „Mit Schirm siehst du richtig vernünftig aus. Leider nur gemalt.“). The screen draws the outfit every evening, so „Zur Abwechslung“ can also read as the screen admitting its own drawings are usually nonsense, which blunts the jab.
2. `11.any` „Das Wetter für morgen ist geklärt. Bei dir bleiben Fragen offen.“: the vetoed frame "the weather's settled, you aren't". The owner vetoed it three times: round 31 „Das Wetter kann sich über Nacht noch ändern. Bei dir rechne ich nicht damit.“, „Gilt für die Kleidung. Für den Rest von dir übernehm ich keine Garantie.“ and „Die Sachen halten also durch. Bei dir bin ich mir nicht so sicher.“ „Fragen offen“ is a vague jab with nothing specific in it, and „Das Wetter ist geklärt“ sounds like officialese, not like something a person says. It is also the same joke as English (see flags).
3. `11.any` „Ich hab mir für morgen viel Mühe gegeben. Beim Wetter hat's geholfen.“: reads wrong under rain, wet-start, snow and colder. If the screen's effort "helped" the weather, the rain at 13 Uhr contradicts it. The jab at the reader is only implied ("…but not with you"), which is thin for 11. The weather-tried-harder-than-you idea is live too (units_11.steady_evening „Das Wetter gibt sich heute mehr Mühe als du.“). Also similar to English (see flags).
4. `11.rain` „Unterm Schirm sieht man morgen nur die Hälfte von dir. Reicht ja auch.“: the starred, live flavour_vf_11.wet „Unterm Schirm erkennt dich wenigstens keiner.“ with a different measurement. Same umbrella, same "being hidden is a mercy" turn.
5. `11.rain` „Bei Regen schaut jeder auf den Boden. Gute Nachricht für dich.“: the same idea as 4 and as the live umbrella line (in the rain nobody sees you, lucky you). The covered-up-is-better jab is also live as now_11.cold „Dick eingepackt gefällst du mir am besten. Man sieht weniger.“
6. `11.colder` „Mit Schal bis zur Nase sieht man morgen nur deine Augen. Das ist ein Fortschritt.“: reads wrong under part of its pool. Colder covers T-shirt-to-sweater days, with no scarf anywhere. The joke is live several times over: now_11.cold „Dick eingepackt … Man sieht weniger.“, units_11.c_scarf „Dann siehst du aus wie ein Bankräuber. Steht dir.“ and units_11.w_scarf „Dann sieht man wieder dein Gesicht. Die Leute haben's ganz gut ausgehalten ohne.“ „Das ist ein Fortschritt“ explains the punch.
7. `11.colder` „Mit Mütze siehst du morgen fast sympathisch aus.“: the best German in the batch, short and cruel, but it fails the pool. A hat isn't guaranteed when colder means T-shirt to sweater (and a „Mütze“ in the line would contradict the drawing). Swapping the garment would be a rewrite. The idea "you look better covered up" is also live (now_11.cold, and the hat version reversed in units_11.p_drier_snow „… Du siehst darunter eh nicht besser aus.“).
8. `11.steady` „Den ganzen Tag dasselbe Outfit. Da haben alle genug Zeit, es sich anzuschauen.“: the setup restates the sentence above („Das Outfit für morgen passt den ganzen Tag.“), and the twist only works with that restatement. The jab is oblique: the reader has to infer that the outfit is ugly. „alle“ also assumes onlookers the screen can't know about. It is the same joke as English (see flags).
9. `11.steady` „Ein Outfit für den ganzen Tag. Wähl's mit Bedacht. Ach, wem sag ich das.“: the setup repeats the sentence (word for word under „Morgen passt ein Outfit für den ganzen Tag.“, the reason round 31 cut its steady 26). „Ach, wem sag ich das“ is the idiom for "you know that best yourself" (cf. „Wem sagst du das!“), so the intended put-down flips into agreement. „Wähl's mit Bedacht“ also ignores that the screen has already drawn the outfit. Similar to English too (see flags).
10. `10.warmer` „Wärmer morgen. Ich mal die Leute dann wieder mit weniger Stoff. Spart Farbe.“: this is live as flavour_vf_10.warming „Das letzte Bild ging am schnellsten. Weniger Stoff, weniger Arbeit.“, and round 31 cut its warmer 20 for exactly this. „Wärmer morgen.“ restates the sentence (and is English word order, see the note under the flags). „die Leute“ is wrong because the screen draws one figure. „Spart Farbe“ makes no sense on a black-and-white e-ink screen. „Ich mal die Leute … mit weniger Stoff“ is clumsy German.
11. `10.warmer` „Wärmer morgen. Ich trau dem Frieden noch nicht.“: a vetoed line almost word for word („Schönes Wetter. Ich trau dem Frieden nicht.“). Distrust of good weather was vetoed four more times („Ich trau dem schönen Wetter auch nicht.“, „Mild, ruhig, alles gut. Verdächtig.“, „Fast verdächtig.“, „Ich hab extra nach einem Haken gesucht …“). The setup restates the sentence. Same joke as English (see flags).
12. `10.warmer` „Wärmer. Da muss ja irgendwo ein Haken sein.“: the same dead idea as 11 (vetoed „Ich hab extra nach einem Haken gesucht. Es gibt keinen. Ärgerlich.“), and a duplicate of 11 within the batch. „Wärmer.“ restates the sentence.
13. `10.warmer` „Wärmer morgen. Na, wer sagt's denn.“: a stock exclamation with no twist, the kind of line the owner vetoed in round 31 („Na gut. Wenn's sein muss.“). It is pleased rather than sarcastic, and when warmer means heat the Grantler cheering reads wrong. The setup restates the sentence.

## Kept

None. Every candidate either repeats a live, starred or vetoed idea, breaks its pool, or restates the sentence above. 1 and 7 come closest (the screen as illustrator, and a short, confident 11), but each fails on its own terms (see above). No spelling or grammar fixes were made because nothing was kept.

## Flags: the same joke as an English line (`en.written.json`)

No kept lines, so nothing to flag for the vote. For the record, the cut lines that tell the English joke:

- 2 = EN `11.any` "Weather-wise, it'll be fine. I can't speak for the rest of you." (and ≈ "The outfit for tomorrow is sorted. Your face is a separate project."): the forecast's settled, you aren't.
- 3 ≈ EN `11.any` "I've planned tomorrow's outfit down to the hour. Your hair still has a mind of its own.": my effort covered tomorrow, not you.
- 8 = EN `11.steady` "The same outfit from morning to night. Bold, given the outfit.": a whole day in it, and the outfit is the problem.
- 9 ≈ EN `11.steady` "A one-outfit day. Even you can't get that wrong. Probably.": one outfit, and you'll still blow it.
- 11, 12 ≈ EN `10.warmer` "Warmer tomorrow. Don't get attached.": don't trust the warmth.
- 13 ≈ EN `10.warmer` "Warmer. Don't tell the weather I said this, but thanks.": grudging approval.
- A note on the frame: all four German warmer lines open the way the English ones do („Wärmer (morgen).“ = "Warmer (tomorrow)."), and 9 opens like EN "A one-outfit day." („Ein Outfit für den ganzen Tag.“). „Wärmer morgen.“ is English word order. A German speaker would say „Morgen also wärmer.“, or just react. This batch reads as if it was written with the English open (BRIEF: "Write it without the English open").

## By slot

| Slot | Target | Kept |
|---|---|---|
| 11.any | 3 | 0 |
| 11.rain | 1 | 0 |
| 11.colder | 1 | 0 |
| 11.steady | 1 | 0 |
| 10.warmer | 2 | 0 |
| **All** | **8** | **0** |

`de.json` is written as `{"lines": []}` on purpose. Without it, `make_round32.py` would fall back to `de.written.json` and put the cut lines on the review page.
