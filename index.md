# Climate

![](temperature.png)

Laten we een steentje bijdragen aan de klimaatdiscussie en data analyseren die door de ECA (European Climate Assessment) [beschikbaar](https://www.ecad.eu/dailydata/predefinedseries.php) wordt gemaakt in grote data files. We beperken ons tot data die de maximumtemperatuur beschrijft voor elke dag in De Bilt sinds 1901.

**Let op: voor deze opdracht krijg je punten per gemaakte opdracht, en niet op basis van een review.**

## Notebooks

Om je voor te bereiden op het vak Netwerkanalyse van volgende periode, en voor verschillende andere vervolgvakken, maak je nu alvast kennis met Jupyter Notebooks. In een notebook kun je programmeren, maar je kunt er ook teksten en plaatjes bij zetten. Een ideale omgeving om de resultaten van jouw programma te presenteren, maar ook een ideaal formaat voor vakken (zoals dit vak) om opdrachten in te verspreiden. Om notebooks te kunnen gebruiken moet je eerst Jupyter geïnstalleerd hebben.


## De notebook-server opstarten

Je runt jupyter notebook d.m.v.

    jupyter notebook

Klik vervolgens op de link met `localhost` erin. Er zijn hier drie tabjes: Files, Running, en Clusters. We hebben nu enkel de eerste nodig. Navigeer binnen Files naar een plek waar je jouw werk wilt opslaan. Dit zijn simpelweg de mappen op jouw computer, dus je kan altijd een nieuwe map aanmaken voor jouw werk. Zodra je bent aangekomen, klik je rechtsboven op het dropdown-menu `new`. Kies hier voor een Python3 notebook. Dan opent er een nieuw tabblad met daarin een nieuwe notebook.

Voor we beginnen, ga linksboven naar het dropdown-menu file en klik rename. Noem je nieuwe notebook: auto. In jouw notebook heb je zogenaamde cells. Dat zijn vakken waar je zowel code als tekst kan schrijven. Probeer maar eens: `print(3 * 4)`. Voer je dit in de cell, en druk je vervolgens op shift+enter (zo **run** je een cell), dan zie je direct onder de cell de uitkomst. Pas op: druk je alleen op enter, dan krijg je een extra regel binnen de cell.

Nieuwe cells kun je aanmaken met de knoppen bovenin het scherm, en je kan ze ook verplaatsen. Uitkomsten van cells zijn beschikbaar in andere cells, zo kun je verder werken met eerdere berekeningen. Let wel, cells updaten niet automatisch als je een andere cell runt. Je zal de cells of handmatig opnieuw moeten runnen of meerdere tegelijk via het dropdown menu Cell.

Behalve code, kunnen we ook tekst schrijven. Dit gaat in Markdown. Dat is een simpel mark-up taaltje (vandaar ook de naam). Zo kun je kopjes aanmaken met hekjes. Bijvoorbeeld # Klimaat creeërt een grote kop met de tekst Klimaat. Voeg je meer hekjes toe, dan krijg je een steeds kleiner kopje. Er zijn meer dingen die je kan doen, zoals links toevoegen, dikgedrukte tekst etc. Spiek maar even in de opdrachten straks!


## Wat moet je doen

De distro voor deze opdracht download je via deze link:

<https://github.com/minprog/climate/raw/2021/dist/climate.zip>

Zorg dat je de map op een logische plek zet waar een backup van gemaakt wordt. Dus laat 'm niet in je Downloads-map staan.

Je start Jupyter Notebook door middel van dit commando:

    jupyter notebook

Daarna open je de (hele lange) URL die daar vermeld staat. Vervolgens kun je het bestand `climate.ipynb` openen om in te werken. Je kunt dit bestand steeds opslaan en later opnieuw openen om in verder te werken. Is de Jupyter-server gestopt? Gebruik dan nogmaals bovenstaande commando om de server weer te starten.

<!--

## Testen

Check na het maken van de opdracht of deze aan de eisen voldoet:

    check50 -l minprog/climate/2021

-->
