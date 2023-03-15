# OPDRACHT: maak twee functies die een lijst van getallen sorteren van groot naar klein. We willen niet zomaar een
# functie schrijven, maar we willen een functie schrijven die ook heel snel is, en goed werkt voor grote lijsten.
# Daarvoor gaan we twee speciale methodes gebruiken: bubble sort en selection sort. Dit zijn twee methodes die je
# kan gebruiken om lijsten te sorteren. Je kan ze vinden op Wikipedia of YouTube. Als we deze twee methodes
# gemaakt hebben, dan kunnen we ze vergelijken. We kunnen kijken welke methode het snelst is, en welke methode
# het beste werkt voor grote lijsten. Daarvoor zullen we hun uitvoeringstijd meten. We zullen dit ook vergelijken
# met quicksort, een meer ingewikkelde methode die je ook kan gebruiken om lijsten te sorteren en die vaak in het
# echt gebruikt wordt.

# dit zijn de packages die je nodig hebt om de uitvoeringstijd te meten
import time
import random

from matplotlib import pyplot as plt


# deze functies kan je gebruiken in de opdracht
def gesorteerd(lijst):
    """
    Controleer of de lijst gesorteerd is van groot naar klein.
    :param lijst: een lijst met getallen
    :return: True als de lijst gesorteerd is, anders False
    """
    return all(lijst[i] >= lijst[i + 1] for i in range(len(lijst) - 1))


# deze functies moet je invullen
def bubble_sort(lijst):
    """
    Sorteer de lijst van groot naar klein met de bubble sort methode. Je mag de ingebouwde functie 'sort' niet gebruiken.

    STAPPENPLAN:
    1. Begin bij het eerste element van de lijst en kijk of het groter is dan het volgende element. Als dat zo is,
    dan wissel je de twee elementen van plaats. Is dit niet zo, dan ga je naar stap 2.
    2. Ga naar het volgende element en herhaal stap 1.
    3. Herhaal stap 1 tot je bij het laatste element bent. De laatste index mag je negeren, want je hebt dan geen
    volgend element meer.
    4. Als je aan het einde van de lijst ben, ga je terug naar het begin en herhaal je stap 1 tot 3. Dit doe je
    zolang er nog elementen zijn die gewisseld moeten worden, dus zolang de lijst nog niet gesorteerd is.
    5. Als laatste gebruik je een return statement om de gesorteerde lijst terug te geven.
    """
    while not gesorteerd(lijst):  # herhaal tot de lijst gesorteerd is
        for i in range(len(lijst) - 1):  # loop door de lijst
            if lijst[i] < lijst[i + 1]:     # als het eerste element groter is dan het volgende element
                lijst[i], lijst[i + 1] = lijst[i + 1], lijst[i]  # wissel de elementen van plaats

    return lijst  # return de gesorteerde lijst


def insertion_sort(lijst):
    """
    Sorteer de lijst van groot naar klein met de insertion sort methode. Je mag de ingebouwde functie 'sort'
    niet gebruiken.

    STAPPENPLAN:
    1. Begin bij het tweede element van de lijst en kijk of het groter is dan het vorige element. Als dat zo is,
    dan wissel je de twee elementen van plaats. Is dit niet zo, dan ga je naar stap 2.
    2. Ga naar het volgende element en kijk of het groter is dan het vorige element.
        2a. Als het groter is, dan wissel je de twee elementen van plaats. Bekijk nu het 'nieuwe' vorige element
        en herhaal stap 2a tot het vorige element niet groter is dan het nieuwe vorige element.
            TIP: gebruik voor 2a een while loop.
        2b. Als het niet groter is, dan ga je naar stap 3.
    3. Herhaal stap 2 tot je bij het laatste element bent.
    4. Als laatste gebruik je een return statement om de gesorteerde lijst terug te geven.
    """
    for i in range(1, len(lijst)):  # loop door de lijst
        j = i
        while j > 0 and lijst[j] > lijst[j - 1]:  # zolang het element groter is dan het vorige element
            lijst[j], lijst[j - 1] = lijst[j - 1], lijst[j]  # wissel de elementen van plaats
            j -= 1

    return lijst  # return de gesorteerde lijst


def merge_sort(lijst):
    """
    Sorteer de lijst van groot naar klein met de merge sort methode. Je mag de ingebouwde functie 'sort'
    niet gebruiken. Je gaat hier gebruik maken van recursie.

    OPGEPAST: dit is een ingewikkelde methode, dus je hoeft deze niet te maken als je dat niet wil. Je kan
    deze functie overslaan. De rest van het programma werkt ook zonder deze functie.

    STAPPENPLAN:
    1. Als de lijst maar 1 element heeft, dan is de lijst al gesorteerd. Je hoeft dan niets te doen.
    2. Als de lijst meer dan 1 element heeft, dan moet je de lijst in twee delen splitsen. Je kan dit doen door
    bijvoorbeeld de lijst in twee helften te splitsen.
    3. Sorteer de twee delen van de lijst met recursie.
    4. Voeg de twee delen samen. Je kan dit doen door de twee delen te vergelijken en de kleinste elementen
    van de twee delen in een nieuwe lijst te plaatsen. Als je een element hebt toegevoegd aan de nieuwe lijst,
    dan moet je het verwijderen uit de lijst waar het vandaan kwam.
    5. Als je de twee delen hebt samengevoegd, dan is de lijst gesorteerd. Je hoeft dan niets meer te doen.
    6. Als laatste gebruik je een return statement om de gesorteerde lijst terug te geven.

    RECURSIE: Wat is recursie? Recursie is een manier om een functie te schrijven die zichzelf kan aanroepen.
    In dit geval roep je de functie 'merge_sort' aan in de functie 'merge_sort'. Dit is een recursieve functie.
    Schrijf je dus in de functie
        >> lijst = merge_sort(lijst)
    dan roep je de functie 'merge_sort' aan in de functie
    'merge_sort'. Dat betekent dat 'lijst' gesorteerd zal zijn na het uitvoeren van deze lijn.
    """
    if len(lijst) == 1:
        return lijst
    else:
        midden = len(lijst) // 2
        lijst1 = merge_sort(lijst[0:midden])
        lijst2 = merge_sort(lijst[midden:len(lijst)])
        # lijst1 en lijst2 zijn nu gesorteerd
        nieuwe_lijst = []  # maak een nieuwe lege lijst aan en voeg de twee gesorteerde lijsten samen
        while lijst1 and lijst2:  # zolang beide lijsten nog elementen bevatten
            if lijst1[0] > lijst2[0]:  # als het eerste element van lijst1 groter is dan het eerste element van lijst2
                nieuwe_lijst.append(lijst1.pop(0))  # voeg het eerste element van lijst1 toe aan de nieuwe lijst
            else:  # als het eerste element van lijst2 groter is dan het eerste element van lijst1
                nieuwe_lijst.append(lijst2.pop(0))  # voeg het eerste element van lijst2 toe aan de nieuwe lijst
        if lijst1:
            nieuwe_lijst.extend(lijst1)
        if lijst2:
            nieuwe_lijst.extend(lijst2)
        return nieuwe_lijst


def tijd_sinds_start(start):
    """
    Geef het aantal seconden sinds 'start' terug. We zullen hier niet de gewone klok gebruiken, maar de
    'high performance' klok van Python. Deze klok is veel nauwkeuriger dan de gewone klok. Je kan deze aanroepen met
    time.perf_counter().
    """
    nu = time.perf_counter()
    return nu - start


# Hieronder staat de code die het programma uitvoert. Deze zal kijken of je functies juist zijn en we zullen ook
# bekijken hoe lang het duurt om de lijsten te sorteren met de verschillende methodes, om zo te kunnen bepalen welke
# methode het snelst is.

#####################################################################
# PAS HIERONDER NIETS AAN ###########################################
#####################################################################

# maak een lijst met 50 willekeurige getallen
lijst = [random.randint(0, 100) for i in range(50)]

# sorteer de lijst met de bubble sort methode
bubble_correct = False
try:
    gesorteerde_lijst = bubble_sort(lijst.copy())
    assert gesorteerde_lijst == sorted(lijst, reverse=True)
    # print in het groen
    bubble_correct = True
    print("\033[92mDe bubble sort methode is correct.\033[0m")
except AssertionError:
    # print in het rood
    print("\033[91mDe bubble sort methode is niet correct.\033[0m")
    print(gesorteerde_lijst)
except Exception as e:
    print("Er is een fout opgetreden bij het sorteren met de bubble sort methode.")
    print(e)

insertion_correct = False
try:
    gesorteerde_lijst = insertion_sort(lijst.copy())
    assert gesorteerde_lijst == sorted(lijst, reverse=True)
    insertion_correct = True
    print("\033[92mDe insertion sort methode is correct.\033[0m")
except AssertionError:
    # print in het rood
    print("\033[91mDe insertion sort methode is niet correct.\033[0m")
    print(gesorteerde_lijst)
except Exception as e:
    print("Er is een fout opgetreden bij het sorteren met de insertion sort methode.")
    print(e)


merge_correct = False
if merge_sort([1]) is None:
    print("De merge sort methode is niet geschreven en wordt genegeerd.")
    merge_correct = True
else:
    try:
        gesorteerde_lijst = merge_sort(lijst.copy())
        assert gesorteerde_lijst == sorted(lijst, reverse=True)
        # print in het groen
        merge_correct = True
        print("\033[92mDe merge sort methode is correct.\033[0m")
    except AssertionError:
        # print in het rood
        print("\033[91mDe merge sort methode is niet correct.\033[0m")
        print(gesorteerde_lijst)
    except Exception as e:
        print("Er is een fout opgetreden bij het sorteren met de merge sort methode.")
        print(e)


if not (bubble_correct and insertion_correct and merge_correct):
    exit()

if bubble_correct and insertion_correct and merge_correct:
    # maak een lijst met 10 000 willekeurige getallen
    lijst = [random.randint(0, 1000) for i in range(int(1e4))]
    print("\n\nTest met een lijst van {} getallen.".format(len(lijst)))
    # sorteer de lijst met de bubble sort methode
    print("\nBubble sort wordt nu uitgevoerd...")
    start = tijd_sinds_start(0)
    bubble_sort(lijst.copy())
    print("Bubble sort duurde {} seconden.".format(tijd_sinds_start(start)))

    # sorteer de lijst met de selection sort methode
    print("\nInsertion sort wordt nu uitgevoerd...")
    start = tijd_sinds_start(0)
    insertion_sort(lijst.copy())
    print("Insertion sort duurde {} seconden.".format(tijd_sinds_start(start)))

    if merge_sort([1]) is not None:
        # sorteer de lijst met de merge sort methode
        print("\nMerge sort wordt nu uitgevoerd...")
        start = tijd_sinds_start(0)
        merge_sort(lijst.copy())
        print(" Merge sort duurde {} seconden.".format(tijd_sinds_start(start)))

    # sorteer de lijst met de Python methode
    print("\nPython sort wordt nu uitgevoerd...")
    start = tijd_sinds_start(0)
    lijst = sorted(lijst, reverse=True)
    print("Python sort duurde {} seconden.".format(tijd_sinds_start(start)))


