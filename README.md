Rapport, Ai projekt

Problem och dataset
I detta projekt valde jag att skapa en modell som kan förutsäga ett testresultat baserat på hur många timmar en elev har studerat. Jag använde ett enkelt dataset med två kolumner: hours_studied och test_score. Datasetet skapades direkt i Python-koden som en mindre datasamling och laddades sedan in med hjälp av Pandas till en DataFrame för vidare hantering.
Detta är ett regressionsproblem eftersom modellen ska förutsäga ett numeriskt värde, alltså ett resultat i poängform och inte en kategori. Anledningen till att jag valde detta exempel är eftersom det är lätt att förstå sambandet mellan indata och resultat. Det blir också tydligt att mer träning eller mer tid ofta påverkar resultatet positivt.
Förberedelse
Datan har lagts in i Python med hjälp av Pandas och sparades i en DataFrame.
Datasetet är litet och rent, därför fanns inga saknade värden att hantera och om detta hade varit ett större verkligt dataset hade det ofta krävts mer datarensning innan modellen kunnat användas. Jag valde hours_studied som feature (indata) och test_score som target (det modellen ska förutsäga). Jag skapade även en visualisering med ett scatter diagram för att visa sambandet mellan studietimmar och resultat. Diagrammet visar tydligt att poängen ökar när antalet studietimmar ökar.
Projektet sparades i en Python-fil (project.py) och diagrammet sparades som en separat bildfil (chart.png).
Val av modell
Jag valde modellen Linear Regression från Scikit-learn.
Anledningen är att datasetet visar ett tydligt linjärt samband där fler studietimmar ofta ger högre poäng. Därför passar linjär regression bra som första val.
Datan delades upp i träningsdata och testdata. Därefter tränades modellen på träningsdatan och testades sedan på data som modellen inte sett tidigare.
Bibliotek:
•	Pandas 
•	Matplotlib 
•	Scikit-learn 

Eftersom jag redan har erfarenhet av Python var det naturligt att arbeta i Visual Studio Code istället för notebook-miljö, så jag valde därför att bygga projektet som ett vanligt Python-program.

Resultat och utvärdering
Modellen testades på testdatan och gav bra resultat.
Jag använde följande metoder:
•	MSE (Mean Squared Error) 
•	R² Score 
Resultat:
•	MSE: 1.17 
•	R² Score: 1.00 
Det visar att modellen passade datan mycket bra och kunde göra träffsäkra uppskattningar.
Modellen kunde även användas för att förutsäga nya värden:
•	3 timmar → cirka 50 poäng 
•	5 timmar → cirka 64 poäng 
•	8 timmar → cirka 84 poäng 

Jag vidareutvecklade även projektet så att användaren kan skriva in flera värden samtidigt. Programmet visar då dessa resultat som röda punkter i diagrammet.
De röda punkterna representerar alltså användarens egna inmatningar medan de blå punkterna visar originaldatan.
Reflektion
Projektet visar hur maskininlärning kan användas för att göra prognoser utifrån tidigare data.
I verkligheten hade ett riktigt dataset varit större och mer komplext, eftersom studieresultat också påverkas av exempelvis sömn, motivation, stress, tidigare kunskap, studiemiljö och hälsa mm, det finns därför begränsningar i denna modell.
Men jag tycker att  projektet visar tydligt hur en enkel AI-modell kan tränas, testas och användas i praktiken. Under projektets gång funderade jag även på att bygga en webbsida där användaren kan mata in sina värden grafiskt, men på grund av tidsbrist valde jag istället att utveckla visualiseringen med diagram och flera markerade prediktioner.
Eftersom jag redan arbetar med kod till vardags och använder Python i olika sammanhang blev projektet också ett sätt att kombinera tidigare kunskap med kursens innehåll.

Sammanfattning
Eftersom jag redan har ganska mycket erfarenhet av programmering, framför allt inom Python och C#, så var själva kodandet inte det svåraste i det här projektet.
Jag har tidigare läst en tvåårig YH-utbildning där vi arbetade mycket med C# och även AI-inriktade delar, bland annat bottar i Azure. Utöver det har jag också läst flera Pythonkurser på Blekinge Tekniska Högskola, så jag hade redan en bra grund med mig in i kursen.
Det som var mest intressant för mig i det här projektet var därför inte själva programmeringen, utan att jobba mer direkt med maskininlärning. Att använda data, träna en modell, testa resultatet och sedan se hur den kan göra egna förutsägelser gjorde att AI-delen blev mer konkret.
Jag har inte följt exakt allt kursmaterial fullt ut eftersom vissa delar varit ganska grundläggande jämfört med det jag redan kan, men projektet har ändå varit roligt och gett mig en bra repetition.
Det gav mig också några nya idéer kring hur liknande lösningar skulle kunna användas på jobbet framöver.
