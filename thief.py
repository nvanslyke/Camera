import cv2 as cv
import yagmail
import yagmail.oauth2
import platform
import os
from PIL import Image
import PIL
import time
from datetime import datetime
import numpy as np


red = (0, 0, 255)

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

        if face_detected(face_cascade, eye_cascade, grey, frame):
            cv.imwrite("UnknownUser.jpg", frame)
            send_text("UnknownUser.jpg")
            break

        cv.imshow('cam', frame)
        if cv.waitKey(1) == ord('q'):
            break

    video.release()
    cv.destroyAllWindows()

def face_detected(face_cascade, eye_cascade, grey, frame):

    faces = face_cascade.detectMultiScale(
        grey,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(75, 75)
    )

    for (x, y, w, h) in faces:

        cv.rectangle(frame, (x, y), (x + w, y + h), red, 2)
        roi_grey = grey[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_grey)

        if len(eyes) > 1:
            return True
    return False

def send_text(file):
    now = datetime.now()

    email = "throwaway3123456@gmail.com"
    password = "fgzpxpcvkycqhsye"
    subject = 'Unauthorized User Detected'
    recipient = '5128155645@mms.att.net'
    current_time = now.strftime("%H:%M:%S")
    content = "Time = " + str(current_time)
    try:
        yag = yagmail.SMTP(user=email, password=password)
        yag.send(to=recipient,
                 subject=subject,
                 contents=content,
                 attachments=file
                 )
        print("Text sent successfully")
    except:
         print("Error, text was not sent")


if __name__ == "__main__":
    main()
