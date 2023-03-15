import random

# OPDRACHT:
# Schrijf een programma dat je een nummer doet raden tussen 0 en 10.
# Als de speler het verkeerde nummer gokt, geef je een hint dat het nummer te klein of te groot is.
# Als de speler het juiste nummer gokt, geef je een bericht dat hij/zij gewonnen heeft en stopt het spel.

# TIP: volgende functies moet je gebruiken uit de random module:
# random.randint(a, b) - kiest een willekeurig getal tussen a en b (inclusief a en b)

geheim_nummer = random.randint(1,10)
gok = int(input("Geef je gok tussen 1 en 10: "))

while geheim_nummer != gok:
    if geheim_nummer > gok:
        print("Je gekozen nummer is te klein!")
    elif geheim_nummer < gok:
        print("Je gekozen nummer is te groot")
    gok = int(input("Geef je gok tussen 1 en 10: "))

print("Juist! Je hebt het juiste nummer geraden!")