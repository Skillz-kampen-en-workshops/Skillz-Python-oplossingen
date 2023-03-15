# OPDRACHT: schrijf een programma dat detecteert of een bepaald woord een palindroom is of niet
# Een palindroom is een woord dat hetzelfde is als je het achterstevoren leest. Bijvoorbeed:
# "lepel" is een palindroom, "lepel" is hetzelfde als "lepel" als je het achterstevoren leest
# "boom" is geen palindroom, "boom" is niet hetzelfde als "moob" als je het achterstevoren leest
# andere voorbeelden van palindromen zijn: "kajak", "racecar", "radar", "rotator", "rotor", "sagas", "solos",
# "stats", "tenet", "wow"

# Het programma vraag de gebruiker om een woord in te voeren. Dit is al gedaan voor jou. Je moet enkel nog de functie
# palindroom() schrijven. Deze functie moet True teruggeven als het woord een palindroom is, en False als het geen palindroom is.
# je kan de functie 'palindroom_test()' gebruiken om te testen of je programma werkt. Hiervoor geef je het woord TEST in als input.

def palindroom(woord):
    """
    PSEUDOCODE:
    1. maak een variabele 'positie_volgend_karakter' aan en zet deze op 0
    2. maak een variabele 'nog_palindroom' aan en zet deze op True
    3. herhaal zolang de volledige string nog niet onderzocht is en nog geen ongelijkheid gevonden is:
        3.1. als het karakter op positie 'positie_volgend_karakter' niet gelijk is aan het karakter op positie 'positie_volgend_karakter' achterstevoren:
            3.1.1. zet 'nog_palindroom' op False
        3.2. verhoog 'positie_volgend_karakter' met 1
    4. geef 'nog_palindroom' terug

    :param woord: het woord dat gecontroleerd moet worden. Het mag geen corner-cases bevatten, zoals spaties,
                    hoofdletters, leestekens, lege strings, ...
    :type woord: str

    :return: True als het woord een palindroom is, False als het geen palindroom is
    """
    positie_volgend_karakter = 0  # positie van het volgende karakter dat gecontroleerd moet worden
    nog_palindroom = True  # zolang nog geen ongelijkheid gevonden is, is het nog een palindroom

    # herhaal zolang de volledige string nog niet onderzocht is en nog geen ongelijkheid gevonden is
    while (positie_volgend_karakter < len(woord) / 2) and nog_palindroom:
        # als het karakter op positie 'positie_volgend_karakter' niet gelijk is aan
        # het karakter op positie 'positie_volgend_karakter' achterstevoren:
        if woord[positie_volgend_karakter] != woord[-positie_volgend_karakter - 1]:
            nog_palindroom = False  # zet 'nog_palindroom' op False
        positie_volgend_karakter += 1  # verhoog 'positie_volgend_karakter' met 1

    return nog_palindroom


############################################################################################################
# TEST FUNCTIE. PAS NIETS AAN IN DEZE FUNCTIE


def palindroom_test():
    # test of het programma werkt
    # kijk of de uitvoer een boolean is
    try:
        assert type(palindroom("lepel")) == bool
        assert type(palindroom("boom")) == bool
    except AssertionError:
        print("De functie palindroom() moet een True of False teruggeven")
        return
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")
        return

    try:
        word = "lepel"
        assert palindroom(word)
        word = "boom"
        assert not palindroom(word)
        word = "kajak"
        assert palindroom(word)
        word = "racecar"
        assert palindroom(word)
        word = "radar"
        assert palindroom(word)
        word = "rotator"
        assert palindroom(word)
        word = "rotor"
        assert palindroom(word)
        word = "sagas"
        assert palindroom(word)
        word = "solos"
        assert palindroom(word)
        word = "stats"
        assert palindroom(word)
        word = "tenet"
        assert palindroom(word)
        word = "wow"
        assert palindroom(word)
        word = "test"
        assert not palindroom(word)
        word = "computer"
        assert not palindroom(word)
    except AssertionError:
        print(f"De functie palindroom() werkt niet voor het woord '{word}'")
        return
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")
        return

    print("De functie palindroom() werkt correct")
    return

woord = input("Geef een woord: ")

if woord == "TEST":
    palindroom_test()
    exit()

if palindroom(woord):
    print("Het woord is een palindroom")
else:
    print("Het woord is geen palindroom")