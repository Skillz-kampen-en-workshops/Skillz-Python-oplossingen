# OPDRACHT: gegeven een lijst van lijsten, maak een nieuwe lijst die de vlakke versie is van de gegeven lijst
#
# Wat is een vlakke lijst? Een lijst waarin geen lijsten meer voorkomen, maar alleen getallen. Bijvoorbeeld:
# [1, 2, 3, [4, 5, 6], 7, 8, 9] wordt [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, [4, 5, 6],[ 7, 8, 9]] wordt [1, 2, 3, 4, 5, 6, 7, 8, 9]
# zorg ervoor dat je programma ook werkt als de lijst leeg is of als de lijst maar uit 1 element bestaat
# als je dit programma uitvoert, zal je functie getest worden op een aantal voorbeelden. Zo kun je zien
# of je programma werkt of niet


# deze functie kan je gebruiken in je programma
def is_vlak(lijst):
    """
    Controleer of de gegeven lijst een vlakke lijst is. Een vlakke lijst bevat geen lijsten meer, maar alleen getallen.

    :param lijst: de lijst die gecontroleerd moet worden
    :return: True als de lijst vlak is, False als de lijst niet vlak is
    """
    return not any(type(elem) == list for elem in lijst)


# deze functie moet je invullen

def lijst_vlak_maken(lijst):
    """
    Maak een nieuwe lijst die de vlakke versie is van de gegeven lijst. Een vlakke lijst bevat geen lijsten meer,
    maar alleen getallen. Gebruik een return statement om de nieuwe lijst terug te geven. De elementen moeten in
    dezelfde volgorde in de nieuwe lijst staan als in de gegeven lijst.

    TIP: het type van een variabele kan je controleren met de functie type()
    TIP: de functie extend() kan je gebruiken om een lijst te verlengen met een andere lijst

    :param lijst: de lijst die gecontroleerd moet worden
    :return: de vlakke versie van de gegeven lijst
    """
    while not is_vlak(lijst):
        for elem in lijst:
            if type(elem) == list:
                index = lijst.index(elem)
                for i in range(len(elem)):
                    lijst.insert(index, elem[i])
                    index += 1
                lijst.remove(elem)
    return lijst

#####################################################################################
# De code hieronder test of je programma werkt. Je hoeft hier niets aan te veranderen
#####################################################################################


def check_lijst(lijst, vlakke_lijst):
    try:
        gegeneerde_lijst = lijst_vlak_maken(lijst.copy())
        assert gegeneerde_lijst == vlakke_lijst
        print("OK: lijst_vlak_maken({}) werkt".format(lijst))
    except AssertionError:
        print("Fout: lijst_vlak_maken({}) geeft \n {} \n maar moet \n {} \n teruggeven".format(lijst, gegeneerde_lijst,
                                                                                               vlakke_lijst))
    except Exception as e:
        print("Fout: lijst_vlak_maken({}) geeft een foutmelding: {}".format(lijst, e))
    print("")


# maak een lijst met voorbeelden die je wilt testen
lijsten = [
    [1, 2, 3, [4, 5, 6], 7, 8, 9],
    [1, 2, 3, [4, 5, 6], [7, 8, 9]],
    [1, 2, 3, [4, 5, 6], [7, 8, 9], [10, 11, 12]],
    # verschillende dieptes
    [1, 2, 3, [4, 5, 6], [7, 8, 9], [10, 11, [12, 13, 14]]],
    [1, 2, 3, [4, 5, 6], [7, 8, 9], [10, 11, [12, 13, [14, 15, 16]]]],
    # lege lijst
    [],
    # lijst met 1 element
    [1],
    # lijst met 1 lijst
    [[1, 2, 3]],
    # lijst met 1 lijst met 1 lijst
    [[[1, 2, 3]]],
]

# maak een lijst met de vlakke versies van de lijsten hierboven
vlakke_lijsten = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    # verschillende dieptes
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    # lege lijst
    [],
    # lijst met 1 element
    [1],
    # lijst met 1 lijst
    [1, 2, 3],
    # lijst met 1 lijst met 1 lijst
    [1, 2, 3],
]

# test alle voorbeelden
for i in range(len(lijsten)):
    check_lijst(lijsten[i], vlakke_lijsten[i])
