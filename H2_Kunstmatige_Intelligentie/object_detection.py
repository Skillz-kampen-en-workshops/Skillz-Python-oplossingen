# object detection using opencv and numpy
# inspired by NeuralNines's tutorial on YouTube (https://www.youtube.com/watch?v=lE9eZ-FGwoE)

# IMPORT STATEMENTS. NIET AANPASSEN ############################
import numpy as np
import cv2
import time

# IMPORT STATEMENTS. NIET AANPASSEN ############################

image_path = r'obj_detection_model\room_people.jpg'
prototxt_path = r'obj_detection_model\MobileNetSSD_deploy.prototxt'
model_path = r'obj_detection_model\mobilenet_iter_73000.caffemodel'
confidence_threshold = 0.25

classes = ['background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow',
           'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']

classes_dutch = ['achtergrond', 'vliegtuig', 'fiets', 'vogel', 'boot', 'fles', 'bus', 'auto', 'kat', 'stoel', 'koe',
                 'eettafel', 'hond', 'paard', 'motorfiets', 'persoon', 'potplant', 'schaap', 'bank', 'trein', 'tv']

np.random.seed(543210)  # set random seed for reproducibility
colors = np.random.uniform(0, 255, size=(len(classes), 3))  # generate random colors for each class (rgb)

net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)  # load the model
image = cv2.imread(image_path)  # load the image
height, width = image.shape[0], image.shape[1]  # get the height and width of the image
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)  # create a blob from the image
# blob = binary large object

net.setInput(blob)  # set the blob as input for the model
detections = net.forward()  # forward pass through the model

for i in range(detections.shape[2]):  # loop over the detections
    confidence = detections[0, 0, i, 2]  # get the confidence of the detection
    if confidence > confidence_threshold:  # if the confidence is above the threshold
        class_index = int(detections[0, 0, i, 1])  # get the class index
        class_name = classes_dutch[class_index]  # get the class name in Dutch
        box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])  # get the bounding box
        (start_x, start_y, end_x, end_y) = box.astype('int')  # get the coordinates of the bounding box
        prediction_text = '{}: {:.2f}%'.format(class_name, confidence * 100)  # create the prediction text
        cv2.rectangle(image, (start_x, start_y), (end_x, end_y), colors[class_index], 3)  # draw the bounding box
        cv2.putText(image, prediction_text, (start_x, start_y - 15 if start_y > 30 else start_y + 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[class_index], 2)

cv2.imshow('image', image)  # show the image
cv2.waitKey(0)  # wait for a key press
cv2.destroyAllWindows()  # destroy all windows
