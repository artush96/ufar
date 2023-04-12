import time

import cv2



class Face:
    def __init__(self, image):
        self.image_name = image

    def read_image(self):
        img = cv2.imread(self.image_name, 0)
        return img

    def show_image(self, image, show = False):
        if show:
            self.show_it = cv2.imshow('preview', image)
            self.show_it.waitKey(0)

    def destroy_window(self):
        self.show_it.destroyAllWindows()

    def set_cascade(self):
        img = self.read_image()
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(img, 1.6, 5)
        img_grayscale = None
        for (x, y, w, h) in faces:
            img_grayscale = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return img_grayscale

    def show_faces(self,img_grayscale):
        cv2.imshow('faces', img_grayscale)
        cv2.waitKey(0)

    def run_recogniser(self):
        img_grayscale = self.set_cascade()
        self.show_faces(img_grayscale)
        time.sleep(3)
        self.destroy_window()


Face("pp.jpg").run_recogniser()



# waitKey() waits for a key press to close the window and 0 specifies indefinite loop


# cv2.destroyAllWindows() simply destroys all the windows we created.


# The function cv2.imwrite() is used to write an image.
#cv2.imwrite('grayscale.jpg', img_grayscale)
