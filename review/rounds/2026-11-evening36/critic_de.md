# Critic, round 36 (German evening line, level 11, any weather)

Input: `de.written.json`, 21 lines. Kept 4, cut 17, fixed 0. There were 12 slots (`evening.jokes_11.any`), but only 4 lines reach the bar the owner set with the live 11 lines (Zahnseide, Flecken, Punkt Punkt Komma Strich, Kamera). The rest are filler, repeat a premise or carry a fault, so they went even though slots are open.

How each line was checked:

- Read under every tomorrow sentence in `evening.facts` (rain, wet start, snow, snow start, colder, warmer, drier, steady) with {FROM} = „ab 13 Uhr“. The longest sentence is tmr_drier with {DRY}, about 72 characters. The longest kept line, 11, has 75, so the total is about 147, under 165.
- Compared with the live evening and daytime pools, the starred and vetoed lists, the owner's verdicts and edits in rounds `2026-11-*`, the round 35 critic, and the other candidates.
- Weekday lines were judged against the owner's veto of „Sonntag. Da darfst du aussehen, wie du immer aussiehst.“ (not funny): a weekday name plus a general jab about looks does not land.
- The owner's November edits push toward plain spoken German. He also rewrote „Das ist kein Datenschutz, das ist Selbstschutz.“ out of its „kein X, sondern Y“ frame.

Numbers are positions in `de.written.json`.

## Kept

1. „Ich mach das hier nur, weil der Spiegel gekündigt hat.“
   - The best line of the batch. In one short sentence the Grantler is a stand-in who took the job the mirror quit, and the reader works out why. That is cruel about looks without saying „hässlich“.
   - „Gekündigt“ is the dry workplace German the voice is built on. Plain and spoken („mach“).
   - It is true for the screen: its job is telling you how to look tomorrow. It reads under every sentence.
   - Risk: the live Groundhog Day line „Das Murmeltier sieht seinen Schatten und erschrickt. Du kennst das vom Spiegel.“ also uses the mirror. That joke is the reader frightening themselves and shows once a year. This one is the mirror resigning, a different joke.
11. „Ich führ Strichliste, wie oft du gut aussiehst. Der Stift ist noch wie neu.“
    - Specific and confident: the unused pen is a concrete picture of "never". The reader gets there one beat late, which is where the laugh is.
    - It fits a screen that draws. „Strichliste führen“ is everyday German.
    - Risks:
      - Its base, "you never look good", is also the base of the vetoed Sonntag line. The tally image is what that line lacked.
      - The longest kept line (75 characters). It still fits.
12. „Das ist keine schlechte Laune. Das ist meine Meinung über dich.“
    - The most Grantler line here: it turns the screen's whole grumpy act into a verdict on the reader. Worth, not looks, which is fair at 11.
    - Short and plain. It reads under every sentence because it is about the voice, not the weather.
    - Risks:
      - It uses the „Das ist kein X. Das ist Y.“ frame. The owner rewrote that frame out of the camera line, and it is in the vetoed „Das ist keine Meinung, das ist eine Kaltfront.“ He may want it plainer, for example „Ich hab gar keine schlechte Laune. Ich hab nur eine Meinung über dich.“
      - Under the very neutral steady sentences, „schlechte Laune“ answers a tone the bold line doesn't have. That depends on readers knowing the Grantler.
      - This is the round's one "screen's opinion of you" line. Lines 17, 18 and 20 share that premise and were cut for it.
21. „Dein Stil hat einen Namen: Hauptsache angezogen.“
    - Short, cruel and on the app's own subject, clothes. „Hauptsache angezogen“ is a phrase people actually say, used here as a style label.
    - It is a new jab. The live „Bei dem Wetter sieht sogar dein Outfit gewollt aus.“ is about the weather flattering the outfit. „Ich hab dich schon schlechter angezogen gesehen.“ is about yesterday.
    - Risks:
      - „Dein Stil hat einen Namen:“ is a little written. The owner may prefer „Dein Stil heißt: Hauptsache angezogen.“
      - The daytime pools already use „Hauptsache, …“ twice („Hauptsache, man hat was zum Meckern.“), with a different meaning.

## Cut

2. „Ich bin ein Kasten. Und trotzdem der Hübschere von uns beiden.“
   - Same premise as the live „Schönes Wetter. Endlich mal was in deiner Nähe, das gut aussieht.“ (the thing next to you looks better), and the Kürbis and Ostereier lines.
   - Vanity is the English screen's trait. The Grantler doesn't call himself „hübsch“.
3. „Ich helf dir jeden Abend beim Anziehen. Andere kriegen dafür einen Pflegegrad.“
   - The closest cut. „Pflegegrad“ is a sharp, very German punch.
   - But the premise was vetoed in round 2026-11-evening: „Ich mach diese Vorschau extra für dich. Andere Leute wissen auch so, was sie anziehen.“ That line is the same idea (you need the screen to dress, others don't).
   - It is also on worth, not looks. If the owner thinks their veto was about the wording and not the idea, this is the line to bring back.
4. `{D:3}` „Mittwoch ist Bergfest. Bei dir ging's schon viel früher bergab.“
   - A pun on the idiom (Bergfest/bergab) with a generic "you're in decline" jab. It is no stronger than the vetoed Sonntag line.
   - The vetoed „Längster Tag des Jahres. Ab morgen geht's wieder bergab.“ already used „bergab“.
5. `{D:2}` „Dienstag. Den merkt sich keiner. Ihr zwei passt gut zusammen.“
   - "You're forgettable" is mild for 11. Weekday plus jab is the Sonntag pattern the owner found not funny.
   - „Ihr zwei“ for a reader and a weekday reads a little constructed.
6. `{D:6}` „Samstag. Ausgehen könntest du schon. Nur reinlassen würd dich keiner.“
   - A close call. The bouncer gives it a picture the Sonntag line lacked.
   - But a Türsteher turning someone away is a stock insult, and it implies plans for Saturday night.
   - The live „Draußen passiert nichts. Kennst du ja von deinen Samstagen.“ already mocks the reader's Saturdays.
7. „Träum was Schönes. Zum Beispiel, dass du gut aussiehst.“
   - It assumes the reader is going to bed, and the evening is not necessarily bedtime.
   - Close to live dream and sleep lines („Das Meer träumt sicher nicht von dir.“, „Schönheitsschlaf ist um die Uhrzeit sowieso nur noch Schadensbegrenzung.“).
   - The „Zum Beispiel“ tail is stock.
8. „Hingucker bist du keiner. Eher so ein Weggucker.“
   - A close call. It is short and natural, but „Weggucker“ is a known Kalauer.
   - The jab ("you're ugly") is as general as the vetoed Sonntag line, with nothing from the screen in it.
9. „Falls ich mal was Nettes über dich sag, ist das ein Bug.“
   - Mandatory cut. It tells nearly the same joke as a live line in the other language (no compliment will ever come), and the two languages must never tell the same joke.
   - It is also close to the vetoed „… und ich kann endlich mal was Nettes sagen. Fast.“
10. „Man sieht, dass du dir Mühe gibst. Mehr sieht man leider nicht.“
    - A neat backhander, but the same premise and tail as the live „Mehr anziehen kannst du. Mehr hermachen leider nicht.“ (more effort, no better look, „… leider nicht.“).
    - The „Mühe“ jab is also live („Das Wetter gibt sich heute mehr Mühe als du.“).
11. (kept)
12. (kept)
13. „Ich bin kein Touchscreen. Nimm deine Chipsfinger da weg.“
    - The chips are an assumption about the reader.
    - It undercuts itself: a screen without touch can't feel the fingers it complains about.
    - „Finger weg …“ lines are live twice (Kühlschrank, Warenkorb).
14. „Hochauflösend bin ich nicht. Bei dir ist das reine Rücksicht.“
    - Same premise as the live „Punkt, Punkt, Komma, Strich. Mehr hab ich für dein Gesicht nicht gebraucht.“ (the screen's picture of you) and the live "better unseen" lines („Die Leute haben's ganz gut ausgehalten ohne.“, „Im Schneetreiben hat man dich wenigstens nicht so genau gesehen.“).
15. „Falls du heute noch eine Gesichtsmaske machst: Lass sie ruhig drauf.“
    - The face mask is an assumption about the reader's evening.
    - "You look better covered" is live („Dann sieht man wieder dein Gesicht. Die Leute haben's ganz gut ausgehalten ohne.“).
    - It is the third „Falls …“ opener in the batch.
16. „In Jogginghose mal ich dich nie. Ein bisschen Kontrolle soll dir bleiben.“
    - The joke depends on the Lagerfeld quote. Without it, „Kontrolle“ is unclear on first read.
    - It assumes sweatpants habits, and the vetoed „… Nur in Jogginghose.“ already went there.
17. „Ich kenn kaum Menschen. Trotzdem bist du nicht mein Lieblingsmensch.“
    - Soft for 11.
    - „Lieblingsmensch“ is a pop-song buzzword, not the Grantler.
    - Same premise as kept 12 (the screen's opinion of you), and weaker.
18. „Vor dir war ich ein ganz freundlicher Bildschirm.“
    - Short and plain, a close call.
    - It shares kept line 12's premise (you are the reason for the grump), and line 12 is sharper.
    - "Knowing you sours people" is near the vetoed „Wie bei allen, die dich näher kennenlernen.“
19. „Beim Wetter lieg ich selten daneben. Bei dir schon: Ich hatte mehr erwartet.“
    - It is built on "the screen is always right", a dead smug-screen idea.
    - The setup is long and „Ich hatte mehr erwartet“ is a stock tail.
    - The vetoed „Das Wetter kann sich über Nacht noch ändern. Bei dir rechne ich nicht damit.“ uses the same weather-versus-you frame.
20. „Falls du was an dir ändern willst: Ich hätt da eine Liste.“
    - "I have a list" is a stock comeback, and the vetoed lines already gave the Grantler lists (Krampus, „Liste mit Beschwerden“).
    - Same premise as kept 12 (the screen's opinion of you).
    - With 11 it would make two lists in one pool.

## By slot

| Slot | Target | Kept |
|---|---|---|
| 11.any | 12 | 4 (1, 11, 12, 21) |

No typo or punctuation fixes were needed. The kept lines are copied unchanged into `de.json` with their (empty) evtag. None of the weekday lines were kept.
