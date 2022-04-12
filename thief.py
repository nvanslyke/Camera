import cv2 as cv
import yagmail
import yagmail.oauth2
import os
from PIL import Image
import PIL
import time
import numpy as np



def main():
    path_to_photo = "C:\\Users\\nvans\\Desktop\\facePhoto\\"
    video = cv.VideoCapture()
    video.open(0, cv.CAP_DSHOW)
    while True:
        useless, frame = video.read()
        grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faceCascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(
            grey,
            scaleFactor=1.3,
            minNeighbors=3,
            minSize=(30, 30)
        )

        if len(faces) > 0:

            cv.imwrite("UnknownUser.jpg", frame)

            send_text()

        cv.imshow('cam', frame)
        if cv.waitKey(1) == ord('q'):
            break

    video.release()
    cv.destroyAllWindows()

def send_text():
    email = "throwaway3123456@gmail.com"
    password = "fgzpxpcvkycqhsye"

    UnknownUser = ["<img src='C:\\Users\\nvans\\Desktop\\Camera\\UnknownUser'>"]

    try:
        yag = yagmail.SMTP(user=email, password=password)
        yag.send(to='5128155645@mms.att.net', subject='Unauthorized User Detected', contents=UnknownUser)
        print("Email sent successfully")
    finally:
        print("Error, email was not sent")


if __name__ == "__main__":
    main()


