import cv2
import numpy as np
from tomlkit import parse
from Tasks.faceRecognitionTask import faceCascadeDetector


class SecurityRoutine(Routine, faceTask):
    def __init__(self,):
        Routine.__init__(self, gray=True)


def load_config(toml_file, table):
    with open(toml_file, "r") as f:
        data = f.read()
        config = parse(data)
        print(config)
    return config[table]


if __name__ == "__main__":
    # set up tasks
    # TODO add CaptureManager or similar class to handle multiple feeds
    feed = cv2.VideoCapture(0)
    frame = feed.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # TODO replace bit below with actual config file
    face_data = {
        "faceCascadePath": "./Tasks/task_data/haarcascade_frontalface_default.xml",
        "eyeCascadePath": "./Tasks/task_data/haarcascade_eye.xml",
    }
    # TODO have constraints passed as cmdline argument in order to choose
    # between different implementations based on performance and accuracy
    faceDetector = faceCascadeDetector(face_data)
