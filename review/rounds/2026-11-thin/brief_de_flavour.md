# Top-up round (de, flavour): thin slots to four lines

You write lines for a TRMNL e-ink weather screen, "What to Wear". German, standard German, no dialect. The speaker is the screen itself: der Grantler, grumpy, dry. Write in this language from scratch; never translate.

These slots have fewer than four live lines, and they are the ones that actually show on screen. Each heading says how many the critic will keep for the owner's vote and how many candidates to write (three times that). At most one candidate per slot may be out of the box (a different angle or form, still clear and on voice); mark it `"wild": true`.

## Learn from what worked, first

- Read `docs/BRIEF.md` (the voice, the levels, every lesson), above all "Tightening": the owner's own proofreading pass. Then `docs/CRITIC.md`: the critic cuts by it, so write so nothing on it applies.
- Read `review/rounds/2026-10-de-tight/changes.md`: every before and after of that pass.
- Read `review/examples/de.md`: the owner's starred lines. Reuse what makes them work (the angle, the rhythm, the length), not their words.
- Read `docs/PROOFREAD_DE.md`: the proofreader checks every line by it. The owner finds machine-sounding German the worst fault: write as a native speaker would say it.
- Skim `review/dont/de.md`: vetoed lines with tags and notes. Never go near those.

## Rules that cost the most votes

- Sarcasm with bite; never merely pleasant, never a restatement of the weather. Clear on first read, short (one or two short sentences).
- No wordplay on the forecast's words, no "like your X" / „wie deine X“ jabs, no predicting the reader's mishaps, never explain the joke.
- Nothing the screen can't know; no assumptions about how the reader lives. Evening (18-22) is not bedtime.
- Garment jokes must fit every garment the slot covers. Storms: no "get inside" lectures. The extra-cold layer is just the scarf.
- Each joke sits at one level: On is not about the reader; 11 is.
- The room, never the hallway (en). Keep the device's spot in the home vague (de).
- No line may repeat another candidate's idea, or a live line's.

## Slots

### `flavour_10.off` (live now: 3; the critic keeps 2, write 6)

Follow-up under a forecast sentence: a layer comes off later (jacket, sweater, coat, scarf) and stays off.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Und dann darfst du {GP} wieder überm Arm spazieren tragen.
- Hier drin merk ich davon natürlich wieder nichts.
- Ich würde ja mitmachen, aber unter dem Rahmen hab ich nichts an.
Starred here before:
- Dann darfst du dich kurz freuen. Aber übertreib's nicht.
- Wohin damit, ist dann dein Problem. Ich sag nur das Wetter an.
Voted out here (stay away):
- Ein Grund zum Meckern weniger. Ich find schon einen neuen. [robotic]
- Und dann liegt's wieder in irgendeinem Büro rum. [not funny]
- Und schon sind wieder alle gut gelaunt. Unerträglich. [not funny, unclear] (note: why are they all gut gelaunt? the weather is cool.)
- Dann sitzen die Ersten wieder draußen im Café, als wär's Juli. Mit Decke. [not funny]

### `flavour_10.pants` (live now: 1; the critic keeps 4, write 12)

Follow-up under a forecast sentence: long pants on a shorts morning: a cold front later.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Sieht nicht danach aus, ich weiß. Stimmt aber trotzdem.
Voted out here (stay away):
- Die Sonne jetzt ist ein Lockangebot. [not funny]
- Die Kaltfront meldet sich nicht vorher an. Außer bei mir. [not funny]
- Kurze Hose gegen Kaltfront. Ich tipp nicht auf die Hose. [not funny]
- Kurze Hosen bei Kaltfront hat noch keiner bereut. Außer allen. [not funny]
- Das ist keine Meinung, das ist eine Kaltfront. [not funny]
- Erst Sommer, dann April. Ganz normaler Tag in Mitteleuropa. [not funny]
- Ich weiß, ich mach mich heute unbeliebt. [not funny]
- Mit der Jacke unterm Arm siehst du jetzt komisch aus. Später aber schlau.
- Ich trau dem schönen Wetter auch nicht. Zu Recht, wie's aussieht. [not funny]
- Die in kurzen Hosen lachen jetzt noch. [not funny, unclear]
- Das jetzt ist nur die Vorschau. Der Hauptfilm heißt Kaltfront. [not funny]

### `flavour_10.shorts` (live now: 1; the critic keeps 4, write 12)

Follow-up under a forecast sentence: go out in shorts on a cold morning: shorts weather later.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Ja, wirklich. Ich sag sowas nicht zum Spaß.

### `flavour_10.scorch` (live now: 3; the critic keeps 2, write 6)

Follow-up under a forecast sentence: dangerous heat: water and shade. Never undercut the advice.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Ich sag's auch dreimal, wenn's sein muss. Schatten, Schatten, Schatten.
- Ich bleib hier. Aber ich hab ja keine Wahl.
- Ich halt das aus, ich bin aus Plastik. Du nicht.
Voted out here (stay away):
- Heute mein ich das ganz ohne Grant. [not funny]

### `flavour_10.storm` (live now: 3; the critic keeps 2, write 6)

Follow-up under a forecast sentence: a thunderstorm: the umbrella, inside while it thunders.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- {M:05,06,07,08,09}Im Freibad pfeift der Bademeister dann wieder alle aus dem Becken. Sein Lieblingsmoment.
- Die Wetter-Apps schicken jetzt wieder Warnungen im Minutentakt. Ich sag's einmal.
- Wagner hätte das gefallen. Mir nicht.
Starred here before:
- Im Freibad pfeift der Bademeister dann wieder alle aus dem Becken. Sein Lieblingsmoment.
Voted out here (stay away):
- Bei Gewitter hat die Oma früher alle Stecker gezogen. Ich hätt endlich mal Ruhe gehabt. [not funny]
- Fällt irgendwo der Strom aus, ist mir das egal. Ich hab Akku. [not funny]
- Irgendwo hängt jetzt noch Wäsche draußen. Nicht mehr lange. [not funny]
- Danach liegt bestimmt wieder irgendwo ein Ast auf der Oberleitung. [not funny]
- Dann gehen überall gleichzeitig die Rollläden runter. Wie einstudiert. [not funny]
- Dein einziger Blitzableiter bist du selbst. Also rein, wenn's donnert. [not funny]
- Bei Donner bleib ich auch drinnen. Wie immer, eigentlich. [not funny]
- Unter einem Baum ist nicht drinnen. [not funny]
- Gegen den Regen hilft der Schirm, gegen Blitze nur ein Dach. [not funny, robotic]
- Spannend wird's heute nur am Himmel. Schau's dir von drinnen an. [not funny, unclear]
- Der Schirm hilft gegen Regen. Gegen Blitze hilft nur drinnen. [not funny, unclear, robotic] (note: i like the direction, but that doesnt work as is in german.)
- Der Schirm ist für den Regen. Für den Blitz ist er eher eine Einladung. [not funny]

### `flavour_10.theme_ghd` (live now: 3; the critic keeps 2, write 6)

THEME DAY: Groundhog Day, 2 February (Murmeltiertag; German readers know it from the film „Und täglich grüßt das Murmeltier“). Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Und täglich grüßt das Murmeltier. Heute sogar offiziell.
- Heute sagt ein Murmeltier das Wetter an. Dem hören alle zu. Mir nie.
- „Und, Murmeltier, wie wird's?“ „Lasst mich schlafen.“
Voted out here (stay away):
- Murmeltiertag. Ein Nagetier mit eigenem Pressesprecher. [not funny]
- Murmeltiertag. In Deutschland hätten wir dafür eine Behörde. [not funny]
- Hier heißt der Tag Lichtmess. Die Bauernregel dazu kennt trotzdem keiner mehr. [not funny]
- Murmeltiertag. Für mich ist das jeden Tag. [not funny]
- Murmeltiertag. Ich sag heute einfach wieder das Gleiche. [not funny]

### `flavour_10.theme_ny` (live now: 3; the critic keeps 2, write 6)

THEME DAY: New Year's Day. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Erst das Silvesterfeuerwerk, dann der Feinstaub. Prost Neujahr.
- Zum Jahreswechsel kann man immer sehen, wer Geld zum Verballern hat.
- Ab heute schreibt wieder jeder bis Februar die falsche Jahreszahl.
Voted out here (stay away):
- Neujahr. Alles hat zu, und die Tankstelle macht das Geschäft des Jahres. [not funny]
- Neujahrskonzert. Beim Radetzkymarsch klatschen wieder alle mit, ob sie wollen oder nicht. [not funny]
- Neues Jahr, Version unverändert. Bekannte Fehler bleiben erhalten. [not funny]

### `flavour_10.theme_spooky` (live now: 3; the critic keeps 2, write 6)

THEME DAY: Halloween. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level On: sarcastic and dry, about the weather, the world, or the screen itself. Not a jab at the reader.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Früher war Reformationstag, da hatte man seine Ruhe.
- Buh. Mehr Halloween gibt's von mir nicht.
- Das Gruseligste ist, dass morgen November ist.
Starred here before:
- Buh. So, das war mein Beitrag.
Voted out here (stay away):
- Halloween. Gleich klingeln wieder Kinder, die man nicht kennt. [not funny] (note: i like the direction, but that one does not land.)
- Halloween. Der Kürbis kostet mehr als der Wocheneinkauf. [not funny]
- Halloween. Die geschnitzten Kürbisse fangen morgen an zu schimmeln. Gruselig genug. [not funny]
- Halloween. Jedes Jahr regen sich dieselben Leute über diesen amerikanischen Brauch auf. Ich auch. [not funny]
- Halloween. Im Supermarkt liegen die Gruselmasken neben den Lebkuchen. Das ist der wahre Horror. [not funny]

### `flavour_11.storm` (live now: 3; the critic keeps 2, write 6)

Follow-up under a forecast sentence: a thunderstorm: the umbrella, inside while it thunders.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Dein „Das zieht vorbei“ hat noch nie gestimmt.
- Bei jedem Donner zusammenzucken und dann so tun, als wär nichts. Schon klar.
- Dein Schirm hat schon bessere Tage gesehen. Du übrigens auch.
Starred here before:
- Wenn's donnert, gehst du rein. Nicht „gleich“, sondern sofort.
- Fotografier's bitte durchs Fenster. Das Foto wird sowieso nichts.
Voted out here (stay away):
- Wenn's blitzt, ist das kein Fotograf. So berühmt bist du nicht. [not funny]
- Heute bist du mal nicht der Lauteste. Ausnahmsweise. [not funny]
- Dein Schirm hat mehr Rückgrat als du. Zumindest bis zur ersten Böe. [not funny]
- Gewitter. Jetzt weißt du, wie's den Leuten um dich herum sonst geht. [not funny]
- Hast du den Schirm? Gut. Und deine Würde? [not funny]
- Wenn's donnert, gehst du rein. Nicht „gleich“, sondern sofort. [not funny]
- Zählen zwischen Blitz und Donner kannst du ja. Bis drei immerhin. [not funny]
- Fotografier's bitte durchs Fenster. Das Foto wird sowieso nichts. [not funny]

### `flavour_11.theme_easter` (live now: 3; the critic keeps 2, write 6)

THEME DAY: Easter Sunday. Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Du isst vom Schokohasen wieder zuerst die Ohren. Ganz schön brutal.
- Der Schokohase ist innen hohl. Ihr habt also was gemeinsam.
- Heute isst du wieder Schokolade zum Frühstück und nennst es Tradition.
Voted out here (stay away):
- Ich hab dieses Jahr nichts versteckt. Bei dir findet man ja nicht mal das Offensichtliche. [not funny]
- Ostern. Jetzt siehst du wieder aus wie ein Schokohase in der Sonne. Etwas zerlaufen. [not funny]
- Ostersonntag. Der Hase verteilt nach Verdienst. Deshalb ist dein Nest so leer. [not funny]
- Ostersonntag. Die Schokoeier hast du vermutlich schon beim Verstecken gegessen. [not funny]
- Ostersonntag. Die Fastenzeit hast du vermutlich am Aschermittwoch schon abgebrochen. [not funny]
- Ostersonntag. Beim Eiersuchen bist du vermutlich wieder langsamer als die Kinder. [not funny]

### `flavour_11.theme_ghd` (live now: 3; the critic keeps 2, write 6)

THEME DAY: Groundhog Day, 2 February (Murmeltiertag; German readers know it from the film „Und täglich grüßt das Murmeltier“). Shown instead of the weather joke on that day. Name it or make it unmistakable.
Level 11: sarcastic and personal, it's about the reader. Looks and worth are fair game.
Placeholders you may use: none, except {GP} (the garment's pronoun) in follow-ups
Live here (don't repeat their ideas):
- Wenn das Murmeltier dich sieht, gibt's sicher noch sechs Wochen Winter.
- Das Murmeltier wird fürs Rauskommen gefeiert. Bei dir klatscht keiner.
- Im Film wird einer durch tausend gleiche Tage ein besserer Mensch. Bei dir bräucht's mehr.
Voted out here (stay away):
- Murmeltiertag. Ein Murmeltier darf so rund sein. Es hat Winterschlaf als Ausrede. [not funny]
- Murmeltier oder du: Wer schaut morgens grantiger aus dem Loch? [not funny]
- Murmeltiertag. Ein Tier mit Pelz und schlechter Laune. Ihr hättet euch viel zu sagen. [not funny]
- Murmeltiertag. Du merkst den Unterschied zu sonst vermutlich nicht. [not funny]
- Heute ist Murmeltiertag. Das Murmeltier kommt wenigstens einmal im Jahr raus. [not funny]
- Und täglich grüßt das Murmeltier. Kennst du ja aus deinem Alltag. [not funny]
- Am Murmeltiertag würd das Murmeltier lieber weiterschlafen. Wie du. [not funny]

## Output

Write `review/rounds/2026-11-thin/de.flavour.raw.json`: `{"lines": [{"path": "...", "text": "..."}, {"path": "...", "text": "...", "wild": true}]}`, using each slot's path exactly as given in its heading (units as `units_10.key`). Mark the out-of-the-box ones `"wild": true`. Add `"months"` (e.g. "11,12,1,2") only for a line that only fits some months. Check the file parses. Don't edit any other file and don't commit.
