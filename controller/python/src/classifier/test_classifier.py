import cv2
import glob
import os
import re
from PIL import Image

car_classifier = cv2.CascadeClassifier('cascade.xml')
if 'test_pngs' not in os.listdir('.'):
    os.mkdir('test_pngs')

for i in os.listdir('./test_images/'):
    name = re.findall('(.+)\.', i)
    img = Image.open('./test_images/' + i)
    img.save('./test_pngs/' + name[0] + '.png', 'png')

folder_len = len('test_pngs')
if 'resized_pngs' not in os.listdir('.'):
    os.mkdir('resized_pngs')

for img_path in glob.glob('test_pngs' + '/*.png'):
    image = cv2.imread(img_path)
    img_resized = cv2.resize(image, (64, 64))
    # cv2.imwrite('resized_pngs' + img_path[folder_len:], img_resized)
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    cars = car_classifier.detectMultiScale(gray)
    print(f"{len(cars)} cars detected in the image")
    for (x, y, w, h) in cars:
        cv2.rectangle(img_resized, (x, y), (x + w, y + h), (255, 0, 0), 3)
    cv2.imshow('img', img_resized)
    cv2.waitKey()

cv2.destroyAllWindows()
