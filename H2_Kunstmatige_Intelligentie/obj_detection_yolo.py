# IMPORT STATEMENTS. NIET AANPASSEN ############################
import torch
import numpy as np
import cv2
import time

# Check of al deze modules geïnstalleerd zijn. Als dat niet zo is, zal je een foutmelding krijgen.
# Als je een foutmelding krijgt, ga dan naar de terminal en typ het volgende commando:
# pip install <module>

# IMPORT STATEMENTS. NIET AANPASSEN ############################

# HIER BEGINT DE CODE DIE JE MOET AANPASSEN #####################

def print_klassen(klassen):
    """
    Print alle klassen die het model kan detecteren. Je doet dit door er telkens een nummer voor te zetten.
    HINT: gebruik een for-loop. De klassennamen zijn in het Engels.
    :param klassen: een lijst met klassen
    :return: geen return. Gebruik alleen print()
    """
    for nummer in range(len(klassen)):
        klasse = klassen[nummer]
        print(str(nummer + 1) + ": " + klasse)


def kleuren_genereren(aantal_klassen):
    """
    Om de afbeelding duidelijker te maken, zullen we elke klasse een eigen kleur geven. Deze functie genereert een lijst
    met willenkeurige kleuren. Eén kleur bestaat uit 3 waarden: rood, groen en blauw. Deze waarden zijn getallen tussen 0 en 255.
    Je moet dus een lijst maken met 3 waarden per klasse, een lijst van lijsten dus. De kleine lijsten hebben lengte 3
    en de grote lijst heeft lengte aantal_klassen.

    TIP: gebruik de functie np.random.uniform() om een lijst met random getallen te genereren. Deze functie heeft 3 parameters:
    - de eerste parameter is de startwaarde van de lijst
    - de tweede parameter is de eindwaarde van de lijst
    - de derde parameter is de lengte van de lijst
    Bijvoorbeeld: np.random.uniform(0, 255, size=(3, 3)) genereert een lijst van 3 lijsten met elk 3 getallen tussen 0 en 255.

    :param aantal_klassen: het aantal klassen dat het model kan detecteren
    :return: een lijst met kleuren. Elke kleur is een lijst met 3 waarden.
    """

    return np.random.uniform(0, 255, size=(aantal_klassen, 3))

    # of met een for-loop:
    # kleuren = []
    # for i in range(aantal_klassen):
    #     kleur = np.random.uniform(0, 255, size=(3))
    #     kleuren.append(kleur)
    # return kleuren


def maak_tekst(label, zekerheid):
    """
    We willen graag weten wat het model detecteert. Deze functie maakt een tekst met de label en de zekerheid.
    Rond de zekerheid af op 2 cijfers achter de komma. Gebruik de functie round().
    :param label: de label van de klasse
    :param zekerheid: de zekerheid van het model
    :return: een string met de tekst. Gebruik een return en geen print!
    """
    afgerond = round(zekerheid, 2)
    tekst = label + ": " + str(afgerond)
    return tekst


## HIER EINDIGT DE CODE DIE JE MOET AANPASSEN #####################
## HIERONDER STAAT DE CODE DIE ALLES SAMEN BRENGT #################
## PAS NIETS AAN HIERONDER ########################################


class ObjectDetection:
    """
    Class implements the Yolov5 model to make inferences on a webcam using OpenCV.
    """

    def __init__(self, seed=42):
        self.model = self.load_model()
        self.classes = self.model.names
        self.colors = self.get_colors(seed)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print('Using device: ', self.device)
        self.print_classes()

        # test function maak_tekst() so that we can catch errors early
        try:
            text = maak_tekst("test", 0.5)
            assert isinstance(text, str), "De functie maak_tekst() moet een string teruggeven"
            assert len(text) > 0, "De functie maak_tekst() moet een string teruggeven"
            assert "test" in text, "De functie maak_tekst() moet het label bevatten"
            assert "0.5" in text, "De functie maak_tekst() moet de zekerheid bevatten"
        except AssertionError as e:
            print("\033[91m De functie maak_tekst() is niet juist:" + str(e) + "\033[00m")
            exit(-2)
        except Exception as e:
            print("\033[91m De functie maak_tekst() geeft een fout \033[00m")
            print(e)
            exit(-2)

    def print_classes(self):
        """
        Print the classes
        """
        classes_list = list(self.classes.values())
        try:
            print_klassen(classes_list)
        except Exception as e:
            # print in red
            print("\033[91m De functie print_klassen() geeft een fout \033[00m")
            print(e)
            exit(-2)

    def get_colors(self, seed):
        """
        Get the colors for the bounding boxes
        :return: a dictionary with {class_id: color}
        """
        np.random.seed(seed)
        try:
            colors = kleuren_genereren(len(self.classes))
            assert len(colors) == len(self.classes), "De lijst met kleuren heeft niet de juiste lengte"
            assert all([len(color) == 3 for color in colors]), "De kleine lijsten in de lijst met kleuren hebben niet de juiste lengte"
            assert all([all([0 <= c <= 255 for c in color]) for color in colors]), "De waarden in de lijst met kleuren moeten tussen 0 en 255 liggen"
        except AssertionError as e:
            print("\033[91m De functie kleuren_genereren() is niet juist:" + str(e) + "\033[00m")
            exit(-2)
        except Exception as e:
            print("\033[91m De functie kleuren_genereren() geeft een fout \033[00m")
            print(e)
            exit(-2)
        colors = np.random.uniform(0, 255, size=(len(self.classes), 3))
        colors = {i: colors[i] for i in range(len(self.classes))}
        return colors

    def load_model(self):
        """
        Load the model from PyTorch Hub
        :return: the model
        """
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        return model

    def score_frame(self, frame):
        """
        Takes a single frame as input and scores the frame using the yolov5 model.
        :param frame: the frame to score in numpy/list/tuple format
        :return: labels and coordinates of the bounding boxes and confidence scores
        """
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cords, confs = results.xyxyn[0][:, -1].numpy(), results.xyxyn[0][:, :-1].numpy(), results.xyxyn[0][:, 4].numpy()
        return labels, cords, confs

    def class_to_label(self, class_id):
        """
        Convert the class id to a label
        :param class_id: the class id
        :return: the label
        """
        return self.classes[int(class_id)]

    def plot_boxes(self, results, frame, threshold):
        """
        Plot the bounding boxes on the frame
        :param frame: the frame to plot the boxes on
        :param results: the results from the model (labels, cords, confs)
        :param threshold: the threshold for the confidence score
        :return: the frame with the bounding boxes
        """
        labels, cord, confs = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if confs[i] > threshold:
                x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(row[3] * y_shape)
                color = self.colors[labels[i]]
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                # text has class and confidence score
                text = maak_tekst(self.class_to_label(labels[i]), confs[i])
                cv2.putText(frame, text, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        return frame

    def run(self):
        """
        Main function to run the webcam
        :return: None
        """
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            start_time = time.perf_counter()
            ret, frame = cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame, 0.2)
            end_time = time.perf_counter()
            fps = 1 / (end_time - start_time)
            cv2.putText(frame, 'FPS: ' + str(round(fps, 2)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('frame', frame)

            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


# Welcome message
print("Welkom bij de opdracht Object Detection met YOLOv5. Vul alle functies in en run het programma om te kijken of "
      "het werkt.")
if input('Typ GO om te beginnen: ') == 'GO':
    # Create an instance of the class and run the webcam
    detection = ObjectDetection(seed=543210)
    detection.run()



