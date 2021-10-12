# File Input & Output

In Python kan je op verschillende manieren werken met (data)bestanden.


## Open en close

Als je een bestand wil inlezen of juist wegschrijven, dan moet je dit bestand *openen* door middel van de `open()`-functie. Als je klaar bent met lezen of schrijven kun je het bestand weer netjes *sluiten* door middel van de `close()`-functie.

    # openen
    data_file = open("myfile.txt")
    
    # lees een regel en print
    print(data_file.readline())
    
    # sluiten
    data_file.close()


## With

Omdat bestanden niet te lang open moeten blijven staan is het belangrijk om ze weer te sluiten. Helaas willen we dat als programmeur nog weleens vergeten. Daarom heeft Python een speciaal construct in het leven geroepen: het `with`-statement. Als je een bestand opent met hulp van het `with`-statement zal het automatisch gesloten worden:

    with open("myfile.txt") as data_file:
        print(data_file.readline())


## Schrijven

Wil je het woord `hello` wegschrijven naar een bestand dan doe je dat zo:

    with open("myotherfile.txt", "w") as data_file:
        data_file.write("hello")

Standaard opent Python een bestand in leesmodus en kun je er dus niet naar schrijven. Om te schrijven moet je die `"w"` van write opgeven aan de functie `open`.


## Lezen en schrijven

Een bekend patroon is om uit één bestand te lezen en dan gegevens weg te schrijven naar het andere bestand.

    with open("inputfile.txt") as input_file, open("outputfile.txt", "w") as output_file:
        line = input_file.readline()
        output_file.write(line)

Bovenstaande code kopieert de eerste regel tekst van één bestand naar het andere. Er is geen filter, geen enkele aanpassing, alleen maar dat kopiëren.


## Alle regels lezen

Er zijn verschillende manieren om meerdere regels uit een bestand te lezen. De makkelijkste en gebruikelijkste is d.m.v. een for-loop. Deze stopt automatisch als je het einde van het bestand bereikt. Zo print je bijvoorbeeld de gehele inhoud van het bestand naar je scherm:

    with open("inputfile.txt") as input_file:
        for line in input_file:
            print(line)


## Oefening: een heel bestand kopiëren

Als je bovenstaande voorbeelden combineert moet je een stukje code kunnen schrijven dat een compleet tekstbestand kopieert. Probeer dit te schrijven en vergelijk je oplossing dan met een medestudent (en daarna eventueel met nog iemand). Kijk ook of het lukt dit uit te testen.
