# Critic, round 33 (German evening line, top-up)

Input: `de.written.json`, 14 lines. Kept 3, cut 11, fixed 0. Targets allowed up to 8 (11.any 3, 11.rain 1, 11.colder 1, 11.steady 1, 10.warmer 2).

How each line was checked:

- Read under every sentence of its pool: rain = tmr_rain + tmr_wet, colder = tmr_colder, warmer = tmr_warmer, steady = tmr_steady, and `any` under all eight lists (the any lines join every kind of tomorrow, snow and drier included). {FROM} = „ab 13 Uhr“.
- Length: every line fits the 165-character budget. The longest total is 4, at 153.
- Compared with the live evening and daytime pools, the starred and vetoed lists, the owner's November verdicts, the critics of rounds 31 and 32, and each other.

Numbers are positions in `de.written.json`.

## Kept

2. `11.any` „Mich schaust du dir jeden Abend an. Die Zahnseide nie.“
   - Why kept: it is specific, a little gross and short. It hangs on the evening habit of checking this screen (the any pool is the screen's own evening), so it doesn't read as a "random sentence … from your weather app".
   - The German: „etwas nicht mal anschauen“ is the everyday idiom for ignoring something, and the ellipsis carries it.
   - Not a repeat: the live hygiene jab (units_11.p_wet_again „Zwei Duschen an einem Tag. Für deine Verhältnisse ist das schon Körperpflege.“) is about rain as a shower. This one is about priorities: the screen gets looked at, the teeth don't.
   - It has no weather in it, so it reads under every sentence. Risk: it reacts to the evening check, not to tomorrow.
7. `11.rain` „An manchen sieht ein Schirm elegant aus. An dir wie geklaut.“
   - Fits the pool: every rain and wet-start sentence names the umbrella, so the line answers the sentence without repeating it.
   - The German: „sieht an dir aus wie geklaut“ is the everyday German put-down for something that doesn't suit a person. Natural and confident, a looks jab with a specific image.
   - Not a repeat: the live umbrella lines turn differently. „Unterm Schirm erkennt dich wenigstens keiner.“ says hidden is better, and flavour_11.storm „Dein Schirm hat schon bessere Tage gesehen. Du übrigens auch.“ says both are worn.
   - It doesn't predict a soaking.
9. `11.colder` „Wie bei allen, die dich näher kennenlernen.“
   - The closest call among the keeps.
   - Under „Morgen geht's wärmer los, ab 13 Uhr wird's wieder kälter.“ it's the cleanest joke in the batch: warm at first, then cold, the way people turn once they know you. Under „Morgen wird's ab 13 Uhr kälter.“ it reads straight. Under „…, dann brauchst du eine Schicht mehr.“ the tail can also attach to the layer (people need an extra layer around you), which is the same insult.
   - Risk: it is the "like your X" tail the checklist names (vetoed „Wie deine Witze.“, „Wie deine Diät.“), and it uses „kälter“ in its social sense.
   - Kept anyway, because the owner keeps that frame when the image is real (starred and live units_11.steady_cold „Wie dein Kaffee, den du wieder irgendwo stehen gelassen hast.“). The owner also keeps the weather turning away from the reader (live „Selbst der Schnee hat dann genug von dir. Versteh ich gut.“).
   - The writer's note is right that this isn't the dead huddling frame („Bei Kälte rücken die Leute zusammen. Nur mit dir nicht.“): nobody huddles, people cool off.
   - „wie bei allen“ is the right German after the impersonal „es wird kälter“.

## Cut

1. `11.any` „Das ist übrigens der Tag, auf den du alles verschoben hast.“
   - The idea has been vetoed seven times, not twice as the writer's note says: „Was du heute früh vorhattest, schaffst du morgen. Ganz sicher.“ and „Die Mails, die du heute ignoriert hast, warten morgen auch noch.“ (both "i like the idea, but this version isnt funny"), „Dein Plan für heute läuft jetzt unter „morgen dann““, „Was heute liegen geblieben ist, ist morgen dringend.“, „So konsequent bist du sonst nur beim Aufschieben.“, „Du verschiebst die Steuer.“ and „Ignorierte Mails gehen nicht weg …“.
   - BRIEF round 6 says: "Don't rework a flat idea twice."
   - This version still stops at the observation and leaves the reader to supply the punch. It's clean German, but it has no turn.
3. `11.any` „Ich seh ja, wie's bei dir aussieht. Da red ich lieber übers Wetter.“
   - It repeats the live now_11.evening „Wie war dein Tag? Lass, ich hab's an deinem Gesicht gesehen.“: I've seen your state, let's not go into it.
   - It also flips the other live now_11.evening line, „Bitte heute Abend mal ein anderes Thema als das Wetter.“.
   - „wie's bei dir aussieht“ is vague: it can mean your flat, or how you're doing (as in „Wie sieht's bei dir aus?“). So the jab has nothing specific in it, and read as the flat, it assumes the state of the reader's home.
4. `11.any` „Wir sind beide keine großen Leuchten. Bei mir hat's wenigstens technische Gründe.“
   - The closest call of the any cuts. It's good German, it's confident, and the pun is true (e-ink gives no light).
   - Nothing in it reacts to tomorrow or to the evening, so under every forecast it is the "random sentence … from your weather app" the owner rejected.
   - The screen's missing light was vetoed twice as a joke: „Beleuchtung hab ich keine. Nachts häng ich also ganz umsonst hier.“ and „Wenn das Licht ausgeht, sieht mich keiner mehr. E-Ink. Also lies zügig.“
   - The screen calling itself dim also goes against the owner's note on „Schönheitsschlaf brauch ich keinen mehr …“: "does not fit with other texts where the screen is beautiful".
5. `11.any` „Ich lauf wochenlang mit einer Akkuladung. Du schnaufst schon im zweiten Stock.“
   - It repeats the live flavour_11.theme_force „Und du atmest beim Treppensteigen wieder wie Darth Vader.“ (out of breath on the stairs).
   - „im zweiten Stock“ assumes stairs in the reader's life, and nothing in it is about tomorrow.
6. `11.any` „Dein Horoskop für morgen erspar ich dir.“
   - It is the vetoed "the weather's fine, you aren't" frame: round 31's „Das Wetter kann sich über Nacht noch ändern. Bei dir rechne ich nicht damit.“, plus „Gilt für die Kleidung. Für den Rest von dir übernehm ich keine Garantie.“
   - It leans on the dead idea of the screen knowing tomorrow before anyone else.
   - It hints at a bad day for the reader without saying what, so it predicts a mishap and has nothing specific in it.
8. `11.rain` „Aufgespannt braucht der Schirm fast so viel Platz wie du.“
   - The slot holds one line, and 7 is the better one.
   - The fat jab is live: flavour_vf_11.cooling „Eine Schicht mehr? Am Bauch hast du ja schon vorgesorgt.“
   - „Aufgespannt“ as the opening word is stiff, written German.
10. `11.colder` „Zwiebellook ist angesagt. Bei dir passt sogar der Geruch.“
    - It is wordplay on the layering idiom that goes with the forecast (Zwiebel = layers and onion smell), the banned kind.
    - The writer's own flag is right: „Zwiebelprinzip“ was vetoed twice, in „Die sagen Zwiebelprinzip. Ich sag Zirkus.“ and „Zwiebelprinzip nennen die das. Ich nenn's Theater.“
    - „Zwiebellook ist angesagt“ restates „dann brauchst du eine Schicht mehr“ in TV-forecaster speak.
    - The smell jab is live (units_11.c_relief „Dein Deo hat trotzdem schon aufgegeben.“) and was vetoed („Lüft dich halt aus. Du riechst schon nach Wohnung.“).
11. `11.steady` „Wie eine Schaufensterpuppe. Bloß ohne die Figur.“
    - It is the vetoed "the outfit is fine, you're the problem" frame („Die Sachen für morgen sehen gut aus. Solange du nicht drinsteckst.“), plus a vetoed body jab („Für eine Strandfigur reicht's bei dir trotzdem nicht.“).
    - It isn't clear on first read. Getting from one outfit all day to a mannequin takes a beat, and under „Morgen passt ein Outfit für den ganzen Tag.“ there is no „du“ for the comparison to attach to.
    - On this screen „die Figur“ is the drawn figure (live „Die Figur da rechts ist schon für morgen angezogen. Streber.“), so „ohne die Figur“ trips the reader for a moment.
12. `10.warmer` „Die Wärme reizt ihre Gleitzeit mal wieder voll aus.“
    - The closest call of the On cuts. It's idiomatic and dry, the workplace metaphor VOICE asks for, and it reads under all four warmer sentences.
    - But the idea is warmth turning up late. That's live as flavour_vf_10.cold „Durchsage: Die Wärme verspätet sich auf unbestimmte Zeit. Grund ist ein vorausfahrender Zug.“ (the writer's own flag) and was vetoed as „Die Wärme wartet immer, bis alle aus dem Haus sind. Das ist kein Zufall.“
    - The owner has vetoed every recent personification of the warming:
      - „Die Wärme kommt heute als Teillieferung …“
      - „Die Temperatur macht heute mehr Fortschritte als jede Baustelle.“
      - „Die Wärme kommt. Ich hab sie angekündigt, jetzt muss sie.“
    - It is one beat with no turn after it.
13. `10.warmer` „Diesmal kommt die Wärme wenigstens ohne Nebenkostenabrechnung.“
    - It mirrors the live colder line „Die Kälte zieht morgen ein. Miete zahlt sie natürlich keine.“ (weather plus the rent bill).
    - „Nebenkostenabrechnung“ assumes the reader rents. The owner's note on the tumble dryer line: "not everyone lives in a rented apartment. for them this won't make sense. remove." In Austria it's also „Betriebskosten“.
    - „Diesmal“ takes two steps to make sense (the last warmth was the heating). In summer, when warmer means heat, there's no heating to compare it with.
14. `10.warmer` „Ein Tag wie eine Koalition: für jeden was dabei, zufrieden ist keiner.“
    - The „Ein Wetter wie X: …“ simile has been vetoed: „Ein Wetter wie bei Familienfeiern: …“ and „Die Wärme ist wie ein übereifriger Kellner: …“
    - „für jeden was dabei, zufrieden ist keiner“ is the stock line about compromise.
    - Nothing in it is about warming; it fits any day that changes.
    - Coalition politics doesn't travel to Switzerland.

## By slot

| Slot | Target | Kept |
|---|---|---|
| 11.any | 3 | 1 (2) |
| 11.rain | 1 | 1 (7) |
| 11.colder | 1 | 1 (9) |
| 11.steady | 1 | 0 |
| 10.warmer | 2 | 0 |
| **All** | **8** | **3** |

No typo or punctuation fixes were needed. The kept lines are copied unchanged into `de.json`.
