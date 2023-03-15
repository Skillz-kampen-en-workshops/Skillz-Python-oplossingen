# In dit bestand ga je je eigen versie van Snake maken !!
# De opdracht begint vanaf de vermelding "BEGIN VAN DE OPDRACHT"

# Laat deze imports staan. Je hebt ze straks nodig
import turtle as t
import time
import random

# ------------------------- BEGIN VAN DE OPDRACHT ----------------------------------

def mijnNaam():
    """
    OPDRACHT: gebruik return om een string terug te geven met je naam
    """
    return 'Xander'

def maakSlang(turtle):
    """
    OPDRACHT: Gebruik Turtle en stel de slang van het spelletje in voor gebruik. Doe hiervoor het volgende:
        0. zet de snelheid van je Turtle op 0 (is al gedaan in de eerste lijn)
        1. Maak de kleur van je turtle zwart
        2. Zet de vorm van je turtle op een vierkant
        3. Hef de pen van je turtle op
        4. Ga naar de positie (0,0)
    """
    turtle.speed(0)
    turtle.color('black')
    turtle.shape('square')
    turtle.penup()
    turtle.goto(0,0)

def maakEten(turtle):
    """
    OPDRACHT: Gebruik Turtle en stel het eten van het spelletje in voor gebruik. Doe hiervoor het volgende:
        0. zet de snelheid op het laagste (is al gedaan in de eerste lijn)
        1. Maak de kleur rood
        2. Maak de vorm een cirkel. PAS OP: het is niet de bedoeling dat je een cirkel tekent!
        3. Hef de pen van je turtle op
        4. zet de beginpositie op (0,100)
    """
    turtle.speed(0)
    turtle.color("red")
    turtle.shape("circle")
    turtle.penup()
    turtle.goto(0,100)

def maakTitel(score, highscore):
    """
    OPDRACHT: maak een string die de score en highscore weergeeft. Hiervoor moet je strings bij elkaar optellen.
            Gebruik hiervoor een return
    VOORBEELD: de string zou er als volgt kunnen uitzien

           " SCORE: 50   HIGHSCORE: 250 "

    TIP: als je een getal als string wil gebruiken, kan je er str(  ) rondzetten
    """
    return "SCORE : " + str(score) + "     HIGHSCORE : " + str(highscore)

def kiesNieuwePositie():
    """
    OPDRACHT: Wanneer de slang het eten opeet, moet je een nieuwe positie voor het eten kiezen.
            Hiervoor heeft de computer een willekeurig getal tussen -290 en 290 nodig. Gebruik een return.
    TIP: gebruik hiervoor het package "random"
    """
    return random.randint(-290,290)

def nieuweScore(score):
    """
    OPDRACHT: Wanneer de slang het eten opeet, krijg je 10 punten erbij. Verhoog de gegeven score met 10 en
                gebruik een return om de nieuwe score terug te geven.
    """
    nieuweScore = score + 10
    return nieuweScore

def kiesMaximum(getal1, getal2):
    """
    OPDRACHT: bepaal het grootste van de 2 gegeven getallen en gebruik een return om dit terug te geven.
    TIP: hiervoor bestaat er een speciale functie. Welke?
    """
    maximum = max(getal1, getal2)
    return maximum

def plaatsNieuwEten(turtle):
    """
    OPDRACHT: als de slang het eten heeft opgegeten, moet er nieuw eten geplaatst worden
                op het bord. Gebruik hiervoor turtle en doe het volgende:
                1)  kies een willekeurige kleur uit rood, blauw, oranje, roos of wit
                2)  plaats het eten op een willekeurige plaats op het bord: geef daarvoor
                de x en y van de turtle een willlekeurige waarde tussen -290 en 290

    TIP: gebruik hiervoor twee functies uit het package "random"
    """
    kleur = random.choice(("red", "blue", "orange", "pink", "white"))
    turtle.color(kleur)

    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    turtle.goto(x, y)

# ----------------------------- EINDE VAN DE OPDRACHT -------------------------------


if (input("Welkom bij Kanon! \n \n"
      "Voordat je dit spelletje kan spelen, moet je eerst alle functies voltooien die in dit bestand staan. \n"
      "Krijg je een foutmelding in de vorm van rode tekst? Lees dan eens de laatste lijn van de foutmelding om te \n"
      "zien wat je foutdeed. Schrijf hier 'ja' als je deze uitleg gelezen hebt. --> ")).lower().__contains__('ja'):
    print("\n z = omhoog, s = omlaag, q = links, d = rechts")
else:
    raise InterruptedError()

DELAY = 0.25
delay = DELAY

# Score
score = 0
high_score = 0

# Set up the screen
wn = t.Screen()
name = mijnNaam()

if type(name) != str:
    print("\033[91m" + "Je functie mijnNaam() geeft geen string terug. Gebruik een return en een string." + "\033[0m")
    exit(-2)
elif len(name) == 0:
    print("\033[91m" + "Je bent vergeten je naam in te geven in mijnNaam()" + "\033[0m")
    exit(-2)
else:
    my_string = "Snake Game van " + name

wn.title(my_string)
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
snake = t.Turtle()
try:
    maakSlang(snake)
    assert snake.shape() == "square", "De vorm van de slang is niet juist"
    assert snake.color() == ("black", "black"), "De kleur van de slang is niet juist"
    assert snake.xcor() == 0, "De x-coördinaat van de slang is niet juist"
    assert snake.ycor() == 0, "De y-coördinaat van de slang is niet juist"
except AssertionError as e:
    print("\033[91m" + "Je functie maakSlang() is niet juist. " + str(e) + "\033[0m")
    exit(-2)
except Exception as e:
    print("\033[91m" + "Er is iets fout gegaan bij het uitvoeren van je functie maakSlang(). " + "\033[0m")
    print(e)
    exit(-2)

snake.direction = "stop"

# Snake food
food = t.Turtle()

try:
    maakEten(food)
    assert food.shape() == "circle", "De vorm van het eten is niet juist"
    assert food.color() == ("red", "red"), "De kleur van het eten is niet juist"
    assert food.xcor() == 0, "De x-coördinaat van het eten is niet juist"
    assert food.ycor() == 100, "De y-coördinaat van het eten is niet juist"
except AssertionError as e:
    print("\033[91m" + "Je functie maakEten() is niet juist. " + str(e) + "\033[0m")
    exit(-2)
except Exception as e:
    print("\033[91m" + "Er is iets fout gegaan bij het uitvoeren van je functie maakEten(). " + "\033[0m")
    print(e)
    exit(-2)

segments = []

# Pen
pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

try:
    scoreboard = maakTitel(score, high_score)
    assert str(score) in scoreboard, "De score wordt niet weergegeven in de titel in je functie maakTitel()!"
    assert str(high_score) in scoreboard, "De high score wordt niet weergegeven in de titel in je functie maakTitel()"
except AssertionError as e:
    print("\033[91m" + str(e) + "\033[0m")
    exit(-2)
except Exception as e:
    print("\033[91m" + "Er is iets fout gegaan bij het uitvoeren van je functie maakTitel(). " + "\033[0m")
    print(e)
    exit(-2)
pen.write(scoreboard, align="center", font=("Courier", 24, "normal"))

# check if KiesNieuwePositie() is correct
try:
    samples = [kiesNieuwePositie() for _ in range(100)]
    assert all([isinstance(sample, int) for sample in samples]), "KiesNieuwePositie() geeft geen integer terug!"
    assert all([-290 <= sample <= 290 for sample in samples]), \
        "KiesNieuwePositie() geeft een waarde terug die niet tussen -290 en 290 ligt!"
    assert len(set(samples)) > 1, "KiesNieuwePositie() geeft altijd dezelfde waarde terug!. Gebruik random.randint."
except AssertionError as e:
    print("\033[91m" + str(e) + "\033[0m")
    exit(-2)
except Exception as e:
    print("\033[91m" + "Er is iets fout gegaan bij het uitvoeren van je functie kiesNieuwePositie(). " + "\033[0m")
    print(e)
    exit(-2)

# Functions
def go_up():
    if snake.direction != "down":
        snake.direction = "up"


def go_down():
    if snake.direction != "up":
        snake.direction = "down"


def go_left():
    if snake.direction != "right":
        snake.direction = "left"


def go_right():
    if snake.direction != "left":
        snake.direction = "right"


def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "z")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "q")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(1)
        snake.goto(0, 0)
        snake.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = DELAY

        pen.clear()
        pen.write(maakTitel(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Check for a collision with the food
    if snake.distance(food) < 20:
        # Move the food to a random spot
        x = kiesNieuwePositie()
        y = kiesNieuwePositie()
        food.goto(x, y)

        # Add a segment
        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        old_score = score
        try:
            score = nieuweScore(score)
            assert score == old_score + 10
        except AssertionError:
            print("\033[91m" + "Je functie nieuweScore() is niet juist. De score wordt niet met 10 verhoogd." + "\033[0m")
            exit(-2)
        except Exception as e:
            print("\033[91m" + "Er is iets fout gegaan bij het uitvoeren van je functie nieuweScore(). " + "\033[0m")
            print(e)
            exit(-2)

        old_high_score = high_score
        try:
            high_score = kiesMaximum(score, high_score)
            assert high_score == max(old_high_score, score)
        except AssertionError:
            print("\033[91m" + "Je functie kiesMaximum() is niet juist!" + "\033[0m")
            exit(-2)
        except Exception as e:
            print("\033[91m" + "Er is iets fout gegaan bij het uitvoeren van je functie kiesMaximum(). " + "\033[0m")
            print(e)
            exit(-2)

        pen.clear()
        pen.write(maakTitel(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(snake) < 20:
            # if we collide with a segment, we reset the game
            try:
                plaatsNieuwEten(food)
                assert -290 <= food.xcor() <= 290 and -290 <= food.ycor() <= 290, \
                    "De positie van het eten is niet correct in je functie plaatsNieuwEten()!"
                # color should be one of "red", "blue", "orange", "pink", "white"
                assert food.color()[0] in ["red", "blue", "orange", "pink", "white"], \
                    "De kleur van het eten is niet correct in je functie plaatsNieuwEten()!"
            except AssertionError as e:
                print("\033[91m" + str(e) + "\033[0m")
                exit(-2)
            except Exception as e:
                print("\033[91m" + "Er is iets fout gegaan bij het uitvoeren van je functie plaatsNieuwEten(). "
                      + "\033[0m")
                print(e)
                exit(-2)

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)


wn.mainloop()