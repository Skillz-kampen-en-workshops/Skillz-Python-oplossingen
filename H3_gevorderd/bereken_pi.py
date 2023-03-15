# OPDRACHT: schrijf een programma dat de waarde van pi schat door gebruik te maken van een Monte Carlo methode.
#   Wat is een Monte Carlo methode? Een Monte Carlo methode is een methode om een probleem op te lossen
#   door het probleem te simuleren. In dit geval simuleren we het probleem van het vinden van pi door een
#   willekeurig punt te kiezen in een vierkant en te kijken of het punt ook in een cirkel ligt. Als het punt in de
#   cirkel ligt, dan is het een 'hit'. Als het punt buiten de cirkel ligt, dan is het een 'miss'. Als we dit
#   willekeurig doen, dan kunnen we de verhouding tussen de hits en de misses gebruiken om de waarde van pi te
#   schatten met de volgende formule:
#
#   pi = 4 * hits / (hits + misses)
#
#   Je moet dan natuurlijk genoeg hits en misses hebben om een goede schatting te maken. Hoe meer hits en misses,
#   hoe nauwkeuriger de schatting. Hoeveel hits en misses heb je nodig? Dat is afhankelijk van de nauwkeurigheid
#   die je wilt. Hoe nauwkeuriger, hoe meer hits en misses je nodig hebt en hoe groter de variabele 'pogingen' moet
#   zijn.

# dit zijn de packages die je nodig hebt
import random
import math


# dit zijn functies die je nodig hebt
def is_binnen_cirkel(x, y):
    """
    Deze functie kijkt na of het punt (x, y) binnen de cirkel ligt. De cirkel heeft straal 1 en ligt in het midden
    van het vierkant. De functie geeft True terug als het punt binnen de cirkel ligt en False als het punt buiten
    de cirkel ligt.
    """
    afstand = math.sqrt(x ** 2 + y ** 2)
    return afstand <= 1


def fout_op_resultaat(resultaat):
    """
    Deze functie berekent de relatieve en absolute fout van het resultaat. De relatieve fout is de absolute fout
    gedeeld door de waarde van pi. De absolute fout is de absolute waarde van het verschil tussen het resultaat
    en de waarde van pi. De functie print beide fouten op het scherm.
    """
    absolute_fout = abs(resultaat - math.pi)
    relatieve_fout = absolute_fout / math.pi
    print("--------------------------------")
    print("De absolute fout is: " + str(round(absolute_fout, 5)))
    print("De relatieve fout is: " + str(round(100 * relatieve_fout, 2)) + "%")
    print("--------------------------------")


# dit is de functie die je moet aanpassen
def bereken_pi():
    """
    Deze functie berekent de waarde van pi door gebruik te maken van een Monte Carlo methode. De functie print
    de geschatte waarde van pi op het scherm en de relatieve en absolute fout van de schatting.
    TIP: maak gebruik van de functies is_binnen_cirkel en fout_op_resultaat.
    TIP: random.random() geeft een willekeurig getal tussen 0 en 1.
    """
    """
    PSEUDOCODE:
    1. Vraag de gebruiker om het aantal pogingen dat hij wil doen.
    2. Maak een variabele 'hits' aan en zet deze op 0.
    3. Maak een variabele 'misses' aan en zet deze op 0.
    4. Maak een for-loop die 'pogingen' keer loopt.
    4a. Kies een willekeurig punt in het vierkant. Dit punt heeft x-coördinaat tussen -1 en 1 en y-coördinaat
        tussen -1 en 1. Je kan hiervoor de functie random.uniform(-1, 1) gebruiken.
    4b. Kijk na of het punt binnen de cirkel ligt. Je kan hiervoor de functie is_binnen_cirkel gebruiken.
    4c. Als het punt binnen de cirkel ligt, dan verhoog je de variabele 'hits' met 1. Anders verhoog je de
        variabele 'misses' met 1.
    5. Bereken de geschatte waarde van pi met de formule pi = 4 * hits / (hits + misses).
    6. Print de geschatte waarde van pi op het scherm en de relatieve en absolute fout van de schatting.
    """
    pogingen = int(input("Hoeveel pogingen wil je doen? "))
    hits, misses = 0, 0
    for i in range(pogingen):
        x = 2 * random.random() - 1
        y = 2 * random.random() - 1
        # alternatief: x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if is_binnen_cirkel(x, y):
            hits += 1
        else:
            misses += 1
    resultaat = 4 * hits / (hits + misses)
    print("De geschatte waarde van pi is: " + str(resultaat))
    fout_op_resultaat(resultaat)


# Voer de functie uit. Laat deze regel staan.
bereken_pi()
