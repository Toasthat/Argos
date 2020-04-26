import cv2


def detect_face_cascade(frame, gray_frame):
    face_cascade = cv2.CascadeClassifier(
        "./task_data/haarcascade_frontalface_default.xml"
    )
    faces = face_cascade.detectMultiScale(gray_frame, 1.08, 5)
    for (x, y, width, height) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)
