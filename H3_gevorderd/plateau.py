# OPDRACHT: vind het langste plateau in een lijst van getallen
#
# Een plateau is een reeks getallen die gelijk zijn aan elkaar. Een plateau kan bestaan uit 1 getal, maar ook uit
# meerdere getallen. Bijvoorbeeld:
# Het langste plateau in [1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9] is [3, 3, 3] en heeft lengte 3
# Het langste plateau in [1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 9, 9] is [9, 9, 9, 9] en heeft lengte 4

# Deze functie moet je invullen

def plateau(lijst):
    """
    Gegeven een lijst van getallen, vind het langste plateau in de lijst. Een plateau is een reeks getallen die gelijk
    zijn aan elkaar. Een plateau kan bestaan uit 1 getal, maar ook uit meerdere getallen. Gebruik een return statement
    om de lengte van het langste plateau terug te geven.
    OPGEPAST: zorg ervoor dat lijsten met lengte 0 en 1 ook correct verwerkt worden.

    :param lijst: De lijst waarin het plateau gezocht moet worden
    :return: de lengte van het langste plateau
    """
    langste_plateau_dusver = 0
    lengte_huidig_plateau = 0
    index = 0
    while index < len(lijst):
        if index == 0:
            lengte_huidig_plateau += 1
        elif lijst[index] == lijst[index - 1]:
            lengte_huidig_plateau += 1
        else:
            lengte_huidig_plateau = 1
        if lengte_huidig_plateau > langste_plateau_dusver:
            langste_plateau_dusver = lengte_huidig_plateau
        index += 1

    return langste_plateau_dusver


###################################################
### DE CODE HIERONDER TEST JE PROGRAMMA         ###
### NIET AANPASSEN                              ###
###################################################

def check_antwoord(lijst, antwoord):
    try:
        uitkomst = plateau(lijst.copy())
        assert uitkomst == antwoord
        # print in het groen
        print("\033[92m" + f"OK: plateau({lijst}) geeft {uitkomst}" + "\033[0m")
    except AssertionError:
        # print in het rood
        print("\033[91m" + f"FOUT: plateau({lijst}) geeft {uitkomst} maar moet {antwoord} geven" + "\033[0m")
    except Exception as e:
        # print in rood
        print("\033[91m" + f"ERROR: plateau({lijst}) geeft een fout: {e}" + "\033[0m")
    print("")


# lijst van voorbeelden om te testen
voorbeelden = [
    [1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9],
    [1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 9, 9],
    [1, 2, 3, 3, 3, 4, 5, 6, 6, 7],
    # niet-gesorteerde lijst
    [1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 9, 9, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 8, 9, 9, 9, 9],
    [5, 9, 7, 8, 8, 8, 8, 8, 4, 4, 3, 6, 4, 4, 4, 4, 8, 2, 2, 2, 4, 5, 10, 11],
    # lege lijst
    [],
    # lijst met 1 element
    [1]
]

# lijst van juiste antwoorden
antwoorden = [3, 4, 3, 4, 5, 0, 1]

for voorbeeld, antwoord in zip(voorbeelden, antwoorden):
    check_antwoord(voorbeeld, antwoord)
