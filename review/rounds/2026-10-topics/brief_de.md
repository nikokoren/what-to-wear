# Fresh topics, de

You write sarcastic lines for a TRMNL e-ink weather screen ("What to Wear"). Two kinds:
- **units**: a forecast sentence and its joke, written together: `forecast sentence || joke`. Path `unit_10.<key>` (sarcasm On, mild) or `unit_11.<key>` (sharper).
- **now lines**: one sarcastic line about the weather right now, shown alone under the drawing. Path `now_10.<mood>` or `now_11.<mood>`.

Voice: der Grantler: ein grantiger, trockener Bildschirm, Standarddeutsch (kein Dialekt).

## What the owner keeps
1. **The screen's own stake**: it is a screen, indoors, it only does forecasts, and it has opinions about that. The owner's own edits keep pulling jokes there ("…but I'm not the one dealing with the consequences.", „Wenn's warm ist, glaubst du mir sowas nie.“).
2. **Truths everyone recognizes**, with **bite**: sarcasm, not gentle observation. Round 20's "Then every car wears a white hat for a few days" got the owner's note "where's the sarcasm?".
3. **Clear on first read.** Round 20's German notes: "what is that supposed to mean?", "joke does not make sense", "no flow".

## What the owner vetoes, nearly always
- Wordplay on a word of the forecast sentence. "Like your X" / „wie deine X“ jabs. Predicting the reader's mishaps or behavior.
- Explaining the joke. Mentioning drawings. Anything the screen can't know (what the reader did, where they are, what's in their bag). Assuming the TRMNL shows only this recipe.
- English: the screen's spot is "room", never hallway. German: keep it open („drinnen“, „hier drin“).

## Rules
- Units: the forecast part comes from that key's live wordings (one is listed below; you may shorten it) and keeps its placeholders: {WHEN}/{WHEN2} times, {WHENP} when rain or snow starts, {WHENSTOP} when it stops, {G}/{GV}/{GP} the garment. Steady days say "all day", never "until tonight".
- Short: a now line under about 90 characters, a unit under about 120.
- Seasonal lines carry "months": "11,12,01".

## The topics (8 candidates per topic, each a different idea; mix units and now lines where the topic allows)

- **Bauernregeln**: Der Grantler zitiert, bezweifelt oder verteidigt Bauernregeln („Kräht der Hahn auf dem Mist …“). Allgemein bekannte, keine obskuren. Good homes: steady-, p_*-Units; now cool/wet. Give each line "topic": "Bauernregeln".
- **der Wetterfrosch**: Früher hat das ein Frosch im Glas auf der Leiter gemacht. Der Bildschirm als sein Nachfolger. Good homes: steady-Units; now cool. Give each line "topic": "der Wetterfrosch".
- **Föhn**: Die Ausrede für jedes Kopfweh und jede Laune südlich der Donau. Nie behaupten, heute sei Föhn: das weiß der Bildschirm nicht. Good homes: w_*-, arc-Units; now nice/cool. Give each line "topic": "Föhn".
- **Kreislauf**: „Bei der Hitze hab ich's mit dem Kreislauf.“ Die deutscheste aller Hitzeklagen. Good homes: steady_hot, w_water; now hot. Give each line "topic": "Kreislauf".
- **Wetterfühligkeit**: Die Allzweck-Ausrede an Tagen, die sich ändern. Good homes: arc-, w_*/c_*-Units. Give each line "topic": "Wetterfühligkeit".
- **Ruhezeiten**: Der Rasenmäher am Sonntag, der Laubbläser am Samstag um acht. Immer „jemand“, nie der Leser. Good homes: steady-Units; now nice/cool. Give each line "topic": "Ruhezeiten".
- **das frisch gewaschene Auto**: Samstag poliert, Sonntag Regen. Irgendjemandes Auto, nicht das des Lesers. Good homes: p_wetter, p_wetter_long-Units. Give each line "topic": "das frisch gewaschene Auto".
- **Hausschuhe**: Kalte Tage: die Hausregel, älter als das Haus. Good homes: steady_cold-Units; now cold. Give each line "topic": "Hausschuhe".
- **Wetter-App gegen Wetterbericht**: Dieselbe Rivalität wie im Englischen, im Ton des Grantlers. Nicht wieder das Regenradar: ein neuer Winkel. Good homes: p_wetter_maybe-Units; now wet. Give each line "topic": "Wetter-App gegen Wetterbericht".
- **Altweibersommer**: Ein warmer, sonniger Tag im September oder Oktober ist genau das. Nur als now_10/now_11.nice mit "months": "09,10". Good homes: now nice, months 09,10. Give each line "topic": "Altweibersommer".

## Eisheilige (special day, 11 to 15 May)

12 candidates, path `flavour_10.day_eisheilige` or `flavour_11.day_eisheilige`, "topic": "Eisheilige". Shows on a dry day whose weather doesn't change, every other hour, under „Was du anhast, passt für den restlichen Tag.“ or alone under the drawing. Name the day in the line (or make it unmistakable): die letzte Frostgefahr, Gärtner warten mit dem Pflanzen, Tomaten erst danach raus.

## Unit keys and one live wording each

- `steady`: Nothing changes all day. About half of all screens; also Visual Forecast's "works all day". e.g. "Dein Outfit passt heute den ganzen Tag."
- `steady_evening`: Nothing changes, from 17:00. e.g. "Dein Outfit passt den ganzen Abend."
- `steady_night`: Nothing changes, from 22:00: the evening wording, late. e.g. "Dein Outfit passt den ganzen Abend."
- `steady_cold`: Steady cold (coat or more), before 17:00. e.g. "Kalt bleibt's heute, und zwar den ganzen Tag."
- `steady_hot`: Steady heat, before 17:00. e.g. "Die Hitze lässt den ganzen Tag nicht nach. Pack eine Flasche Wasser ein und such dir Schatten."
- `w_jacket`: Warms up: the jacket comes off. e.g. "Mit der Jacke ist {WHEN} Schluss, dann wird's wärmer."
- `w_hoodie`: Warms up: the sweater comes off. e.g. "Mit dem Pulli ist {WHEN} Schluss, dann wird's wärmer."
- `c_jacket`: Cools to jacket weather: a jacket needed later. e.g. "{WHEN} brauchst du eine Jacke, also nimm eine mit."
- `c_hoodie`: Cools to sweater weather: a sweater needed later. e.g. "{WHEN} brauchst du einen Pulli, also nimm einen mit."
- `w_scarf`: Warms up: hat, scarf and gloves come off, the coat stays. e.g. "Mütze, Schal und Handschuhe kannst du {WHEN} einpacken."
- `w_coat`: Warms up: the winter coat comes off. e.g. "{WHEN} wird's mild genug, um die Winterjacke auszuziehen."
- `w_water`: Climbs into heat. Nothing left to take off. e.g. "Noch geht's, aber {WHEN} wird's heiß. Nimm genug Wasser mit."
- `c_scarf`: Cools to bundled: hat, scarf and gloves needed later. e.g. "Denk an Mütze, Schal und Handschuhe, {WHEN} wird's ungemütlich kalt."
- `c_coat`: Cools to coat weather: the winter coat needed later. e.g. "{WHEN} kühlt's deutlich ab, dann ist die Winterjacke dran."
- `c_relief`: The heat breaks, but it stays warm. Nothing to bring. e.g. "{WHEN} ist das Schlimmste der Hitze vorbei, es bleibt aber warm."
- `arc_warmer`: The jacket comes off and stays off: the evening is still warmer than now. e.g. "{WHEN} {GV} weg, und zwar für den Rest des Tages."
- `arc_level`: The jacket comes off, and is wanted back in the evening. e.g. "{WHEN} {GV} weg. Nimm {GP} trotzdem mit, {WHEN2} wird's wieder kühler."
- `arc_colder`: The jacket comes off; the evening is colder than now: jacket back, plus a layer. e.g. "{WHEN} {GV} weg. Pack {GP} trotzdem ein, dazu was Warmes, {WHEN2} wird's richtig kühl."
- `shorts_early`: A cool morning in long-pants weather that turns into shorts weather; the line suggests shorts, the drawing shows long pants. e.g. "Gerade ist's frisch, aber {WHEN} ist Shorts-Wetter."
- `p_wetter`: Rain later, a short spell. Shown alone (a steady day); on a day that changes, it follows that sentence. e.g. "{WHENP} regnet's kurz. Mit Schirm bleibst du trocken."
- `p_wetter_long`: Rain later, and it stays. Shown alone; after a change, it follows that sentence. e.g. "{WHENP} kommt Regen, und der hört so schnell nicht auf. Nimm den Schirm mit."
- `p_wetter_maybe`: Rain possible later, not likely. Shown alone; after a change, it follows that sentence. e.g. "{WHENP} ist ein Schauer drin, also lieber den Schirm einpacken."
- `p_stays_wet`: Raining now and all day. e.g. "Eine Regenpause gibt's heute nicht, nimm den Schirm mit."
- `p_drier`: Raining now, stops later. e.g. "Nimm den Schirm mit, der Regen hört erst {WHENSTOP} auf."
- `p_wet_again`: Raining now, stops, comes back. e.g. "{WHENSTOP} hört der Regen auf, {WHENP} kommt er wieder. Behalt den Schirm bei dir."
- `p_snow_coming`: Snow later. e.g. "Rechne {WHENP} mit Schnee."
- `p_stays_wet_snow`: Snowing now and all day. e.g. "Heute schneit's ohne Unterbrechung."
- `p_drier_snow`: Snowing now, stops later. e.g. "Der Schneefall hört {WHENSTOP} auf."
- `p_wet_again_snow`: Snowing now, stops, comes back. e.g. "{WHENSTOP} hört's auf zu schneien, {WHENP} geht's wieder los."

## Now moods

- `nice`: T-shirt weather (18–30 °C feels-like) under a clear or partly cloudy sky
- `cool`: sweater or jacket weather, or any grey/overcast day that isn't cold
- `cold`: winter coat weather or colder
- `hot`: hot (above 30 °C feels-like)
- `wet`: raining right now
- `snow`: snowing right now
- `evening`: 18:00–22:00, dry
- `night`: after 22:00, dry

## Lines the owner starred recently (study the tone)

- Endlich passt das Wetter mal zu deinem Gesicht.
- Fünf Zentimeter, und im Radio heißt's Schneechaos.
- Nimm einen Pulli mit, {WHEN} kühlt's ab.
- Noch eine Folge, sagst du. Seit drei Folgen.
- Jetzt hamstern's wieder alle Streusalz, als käm die Eiszeit.
- So spät noch wach? Ab ins Bett mit dir.
- Alle starren wieder aufs Regenradar. Als ob das was hilft.
- Bei der Kälte schmeckt sogar Glühwein.
- Pack eine Jacke ein, {WHEN} wird's kühler.
- Heut bist du mal passend angezogen. Am Rest arbeiten wir noch.
- Die Bahn hat bestimmt schon aufgegeben.
- Dick eingepackt gefällst du mir am besten. Man sieht weniger.
- Saukalt. Mehr gibt's nicht zu sagen.
- {WHEN} {GV} weg, aber behalt {GP} griffbereit für {WHEN2}.
- {WHEN} wird's wärmer, dann kann die Winterjacke weg.
- Erst zu warm, dann zu kalt. Hauptsache, man hat was zum Meckern.
- {WHEN} wird's wärmer, dann kann der Pulli weg.
- „Nur noch eine Folge.“ Das war vor zwei Folgen.
- Weihnachtsspaziergang nach dem Essen? Sagst du jedes Jahr.
- Was du anhast, passt für den ganzen Abend.
- Gleich kommt wieder: „Früher war es auch schon heiß.“
- Die Kälte bleibt den ganzen Tag.
- „Es gibt kein schlechtes Wetter.“ Doch, gibt's.
- Nimm den Schirm mit, {WHENP} fängt's an zu regnen, und zwar länger.
- So ein Wetter hätten sich andere mehr verdient.
- Ob's dir steht, ist eine andere Frage.
- Zumindest bis zum ersten Kaffeefleck.
- Dann kann ja nur noch alles andere schiefgehen.
- Da hätt ich heute auch frei nehmen können.
- Wohin damit, ist dann dein Problem. Ich sag nur das Wetter an.
- Es bleibt den ganzen Tag so kalt. || Das ist keine Vorhersage, das ist eine Drohung.
- Was du anhast, passt für den Rest der Nacht. || Um die Uhrzeit sieht dich ja sowieso keiner mehr. Gott sei Dank.
- Was du anhast, passt den ganzen Tag. || Mehr kann ich für dich heute nicht tun.
- Was du anhast, passt den ganzen Tag. || Auch für die Joggingrunde, die du dann doch nicht drehst.
- Was du anhast, passt für den Rest der Nacht. || Warum du jetzt noch aufs Wetter schaust, frag ich lieber nicht.
- Wärmer wird's heute den ganzen Tag nicht. || Du kannst es trotzdem gern noch mal mit Jammern versuchen.
- Es wird den ganzen Tag nicht wärmer. || Du kannst also aufhören, mich alle fünf Minuten anzuglotzen.
- Es bleibt den ganzen Tag so kalt. || Da hilft auch kein Jammern.
- Was du anhast, passt den ganzen Tag. || Da hätt ich heute auch frei nehmen können.
- Es bleibt den ganzen Tag so kalt. || Das Handy bedienst du wieder mit der Nasenspitze. Sehr elegant.
- Es bleibt den ganzen Tag so kalt. || Dann fällt das Fitnessstudio heute ja wieder aus. „Wegen dem Wetter“.
- Wettermäßig passt, was du anhast, den ganzen Tag. || Modisch reden wir lieber nicht drüber.
- Was du anhast, passt für den Rest der Nacht. || Auch für den dritten Gang zum Kühlschrank.
- Was du anhast, passt für den Rest der Nacht. || Also für die zehn Minuten, bis du auf dem Sofa einschläfst.
- Es bleibt den ganzen Tag so kalt. || Dick eingepackt gefällst du mir sowieso am besten. Man sieht weniger.
- Was du anhast, passt den ganzen Abend. || Für ein Kompliment reicht's trotzdem nicht.
- Heute bleibt's heiß, trink viel Wasser und such dir Schatten. || Und komm mir nicht mit „Ich hab keinen Durst“.
- Was du anhast, passt den ganzen Tag. || Wenigstens das Wetter ist heute mal unkompliziert.
- Dein Outfit passt heute den ganzen Tag. || Wenn doch alles so einfach wär.
- Es bleibt den ganzen Tag so kalt. || Deine schlechte Laune hat heute ausnahmsweise mal einen Grund.
- Was du anhast, passt den ganzen Tag. || Dann bin ich heute wohl nur Deko.
- Was du anhast, passt den ganzen Tag. || Ich hab dich schon schlechter angezogen gesehen. Gestern zum Beispiel.
- Was du anhast, passt den ganzen Abend. || Gut so. Für Überraschungen bin ich schon zu müde.
- Was du anhast, passt den ganzen Abend. || Eine Sorge weniger. Aber dir fällt bestimmt was Neues ein.
- Es bleibt den ganzen Tag so kalt. || Dann hast du ja den ganzen Tag ein Gesprächsthema.
- Heute ändert sich nichts, was du anhast, passt den ganzen Tag. || Für so eine Ansage bin ich eigentlich überqualifiziert.
- Es bleibt den ganzen Tag so kalt. || Wer jetzt „herrlich frisch“ sagt, kriegt von mir keinen Wetterbericht mehr.
- Die Kälte hält den ganzen Tag an. || Da bleibt immerhin das Bier auf dem Balkon schön kühl.
- Was du anhast, passt den ganzen Tag. || Damit hast du die einzige richtige Entscheidung des Tages schon hinter dir.
- Was du anhast, passt den ganzen Tag. || Ob's dir steht, ist eine andere Frage.

## Output

Write `review/rounds/2026-10-topics/de.raw.json`: `{"lines": [{"path": "now_10.cold", "text": "…", "topic": "feels like"}, {"path": "unit_10.steady_cold", "text": "fact || joke", "topic": "feels like", "months": "11,12"}]}`. Check it parses. Don't edit any other file, don't commit.
