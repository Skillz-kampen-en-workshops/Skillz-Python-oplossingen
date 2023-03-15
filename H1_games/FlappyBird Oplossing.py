from freegames import vector
import random
import turtle


# ------------------------ HIER BEGINT HET EERSTE DEEL VAN DE OPDRACHT-----------------------------
# Vul hieronder de functies aan, zodat ze doen wat gevraagd wordt in de opgave.


def scorebord(score, level):
    """
    Maak een string met een scorebord en gebruik een return.
    Een scorebord moet er als volgt uitzien:

                SCORE : 50    LEVEL 4

    Tip: wil je een getal in een string gebruiken, moet je gebruik maken van str (  )
    """
    return "SCORE : " + str(score) + "     LEVEL  " + str(level)


def binnenin(punt):
    """
    Deze functie geeft waar (True) terug als een punt binnenin het scherm ligt. Een punt ligt binnenin het scherm
    als de waarde ervan tussen -200 en 200 ligt. Is dat niet het geval, geeft de functie onwaar (False) terug. Gebruik
    een return.
    """
    if -200 < punt < 200:
        return True
    else:
        return False


def kleur(levend):
    """
    Zolang je nog leeft, ziet je balletje groen. Als je een bal raakt, ga je dood en wordt het balletje rood. Deze functie
    geeft de juiste kleur terug. Als levend dus waar is (True), dan geeft de functie 'groen' terug, anders 'rood'.
    """
    if levend:
        return "groen"
    else:
        return "rood"


def willekeurig_getal():
    """
    Geef een willekeurige integer terug tussen -199 en 199. Gebruik hiervoor een return.
    """
    getal = random.randint(-199, 199)
    return getal


# ------------------------------------ HIER EINDIGT HET EERSTE DEEL VAN DE OPDRACHT------------------------------------

# ------------------------------------ HIER BEGINT HET TWEEDE DEEL VAN DE OPDRACHT ------------------------------------
# Let op: dit is een moeilijke opdracht. Doe dit enkel als je Python goed begrijpt.


# Vul hieronder de functie aan, zodat ze doet wat gevraagd wordt in de opgave.


def maakBal(hoogte, ballen):
    """
    Deze functie maakt een bal aan. In Python wordt een bal voorgesteld door een "Vector". Wat dit precies is, is niet
    zo belangrijk. Je kunt een nieuwe vector maken, met de naam "bal" op de volgende manier
    bal = Vector(breedte, hoogte). Bijvoorbeeld

    >> bal = Vector(250, 50)

    maakt een bal op 250 pixels rechts van het midden en 50 pixels boven het midden.

    Nadat je een bal hebt aangemaakt, moet je deze toevoegen aan de lijst met ballen. Die lijst heet gewoon "ballen".
    Een bal toevoegen doe je met "append", wat Engels is voor "eraan toevoegen". Bijvoorbeeld

    >> lijst.append((nieuw_stukje,extra_info))

    voegt een nieuw stukje toe aan de lijst met naam "lijst".

    OPDRACHT: Zorg ervoor dat de ballen verschillende groottes hebben. De maximale grootte is 40 en de minimale
    grootte is 5.
    """
    bal = vector(199, hoogte)
    grootte = random.randint(5, 40)  # wijzigen van = 20
    ballen.append((bal, grootte))  # 20 vervangen door grootte


def tekenBal(ballen):
    """
    Nu je ervoor gezorgd hebt dat ballen een verschillende grootte hebben, gaan we ook zorgen dat het programma
    de ballen tekent met de juiste grootte.
    OPDRACHT: zorg ervoor dat de ballen getekend worden met de juiste grootte

    TIP: 'for __ in ballen' betekent dat je iets doet voor alle ballen.
    """
    for bal, grootte in ballen:
        turtle.goto(bal.x, bal.y)
        turtle.dot(grootte, "black")  # 20 vervangen door grootte


# ------------------------------------ HIER EINDIGT DE OPDRACHT -------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# -------------------------------                                         ---------------------------------------------
# -------------------------------     PAS HIERONDER GEEN CODE AAN !!      ---------------------------------------------
# -------------------------------                                         ---------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

bird = vector(0, 0)
balls = []


def up(x, y):
    "Move bird up in response to screen tap."
    up = vector(0, 30)
    bird.move(up)


def inside(point):
    try:
        assert binnenin(point.x) == (-200 < point.x < 200)
        assert binnenin(point.y) == (-200 < point.y < 200)
        return binnenin(point.x) and binnenin(point.y)
    except AssertionError:
        print("\033[91m" + "Je functie binnenin( ) geeft het verkeerde resultaat. Kijk nog eens goed na." + "\033[0m")
        exit(-2)
    except TypeError:
        print("\033[91m" + "Je functie binnenin( ) geeft geen waar of onwaar (True / False) terug. Kijk nog eens na." + "\033[0m")
        exit(-2)
    except Exception as e:
        print("\033[91m" + "Je functie binnenin( ) werkt niet goed. Kijk nog eens goed na." + "\033[0m")
        print(e)
        exit(-2)


def draw(alive, score, level):
    """Draw screen objects."""
    turtle.clear()

    turtle.goto(0, 180)
    turtle.showturtle()

    try:
        my_string = scorebord(score, level)
        assert type(my_string) == str, "Je functie scorebord( ) geeft geen string terug."
        assert str(score) in my_string, "Je functie scorebord( ) geeft de score niet weer."
        assert str(level) in my_string, "Je functie scorebord( ) geeft het level niet weer."
    except AssertionError as e:
        print("\033[91m" + str(e) + "\033[0m")
        exit(-2)
    except Exception as e:
        print("\033[91m" + "Je functie scorebord( ) werkt niet goed." + "\033[0m")
        print(e)
        exit(-2)
    turtle.write(scorebord(score, level), align='center', font=("Calibri", 15, "bold"))

    turtle.hideturtle()
    turtle.goto(bird.x, bird.y)

    try:
        color = kleur(alive).lower()
        assert type(color) == str, "Je functie kleur( ) geeft geen string terug."
        assert color == "groen" if alive else "rood", "Je functie kleur( ) geeft een verkeerde kleur, of helemaal geen kleur terug. Kijk nog eens na."
    except AssertionError as e:
        print("\033[91m" + str(e) + "\033[0m")
        exit(-2)
    except Exception as e:
        print("\033[91m" + "Je functie kleur( ) werkt niet goed." + "\033[0m")
        print(e)
        exit(-2)

    color = "green" if color == "groen" else "red"
    turtle.dot(10, color)

    if enable:
        try:
            tekenBal(balls)
        except:
            print("\033[91m" + "Je functie tekenBal( ) werkt niet goed." + "\033[0m")
            exit(-2)
    else:
        for ball, size in balls:
            turtle.goto(ball.x, ball.y)
            turtle.dot(20, 'black')

    turtle.update()


def move():
    """Update object positions."""
    turtle.listen()
    turtle.onkey(up, "Up")
    bird.y -= 5

    global enable
    global score
    global ball_speed
    global level

    for ball, _ in balls:
        ball.x -= ball_speed

    if random.randrange(10 // level) == 0:
        try:
            y = willekeurig_getal()
            assert y in range(-200, 200)
        except AssertionError:
            print("\033[91m" + "Je functie willekeurig_getal() geeft een getal terug dat te groot of te klein is."
                  + "\033[0m")
            exit(-2)
        except TypeError:
            print("\033[91m" + "Je functie willekeurig_getal() geeft geen getal terug." + "\033[0m")
            exit(-2)
        except Exception as e:
            print("\033[91m" + "Je functie willekeurig_getal() werkt niet goed." + "\033[0m")
            print(e)
            exit(-2)

        if enable:
            try:
                bal = maakBal(y, balls)
            except Exception as e:
                print("\033[91m" + "Je functie maakBal( ) werkt niet goed." + "\033[0m")
                print(e)
                exit(-2)
        else:
            size = 30
            ball = vector(199, y)
            balls.append((ball, size))

    while len(balls) > 0 and not inside(balls[0][0]):
        balls.pop(0)
        score += 1
        if score % 15 == 0 and score != 0:
            ball_speed += 1.5
            level += 1

    if not inside(bird):
        draw(False, score, level)
        return

    for ball, size in balls:
        if abs(ball - bird) < size // 2:
            draw(False, score, level)
            return

    draw(True, score, level)
    turtle.ontimer(move, 50)


if 'ja' not in (input("Welkom bij Flappy Bird! \n \n"
                      "Voordat je dit spelletje kan spelen, moet je eerst alle functies voltooien die in dit bestand staan. \n"
                      "Krijg je een foutmelding in de vorm van rode tekst? Lees dan eens de laatste lijn van de foutmelding om te \n"
                      "zien wat je foutdeed. Schrijf hier 'ja' als je deze uitleg gelezen hebt. --> ")).lower():
    exit(-2)
else:
    print("")
    if 'ja' in (input("Heb je ook het tweede deel van de opdracht gemaakt? Ja / Nee ---> ")).lower():
        enable = True
    else:
        enable = False

score = 0
ball_speed = 3
level = 1

turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.up()
turtle.tracer(False)
turtle.onscreenclick(up)
move()
turtle.done()
