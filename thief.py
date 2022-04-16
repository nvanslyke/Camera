import cv2 as cv
import platform
import os
from PIL import Image
import PIL
import time
import numpy as np
import face_recognition
import sendtext
import facedetect


def main():

    video = cv.VideoCapture()

    if platform.system() == "Windows":
        video.open(0, cv.CAP_DSHOW)
    else:
        video.open(0, cv.CAP_V4L)

    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")

    while True:

        useless, frame = video.read()
        grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        if facedetect.face_detected(face_cascade, eye_cascade, grey, frame):
            cv.imwrite("UnknownUser.jpg", frame)
            sendtext.send_text("UnknownUser.jpg")
            os.remove("UnknownUser.jpg")
            break

        cv.imshow('cam', frame)
        if cv.waitKey(1) == ord('q'):
            break

    video.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
