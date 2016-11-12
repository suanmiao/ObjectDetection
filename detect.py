import numpy as np
import cv2


def detect():
    cascade = cv2.CascadeClassified('')
    img = cv2.imread('')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    targets = cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in targets:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        rio_gray = gray[y:y + h, x:x + w]
        rio_color = img[y:y + h, x:x + w]
    cv2.imshow("detect", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect()
