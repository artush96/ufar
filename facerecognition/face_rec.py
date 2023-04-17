import cv2
import face_recognition

class FaceComparer:
    def __init__(self, img1, img2):
        self.img1 = img1
        self.img2 = img2

    def load_image(self):
        self.img1 = face_recognition.load_image_file(self.img1)
        self.img1 = cv2.cvtColor(self.img1, cv2.COLOR_BGR2RGB)
        self.img2 = face_recognition.load_image_file(self.img2)
        self.img2 = cv2.cvtColor(self.img2, cv2.COLOR_BGR2RGB)

    def locate_faces(self):
        self.faceLoc1 = face_recognition.face_locations(self.img1)[0]
        self.encode1 = face_recognition.face_encodings(self.img1)[0]
        self.faceLoc2 = face_recognition.face_locations(self.img2)[0]
        self.encode2 = face_recognition.face_encodings(self.img2)[0]

    def compare_faces(self):
        results = face_recognition.compare_faces([self.encode1], self.encode2)
        faceDistance = face_recognition.face_distance([self.encode1], self.encode2)
        self.results = results
        self.faceDistance = faceDistance

    def annotate_images(self):
        cv2.rectangle(self.img1, (self.faceLoc1[3], self.faceLoc1[0]), (self.faceLoc1[1], self.faceLoc1[2]),
                      (106, 0, 128), 2)
        cv2.rectangle(self.img2, (self.faceLoc2[3], self.faceLoc2[0]), (self.faceLoc2[1], self.faceLoc2[2]),
                      (106, 0, 128), 2)
        cv2.putText(self.img2, f'{self.results} {round(self.faceDistance[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (0, 0, 255), 2)


    def display_images(self):
        cv2.imshow('Image 1', self.img1)
        cv2.imshow('Image 2', self.img2)
        cv2.waitKey(0)

    def img_compare(self):
        self.load_image()
        self.locate_faces()
        self.compare_faces()
        self.annotate_images()
        self.display_images()


FaceComparer('z1.jpg', 'z2.jpg').img_compare()