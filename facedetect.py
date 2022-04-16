import cv2 as cv

red = (0, 0, 255)


def face_detected(face_cascade, eye_cascade, grey, frame):

    faces = face_cascade.detectMultiScale(
        grey,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(50, 50)
    )

    for (x, y, w, h) in faces:

        roi_grey = grey[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_grey)

        if len(eyes) > 1:
            cv.rectangle(frame, (x, y), (x + w, y + h), red, 2)
            return True
    return False
