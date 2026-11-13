# Critic, round 35 (German evening line, any weather)

Input: `de.written.json`, 18 lines. Kept 6, cut 12, fixed 0. Targets allowed up to 14 (10.any 7, 11.any 7). Kept: 10.any 4 (one Monday only), 11.any 2 (one Sunday only). The bar is round 34, the round the owner called good: the two starred lines and the two kept 11 lines. Filler went, even with slots open.

How each line was checked:

- Read under every tomorrow sentence in `evening.facts` (rain, wet start, snow, snow start, colder, warmer, drier, steady) with {FROM} = „ab 13 Uhr“.
- Length: the longest total is line 7, about 145 characters under the longest sentence (tmr_drier, about 72). Every line fits.
- Compared with the live evening and daytime pools, the starred and vetoed lists, the owner's November verdicts and edits, the critic of round 34, and each other.
- Screen facts: the weekday tag is abbreviated („Morgen · Mo“, `evening.days`). The view ends at midnight. The screen has no camera and shows no colour.

Sprite check (`build/review/sprites/`). I opened jacket_rain, sweater_dry and heat_dry. Every face is two dot eyes, a nose dash and a flat mouth line, all with the same blank look. On hot days, sunglasses cover the eyes and the mouth turns up slightly.

Numbers are positions in `de.written.json`.

## Kept

1. `10.any {D:1}` „„Mo“. Mehr Buchstaben ist mir der Montag nicht wert.“
   - It reacts to something that really is on screen, the „Morgen · Mo“ tag. The Grantler pretends the short form is contempt.
   - The reader sees „Fr“ and „Sa“ too, so the claim is plainly a grumpy pose. That is the joke, and it isn't a false fact.
   - It is natural spoken German, with the object first.
   - It is about the day, not the reader, so it fits On.
   - Risks:
     - The owner vetoed a run of generic „Montag. …“ daytime lines. This one has a screen hook those lacked, and it doesn't open with „Montag.“
     - The live rain line „Der Montag lässt wirklich nichts aus.“ is also {D:1}. It is a different joke (Monday piles on), but both could show on a rainy Monday evening on different nights.
3. `10.any {S}` „Ein Ausrufezeichen hat sich das Wetter bei mir noch nie verdient.“
   - It points at the bold sentence and its plain full stop. The Grantler has never been impressed by any weather, good or bad, so it reads under every sentence.
   - This is the starred „höfliche Version“ direction (the screen on how it words the sentence) with a different joke: refusing enthusiasm, not holding back an insult.
   - Pure Grantler: short, dry, no wordplay, no restatement.
   - Risk: not strictly true. Two daytime ice facts open with „Achtung, Glatteis!“ and „Vorsicht, Glatteis!“. On an evening when freezing rain still ends tonight, today's line can precede tomorrow's sentence on the evening screen. That case is rare. The owner may want the line anyway, or may want to drop those two „!“.
5. `10.any` „Meine Figuren haben alle denselben Gesichtsausdruck. Meinen.“
   - True to the sprites: one blank face with a flat mouth (see the sprite check). The one-word turn „Meinen.“ claims the blank grump as a self-portrait. It is confident and fast.
   - It belongs to the drawing direction the owner keeps at On (the starred Hagel and „heimlich um“ lines, Hintergrund, Flocken).
   - At On it is about the screen, not the reader.
   - Risks:
     - The live 11 line „Punkt, Punkt, Komma, Strich …“ is also about the drawn face. That joke is the reader's plain features; this one is the screen's mood, a different premise on a different level.
     - On hot days the sunglasses and the slight smile make „alle“ a little loose.
7. `10.any` „Irgendwer freut sich auf genau dieses Wetter. Den möcht ich nicht kennen.“
   - Classic Grantler misanthropy, aimed at other people and not the reader. „Genau dieses Wetter“ ties it to the sentence above, whatever it says. That makes it funnier under bad weather (rain lovers) and just as grumpy under good weather.
   - Natural spoken German („möcht“, „Den“ first).
   - New: the live people lines quote others („Ist doch herrlich draußen!“, „So warm hätt's …“). None is the screen refusing to know them.
   - Risk: it is the most generic keep, since it reacts to the sentence rather than to a picture or tag. Round 34 cut „Das Wetter hat sich noch nie krankgemeldet.“ for being generic. This one at least points at tomorrow's weather.
11. `11.any` „Kamera hab ich keine. Das ist kein Datenschutz, das ist Selbstschutz.“
    - True for the device, and the most German line of the batch: Datenschutz is a national reflex, and the compound pair carries the jab (I'd rather not see you). Short, confident, a little cruel: the 11 the owner asks for.
    - It reacts to the screen itself and reads under every sentence.
    - Risks:
      - Elsewhere the 11 voice pretends to see the reader, including in this pool („Jetzt zu den Flecken an deinem T-Shirt.“, „Ich hab dich schon nass gesehen.“). This line admits it can't. Readers may take that as a wink, or the owner may find it breaks the pose.
      - „Das ist kein X, das ist Y“ is a familiar frame. Here the second word does the work.
13. `11.any {D:0}` „Sonntag. Da darfst du aussehen, wie du immer aussiehst.“
    - It reacts to the „Morgen · So“ tag and names the day in the line, like the starred „Freitag. …“.
    - The jab is about looks, and it is specific: your normal is everyone else's Sunday slob. It assumes nothing about the reader's plans.
    - Plain, natural German.
    - Risk: "you always look bad" is a common 11 base („Fertig aussehen tust du schon länger“). The Sunday licence is what makes it new.

## Cut

2. `10.any {D:0}` „Sonntag. Alles hat zu, nur das Wetter hat wie immer geöffnet.“
   - Pleasant observation, not sarcasm: there is no Grantler bite, and „wie immer“ pads the line.
   - Shops closing on Sunday is a stock remark.
   - Kept line 13 already uses the Sunday tag.
4. `10.any {P}` „Die Nacht dazwischen spar ich mir. Wär eh nur ein schwarzes Bild.“
   - It answers a gap no reader has noticed, which is a setup the screen doesn't give.
   - „Schwarzes Bild“ isn't how the screen draws: it draws figures, not skies.
   - Lazy-screen self-pity with no snap.
6. `10.any {S}` „Fett gedruckt, weil's sonst wieder keiner glaubt.“
   - It plays on the forecast being disbelieved and the screen being right. That is near the dead "always right / everyone checks me" smugness and the vetoed „Wer hätte das ahnen können? Ich, zum Beispiel.“
   - It is a third line about the sentence's form, after the live „höfliche Version“ and kept line 3. Line 3 is the stronger of the two new ones.
8. `10.any` „Früher hat das ein Wetterhäuschen gemacht. Aus Holz und ohne Kommentar.“
   - Old ways against the screen was vetoed („Früher hat man dafür aus dem Fenster geschaut.“).
   - The punch praises the predecessor and pokes at the screen's own talking. That is wry, not grumpy.
9. `10.any {P}` „Links heute, rechts morgen. Politisch ist das nicht gemeint.“
   - A pun on the layout's words and a stock Kabarett disclaimer.
   - It brings politics onto a kitchen screen every few weeks for a year.
   - It restates the layout before the joke.
10. `10.any` „Um Mitternacht ist der Zauber vorbei. Aschenputtel durfte wenigstens tanzen.“
    - The midnight switch is true, but the reader doesn't know it. „Der Zauber“ is unclear on first read: what magic, on a weather screen?
    - Needs a setup the screen doesn't give, as with the Omas veto.
12. `11.any` „Auf 11 hast du mich selbst gestellt. Selbstachtung sieht anders aus.“
    - Mandatory cut: it tells the same joke as a live line in the other language (the reader chose level 11 themselves), and the project never lets the two languages tell the same joke.
14. `11.any {S}` „Für jemand Wichtigeren hätt ich mir bei dem Satz mehr Mühe gegeben.“
    - Same premise as the live „Ich hab's für dich extra einfach formuliert.“ (and „… extra simpel formuliert.“ as a unit): the sentence is plain because of the reader.
15. `11.any` „Wie du heißt, weiß ich gar nicht. Gefragt hab ich auch nie.“
    - The closest 11 cut. It's true and cold, but the jab is only implied. It is not about looks, nor specific, and it lands softly („gar nicht“, „auch nie“) next to the bar of Punkt, Punkt and Flecken.
16. `11.any` „Farbe kann ich nicht. Bei deinem Geschmack ist das ein Segen.“
    - The screen's missing colour was vetoed twice („Ich hab nicht mal Farbe.“, „… schwarzweiß wie ich …“) and is live as „Mein Weihnachtswunsch: ein bisschen Farbe.“
    - Not true for the screen: it draws its own outfit, never the reader's clothes, so the reader's taste never reaches it.
    - „Bei deinem Geschmack“ is a stock tail.
17. `11.any` „Eingerichtet hast du mich ganz allein. Hätt ich dir nicht zugetraut.“
    - Something the screen can't know: in a household, the one reading may not be the one who set it up.
    - Setup was months ago, so there is no reason to say it tonight.
    - The backhanded compliment is mild.
18. `11.any` „Abends schon das Wetter für morgen studieren. Fehlt nur noch die Strickweste.“
    - It mocks the reader for doing the very thing the evening screen exists for. That is close to the vetoed „Ich mach diese Vorschau extra für dich. Andere Leute wissen auch so, was sie anziehen.“
    - It assumes the reader "studies" a screen they pass.
    - „Strickweste“ is less idiomatic than the usual Strickjacke.
    - The verbless infinitive opener reads like a note.

## By slot

| Slot | Target | Kept |
|---|---|---|
| 10.any | 7 | 4 (1 Monday only, 3, 5, 7) |
| 11.any | 7 | 2 (11, 13 Sunday only) |
| **All** | **14** | **6** |

No typo or punctuation fixes were needed. The kept lines are copied unchanged into `de.json` with their evtag.
