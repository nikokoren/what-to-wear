# Joke shapes

How to write a sarcastic line the owner stars. Taken from about 7,700
votes (`review/decisions/`, November 2026); `python3 tools/shape_report.py`
re-counts them after every round, with `--examples` for starred lines in
each shape. The counts come from patterns, so they are approximate.

The late writing rounds (`2026-11-thin`, `2026-11-thin2`) were vetoed 55
to 83%. The pools weren't empty: the writers were asked for "more lines
for this mood" and wrote whatever came, mostly in the weak shapes below.
A shape is a mechanism, not a topic. Brief a round by shape: "three in
shape X for this situation", with the starred examples of that shape,
and the writer has something to aim at.

## Rules that hold in every shape

- **Short.** A joke under 45 characters is starred about 30% of the
  time, 70 characters and over 15 to 16%, in both languages. Aim for
  under 60.
- **End on the laugh.** Cut everything after it, and everything before
  it that restates the weather.
- **One idea.** A line with a setup sentence and a punchline sentence is
  fine; a line with two jokes loses both.
- **It follows the fact.** Read it under the forecast sentence as the
  screen shows it. If it needs explaining, it's out.

## English: the screen on your wall

At On, 15% of votes are stars and 44% vetoes; at 11, 20% and 39%.

### Strong

| Shape | On | 11 | |
|---|---|---|---|
| **The screen's own limits** | 36% starred, 19% vetoed | 27%, 22% | the best shape at On |
| **Taking credit, denying blame** | 37%, 12% | (few) | |
| **Ends on a sting word** ("Again." "Twice." "Almost.") | 44% (few) | 38%, 17% | the best ending at 11 |
| **Your habits, predicted** ("You'll…") | 15%, 40% | 24%, 36% | an 11 shape; average at On |
| **Your words thrown back** ('It's not that cold,' you'll say.) | 21%, 42% | 22%, 37% | works when the quote is something people really say |

**The screen's own limits.** The screen is a screen: it can't go out,
get wet, sweat, freeze, leave the wall or the WiFi. It envies you, or
is smug about it.
- I'd come along, but I only work in range of your WiFi.
- I'd make a terrible umbrella. Gorgeous, but terrible.
- That's your one reminder. I don't do push notifications.
- My only weakness is the cold. Kidding, I don't have one.

**Taking credit, denying blame.** The screen takes the credit for good
weather, or swears the bad weather wasn't its doing.
- Somebody cranked the outside too high. Wasn't me.
- Two snowfalls in one day. I'll take the credit for both.
- I have a bad feeling about this. Kidding. It's fine.

**Your habits, predicted (11).** What you'll do today, the way someone
who has watched you for years would say it. A habit, never a one-off
moment the screen can't time ("the first sneeze").
- You'll double-check on your phone. As if it knows better.
- You'll read all this, then do what you were going to anyway.
- You'll put {GP} back on later anyway, out of spite.

**Ends on a sting word (11).** The last word turns a neutral sentence
into a jab.
- Perfect for browsing flights somewhere warm and booking nothing. Again.
- You'll search 'ice cream near me' later. Twice.
- Next to all that white, you almost look tanned. Almost.

### Weak

| Shape | On | 11 |
|---|---|---|
| **Other people** (everyone, someone, the neighbors) | 12% starred, 52% vetoed | 9%, 57% |
| **A simile** ("like a…") | 11%, 47% | 21%, 54% |

Other people only work when the screen is the point ("On rainy days,
everyone checks me twice. I'm not complaining.").

## German: der Grantler

At On, 18% stars and 35% vetoes; at 11, 17% and 31%. German votes are
less spread out than English ones: the Grantler's voice carries most
shapes, and phrasing matters more than shape (the owner's notes on
German are mostly about wording, „wetterfühlig“, sentences that are too
complex). Write plain spoken German with a southern touch at most.

### Strong

| Shape | On | 11 | |
|---|---|---|---|
| **Zitat zurück** (what people say, thrown back) | 24% starred, 21% vetoed | 32%, 36% | the best shape in German |
| **„Ich kenn dich“** (your habits, predicted) | 17%, 37% | 25%, 22% | an 11 shape |
| **Seitenhieb** (a jab at you) | (few) | 26%, 24% | 11 only |
| **Eltern-Ton** (the parent's scold) | 11%, 78% | 24%, 27% | 11 only: at On it's a level error |
| **Der Grantler über sich** | 19%, 30% | 21%, 29% | the voice's base |

**Zitat zurück.** A thing people say, and the Grantler's answer to it.
- „Kälte härtet ab“, sagen die mit der Heizung auf fünf.
- „Es gibt kein schlechtes Wetter.“ Doch, gibt's.
- „Nur noch eine Folge.“ Das war vor zwei Folgen. (11)
- Dein „Mir ist nie kalt“ hebst du dir bitte für einen anderen Tag auf. (11)

**„Ich kenn dich“ (11).** He knows what you'll do, and he's tired of it.
- Den Schirm siehst du. Mitnehmen wirst du ihn trotzdem nicht.
- Ich sag's dir, und du bist trotzdem überrascht. Jedes Mal.
- Du schaust trotzdem noch dreimal nach. Ich kenn dich.

**Seitenhieb (11).**
- Jeder Schneemann hat heute mehr Ausstrahlung als du.
- Deine Hände sind heut fast so kalt wie dein Herz.
- Dann ist draußen endlich alles so blass wie du.

**Eltern-Ton (11).**
- Wenn's donnert, gehst du rein. Nicht „gleich“, sondern sofort.
- Und komm mir nicht mit „Ich hab keinen Durst“.

**Der Grantler über sich.** Grumpy, put-upon, on duty against his will.
- Dann bin ich heute wohl wieder nur Deko.
- Heute gibt's nichts auszusetzen. Das ärgert mich.
- Ich bin um die Uhrzeit nur noch aus Höflichkeit an.

### Weak

| Shape | On | 11 |
|---|---|---|
| **Andere Leute** | 16% starred, 35% vetoed | 13%, 31% |
| **Vergleich „wie ein“** | 12%, 50% | 10%, 28% |

Unlike in English, other people are about average at On in German,
when the Grantler is grumbling about them („Und gleich wird trotzdem
wieder stoßgelüftet.“); they fail as plain observation.

## How a round uses this

1. Pick the situation and its level. Read the slot's starred lines and
   its vetoes (`review/examples/`, `review/dont/`).
2. Ask for lines by shape: at On mostly the strong On shapes, at 11 the
   strong 11 shapes, and a few in other shapes for variety. Give each
   shape its examples above.
3. The critic (`docs/CRITIC.md`) cuts by the rules there, keeps the
   shape mix, and keeps lines under about 60 characters unless they earn
   it.
4. After the vote, `tools/shape_report.py` shows whether the shapes
   still hold.

## Round 39, the first round written this way

`2026-11-turns` (`review/rounds/make_round39.py`), voted 19 November 2026.
59 jokes, 4 starred, 49% vetoed overall, but two very different halves:

| Situation | Vetoed | Starred |
|---|---|---|
| Tomorrow, rain possible (evening) | 22% | 4 of 23 |
| Snowing now, rain later (units) | 67% | 0 of 36 |

The thin rounds before it were vetoed 55 to 83%. So shapes help where the
situation gives the joke something to push against: a maybe-rain evening
is about the reader's umbrella dithering, which fits "your habits" and
"I can't be wrong" exactly. Snow turning to slush gives a joke almost
nothing but "the nice part ends", and no shape rescued it; the vetoes
were "not funny, forced" across every shape. Two lessons:

- **Before writing, ask what the situation gives the joke.** If the only
  angle is the weather itself, write fewer lines (a thin, rare situation
  can live with three units) or find the human angle first.
- **"Your habits, predicted" held up:** 9 of 13 kept, the best shape in
  the round, at 11 in both languages. "Zitat zurück" did worse here (2
  of 7) than its history; one of the two kept was starred.

## Round 40: the steady screens

`2026-11-steady` (`review/rounds/make_round40.py`), voted 20 November
2026. 82 units, 2 starred, **72% vetoed**: worse than round 39 and in the
range of the thin rounds. No veto carried a tag or a note.

| | Kept |
|---|---|
| English | 17 of 42 (40%) |
| German | 6 of 40 (15%) |
| Jabs at you (11) | 2 of 19 |
| Quotes thrown back | 0 of 6 |
| Habits, credit, the screen's limits | 12 of 32 (about 40%) |

What it says:

- **Shapes don't refill a full pool.** The steady slots already held
  11 to 22 voted lines each, covering the obvious angles (nothing to do,
  nothing to blame, you'll check anyway). New lines landed in the same
  angles and read as seen before. The shape method helps a new or thin
  situation (round 39's maybe-rain evening); it doesn't help here.
- **The German was weak.** 15% kept, every German slot under 25%. As in
  the owner's earlier notes, it reads as written rather than spoken.
  German needs a native writer, or the owner's own lines, more than more
  rounds.
- **Jabs at 11 failed** this time (11% kept) after doing well in the
  history; a jab needs a fresh target, and steady days don't give one.
- **The owner cut the sting endings** in two kept lines ("Riveting
  stuff.", "You won't."): end on the laugh, and the laugh was earlier.

So for the steady screens the next step is not another writing round but
the markup: rotate through the voted lines better (see `docs/TODO.md`).

