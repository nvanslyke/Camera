import face_recognition
import numpy
import cv2 as cv
import platform
import os
import pickle
import time
#import gui
import sendtext
#import faceload

red = (0, 0, 255)
green = (0, 255, 0)


def main():

  
    '''
    try:
        with open('dataset_faces.dat', 'rb') as f:
            authorized_encodings = pickle.load(f)
    except:
            #faceload.load_faces()
            gui.main()
            with open('dataset_faces.dat', 'rb') as f:
                authorized_encodings = pickle.load(f)
'''
    with open('dataset_faces.dat', 'rb') as f:
        authorized_encodings = pickle.load(f)

    
    video = cv.VideoCapture()

    if platform.system() == "Windows":
        video.open(0, cv.CAP_DSHOW)
    else:
        video.open(0, cv.CAP_V4L)

    while True:
       
        useless, frame = video.read()
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        breaker = False
        i = 0
        for (x, y, w, h), face_encoding in zip(face_locations, face_encodings):
            
            i += 1
            #print(str(i) + str(len(face_locations)))
            results = face_recognition.compare_faces(authorized_encodings, face_encoding)
            print(results)
            print("bruh")
            if True in results:
                cv.rectangle(frame, (h, x), (y, w), green, 2)
                #time.sleep(10)
                break
            elif i >= len(face_locations):
                cv.rectangle(frame, (h, x), (y, w), red, 2)
                cv.imwrite("UnknownUser.jpg", frame)
                sendtext.send_text("UnknownUser.jpg")
                os.remove("UnknownUser.jpg")
                breaker = True
            else:
                cv.rectangle(frame, (h, x), (y, w), red, 2)

            if breaker:
                break

        if breaker:
            break

        

        if cv.waitKey(1) == ord('q'):
            break
        
        cv.imshow('pic', frame)
    
    video.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
