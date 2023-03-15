# OPGEPAST:
# De opdracht begint vanaf de vermelding "Hier begint de opdracht"
# Laat deze import staan. Je hebt hem straks nodig
import random


# ------------------ HIER BEGINT DE OPDRACHT ----------------------
# Vul de volgende functies aan om je eigen tic-tac-toe te maken

def keuze_van_computer():
    """ OPDRACHT: gebruik een return om een willekeurig getal terug te geven van 0 tot en met 8.
        TIP: in dit bestand is het package "random" al geïmporteerd
    """
    return random.randint(0, 8)


def keuze_van_speler():
    """
    OPDRACHT: vraag aan de speler een getal tussen 1 en 9.
    Als de speler een te groot getal geeft, vraag je het nog eens.
    Gebruik een return om het antwoord terug te geven.
    TIP: gebruik een while-lus om te checken of de input juist was.
    """
    getal = int(input("Geef een getal van 1 tot en met 9."))

    while getal > 9:
        getal = int(input("Je getal is te groot! Geef een getal van 1 tot en met 9."))

    return getal


def verminder_getal(getal):
    """
    OPDRACHT: verlaag het gegeven getal met 1 en gebruik een return om het terug te geven
    TIP: gebruik hiervoor een nieuwe variabele
    """
    verminderd_getal = getal - 1
    return verminderd_getal


def niet_bezet(vakjes, vak):
    """
    OPDRACHT: ga na of een vakje al bezet is. Een vakje niet bezet als het gelijk is aan ' ' (een spatie).
    TIP: om het juiste vakje te kiezen, kan je gebruik maken van de variabele vakjes[vak]
    """
    if vakjes[vak] == ' ':
        return True
    else:
        return False
    # Korter is natuurlijk return vakjes[vak] == ' ', maar dat is minder expliciet en intuïtief


def print_uitkomst(uitkomst, winnaar):
    """
    OPDRACHT: Print de winnaar van het spel, of gelijkstand.
    De variabele 'uitkomst' bevat oftewel gelijk, oftewel 'gewonnen'. Winnaar bevat wie gewonnen is.
    TIP:
        kijk eerst of de uitkomst 'gewonnen' of 'gelijk' is. Als de uitkomst 'gelijk' is, print je 'gelijkstand'.
        Zo niet moet je bekijken wie er gewonnen heeft
    """
    if uitkomst == "gelijk":
        print('Gelijkstand!')
    elif uitkomst == 'gewonnen':
        if winnaar == "mens":
            print("Proficiat! Je bent gewonnen.")
        elif winnaar == "computer":
            print("Spijtig! Je bent verloren.")


# -------------------- HIER EINDIGT DE OPDRACHT --------------------
# Pas hieronder geen code aan !!
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
boxes = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
MENS = 'X'
COMPUTER = '0'
first_player = MENS
turn = 1
winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]


def print_board(initial=False):
    """ Print the game board. If this is the beginning of the game,
        print out 1-9 in the boxes to show players how to pick a
        box. Otherwise, update each box with X or 0 from boxes[].
    """
    board = '''
             {} | {} | {} 
            -----------
             {} | {} | {}
            -----------
             {} | {} | {} 
        '''
    print(board.format(*([x for x in range(1, 10)] if initial else boxes)))


def take_turn(player, turn):
    """ Create a loop that keeps asking the current player for
        their input until a valid choice is made.
    """

    # test verminder_getal()
    try:
        getal = verminder_getal(5)
        assert type(getal) == int, "Getal moet een integer zijn."
        assert getal == 4, "De functie verminder_getal() geeft niet het juiste resultaat."
    except AssertionError as e:
        print("\033[91m" + "Je functie verminder_getal() werkt niet correct:" + str(e) + "\033[0m")
        exit(-2)
    except Exception as e:
        print("\033[91m" + "Er zit een fout in je functie verminder_getal()." + "\033[0m")
        print(e)

    while True:
        if player is COMPUTER:
            try:
                box = keuze_van_computer()
                assert box in range(9)
            except AssertionError:
                print(
                    "\033[91m" + "\n Je functie keuze_van_computer() geeft geen getal terug tussen 0 en 8!" + "\033[0m")
                exit(-2)
            except Exception as e:
                print("\033[91m" + "\n Er zit een fout in je functie keuze_van_computer()." + "\033[0m")
                print(e)
                exit(-2)
        else:
            try:
                box = verminder_getal(keuze_van_speler())
                assert type(box) == int, \
                    "Getal moet een integer zijn. Ben je zeker dat je een getal vroeg en geen string?."
                assert box in range(9), "Getal moet tussen 1 en 9 liggen."
            except AssertionError as e:
                print("\033[91m" + "Je functie keuze_van_speler() werkt niet correct:" + str(e) + "\033[0m")
                exit(-2)
            except Exception as e:
                print("\033[91m" + "\n Er zit een fout in je functie keuze_van_speler()." + "\033[0m")
                print(e)
                exit(-2)

        try:
            nt_bezet = niet_bezet(boxes, box)
            assert type(nt_bezet) == bool, "niet_bezet() moet True of False teruggeven met een return-statement."
            assert (boxes[box] == ' ') if nt_bezet else (boxes[box] != ' '), \
                "niet_bezet() voert geen juiste vergelijking uit."
        except AssertionError as e:
            print("\033[91m" + "Je functie niet_bezet() werkt niet correct:" + str(e) + "\033[0m")
            exit(-2)
        except Exception as e:
            print("\033[91m" + "Er zit een fout in je functie niet_bezet()." + "\033[0m")
            print(e)
            exit(-2)

        if niet_bezet(boxes, box):  # initial value
            boxes[box] = player  # set to value of current player
            break
        elif player is MENS:
            print('Dit veldje is al bezet. Probeer opnieuw')


def switch_player(turn):
    """ Switch the player based on how many moves have been made.
        X starts the game so if this turn # is even, it's 0's turn.
    """
    current_player = COMPUTER if turn % 2 == 0 else MENS
    return current_player


def check_for_win(player, turn):
    """ Check for a win (or a tie). For each combo in winning_combos[],
        count how many of its corresponding squares have the current
        player's mark. If a player's score count reaches 3, return a win.
        If it doesn't, and this is already turn # 9, return a tie. If
        neither, return False so the game continues.
    """
    if turn > 4:  # need at least 5 moves before a win is possible
        for combo in winning_combos:
            score = 0
            for index in combo:
                if boxes[index] == player:
                    score += 1
                if score == 3:
                    return 'gewonnen'

        if turn == 9:
            return 'gelijk'


def play(player, turn):
    """ Create a loop that keeps the game in play
        until it ends in a win or tie
    """
    while True:
        take_turn(player, turn)
        print_board()
        result = check_for_win(player, turn)
        if result is not None:
            player_ext = ("mens" if player == 'X' else "computer") if result == 'gewonnen' else None
            try:
                print_uitkomst(result, player_ext)
            except Exception as e:
                print("\033[91m" + "Je functie print_uitkomst() werkt niet correct!" + "\033[0m")
                print(e)
                exit(-2)

            if result == 'gelijk':
                print("\033[94m" + "DIT IS EEN CONTROLE: het spel was gelijk. Zegt de lijn hierboven dat ook?" +
                      "\033[0m")
            if result == 'gewonnen':
                print("\033[94m" + f"DIT IS EEN CONTROLE: het spel was gewonnen door {player_ext}. "
                                   f"Zegt de lijn hierboven dat ook?" + "\033[0m")
            break

        turn += 1
        player = switch_player(turn)


# Begin the game:
print('\n\nWelkom bij Tic-Tac-Toe versus de computer!')
antw = input("Ben je zeker dat je enkel code hebt aangepast waar het moest (dus tussen de twee "
             "OPDRACHT-vermeldingen)? \n"
             "Als je dit wel gedaan hebt, zal je spelletje niet werken! Geef 'ja' in als je zeker bent --> ")
if 'ja' not in antw.lower():
    exit(-2)

print_board(initial=True)
play(first_player, turn)
