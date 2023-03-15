# text generation using a recurrent neural network
# inspired by NeuralNine's tutorial on YouTube (https://www.youtube.com/watch?v=QM5XDc4NQJo)

# IMPORT STATEMENTS. NIET AANPASSEN ############################
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation
import time

# Check of al deze modules geïnstalleerd zijn. Als dat niet zo is, zal je een foutmelding krijgen.
# Als je een foutmelding krijgt, ga dan naar de terminal en typ het volgende commando:
# pip install <module>

# IMPORT STATEMENTS. NIET AANPASSEN ############################

# HIER BEGINT DE OPDRACHT ######################################


def gedichten_opschonen(gedichten, minimale_lengte):
    """
    De variabele 'gedichten' bestaat uit een lijst met duizenden gedichten. Elk gedicht wordt voorgesteld als een
    string. Deze functie verwijdert alle gedichten die te kort zijn (minder dan 'minimale_lengte' karakters lang) of
    die leeg zijn uit de lijst. De functie geeft een lijst terug met alle gedichten die voldoen aan de voorwaarden.
    Daarvoor gebruik je een return-statement. Vlak voor het return-statement, print je het aantal gedichten dat je hebt
    overgehouden.
    """
    for gedicht in gedichten:
        if len(gedicht) < minimale_lengte:
            gedichten.remove(gedicht)
        elif gedicht == '':
            gedichten.remove(gedicht)

    print("Aantal gedichten:", len(gedichten))
    return gedichten


def aantal_herhalingen():
    """
    Deze functie moet een getal teruggeven dat aangeeft hoeveel keer je gedichtenschrijver de gedichten gaat bekijken.
    LET OP: als je een groot getal kiest, kan het zijn dat je computer er lang over doet om de gedichten te trainen.
    Kies dus een getal dat niet te groot is, best tussen de 3 en 10.
    """
    return 4


def verstreken_tijd(start_tijd):
    """
    Deze functie berekent hoeveel tijd er verstreken is sinds de variabele 'start'. De variabele 'start' is een
    kommagetal dat het aantal seconden sinds 1 januari 1970 voorstelt. De functie geeft het aantal seconden terug
    tussen 'start' en nu. Je kan deze functie gebruiken om te zien hoeveel tijd je gedichtenschrijver nodig heeft om
    de gedichten te leren schrijven. Voor deze functie moet je een return-statement gebruiken.

    TIP: je kan de functie 'time.time()' gebruiken om het aantal seconden sinds 1 januari 1970 te krijgen.
    """
    return time.time() - start_tijd


################################################################
##   HIERONDER NIETS MEER AANPASSEN.                          ##
##   ALLE CODE DIE JE HIERONDER ZIET, IS AL VOOR JE GEMAAKT.  ##
################################################################

# PARAMETERS. NIET AANPASSEN ##############################
SEQ_LENGTH = 40
STEP_SIZE = 3

filepath = 'poems.txt'

# read the text and convert it to lowercase
text = ''
try:
    text = open(filepath, 'rb').read().decode(encoding='utf-8')
except FileNotFoundError:
    print("\033[91m Het bestand 'poems.txt' is niet gevonden. Zorg dat je het bestand in dezelfde map hebt "
          "staan als dit script. \033[00m")
    exit()
except UnicodeDecodeError:
    print("\033[91m Het bestand 'poems.txt' bevat ongeldige karakters. Zorg dat het bestand alleen tekst bevat. "
          "\033[00m")
    exit()
except Exception as e:
    print(e)
    print("\033[91m Er is iets misgegaan bij het lezen van het bestand. \033[00m")
    exit()
finally:
    print("Het bestand 'poems.txt' is ingelezen.")

text = text.lower()

# split into individual poems
poems = text.splitlines()

# remove poems that are too short or empty
try:
    poems = gedichten_opschonen(poems, SEQ_LENGTH)
except:
    print("\033[91m Je functie gedichten_opschonen werkt niet goed \033[00m")
    exit()
assert not any(len(poem) < SEQ_LENGTH for poem in poems), "Sommige gedichten zijn nog steeds te kort. " \
                                                          "Pas je functie gediten_opschonen aan."
assert not any(poem == '' for poem in poems), "Sommige gedichten zijn nog steeds leeg. Pas je functie " \
                                              "gedichten_opschonen aan."

TRAINING_SET_SIZE = 3500 if len(poems) > 3500 else len(poems)
training_set = poems[:TRAINING_SET_SIZE]

# create a set of all the characters in the text
character_set = sorted(set(text))
print('Totaal aantal karakters:', len(character_set))
print(character_set)

# create a dictionary that maps each character to an index
character_to_index = {c: i for i, c in enumerate(character_set)}  # dictionary comprehension
index_to_character = {i: c for i, c in enumerate(character_set)}  # dictionary comprehension

sentences = []
next_characters = []

# create a list of all the sequences of SEQ_LENGTH characters
for poem in training_set:
    for i in range(0, len(poem) - SEQ_LENGTH, STEP_SIZE):
        sentences.append(poem[i: i + SEQ_LENGTH])
        next_characters.append(poem[i + SEQ_LENGTH])

# create a matrix of zeros with the dimensions (number of sentences, SEQ_LENGTH, number of characters)
# this matrix will be filled with 1s and 0s, depending on which characters are present in each sequence
# it will be 1 if the character is present at the given position, and 0 if it is not
x = np.zeros((len(sentences), SEQ_LENGTH, len(character_set)), dtype=bool)  # input matrix
# create a matrix of zeros with the dimensions (number of sentences, number of characters)
# this matrix will be filled with 1s and 0s, depending on which character is the next character
# it will be 1 if the character is the next character, and 0 if it is not
y = np.zeros((len(sentences), len(character_set)), dtype=bool)  # output matrix

# fill the matrices with 1s and 0s
for i, sentence in enumerate(sentences):
    for t, character in enumerate(sentence):
        x[i, t, character_to_index[character]] = 1
    y[i, character_to_index[next_characters[i]]] = 1

model = Sequential()
model.add(LSTM(128, input_shape=(SEQ_LENGTH, len(character_set))))  # long short-term memory layer
# a long short-term memory layer is a type of recurrent neural network which is able to remember
# information for a long time
model.add(Dense(len(character_set)))  # dense layer
model.add(Activation('softmax'))  # activation layer

model.compile(loss='categorical_crossentropy', optimizer='rmsprop')  # compile the model

epochs = aantal_herhalingen()
assert isinstance(epochs, int), "Je functie aantal_herhalingen() moet een getal teruggeven."
assert epochs > 0, "Je functie aantal_herhalingen() moet een getal groter dan 0 teruggeven."
if epochs > 8:
    print("\033[93m Je hebt een groot getal gekozen voor het aantal herhalingen. Dit kan een tijdje duren. \033[00m")

start = time.time()

# we will test the correctnes of the function 'verstreken_tijd' by calling it before training the model so an error
# message will be displayed directly and not after training the model

test = 0.0
try:
    test = verstreken_tijd(start)
except:
    print("\033[91m Je functie verstreken_tijd werkt niet goed \033[00m")
    exit()
assert isinstance(test, float), "Je functie verstreken_tijd() moet een getal teruggeven."
assert test > 0, "Je functie verstreken_tijd() moet een getal groter dan 0 teruggeven."
# assume the elapsed time is less than 1 second
assert test < 1, "Je functie verstreken_tijd() geeft het verkeerde aantal seconden terug."

hist = model.fit(x, y, batch_size=128, epochs=epochs, verbose=1)  # train the model
model.save('poems_model.h5')  # save the model

training_time = verstreken_tijd(start)
training_time = "{:.2f}".format(training_time)
print("Training duurde " + training_time + " seconden.")
print("Model opgeslagen als 'poems_model.h5. Maak nu de opdracht in het bestand 'gedichten_schrijven.py' af.")
