import cv2 as cv
import yagmail
import yagmail.oauth2
import face_recognition


def main():

    video = cv.VideoCapture()
    video.open(0, cv.CAP_DSHOW)
    while True:
        ret, frame = video.read()
        cv.imshow('cam', frame)


def send_text(file):
    try:
        yag = yagmail.SMTP(user='throwaway3123456@gmail.com', password='throwAway!123')
        yag.send(to='5128155645@mms.att.net', subject='Unauthorized user detected', contents=file)
        print("Email sent successfully")
    finally:
        print("Error, email was not sent")


if __name__ == "__main__":
    main()

