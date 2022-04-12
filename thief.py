import cv2 as cv
import yagmail
import yagmail.oauth2
import os
from PIL import Image
import PIL
import time
from datetime import datetime
import numpy as np



def main():

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

            send_text("UnknownUser.jpg")
            break

        cv.imshow('cam', frame)
        if cv.waitKey(1) == ord('q'):
            break

    video.release()
    cv.destroyAllWindows()

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


