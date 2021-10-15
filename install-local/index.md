# Installatie van Python en Jupyter

Je gaat vanaf nu werken op je eigen laptop, in plaats van via de CS50 IDE.
Volg deze stappen om te kijken of Python en Jupyter goed geinstalleerd is, en zonodig om te installeren.

# Korte versie

Voor experts hier de korte versie:

- Zorg dat Python 3.x geïnstalleerd is.
- Zorg dat het package `notebook` geïnstalleerd is.
- Check of je `jupyter notebook` kunt starten via de command line.

# 1. Check Jupyter Notebook

Kijk of Python al geinstalleerd is in de terminal:

- **Windows**  Open de "command line" of "opdrachtprompt" ([WikiHow](https://nl.wikihow.com/De-opdrachtprompt-openen-in-Windows))

- **Mac**  Open de "terminal" ([WikiHow](https://www.wikihow.com/Open-a-Terminal-Window-in-Mac))

Geef daar het commando:

        jupyter notebook

✅ Krijg je nu een uitvoer zoals de volgende? Dan is alles goed geinstalleerd.

![](starting.png)

Kopieer dan de link in het scherm (met `localhost` erin) en open deze in je webbrowser. Je bent nu helemaal klaar met dit stappenplan.

❌ Krijg je een foutmelding dat het niet gevonden kan worden? Dan is `jupyter` waarschijnlijk niet geinstalleerd. Ga dan naar stap 2. Weet je het niet zeker, check dan even met een medestudent die veel ervaring met computers heeft.

# 2. Check Python3

Open weer de command line of terminal. Geef dan het volgende commando:

    python3

✅ Krijg je zoiets als hieronder? Dan is Python wel al goed geïnstalleerd.

![](python.png)

Stop Python door het commando `exit()` te geven (met haakjes!), en ga naar stap 4 om Jupyter te installeren.

❌ Krijg je een foutmelding dat het niet gevonden kan worden? Ga dan naar stap 3.

# 3. Check Python

Open weer de command line of terminal. Geef dan het volgende commando:

    python

✅ Krijg je zoiets als hieronder? Dan is Python wel al goed geïnstalleerd. Check zéér nauwkeurig of er staat dat het Python **3** is. Dus er staat bijvoorbeeld `Python 3.8.1`, `Python 3.7.4` of `Python 3.9.1`.

Stop Python door het commando `exit()` te geven (met haakjes!), en ga naar stap 4 om Jupyter te installeren.

![](python.png)

❌ Is het de verkeerde versie van Python (versie `2.7` bijvoorbeeld) of krijg je een foutmelding dat het niet gevonden kan worden? Ga dan naar stap 5.

# 4. Installeer Jupyter notebook

Geef het volgende commando om Jupyter Notebook te installeren:

    pip3 install notebook

Krijg je een melding dat `pip3` niet gevonden kan worden, probeer dan:

    pip install notebook

Dit kan even duren omdat er software gedownload moet worden. Naderhand kun je kijken of het werkt met het commando:

    jupyter notebook

✅ Gelukt? Dan ben je klaar.

❌ Gaat dit mis? Neem dan direct contact op met de laptophelpdesk <mailto:laptops-fnwi@uva.nl> om het op te lossen.

# 5. Ga naar de laptophelpdesk

Als je hier bent uitgekomen moet waarschijnlijk Python nog geinstalleerd worden.

**Alleen voor Windows** Ga naar de website van [Python](https://www.python.org/downloads/release/python-396/) en installeer de Windows Installer (64-bit). Let op dat je het vinkje **Add Python 3.9 to PATH** aanzet!! Lukt het niet, neem contact op met de laptophelpdesk (zie onder).

![](path.png)

**Alleen voor Mac** Python zou wel degelijk geïnstalleerd moeten zijn, dus je kunt het beste direct contact opnemen met de laptophelpdesk.

✅ Gelukt? Ga dan terug naar stap 4.

❌ Niet gelukt? De laptophelpdesk kan je helpen met installeren <mailto:laptops-fnwi@uva.nl>.
