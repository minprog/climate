# Climate

![](temperature.png)

Laten we een steentje bijdragen aan de klimaatdiscussie en data analyseren die door de ECA (European Climate Assessment) [beschikbaar](http://eca.knmi.nl/dailydata/predefinedseries.php) wordt gemaakt in grote data files. We beperken ons tot data die de maximumtemperatuur beschrijft voor elke dag in De Bilt sinds 1901.

## Notebooks

Om je voor te bereiden op Netwerk Analyse en verschillende andere vervolgvakken, maak je nu alvast kennis met Jupyter Notebooks. In een notebook kun je programmeren, maar je kunt er ook teksten en plaatjes bij zetten. Een ideale omgeving om de resultaten van jouw programma te presenteren, maar ook een ideaal formaat voor vakken (zoals dit vak) om opdrachten in te verspreiden. Om notebooks te kunnen gebruiken moet je eerst Jupyter geïnstalleerd hebben.

## De notebook-server opstarten

Je runt jupyter notebook in de cs50 IDE d.m.v.

    jupyter notebook

Klik vervolgens op de link met `vfs.cloud9.us-west-2.amazonaws.com` erin. Er zijn hier drie tabjes: Files, Running, en Clusters. We hebben nu enkel de eerste nodig. Navigeer binnen Files naar een plek waar je jouw werk wilt opslaan. Dit zijn simpelweg de mappen op jouw computer, dus je kan altijd een nieuwe map aanmaken voor jouw werk. Zodra je bent aangekomen, klik je rechtsboven op het dropdown-menu `new`. Kies hier voor een Python3 notebook. Dan opent er een nieuw tabblad met daarin een nieuwe notebook.

Voor we beginnen, ga linksboven naar het dropdown-menu file en klik rename. Noem je nieuwe notebook: auto. In jouw notebook heb je zogenaamde cells. Dat zijn vakken waar je zowel code als tekst kan schrijven. Aangezien we een Python 3 notebook hebben, kunnen we Python3 code schrijven. Probeer maar eens: `print(3 * 4)`. Voer je dit in de cell, en druk je vervolgens op shift+enter (zo run je een cell), dan zie je direct onder de cell de uitkomst! Druk je enkel op enter, dan krijg je een extra regel binnen de cell.

Nieuwe cells kun je aanmaken met de knoppen bovenin het scherm, en je kan ze ook verplaatsen. Uitkomsten van cells zijn beschikbaar in andere cells, zo kun je verder werken met eerdere berekeningen. Let wel, cells updaten niet automatisch als je een andere cell runt. Je zal de cells of handmatig opnieuw moeten runnen of meerdere tegelijk via het dropdown menu Cell.

Behalve code, kunnen we ook tekst schrijven. Dit gaat in Markdown. Dat is een simpel mark-up taaltje (vandaar ook de naam). Zo kun je kopjes aanmaken met hekjes. Bijvoorbeeld # Klimaat creeërt een grote kop met de tekst Klimaat. Voeg je meer hekjes toe, dan krijg je een steeds kleiner kopje. Er zijn meer dingen die je kan doen, zoals links toevoegen, dikgedrukte tekst etc. Spiek maar even in de opdrachten straks!


## Wat moet je doen

Hier ga je data analyseren door bestanden in te lezen, te verwerken en weg te schrijven. Zie [de theoriepagina over het inlezen en schrijven van bestanden](/theory/io).

De distro voor deze opdracht download je zo:

    wget https://github.com/minprog/climate/raw/2020/climate.zip
    unzip climate.zip
    rm climate.zip
    mv distro climate
    cd climate

Bovenstaande moet je maar één keer doen!

Je start Jupyter Notebook in de CS50 IDE door middel van:

    jupyter notebook

Daarna open je de (hele lange) URL die daar vermeld staat. Vervolgens kun je via **File** > **Open** het bestand `climate.ipynb` openen om in te werken. Je kunt dit bestand steeds opslaan en later opnieuw openen om in verder te werken. Is de Jupyter-server gestopt? Gebruik dan nogmaals bovenstaande commando om de server weer te starten.


## Probleemanalyse ##

De vier opdrachtjes in Climate zijn zeer geschikt voor een probleemanalyse volgens het [stappenplan](/steps). Hierbij enkele aanwijzingen om de analyse goed te doen.

**Gebruik de informatie uit het college en de hints**

Bij de preprocessing-stap is een regel code gegeven, die de inputfile en de outputfile opent. Deze lijkt erg op de regel in de [uitleg over file IO](/theory/io) die gelinkt is in de opdracht. Als je daar kijkt zie je hoe je regels uit één file naar een andere file kunt schrijven. Gebruik dit als basis!

Naast het simpelweg kopiëren van de data moeten er twee dingen gebeuren:

- een aantal regels moet worden overgeslagen
- elke regel moet worden *getransformeerd* (kennelijk moeten de spaties worden weggehaald)

Voor het overslaan van X regels moet je dus eigenlijk weten wat het regelnummer is terwijl je aan het loopen bent. Helaas kun je dat niet opvragen met zoiets als "line.number", maar je kunt wel degelijk zelf het regelnummer bijhouden in de loop! Maak een extra variabele aan om dit bij te houden.

Voor de transformatie van elke regel is het zinvol om de hints uit de opdracht te kijken. Zoek op wat `str.split` en `str.strip` betekenen en bedenk hoe je die zou kunnen gebruiken. Gebruik misschien even "print" om te kijken of je transformaties goed werken. Of open de output-CSV-file apart in de notebooks-omgeving om te kijken of het gelukt is (en vooral om te kijken wat er nog beter kan).

Over het wegschrijven van CSV-files wordt uitgebreid gesproken in David's college. Je kunt zijn csv.writer gebruiken om een rijtje data weg te schrijven. Alles dat je daarvoor nodig hebt zijn een aantal variabelen die gevuld zijn met informatie (zoals de datum en de temperatuur van één dag).

**Deel het probleem op**

Zoek naar manieren om het probleem op te splitsen in onafhankelijke delen. In deze opdracht is dit niet vaak mogelijk, maar bij Vraag 1 kan het sowieso wel: je kunt eerst de data analyseren en dan pas nadenken over hoe je een "datum" netjes kunt opschrijven.

**Maak voorbeeldproblemen**

Stap 1 van de [probleemanalyse](/steps) is het maken van eigen voorbeelden waarmee je straks een algoritme kunt ontwikkelen. Dat is bij deze opdracht belangrijker dan ooit. De datafile die je hebt gekregen is erg groot, dus door er naar te kijken krijg je niet snel een goed beeld van het probleem.

Als je kijkt naar Vraag 1 over de meest extreme temperaturen, dan kun je ook zeggen: stel ik heb een datafile voor slechts 10 dagen, hoe vind ik dan de extreme temperaturen? Besef daarbij dat 4 dingen gevraagd worden: max/min temperatuur, en voor beide de datum.

Als je maar 10 regels hebt kun je hier veel makkelijker zelf een tabelletje voor maken, bijvoorbeeld in Word, Excel of Numbers.

| loopstap | TX |     DATE | hoogste tot nu toe |    datum | laagste tot nu toe |    datum |
| -------: | -: | -------: | -----------------: | -------: | -----------------: | -------: |
|        1 |  5 | 20010101 |                  5 | 20010101 |                  5 | 20010101 |
|        2 |  4 | 20010102 |                  5 | 20010101 |                  4 | 20010102 |
|        3 |  3 | 20010103 |                  5 | 20010101 |                  3 | 20010103 |
|        4 |  4 | 20010104 |                  5 | 20010101 |                  3 | 20010103 |
|        5 |  2 | 20010105 |                  5 | 20010101 |                  2 | 20010105 |
|        6 | -8 | 20010106 |                  5 | 20010101 |                 -8 | 20010106 |
|        7 | -8 | 20010107 |                  5 | 20010101 |                 -8 | 20010106 |
|        8 |  6 | 20010108 |                  6 | 20010108 |                 -8 | 20010106 |
|        9 | 10 | 20010109 |                 10 | 20010109 |                 -8 | 20010106 |
|       10 | 11 | 20010110 |                 11 | 20010110 |                 -8 | 20010106 |

De kolommen "TX" en "DATE" zijn vergelijkbaar met de data uit de inputfile (we hebben de data zelf verzonnen in dit geval). Daarnaast hebben we voor elke regel de 4 gevraagde gegevens bijgehouden.

Let goed op dat er staat **tot nu toe**. Als je een loop schrijft dan ga je altijd **per regel** door de data. Je computer kan niet vooruit- of achteruit kijken! Op elk moment in de loop kun je dus niet anders dan een conclusie trekken over de data die je **tot dat moment** gezien hebt!

Ook voor de andere opdrachten kun je dergelijke tabelletjes maken. Daarmee kun je vóórdat je gaat programmeren aantonen dat je een algoritme hebt dat "werkt". Lukt het niet om te bedenken wat er in de tabel moet? Maak je tabel dan zo goed mogelijk (zet er alvast voorbeelddata in) en spreek met een assistent.


## Testen

Check na het maken van de opdracht of deze aan de eisen voldoet:

    check50 -l minprog/climate/2020
