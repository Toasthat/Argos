import cv2
import os
import numpy as np
from argos_common import ARGOS_CONFIG, ARGOS_HOME, load_config

if __name__ == "__main__":
    feed = cv2.VideoCapture(0)
    config = load_config(ARGOS_CONFIG, "embeddingsExtractor")
    label = input("please enter your first name:")
    detector = cv2.dnn.readNetFromCaffe(
        ARGOS_HOME + config["dnn_detector_path"],
        ARGOS_HOME + config["dnn_weights_path"],
    )
    photo_count = 0
    ret, frame = feed.read()
    cv2.namedWindow("capture user photos")
    cv2.waitKey(10)
    labelPath = ARGOS_HOME + config["training_directory"] + label
    os.mkdir(labelPath)
    while photo_count < 24:
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
            cv2.imwrite("photo{}.jpg".format(photo_count), labelPath)
            photo_count += 1
        cv2.imshow("capture user photos", frame)
        cv2.waitKey(10)
    print("success?")
    cv2.destroyAllWindows()
