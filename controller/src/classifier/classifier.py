import os

import cv2


class Classifier:
    def __init__(self, classifier_path=None):
        self.classifier_path = 'E:\\Files\\Code\\Thesis\\controller\\src\\classifier\\cascade.xml' if classifier_path is None else classifier_path
        self.image_resized = None
        self.cars = None

    def count_cars(self, img_path) -> int:
        car_classifier = cv2.CascadeClassifier(self.classifier_path)
        image = cv2.imread(img_path)
        self.image_resized = cv2.resize(image, (320, 320))
        gray = cv2.cvtColor(self.image_resized, cv2.COLOR_BGR2GRAY)
        self.cars = car_classifier.detectMultiScale(gray, 1.1, 2)
        self.draw_on_detected_cars()
        return len(self.cars)

    def draw_on_detected_cars(self):
        if self.image_resized is None or self.cars is None:
            print('please use count_cars() first')
        else:
            for (x, y, w, h) in self.cars:
                cv2.rectangle(self.image_resized, (x, y), (x + w, y + h), (0, 255, 255), 2)
            cv2.imshow('img', self.image_resized)
            cv2.waitKey()
            cv2.destroyAllWindows()


# classifier = Classifier()
# classifier.count_cars('E:\\Files\\Code\\Thesis\\controller\\src\\classifier\\test_images\\0.jpg')
# classifier.draw_on_detected_cars()
