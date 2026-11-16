# Critic, round 31 (German evening line)

Input: `de.written.json`, 30 lines. Kept 8, cut 22, fixed 0. Every line was read under every tomorrow sentence of its pool (`any` lines under all of them, with {FROM} = „ab 13 Uhr“). Lines were checked against the live evening and daytime pools, the starred and vetoed lists, round 30's verdicts and each other. Numbers are positions in `de.written.json`.

## Cut

1. `10.any` „Falls morgen früh alles anders aussieht: Ich war's nicht. Ich hab nur gemalt.“: repeats the live starred overnight-change line („Ändert sich das doch noch, mal ich's heimlich um …“). The "not my fault, I only pass it on" disclaimer is also live („Ich geb die Infos nur weiter“) and was vetoed twice („Diese Vorschau ist unverbindlich“, „alle Angaben ohne Gewähr“). „alles anders aussieht“ is also unclear.
2. `10.any` „Nach mir zeigt der Bildschirm wieder was anderes. Ab da bist du wettermäßig auf dich allein gestellt.“: too long. At 101 characters it reaches 173 under the longest sentences it can sit under (tmr_drier, tmr_rain), over the 165 budget. The line also leans on the vetoed smug-screen move (you're lost without me).
3. `10.any` „Über morgen hab ich mich schon ausgiebig aufgeregt. Jetzt ist erst mal Feierabend.“: the same joke as the live „Ich meckere heute schon mal vor. Morgen reicht dann ein Seufzer.“ (grumbling done in advance, then rest). The screen's „Feierabend“ is live too („Eigentlich hab ich schon Feierabend.“, „Feierabend. Jetzt lass mich in Ruhe.“).
4. `10.any` „Ich hab nach einem anderen Morgen gefragt. Umtausch erst nach Gebrauch.“: the live „Ich hab mich bei den Wettergöttern schon beschwert. Zu kurzfristig, hieß es.“ with a different service-desk brush-off. The frame is the same ("I asked to change tomorrow" + a policy refusal). It is also the same joke as English (see flags).
5. `10.any` „Muss das sein? Offenbar ja.“: reads wrong under the steady and warmer sentences. A protest after „Das Outfit für morgen passt den ganzen Tag.“ or „… dann reicht was Leichteres.“ makes no sense. It is also the same resigned shrug as 6, which works everywhere.
7. `11.any {P}` „Links du heute, rechts du morgen. Ich hab mir bei beiden Mühe gegeben. Sieht man nicht, ich weiß.“: too long. It has three sentences, and at 97 characters it reaches 169 under the longest sentences, before today's line is put in front on evenings when tonight still changes. It is also the same joke as English (see flags).
9. `11.any` „Ich meckere heute über morgen. Über dich meckere ich das ganze Jahr.“: the setup is the live „Ich meckere heute schon mal vor“, and the twist is a generic jab with nothing specific in it. That is the kind of 11 the owner vetoes („Verderben kann den Abend jetzt nur noch einer. Du.“).
10. `10.rain` „Der Regen geht heut früh ins Bett. Morgen will er gründlich sein.“: „heut(e) früh“ reads as "this morning" in standard German. The line is whimsical rather than sarcastic, when the owner asked for more sarcasm in this direction. „gründlich“ claims a heavy rain the forecast doesn't give. It is also the round 30 English sample ("tomorrow's rain is getting an early night. Big day ahead") in German.
11. `10.rain {T}` „Der Regen hat sich sogar mit Uhrzeit angekündigt. Höflich ist er ja, das muss man ihm lassen.“: the same joke as 22 (the rain gives a time, so it has manners). 22 is the tighter telling and needs no tag.
12. `11.rain` „Nach dem Regen siehst du wenigstens frisch gewaschen aus. Fürs Erste.“: the rain as the reader's wash is live („Zwei Duschen an einem Tag. Für deine Verhältnisse ist das schon Körperpflege.“, „Regen ist gut für die Haut …“). It predicts the reader getting soaked right under „denk an den Schirm“, and „Fürs Erste“ muddles the punch.
14. `10.snow` „Schnee. Na dann.“: an echo of the sentence's last word plus a neutral shrug. „Na dann“ isn't a grumble. The owner pushed this format toward sarcasm (EN „Marvelous. Truly.“ became "Just what we needed."), and „Auch das noch.“ already covers snow.
15. `11.snow` „Im Schnee sieht jeder ein bisschen besser aus. Fast jeder.“: the mirror of the starred live „Nass sieht jeder ein bisschen erbärmlich aus. Du hast da einen Vorsprung.“ (same frame, same "except you" turn). „Fast jeder“ is a stock twist.
17. `10.colder` „Kälter. War ja klar.“: the live frame word for word („Schon wieder Regen. War ja klar.“, starred „Nass ist's. War ja klar.“). It is also the same joke as English (see flags).
18. `11.colder` „Eine Schicht mehr. Dann machst du wenigstens was her.“: vetoed in round 29 as „Mit einer Schicht mehr hast du endlich mal Schultern.“. Also live as „Mehr anziehen kannst du. Mehr hermachen leider nicht.“ and „In mehr Schichten wirkst du fast kräftig. Von Weitem.“
19. `10.warmer` „Wärmer. Ich find schon noch was zum Meckern.“: live as „Nichts zu meckern. Ich hab trotzdem schon mal einen Zettel angefangen.“ (plus „Heute gibt's nichts auszusetzen. Das ärgert mich.“, „Heute kann ich also nicht meckern …“).
20. `10.warmer` „Weniger Schichten zu malen. Endlich mal ein ruhiger Tag für mich.“: live as „Das letzte Bild ging am schnellsten. Weniger Stoff, weniger Arbeit.“ It is also the same joke as English (see flags). It is wrong too when warmer means T-shirt to shorts, which is no layer at all.
21. `11.warmer` „Wärmer morgen. Weniger anziehen musst du trotzdem nicht. Glaub mir.“: "less clothing shows more of you" is heavily live (warming, w_jacket, w_coat and shorts lines). The setup restates the sentence, and it contradicts „dann reicht was Leichteres“.
23. `10.drier` „Erst nass, dann trocken. Entscheid dich halt.“: the live frame „Erst zu warm, dann zu kalt. Hauptsache …“ with the live idea of a weather that can't decide („So ein Hin und Her hält ja kein Mensch aus.“). Rain stopping isn't indecision. Under sentences that address „du“, „Entscheid dich halt.“ also reads as an order to the reader at On.
24. `11.drier` „Erst nass, dann trocken. Deine Frisur kommt da so schnell nicht hinterher.“: the hair-after-rain joke is live in this exact situation (units_11.p_drier: „Für deine Frisur ist's sowieso zu spät.“). It predicts the reader getting soaked and reuses 23's setup.
26. `10.steady` „Ein Outfit für den ganzen Tag. Mehr Komfort gibt's bei mir nicht.“: under „Morgen passt ein Outfit für den ganzen Tag.“ the setup repeats the sentence word for word. „Komfort“ is unclear, and „Mehr X gibt's (bei mir) nicht“ is a live frame („Mehr gute Nachrichten gibt's heute nicht.“).
27. `11.steady` „Ein Outfit für den ganzen Tag. Das ist mehr Beständigkeit, als du sonst so hinkriegst.“: the dead idea "finally someone commits: the weather" (vetoed „Endlich legt sich mal einer fest. Ausgerechnet das Wetter.“). Also live as „Einmal entscheiden und durchziehen. Das Wetter kann's. Du musst noch üben.“ The setup restates the sentence.
28. `10.any {D:1}` „Montag. Da ist das Wetter noch das kleinere Übel.“: too close to the vetoed „Montag. Das Wetter kann nichts dafür. Ich auch nicht.“ (Monday, the weather isn't the problem). 29 does the owner's "Monday makes life miserable" note better.

## Kept

6. `10.any` „Na gut. Wenn's sein muss.“: the approved sigh format, and unlike 5 it fits every pool. Grudging under bad news, and the Grantler grudging even good news under steady or warmer.
8. `11.any` „Das Wetter kann sich über Nacht noch ändern. Bei dir rechne ich nicht damit.“: true under every sentence, confident and cruel. It turns the starred overnight-change direction on the reader.
13. `10.snow` „Schnee. Und ich darf wieder jede Flocke einzeln malen.“: a specific complaint about the screen's own job, and true: the snow drawing has flakes. The opposite claim to the daytime „Heute brauch ich kaum schwarze Pixel“, but a different joke.
16. `10.colder` „Die Kälte zieht morgen ein. Miete zahlt sie natürlich keine.“: builds on the owner's own edit („… zieht sie bei dir ein“) with the sarcasm he asked for. The cold is a freeloading flatmate (and you pay the heating). „Die Kälte“ is season-neutral by the brief.
22. `10.drier` „Der Regen sagt sogar, wann er geht. Manieren hat er.“: the appointments direction with ironic praise, short and dry. Every drier sentence names the time it refers to.
25. `10.steady` „Es tut sich nichts. Ich mal dann halt ein bisschen Hintergrund, damit's nach Arbeit aussieht.“: the owner's own suggestion for the bored illustrator, carried out. The screen faking busywork is new, and it's idiomatic.
29. `10.rain {D:1}` „Montag und Regen. Der Montag lässt wirklich nichts aus.“: the owner's note for the weekday direction ("Monday trying its best to make life miserable", lighter at On) in idiomatic German. It reads under both rain and wet-start sentences.
30. `10.steady {D:6}` „Samstag, und das Wetter spielt mit. Kommt selten genug vor.“: the everyday grumble that good weekend weather is rare. „Spielt mit“ holds on any steady day, because steady is always dry.

## Flags: the same joke as an English line (`en.written.json`)

- Kept 6 „Na gut. Wenn's sein muss.“ = EN `10.any` "Fine. I suppose." (the same shrug).
- Kept 8 „Das Wetter kann sich über Nacht noch ändern. Bei dir rechne ich nicht damit.“ = EN `11.any` "If the forecast changes overnight, I'll redraw it. You, I can't fix."
- Kept 25 „… ein bisschen Hintergrund, damit's nach Arbeit aussieht.“ = EN `10.steady` "… I may draw a few houses in the background. For morale." (both follow the owner's note).
- Kept 29 „Montag und Regen. Der Montag lässt wirklich nichts aus.“ ≈ EN `10.any {D:1}` "Monday tomorrow. The weather is just helping." (Monday and the weather piling on).
- Kept 30 „Samstag, und das Wetter spielt mit. Kommt selten genug vor.“ ≈ EN `10.colder {D:6}` "Saturday and colder. Somebody had plans." (weekend weather against plans). The live EN "{D:6}Rain on a Saturday. Great." is the same idea.
- Cut anyway, for the record: 1 ≈ EN "I'll check again at midnight. If it's changed, this conversation never happened."; 3 ≈ "I've already sighed about tomorrow twice. Pacing myself."; 4 = "I asked for a different tomorrow. This was the only one in stock."; 7 = "Current you, future you. Neither one's my best work."; 9 ≈ "I've got two complaints about tomorrow. The weather's the second one."; 17 = "Colder. Of course."; 20 = "Fewer layers to draw tomorrow. I won't pretend I'm not relieved."

## By pool

| Pool | On kept | 11 kept |
|---|---|---|
| any | 1 (6) | 1 (8) |
| rain | 1 (29, Monday only) | 0 |
| snow | 1 (13) | 0 |
| colder | 1 (16) | 0 |
| warmer | 0 | 0 |
| drier | 1 (22) | 0 |
| steady | 2 (25, 30 Saturday only) | 0 |

None of the six weather-specific 11 lines survived. Each repeated a live or vetoed jab about the reader's looks, or the dead "the weather commits more than you". The weather-specific 11 pools and the warmer pool get nothing new from this round.
