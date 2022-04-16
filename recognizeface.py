import face_recognition


def recognize_face(image, compare):

    try:
        secure_user = face_recognition.load_image_file(image)

        compare_user = face_recognition.load_image_file(compare)

        secure_encoding = face_recognition.face_encodings(secure_user)[0]
        compare_encoding = face_recognition.face_encodings(compare_user)[0]

        return face_recognition.compare_faces([secure_encoding], compare_encoding)

    except IndexError as e:
        print(e)
        return

