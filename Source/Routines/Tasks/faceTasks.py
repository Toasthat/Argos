import cv2
import numpy as np


class faceCascadeDetector(object):
    def __init__(self, faceCascadePath, eyeCascadePath):
        self.face_cascade = cv2.CascadeClassifier(faceCascadePath)
        self.eye_cascade = cv2.CascadeClassifier(eyeCascadePath)

    def getFaces(self, gray_frame):
        return self.face_cascade.detectMultiScale(
            gray_frame, 1.3, 5, minSize=(120, 120)
        )


class EigenFace(object):
    """ use EigenFace based algorithm to recognize faces """
