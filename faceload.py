import face_recognition
import pickle


def load_faces(file):

    all_face_encodings = {}

    #nathan = face_recognition.load_image_file("nathan.JPG")
    #nathan_encoding = face_recognition.face_encodings(nathan)[0]

    #aaroh = face_recognition.load_image_file("aaroh.jpg")
    #aaroh_encoding = face_recognition.face_encodings(aaroh)[0]


    #all_face_encodings = [nathan_encoding, aaroh_encoding]
    
    face = face_recognition.load_image_file(file)
    face_encoding = face_recognition.face_encodings(face)[0]

    all_face_encodings = [face_encoding]

    with open('dataset_faces.dat', 'wb') as f:
        pickle.dump(all_face_encodings, f)

    print("loaded authorized faces")



















