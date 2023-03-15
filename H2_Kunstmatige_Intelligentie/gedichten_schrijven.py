# text generation using a recurrent neural network
# inspired by NeuralNine's tutorial on YouTube (https://www.youtube.com/watch?v=QM5XDc4NQJo)

# IMPORT STATEMENTS. NIET AANPASSEN ############################
import random
import time
import numpy as np
from keras.models import load_model

# Check of al deze modules geïnstalleerd zijn. Als dat niet zo is, zal je een foutmelding krijgen.
# Als je een foutmelding krijgt, ga dan naar de terminal en typ het volgende commando:
# pip install <module>


# IMPORT STATEMENTS. NIET AANPASSEN ############################

# HIER BEGINT DE OPDRACHT ######################################


def creativiteit():
    """
    Deze functie moet een getal tussen 0 en 1 returnen.
    Hoe hoger dit getal, hoe creatiever de gedichten zullen zijn. Als je het getal te laag maakt, zullen de gedichten
    veel dezelfde woorden bevatten als de gedichten in de trainingset. Als je het getal te hoog maakt, zullen de
    gedichten onleesbaar worden. Probeer een getal te vinden dat het midden houdt. Een getal van 0.5 is een goede
    start.
    """
    return 0.5


def lengte():
    """
    Deze functie moet een getal returnen. Dit getal bepaalt hoeveel letters het gedicht zal bevatten.
    Maak het niet te lang, want dan wordt het gedicht onleesbaar. Een getal van ongeveer 300 is een goede start.
    """
    return 1000


def tijd_sinds_start(start):
    """
    Deze functie berekent hoeveel seconden er zijn verstreken sinds de start van het programma.
    De variabele 'start' is de tijd (in seconden) waarop het programma is gestart. Bereken hoeveel seconden er
    zijn verstreken sinds de start van het programma en gebruik een return-statement om dit getal te returnen.
    """
    return time.time() - start


def startletter(tekstlengte):
    """
    Deze functie moet een getal returnen. Dit getal bepaalt vanaf welke letter in de trainingset het gedicht zal
    beginnen. De variabele 'tekstlengte' is de lengte van de trainingset. Gebruik een return-statement om een
    getal te returnen. Dit getal moet tussen 0 en de lengte van de trainingset liggen.
    """
    return random.randint(0, tekstlengte - 1)


# HIER EINDIGT DE OPDRACHT #####################################
# PAS HIERONDER NIETS AAN. #####################################
# ALLE CODE DIE JE HIERONDER ZIET, IS AL VOOR JE GEMAAKT. ######
################################################################

# PARAMETERS
SEQ_LENGTH = 40
STEP_SIZE = 3


def sample(preds, temperature=1.0):
    """
    helper function to sample an index from a probability array
    :param preds: the probability array
    :param temperature: the temperature. This will determine how random the output will be.
    :return: the index of the character that was sampled
    """
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def text_generation(model, temperature, length, print_details=False, truncate=False):
    """
    generate text using a trained model
    :param model: the trained model
    :param temperature: the temperature. This will determine how random the output will be.
    :param length: the length of the generated text
    :param print_details: whether to print the details of the generation process
    :param truncate: whether to truncate the generated text to omit the seed
    :return: the generated text
    """
    try:
        start_index = startletter(len(text) - SEQ_LENGTH)
    except:
        raise AssertionError("De functie 'startletter' is nog niet goed geïmplementeerd.")

    assert isinstance(start_index, int), "De functie 'startletter' is nog niet goed geïmplementeerd. De functie " \
                                         "moet een getal returnen."
    assert start_index >= 0, "De functie 'startletter' is nog niet goed geïmplementeerd. De functie moet een getal " \
                             "returnen dat groter is dan 0."
    assert start_index < len(text) - SEQ_LENGTH, \
        "De functie 'startletter' is nog niet goed geïmplementeerd. De functie " \
        "moet een getal returnen dat kleiner is dan de lengte van de " \
        "trainingset."

    sentence = text[start_index: start_index + SEQ_LENGTH]
    generated_text = sentence
    t0 = time.time()
    if print_details:
        print('----- Genereren met startzin: "' + sentence + '"')

    # test of de functie 'tijd_sinds_start' goed is geïmplementeerd
    try:
        test = tijd_sinds_start(t0)
    except:
        raise AssertionError("De functie 'tijd_sinds_start' is nog niet goed geïmplementeerd.")

    assert isinstance(test, float), "De functie 'tijd_sinds_start' is nog niet goed geïmplementeerd. De functie " \
                                    "moet een getal returnen."
    assert test >= 0, "De functie 'tijd_sinds_start' is nog niet goed geïmplementeerd. De functie moet een getal " \
                      "returnen dat groter is dan 0."
    assert test < 10, "De functie 'tijd_sinds_start' is nog niet goed geïmplementeerd. De functie geeft het verkeerde " \
                      "tijdsverschil terug. "

    for i in range(length):
        x = np.zeros((1, SEQ_LENGTH, len(character_set)))
        for t, character in enumerate(sentence):
            x[0, t, character_to_index[character]] = 1
        preds = model.predict(x, verbose=0)[0]
        next_index = sample(preds, temperature)
        next_character = index_to_character[next_index]

        if print_details and i % 10 == 0:
            t1 = tijd_sinds_start(t0)
            print('Tijd gepasseerd: ', round(t1, 3), 's')
            print('Bezig aan letter ', i, ' van ', length)

        generated_text += next_character
        sentence = sentence[1:] + next_character

    if truncate:
        generated_text = generated_text[SEQ_LENGTH:]
    return generated_text


filepath = 'poems.txt'

# read the text and convert it to lowercase
try:
    text = open(filepath, 'rb').read().decode(encoding='utf-8')
except UnicodeDecodeError:
    # print in red
    print('\033[91m' + "Het bestand met gedichten bevat ongeldige karakters." + '\033[0m')
    exit()
except FileNotFoundError:
    print('\033[91m' + "Het bestand met gedichten is niet gevonden. Zorg ervoor dat je het bestand in dezelfde map " +
          "opslaat als dit script." + '\033[0m')
    exit()
except Exception as e:
    print('\033[91m' + "Er is een onbekende fout opgetreden bij het lezen van het bestand met gedichten." + '\033[0m')
    print(e)
    exit()
finally:
    print("Het bestand met gedichten is succesvol ingelezen.")

text = text.lower()

# split into individual poems
poems = text.splitlines()
# remove empty lines
poems = [poem for poem in poems if poem != '']
# remove poems that are too short
poems = [poem for poem in poems if len(poem) > SEQ_LENGTH]
TRAINING_SET_SIZE = 2500
training_set = poems[:TRAINING_SET_SIZE]

# create a set of all the characters in the text
character_set = sorted(set(text))
print(character_set)

# create a dictionary that maps each character to an index
character_to_index = {c: i for i, c in enumerate(character_set)}  # dictionary comprehension
index_to_character = {i: c for i, c in enumerate(character_set)}  # dictionary comprehension

model = load_model('poems_model.h5')

temperature = creativiteit()
length = lengte()
assert 0 <= temperature <= 1, 'creativiteit() moet een getal tussen 0 en 1 returnen.'
assert isinstance(length, int), 'lengte() moet een getal returnen.'
text = text_generation(model, temperature, length, print_details=True)

# format text to make it look nice: 10 words per line
text = text.split()  # split the text into a list of words
# print 10 words per line
for i in range(0, len(text), 10):
    print(' '.join(text[i:i + 10]))
