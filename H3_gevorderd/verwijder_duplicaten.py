# OPDRACHT: gegeven een lijst, waar mogelijk sommige getallen dubbel voorkomen,
# verwijder de duplicaten en geef de lijst terug. Je moet telkens het eerste
# voorkomen van een getal laten staan. Al de andere voorkomens moeten verwijderd
# worden.

def verwijder_duplicaten(lijst):
    """
    Verwijdert alle duplicaten uit een lijst. Het eerste voorkomen van een getal moet blijven staan.
    Al de andere voorkomens moeten verwijderd worden. Gebruik een return statement om de lijst terug te geven.
    :param lijst: een lijst met getallen die mogelijk duplicaten bevat
    :return: een lijst met alle duplicaten verwijderd
    """
    huidige_index = 0
    while huidige_index < len(lijst):  # of for huidige_index in range(len(lijst)):
        getal = lijst[huidige_index]
        # kijk of getal al eerder voorkomt in de lijst
        if getal in lijst[:huidige_index]:
            lijst.pop(huidige_index)
            # OPGEPAST: lijst.remove verwijdert het EERSTE voorkomen van getal in lijst, dus is niet geschikt
            # je kan ook de lijst opnieuw maken door twee stukken te nemen:
            # lijst = lijst[:huidige_index] + lijst[huidige_index + 1:]
        else:
            huidige_index += 1
    return lijst


#################################################
# DE CODE HIERONDER TEST JE PROGRAMMA ###########
# NIET AANPASSEN ################################

def check_antwoord(lijst, antwoord):
    try:
        uitkomst = verwijder_duplicaten(lijst.copy())
        assert uitkomst == antwoord
        # print in het groen
        print("\033[92m" + f"OK: verwijder_duplicaten({lijst}) geeft {uitkomst}" + "\033[0m")
    except AssertionError:
        # print in het rood
        print("\033[91m" + f"FOUT: verwijder_duplicaten({lijst}) geeft {uitkomst} maar moet {antwoord} geven" + "\033[0m")
    except Exception as e:
        # print in rood
        print("\033[91m" + f"ERROR: verwijder_duplicaten({lijst}) geeft een fout: {e}" + "\033[0m")
    print("")

# voorbeelden van lijsten
voorbeelden = [
    [], [20], [2, 3, 2, 5, 2, 3, 7],
    [2, 3, 2, 5, 2, 7, 2, 8, 2],
    [2, 2, 5, 4, 7, 8, 1],
    [10, 10, 10, 10, 10]
]

oplossingen = [
    [], [20], [2, 3, 5, 7],
    [2, 3, 5, 7, 8],
    [2, 5, 4, 7, 8, 1],
    [10]
]

for voorbeeld, oplossing in zip(voorbeelden, oplossingen):
    check_antwoord(voorbeeld, oplossing)