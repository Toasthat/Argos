import cv2
import os
import numpy as np
import time
import sys
from argos_common import ARGOS_CONFIG, ARGOS_HOME, load_config

if __name__ == "__main__":
    feed = cv2.VideoCapture(0)
    config = load_config(ARGOS_CONFIG, "embeddingsExtractor")
    if len(sys.argv) > 1:
        label = sys.argv[1]
    else:
        label = input("Please enter your name: ")
    detector = cv2.dnn.readNetFromCaffe(
        ARGOS_HOME + config["dnn_detector_path"],
        ARGOS_HOME + config["dnn_weights_path"],
    )
    photo_count = 0
    number_of_photos = len(
        [
            name
            for name in os.listdir(
                ARGOS_HOME + config["training_directory"] + "stranger_danger/"
            )
            if os.path.isfile(
                os.path.join(
                    ARGOS_HOME + config["training_directory"] + "stranger_danger/", name
                )
            )
        ]
    )
    ret, frame = feed.read()
    cv2.namedWindow("capture user photos")
    cv2.waitKey(10)
    labelPath = ARGOS_HOME + config["training_directory"] + label
    if not os.path.exists(labelPath):
        os.mkdir(labelPath)
    while photo_count < number_of_photos:
        ret, frame = feed.read()
        detector.setInput(
            cv2.dnn.blobFromImage(
                cv2.resize(frame, (300, 300)),
                1.0,
                (300, 300),
                (104.0, 177.0, 123.0),
                swapRB=False,
                crop=False,
            )
        )
        detections = detector.forward()
        bestGuess = np.argmax(detections[0, 0, :, 2])
        # if this photo probably contains a face
        if detections[0, 0, bestGuess, 2] > 0.7:
            cv2.imwrite(labelPath + "/photo{}.jpg".format(photo_count), frame)
            photo_count += 1
            time.sleep(0.5)
        cv2.imshow("capture user photos", frame)
        cv2.waitKey(10)
    print("success?")
    cv2.destroyAllWindows()
