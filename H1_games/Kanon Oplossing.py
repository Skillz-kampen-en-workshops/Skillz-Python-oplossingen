# Kanon: raak zo veel mogelijk doelen
# De opdracht begint bij "HIER BEGINT DE OPDRACHT"

# Laat deze imports staan: je hebt ze straks nodig.
import collections.abc as collections
import math
import random
import turtle
from freegames import vector

# --------------------------- HIER BEGINT DE OPDRACHT ---------------------------------


def verbergTurtle():
    """
    OPDRACHT: Gebruik een commando uit het turtle-package om de turtle te verbergen.
    TIP: dit kan in 1 lijn!
    """
    turtle.hideturtle()


def snelheidVanDoelen():
    """
    OPDRACHT: Gebruik een return-statement om de snelheid van de doelen te bepalen.
        Dit is een kommagetal tussen 0 en 3. Je mag zelf kiezen hoe snel je doelen vliegen.
    """
    return 1


def verhoogScore(score):
    """
    OPDRACHT: Als je een bal raakt, verdien je een punt. Gebruik een return om een verhoogde score terug te geven.
            Een verhoogde score is de score met één punt bij.
    """
    verhoogdeScore = score + 1
    return verhoogdeScore


def spelVoorbij(status):
    """
    OPDRACHT: Print een bericht als het spel afgelopen is. Het spel is afgelopen als de variabele status gelijk is
            aan 'gedaan'.
    """
    if status == "gedaan":
        print('Game over.')


def positieVanDoelen():
    """
    OPDRACHT: De doelen verschijnen op een willekeurige plaats langs de zijkant. Om die plaats te bepalen, moet je een
                return gebruiken om een willekeurig getal tussen -150 en 150 terug te geven
    TIP: het package 'random' is al geïmporteerd
    """
    return random.randint(-150, 150)


def scorebord(score):
    """
    OPDRACHT: maak een string voor het scorebord die de score weergeeft.
            !! Gebruik een return om je string terug te geven. !!
    VOORBEELD: Zo'n string ziet er bijvoorbeeld als volgt uit.

            " SCORE : 12 "

    TIP: Wil je een getal gebruiken in een string, kan je dit doen door er str(  ) rond te zetten
    """
    return "SCORE : " + str(score)


# ------------------------------------ HIER EINDIGT DE OPDRACHT -------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------                                         ---------------------------------------------
# -------------------------------     PAS HIERONDER GEEN CODE AAN !!      ---------------------------------------------
# -------------------------------                                         ---------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------



ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
score = 0


def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw(nb_hits):
    "Draw ball and targets."
    turtle.clear()

    for target in targets:
        turtle.goto(target.x, target.y)
        turtle.dot(20, 'blue')

    if inside(ball):
        turtle.goto(ball.x, ball.y)
        turtle.dot(6, 'red')

    update_score(nb_hits)
    turtle.update()


def update_score(nb_hits):
    global score
    try:
        old_score = score
        for i in range(nb_hits):
            score = verhoogScore(score)
        assert score == old_score + nb_hits
    except AssertionError:
        print("\033[91m" + "Je functie verhoogScore() geeft niet de juiste score terug. Kijk nog eens na." + "\033[0m")
        exit(-2)
    except Exception as e:
        print("\033[91m" + "Je functie verhoogScore() werkt niet correct. Kijk nog eens na." + "\033[0m")
        print(e)
        exit(-2)

    turtle.goto(0, 175)
    turtle.pendown()
    try:
        my_string = scorebord(score)
        assert isinstance(my_string, str), "Je functie scorebord() maakt geen string aan! Denk aan str( )."
        assert str(score) in my_string, "De score wordt niet weergegeven in de functie scorebord()."
    except AssertionError as e:
        print("\033[91m" + str(e) + "\033[0m")
        exit(-2)
    except Exception as e:
        print("\033[91m" + "Je functie scorebord() werkt niet correct. Kijk nog eens na." + "\033[0m")
        print(e)
        exit(-2)
    turtle.write(my_string, align='center', font=("Arial", 20, 'normal'))
    turtle.penup()


def move():
    "Move ball and targets."
    global score
    if random.randrange(40) == 0:
        try:
            y = positieVanDoelen()
            assert y in range(-150,150)
            target = vector(200, y)
        except AssertionError:
            print("\033[91m" + "Je functie positieVanDoelen() geeft geen getal terug tussen -150 en 150." + "\033[0m")
            exit(-2)
        except Exception as e:
            print("\033[91m" + "Je functie positieVanDoelen() werkt niet correct. Kijk nog eens na." + "\033[0m")
            print(e)
            exit(-2)
        targets.append(target)

    for target in targets:
        try:
            target.x -= (snelheidVanDoelen() * 0.5 if snelheidVanDoelen() != 0 else 0.5)
        except:
            target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    nb_hits = 0
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            nb_hits += 1

    draw(nb_hits)


    for target in targets:
        try:
            # sanity check
            spelVoorbij(" ")
        except Exception as e:
            print("\033[91m" + "Je functie spelVoorbij() werkt niet correct. Kijk nog eens na." + "\033[0m")
            print(e)
        if not inside(target):
            spelVoorbij("gedaan")
            return

    turtle.ontimer(move, 50)


if 'ja' in (input("Welkom bij Kanon! \n \n"
          "Voordat je dit spelletje kan spelen, moet je eerst alle functies voltooien die in dit bestand staan. \n"
          "Krijg je een foutmelding in de vorm van rode tekst? Lees dan eens de laatste lijn van de foutmelding om te \n"
          "zien wat je foutdeed. Schrijf hier 'ja' als je deze uitleg gelezen hebt. --> ")).lower():

    turtle.setup(420, 420, 370, 0)
    try:
        verbergTurtle()
        assert not turtle.isvisible(), "Je moet je turtle verbergen met de functie verbergTurtle()!"
    except AssertionError as e:
        print("\033[91m" + str(e) + "\033[0m")
        exit(-2)
    except Exception as e:
        print("\033[91m" + "Je functie verbergTurtle() werkt niet correct. Kijk nog eens na." + "\033[0m")
        print(e)
        exit(-2)

    turtle.up()
    turtle.tracer(False)
    turtle.onscreenclick(tap)
    move()
    turtle.done()
else:
    print("Lees bovenstaand bericht goed en herstart je spelletje!")
    exit(-2)
