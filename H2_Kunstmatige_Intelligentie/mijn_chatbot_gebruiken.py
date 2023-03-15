# IMPORT STATEMENTS: NIET AANPASSEN ############################################

import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model


# IMPORT STATEMENTS: NIET AANPASSEN ############################################

# HIER BEGINT DE OPDRACHT #####################################################

def maak_kleine_letter(woord):
    """
    Maak van alle hoofdletters kleine letters
    Gebruik een return statement om het resultaat terug te geven
    TIP: je kan dit doen met één regel code
    """
    return woord.lower()


def woorden_naar_lijst(woorden, woordenboek, zin, toon_details):
    """
    De variabele 'woordenboek' is een lijst met allemaal nullen. We gaan nu voor elk woord in de woordenlijst kijken
    of het voorkomt in de zin. Als het woord voorkomt in de zin, dan veranderen we de nul in een 1 op de plek waar het
    woord staat. Daarvoor gebruik je een lus. Je kan zelf kiezen of dit een for of een while lus wordt. Let op: je moet
    ook de index van het woord weten.
    Je moet in deze functie geen print statement of return statement gebruiken.

    EXTRA: als de variabele toon_details True is, dan print je de index van het woord telkenmale als je het woord in de
    zin tegenkomt. Dit kan je doen met een print statement.

    :param woorden: de lijst met alle woorden. het woord op de i-de plek vind je met woorden[i]
    :param woordenboek: de lijst met allemaal nullen. De nul op de i-de plek moet je vervangen als het woord op de i-de
    plek in de zin voorkomt.
    :param zin: de zin waarin je de woorden gaat zoeken
    """
    for index in range(len(woorden)):
        woord = woorden[index]
        if woord in zin:
            woordenboek[index] = 1
            if toon_details:
                print("Woord gevonden: ", woord, " op index ", index)


def foutbericht(zekerheid, minimum_zekerheid):
    """
    Als de chatbot niet zeker genoeg is van zijn antwoord, dan geeft hij een foutbericht terug. Dat kan bijvoorbeeld
    een zin zijn zoals "Sorry, ik begrijp je niet helemaal. Kan je het anders formuleren?". Het foutbericht moet
    een string zijn.
    OPDRACHT: kijk na of de zekerheid groter is dan de minimum zekerheid. Als dat zo is, dan geef je een lege string
    terug. Anders geef je een foutbericht terug.
    Voor deze functie moet je een return statement gebruiken.
    """
    fout = "Sorry, ik begrijp je niet helemaal. Kan je het anders formuleren?"
    leeg = ""
    if zekerheid < minimum_zekerheid:
        return fout
    else:
        return leeg

# HIER EINDIGT DE OPDRACHT #####################################################
# PAS HIERONDER NIETS MEER AAN #################################################

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')


def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)  # tokenize the pattern
    test_word = sentence_words[0]
    try:
        lower_case = maak_kleine_letter(test_word)
    except:
        # print in red
        print("\033[91m Je functie maak_kleine_letter werkt niet goed \033[00m")
        exit()
    if lower_case != test_word.lower():
        print("\033[91m Je functie maak_kleine_letter doet iets anders dan hoofdletters verwijderen! \033[00m")
        exit()

    sentence_words = [lemmatizer.lemmatize(maak_kleine_letter(word)) for word in sentence_words]
    # lemmatize each word - create base word, in attempt to represent related words
    return sentence_words


def bag_of_words(sentence, words, show_details=True):
    """
    :return: the bag of words array: 0 or 1 for each word in the bag that exists in the sentence
    """
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)  # initialize bag of words
    for sentence_word in sentence_words:
        try:
            woorden_naar_lijst(words, bag, [sentence_word], show_details)
        except:
            print("\033[91m Je functie woorden_naar_lijst werkt niet goed \033[00m")
            exit()
        assert len(bag) == len(words), "Je functie woorden_naar_lijst past de lengte van woorden aan. " \
                                       "Dat is niet de bedoeling."

    # construct the correct bag of words and check if the correct solution is returned
    actual_bag = [0] * len(words)
    for sentence_word in sentence_words:
        for i, word in enumerate(words):
            if sentence_word == word:
                actual_bag[i] = 1
    assert bag == actual_bag, "Je functie woorden_naar_lijst geeft niet het juiste resultaat terug. " \
                              "Kijk nog eens goed naar de opdracht."

    # convert bag of words to numpy array and return
    return np.array(bag)


def predict_class(sentence, model):
    # filter out predictions below a threshold
    bow = bag_of_words(sentence, words, show_details=False)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[index, result] for index, result in enumerate(res) if result > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


MIN_PROBABILTY = 0.30
print("\033[94m" + 'Chatbot is gestart ...' + "\033[0m")
print("\033[94m" + 'Typ je vraag achter >>> ' + "\033[0m")
while True:
    print("\033[94m >>> \033[94m ", end="")
    message = input("")
    ints = predict_class(message, model)
    res = get_response(ints, intents)

    # if the probability is too low, print error
    probability = float(ints[0]['probability'])
    try:
        not_certain_answer = foutbericht(probability, MIN_PROBABILTY)
    except:
        print("\033[91m Je functie foutbericht() werkt niet goed \033[00m")
        exit()

    if probability < MIN_PROBABILTY and not_certain_answer == "":
        print("\033[91m Je functie foutbericht() geeft geen foutbericht terug als de zekerheid te laag is \033[00m")
        exit()
    elif probability >= MIN_PROBABILTY and not_certain_answer != "":
        print("\033[91m Je functie foutbericht() geeft een foutbericht terug als de zekerheid hoog genoeg is."
              "In dit geval moet je een lege string teruggeven! \033[00m")
        exit()

    if probability < MIN_PROBABILTY:
        print(not_certain_answer)
    else:
        print(res)

    # if the intent is goodbye, stop the loop
    if ints[0]['intent'] == 'goodbye':
        # print in blue
        print("\033[94m" + 'Chatbot sluit af ...' + "\033[0m")
        break
