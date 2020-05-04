"""Holds the class that makes objects which perform
the acts of noticing faces"""

import cv2
#import numpy as np


class FaceCascadeDetector(object):
    """class which is passed an image of a face?"""
    def __init__(self, face_data):
        self.face_cascade = cv2.CascadeClassifier(face_data["faceCascadePath"])
        self.eye_cascade = cv2.CascadeClassifier(face_data["eyeCascadePath"])

    def get_faces(self, gray_frame):
        """is passed a frame that is tested
        for faces"""
        return self.face_cascade.detectMultiScale(
            gray_frame, 1.3, 5, minSize=(120, 120)
        )


class EigenFace(object):
    """ use EigenFace based algorithm to recognize faces """
