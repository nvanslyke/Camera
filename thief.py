import cv2 as cv
import yagmail
import yagmail.oauth2
#import face-recognition


def send_text():

    yag = yagmail.SMTP(user='throwaway3123456@gmail.com', password='throwAway!123')
    yag.send(to='5128155645@txt.att.net', subject='Testing Yagmail', contents='Hurray, it worked!')
    print("Email sent successfully")

    print("Error, email was not sent")


send_text()

print("hello world")
print("goodbye world")