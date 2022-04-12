import cv2 as cv
import yagmail
import yagmail.oauth2
import numpy as np
#import face_recognition


def main():

    video = cv.VideoCapture()
    video.open(0, cv.CAP_DSHOW)
    while True:
        useless, frame = video.read()
        cv.imshow('cam', frame)
        if cv.waitKey(1) == ord('q'):
            break

    video.release()
    cv.destroyAllWindows()

def send_text(file):
    email = "throwaway3123456@gmail.com"
    password = "fgzpxpcvkycqhsye"

    try:
        yag = yagmail.SMTP(user=email, password=password)
        yag.send(to='5128155645@mms.att.net', subject='Unauthorized User Detected', contents=file)
        print("Email sent successfully")
    finally:
        print("Error, email was not sent")


if __name__ == "__main__":
    main()


