
import face_recognition


known_image = face_recognition.load_image_file("Pictures/pic1.jpg")
unknown_image = face_recognition.load_image_file("Pictures/pic2.jpg")

known_image_encoding = face_recognition.face_encodings(known_image)[0]
unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([known_image_encoding], unknown_image_encoding)

print(results)