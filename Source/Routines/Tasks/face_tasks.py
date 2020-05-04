"""Holds the class that makes objects which perform
the acts of noticing faces"""

import cv2
#import numpy as np

class FaceCascadeDetector(object):
    """This class makes an object that does
    the facial detection for the program"""
    def __init__(self, faceCascadePath, eyeCascadePath):
        self.face_cascade = cv2.CascadeClassifier(faceCascadePath)
        self.eye_cascade = cv2.CascadeClassifier(eyeCascadePath)

    def get_faces(self, gray_frame):
        """is passed a frame that is tested
        for faces"""
        return self.face_cascade.detectMultiScale(
            gray_frame, 1.3, 5, minSize=(120, 120)
        )


class EigenFace(object):
    """ use EigenFace based algorithm to recognize faces """
