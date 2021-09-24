import cv2


def detect_car(img_path):
    car_classifier = cv2.CascadeClassifier('cascade.xml')
    image = cv2.imread(img_path)
    img_resized = cv2.resize(image, (64, 64))
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    cars = car_classifier.detectMultiScale(gray)
    print(f"{len(cars)} cars detected in the image")
    for (x, y, w, h) in cars:
        cv2.rectangle(img_resized, (x, y), (x + w, y + h), (255, 0, 0), 3)
    cv2.imshow('img', img_resized)
    cv2.waitKey()


cv2.destroyAllWindows()



















