"""Holds the class that makes objects which perform
the acts of noticing faces"""

import cv2
from pickle import loads

# import numpy as np


class FaceCascadeDetector(object):
    """This class makes an object that uses haar cascade
    based facial detection"""

    def __init__(self, faceCascadePath, eyeCascadePath):
        self.face_cascade = cv2.CascadeClassifier(faceCascadePath)
        self.eye_cascade = cv2.CascadeClassifier(eyeCascadePath)

    def get_faces(self, gray_frame):
        """is passed a frame that is tested
        for faces"""
        return self.face_cascade.detectMultiScale(
            gray_frame, 1.3, 5, minSize=(120, 120)
        )


class svmFace(object):
    """This class makes an object that uses svm based
    facial recognition"""

    def __init__(self, embedder_path, svm_recognizer_path, svm_labels_path):
        self.embedder = cv2.dnn.readNetFromTorch(embedder_path)
        self.recognizer = loads(open(svm_recognizer_path))
        self.label_encoder = loads(open(svm_labels_path))

    def check_if_user(frame):
        pass


class EigenFace(object):
    """ use EigenFace based algorithm to recognize faces """

    pass
