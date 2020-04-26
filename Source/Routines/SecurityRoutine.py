import cv2
import numpy as np
from tomlkit import parse
from Tasks.faceTasks import faceCascadeDetector
import os


# class SecurityRoutine(Routine, faceTask):
#    def __init__(self,):
#        Routine.__init__(self, gray=True)


def load_config(toml_path, table):
    with open(toml_path, "r") as f:
        data = f.read()
        config = parse(data)
        print(config)
    return config[table]


if __name__ == "__main__":
    # initilize the feed
    # TODO add CaptureManager or similar class to handle multiple feeds
    feed = cv2.VideoCapture(0)
    print("yeet")
    frame = feed.read()
    print("yak")
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # load necessary configs from argos.toml
    argos_home = os.getenv("ARGOS_HOME")

    face_data = load_config(argos_home + "/Storage/config/argos.toml", "face_data")
    # set up tasks

    # TODO have constraints passed as cmdline argument in order to choose
    # between different implementations based on performance and accuracy
    print(face_data)
    faceDetector = faceCascadeDetector(face_data)

    # next main loop
