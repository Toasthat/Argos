import cv2
import numpy as np


class faceTask(object):
    def __init__(self, face_data):
        face_cascade = cv2.CascadeClassifier(face_data["faceCascadePath"])
        eye_cascade = cv2.CascadeClassifier(face_data["eyeCascadePath"])

    def detectFace(gray_frame):
        pass
