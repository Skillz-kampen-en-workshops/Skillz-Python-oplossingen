# In deze opdracht ga je op zoek naar verdachte bankrekeningen. Je krijgt een lijst met bankrekeningen en een aantal
# overschrijvingen. Je moet de bankrekeningen die verdacht zijn, teruggeven.
# Een overschrijving bestaat uit een bedrag en een andere bankrekening. Als het geld ontvangen wordt, is het positief,
# als het geld wordt overgemaakt, is het negatief.
# Een bankrekening is verdacht als de hoeveelheid geld dat wordt gestort op de rekening groter is dan 1M euro.
#
# de input van de functie is een lijst met bankrekeningen en een lijst met overschrijvingen,
# bijvoorbeeld:
# bankrekeningen = ["BE1234567890", "BE9876543210"]
# overschrijvingen = [ [ (50000, "BE124897897"), (-100000, "BE9876543210") ], [ (1000000, "BE1234567890") ] ]
#   Dit betekent dat er 2 bankrekeningen zijn, BE1234567890 en BE9876543210. Er zijn 2 overschrijvingen voor de eerste
#   bankrekening, 50000 euro wordt ontvangen van BE124897897 en 100000 euro wordt gestort op BE9876543210.
#   Voor de tweede bankrekening is er 1 overschrijving, 1000000 euro wordt ontvangen van BE1234567890.


def verdachte_bankrekeningen(bankrekeningen, overschrijvingen):
    """
    geef een lijst terug met alle verdachte bankrekeningen. Een bankrekening is verdacht als de hoeveelheid geld
    die wordt gestort op de rekening groter is dan 1M euro. Gebruik een return.
    :param bankrekeningen: lijst met bankrekeningen
    :param overschrijvingen: lijst met overschrijvingen van de vorm (bedrag, andere_bankrekening). Een positief bedrag
    betekent dat het geld ontvangen wordt, een negatief bedrag betekent dat het geld wordt overgemaakt.
    :return: lijst met verdachte bankrekeningen
    """
    DREMPEL = 1000000
    alle_verdachte_bankrekeningen = []
    for index in range(len(bankrekeningen)):
        bankrekening = bankrekeningen[index]
        overschrijvingen_van_bankrekening = overschrijvingen[index]
        totaal_bedrag = 0
        for overschrijving in overschrijvingen_van_bankrekening:
            if overschrijving[0] > 0:
                totaal_bedrag += overschrijving[0]
        if totaal_bedrag > DREMPEL:
            alle_verdachte_bankrekeningen.append(bankrekening)

    return alle_verdachte_bankrekeningen


########### HIER EINDIGT DE OPDRACHT ###########
########### HIER START DE TESTCODE #############
########### PAS HIERONDER NIETS AAN ############


alle_data = {}

# test 1: eenvoudig geval dat niet verdacht is
rekening = "BE1234567890"
overschrijving = [(50000, "BE124897897"), (-100000, "BE9876543210")]
alle_data.update({rekening: overschrijving})

rekening = "BE9876743210"
overschrijving = [(100000, "BE1234567890"), (500000, "BE124897897"), (-10000, "BE9876543210")]
alle_data.update({rekening: overschrijving})

# test 2: eenvoudig geval dat wel verdacht is
rekening = "BE9876543210"
overschrijving = [(1000000, "BE1234567890"), (500000, "BE124897897"), (-100000, "BE9876543210")]
alle_data.update({rekening: overschrijving})

rekening = "BE1234567890"
overschrijving = [(2500000, "BE1234567890"), (700000, "BE124897897"), (-10000, "BE9876543210")]
alle_data.update({rekening: overschrijving})

# test 3: geval zonder overschrijvingen
rekening = "BE124897897"
overschrijving = []
alle_data.update({rekening: overschrijving})

# test 4: geval met 1M euro overmaking, en dus niet verdacht
rekening = "BE124897897"
overschrijving = [(-1000000, "BE1234567890"), (-50000, "BE78784548")]
alle_data.update({rekening: overschrijving})

# test 5: geval waarbij alles opgeteld minder is dan 1M euro, maar er toch stortingen zijn voor meer dan 1M euro
rekening = "BE7894457845"
overschrijving = [(-500000, "BE1234567890"), (1000000, "BE9876543210"), (500000, "BE124897897"),
                  (-1000000, "BE9876543210")]
alle_data.update({rekening: overschrijving})

try:
    alle_data_list = list(alle_data.items())
    bankrekeningen = [x[0] for x in alle_data_list]
    overschrijvingen = [x[1] for x in alle_data_list]
    verdacht = verdachte_bankrekeningen(bankrekeningen, overschrijvingen)
    assert type(verdacht) == list
except AssertionError:
    print("\033[91m" + f"Je functie moet een lijst teruggeven, maar geeft het type ´´{type(verdacht)}´´ terug." + "\033[0m")
    exit(1)
except Exception as e:
    print("\033[91m" + "Je functie werkt niet. Er is een fout opgetreden: " + str(e) + "\033[0m")
    exit(1)

antwoord = {"BE9876543210", "BE1234567890", "BE7894457845"}

if set(verdacht) == antwoord:
    # print in groen
    print("\033[92m" + "Tests geslaagd! Je funtie werkt" + "\033[0m")
else:
    # print in rood
    print("\033[91m" + "Tests mislukt. Je functie werkt niet." + "\033[0m")
    vals_positief = set(verdacht) - antwoord
    vals_negatief = antwoord - set(verdacht)
    if len(vals_positief) > 0:
        print("Volgende bankrekeningen beschouw je verdacht, maar dat zijn ze niet: ")
        for bankrekening in vals_positief:
            print(bankrekening)
            print("De overschrijvingen zijn: ")
            for overschrijving in alle_data[bankrekening]:
                print(overschrijving)
            print(" ------------------ ")
        print("")
    if len(vals_negatief) > 0:
        print("Volgende bankrekeningen beschouw je niet verdacht, maar dat zijn ze wel: ")
        for bankrekening in vals_negatief:
            print(bankrekening)
            print("De overschrijvingen zijn: ")
            for overschrijving in alle_data[bankrekening]:
                print(overschrijving)
            print(" ------------------ ")
