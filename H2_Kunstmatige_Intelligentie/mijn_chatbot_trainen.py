# IMPORT STATEMENTS. NIET AANPASSEN ############################
# chatbot trainer gebaseerd op https://www.youtube.com/watch?v=1lwddP0KUEg van NeuralNine
import random
import json
import pickle
import numpy as np
import nltk

nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
from keras.models import Sequential
from keras.layers import Dense, Dropout

# IMPORT STATEMENTS. NIET AANPASSEN ############################

# HIER BEGINT HET PROGRAMMA DAT JE MOET AANPASSEN ############################
"""
MAAK JE EIGEN CHATBOT, DEEL 1: BOUW JE CHATBOT EN LEER HEM SPREKEN
Dit is het eerste van twee delen van de chatbot-opdracht. Onze chatbot kan nu nog niets, dus moeten we hem als eerste
een beetje Nederlands leren. Dit doen we door hem (of haar) te leren praten over een aantal specifieke situaties, die
we klassen noemen. Voorbeelden van klassen zijn 'begroeting', 'afscheid', 'het weer', enzovoort. De chatbot zal deze
leren herkennen aan patronen (dat zijn zinnen die jij aan de chatbot geeft en die jij dus typt) en zal dan een antwoord
geven waarvan de chatbot denkt dat het meest juist is.

OPGEPAST: dit programma uitvoeren kan enkele minuten duren. Als het dus niet na een paar seconden gedaan is, geen
zorgen, dat is normaal.

Vul de opdrachten hieronder verder aan om je chatbot te trainen. Als je op het einde van je programma en bericht krijgt
dat alles goed is uitgevoerd, kan je het tweede deel van de opdracht maken in het bestand "mijn_chatbot_gebruiken.py".
"""

def voeg_toe_aan_lijst(lijst, woord):
    """
    Voegt een woord toe aan een lijst, maar alleen als het woord nog niet in de lijst staat.
    Je moet in deze functie geen print() statements of return statements gebruiken.
    """
    if woord not in lijst:
        lijst.append(woord)


def verwijder_duplicaten_en_sorteer(lijst):
    """
    Verwijdert alle duplicaten uit een lijst en sorteert de lijst.
    Je moet in deze functie een return statement gebruiken.
    HINT: je kan duplicaten verwijderen door de lijst om te zetten in een set, en dan terug te zetten naar een lijst:
    lijst = list(set(lijst))
    """
    lijst = list(set(lijst))
    lijst.sort()
    return lijst


def print_alle_woorden_en_klassen(woord_lijst, klasse_lijst):
    """
    Print alle woorden en alle klassen. woord_lijst en klasse_lijst zijn lijsten. Je kan ze oftewel printen als
    een lijst, of je gebruikt een for loop om alle woorden/klassen afzonderlijk te printen.
    Je moet in deze functie geen return statement gebruiken.
    """
    print("Alle woorden: ", woord_lijst)
    print("Alle klassen: ", klasse_lijst)


def voeg_klassen_toe():
    """
    Voeg klassen toe aan de informatie die je chatbot zal gebruiken. Een klasse ziet er als volgt uit:
      {
        "tag": "klasse_naam",
        "patronen": ["patroon1", "patroon2", "patroon3"],
        "antwoorden": ["antwoord1", "antwoord2", "antwoord3"]
      }
    Bijvoorbeeld:
      {
        "tag": "tot ziens",
        "patronen": ["Tot ziens", "Stop", "Ik ben weg", "bye", "tot de volgende keer"],
        "antwoorden": ["Tot ziens.", "Tot de volgende keer."]
      },
    Om een klasse toe te voegen, moet je de volgende stappen uitvoeren:
    1. maak een lege lijst aan met de naam "klassen"
    2. maak een lijst aan die bestaat uit drie elementen
        a. een string met de naam van de klasse
        b. een lijst met patronen
        c. een lijst met antwoorden
    3. voeg deze lijst toe aan de lijst "klassen". Welk commando gebruik je hiervoor?
    4. herhaal stap 2 en 3 voor elke klasse die je wil toevoegen
    5. gebruik een return statement om de lijst "klassen" terug te geven

    Volgende klassen zijn al aanwezig, dus moet je niet meer toevoegen:
    - groeten
    - afscheid
    - leeftijd van de chatbot
    - naam van de chatbot
    - tijd
    - wie heeft de chatbot gemaakt
    - vertel een grap
    - dankjewel
    """
    # enkele voorbeelden van klassen
    klassen = []
    nieuwe_tag = "Het weer"
    patronen = ["Hoe is het weer?", "Wat is het weer?", "Hoe is het weer vandaag?", "Wat is het weer vandaag?"]
    antwoorden = ["Dat weet ik niet, kijk zelf eens naar buiten!", "Ik heb geen idee, kijk zelf eens naar buiten!"]
    nieuwe_klasse = [nieuwe_tag, patronen, antwoorden]
    klassen.append(nieuwe_klasse)

    nieuwe_tag = "Hoe gaat het met je?"
    patronen = ["Hoe gaat het met je?", "Hoe gaat het met jou?", "Hoe gaat het?", "Hoe gaat het met u?"]
    antwoorden = ["Goed, dankjewel!", "Goed, en met jou?", "Goed, en met u?"]
    nieuwe_klasse = [nieuwe_tag, patronen, antwoorden]
    klassen.append(nieuwe_klasse)

    return klassen


def shuffle_training_data(training_data):
    """
    Schudt de training_data door elkaar. Je kan hiervoor de functie random.shuffle() gebruiken.
    Je moet in deze functie een return statement gebruiken.
    """
    random.shuffle(training_data)
    return training_data


# HIER EINDIGT HET PROGRAMMA DAT JE MOET AANPASSEN ############################
# PAS HIERONDER NIETS MEER AAN ################################################
################################################################################
################################################################################

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

user_defined_classes = None
try:
    user_defined_classes = voeg_klassen_toe()
except:
    print("\033[91m" + "ERROR: Je functie voeg_klassen_toe werkt niet." + "\033[0m")
    exit()

if user_defined_classes is not None:
    assert type(user_defined_classes) == list, "Je functie voeg_klassen_toe moet een lijst teruggeven."
    assert all([type(user_defined_class) == list for user_defined_class in user_defined_classes]), \
        "Je functie voeg_klassen_toe moet een lijst van lijsten teruggeven."
    assert all([len(user_defined_class) == 3 for user_defined_class in user_defined_classes]), \
        "Je functie voeg_klassen_toe moet een lijst van lijsten teruggeven met elk 3 elementen."
    assert all([type(user_defined_class[0]) == str for user_defined_class in user_defined_classes]), \
        "De eerste element van elke lijst in de lijst die je functie voeg_klassen_toe teruggeeft moet een string zijn."
    assert all([type(user_defined_class[1]) == list for user_defined_class in user_defined_classes]), \
        "De tweede element van elke lijst in de lijst die je functie voeg_klassen_toe teruggeeft moet een lijst zijn."
    assert all([type(user_defined_class[2]) == list for user_defined_class in user_defined_classes]), \
        "De derde element van elke lijst in de lijst die je functie voeg_klassen_toe teruggeeft moet een lijst zijn."
    assert all([all([type(pattern) == str for pattern in user_defined_class[1]]) for user_defined_class in user_defined_classes]), \
        "De tweede element van elke lijst in de lijst die je functie voeg_klassen_toe teruggeeft moet een lijst zijn met strings."
    assert all([all([type(response) == str for response in user_defined_class[2]]) for user_defined_class in user_defined_classes]), \
        "De derde element van elke lijst in de lijst die je functie voeg_klassen_toe teruggeeft moet een lijst zijn met strings."

    print("\033[92m" + "Eigen klassen worden toegevoegd" + "\033[0m")
    # add the user defined classes to the intents
    for user_defined_class in user_defined_classes:
        intents['intents'].append({
            "tag": user_defined_class[0],
            "patterns": user_defined_class[1],
            "responses": user_defined_class[2]
        })
    # update the intents.json file
    with open('intents.json', 'w') as outfile:
        json.dump(intents, outfile)
        outfile.close()

words = []
classes = []
documents = []
ignore_letters = ['?', '!', ',', '.']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)  # tokenize each word
        words.extend(word_list)  # add to our words list
        documents.append((word_list, intent['tag']))  # add to documents in our corpus

        # opdracht 1: voeg de tag toe aan de lijst classes
        try:
            voeg_toe_aan_lijst(classes, intent['tag'])  # if the tag is not in our classes list, add it
        except:
            print("\033[91m" + "ERROR: Je functie voeg_toe_aan_lijst werkt niet." + "\033[0m")
            exit()

        try:
            assert len(classes) == len(set(classes))  # check for duplicates
            assert type(classes) == list
            assert all(type(x) == str for x in classes)
        except AssertionError:
            print("\033[91m" + "ERROR: In de functie voeg_toe_aan_lijst. "
                               "Je lijst bevat dubbele waarden of is geen lijst van strings." + "\033[0m")
            exit()

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]
try:
    words = verwijder_duplicaten_en_sorteer(words)  # remove duplicates and sort
except:
    print("\033[91m" + "ERROR: Je functie verwijder_duplicaten_en_sorteer werkt niet." + "\033[0m")
    exit()

try:
    assert len(words) == len(set(words))  # check for duplicates
    assert type(words) == list
except AssertionError:
    print("\033[91m" + "ERROR: In de functie verwijder_duplicaten_en_sorteer. "
                       "Je lijst bevat duplicaten of is niet van het type 'lijst" + "\033[0m")
    exit()

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

print("Dit zijn de woorden en klassen die ik ken: \n")
print_alle_woorden_en_klassen(words, classes)

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]  # list of tokenized words for the pattern
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in
                     word_patterns]  # lemmatize each word - create base word, in attempt to represent related words
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)  # create a copy of our output '0' for each tag
    output_row[classes.index(document[1])] = 1  # set tag as 1

    training.append([bag, output_row])
    # out training set will have a bag of words model and the output row that tells which tag that corresponds to

try:
    training = shuffle_training_data(training)  # shuffle our features and turn into np.array
    assert type(training) == list
    assert all(type(x) == list for x in training)
except:
    print("\033[91m" + "ERROR: Je functie shuffle_training_data werkt niet." + "\033[0m")
    exit()

training = np.array(training)

train_x = list(training[:, 0])  # list of patterns (features)
train_y = list(training[:, 1])  # list of intents (labels)

# create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains
# number of neurons equal to number of intents to predict output intent with softmax

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

print("\033[92m" + "Model is aan het trainen..." + "\033[0m")
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
hist = model.fit(np.array(train_x), np.array(train_y), epochs=400, batch_size=5, verbose=1)
model.save('chatbot_model.h5', hist)
print("\033[92m" + "Model is opgeslagen als chatbot_model.h5. \n"
                   "Maak nu het tweede deel van de opdracht in 'mijn_chatbot_gebruiken.py' "
                   "en begin the praten met je chatbot!" + "\033[0m")
