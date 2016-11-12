import numpy as np
import cv2
from os.path import isfile, join
import imutils
import os
import util
from os import listdir


def main():
    process_image()


def process_image():
    path = "test"
    for r in listdir(path):
        file_path = join(path, r)
        if r.endswith("pgm") or r.endswith("jpg") or r.endswith("jpeg"):
            # load the image and convert it to grayscale
            image = cv2.imread(file_path)
            frame_process(image)
            cv2.waitKey(0)


def frame_process(img):
    cascade = cv2.CascadeClassifier('data/cascade.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    targets = cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in targets:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        rio_gray = gray[y:y + h, x:x + w]
        rio_color = img[y:y + h, x:x + w]
    cv2.imshow("detect", img)


main()
