import yagmail
import yagmail.oauth2
from datetime import datetime


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
