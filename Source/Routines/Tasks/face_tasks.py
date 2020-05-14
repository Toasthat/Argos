"""Holds the class that makes objects which perform
the acts of noticing faces"""

import cv2
from pickle import loads

import numpy as np


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


class dnnFaceDetector(object):
    def __init__(
        self,
        dnnDetectorPath,
        dnnWeightsPath,
        minimumConfidence=0.5,
        blobMean=(104.0, 177.0, 123.0),
    ):

        self.detector = cv2.dnn.readNetFromCaffe(dnnDetectorPath, dnnWeightsPath)
        self.minimumConfidence = minimumConfidence
        self.blobSize = (300, 300)
        self.blobMean = blobMean
        self.feedWidth = 640
        self.feedHeight = 480
        self.ROI_multiplicand = np.array(
            [self.feedWidth, self.feedHeight, self.feedWidth, self.feedHeight]
        )

    def getFaceRegions(self, image):

        self.blob = cv2.dnn.blobFromImage(
            cv2.resize(image, self.blobSize),
            1.0,
            self.blobSize,
            self.blobMean,
            swapRB=False,
            crop=False,
        )
        ROIs = []
        self.detector.setInput(self.blob)
        detections = self.detector.forward()
        # only executes if at least one face is found
        for i in range(0, detections.shape[2]):
            # if probabiliy of face higher than minimum
            if detections[0, 0, i, 2] > self.minimumConfidence:
                # Get bounding box for region
                (startX, startY, endX, endY) = (
                    detections[0, 0, i, 3:7] * self.ROI_multiplicand
                ).astype("int")
                # if the region is sufficiently large
                if endX - startX > 20 and endY - startY > 20:
                    ROIs.append((startX, startY, endX, endY))
        return ROIs


class svmFace(object):
    """This class makes an object that uses svm based
    facial recognition"""

    def __init__(
        self, embedderPath, svmRecognizerPath, svmLabelsPath,
    ):

        self.embedder = cv2.dnn.readNetFromTorch(embedderPath)
        self.recognizer = loads(open(svmRecognizerPath, "rb").read())
        self.label_encoder = loads(open(svmLabelsPath, "rb").read())
        self.blobScaleFactor = 1.0 / 255
        self.blobSize = (96, 96)

    def identify(self, frame, facialRoI):
        (startX, startY, endX, endY) = facialRoI
        face = frame[startY:endY, startX:endX]
        """
        faceBlob = (
            cv2.dnn.blobFromImage(
                face,
                self.blobScaleFactor,
                self.blobSize,
                (0, 0, 0),
                swapRB=True,
                crop=False,
            ),
        )
        """
        # print(faceBlob)
        self.embedder.setInput(
            cv2.dnn.blobFromImage(
                face,
                self.blobScaleFactor,
                self.blobSize,
                (0, 0, 0),
                swapRB=True,
                crop=False,
            )
        )
        vector = self.embedder.forward()

        predictions = self.recognizer.predict_proba(vector)[0]
        bestGuess = np.argmax(predictions)
        name, probability = (
            self.label_encoder.classes_[bestGuess],
            predictions[bestGuess],
        )
        return name, probability

    def labelFrame(self, frame, facialROI):
        name, probability = self.identify(frame, facialROI)
        (startX, startY, endX, endY) = facialROI
        label_location = startY - 10 if startY > 20 else startY + 10

        bestGuess = "{}: {:.2f}%".format(name, probability * 100)
        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
        cv2.putText(
            frame,
            bestGuess,
            (startX, label_location),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.45,
            (0, 0, 255),
            2,
        )
        return frame


class EigenFace(object):
    """ use EigenFace based algorithm to recognize faces """

    pass
