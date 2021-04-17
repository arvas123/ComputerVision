import cv2
import numpy as np
import matplotlib.pyplot as plt

licenseCascade = cv2.CascadeClassifier("haarcascades/haarcascade_russian_plate_number.xml")
img = cv2.imread('SampleImages/License/license2.jfif')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
lic_rects = licenseCascade.detectMultiScale(gray_img, 1.3, 5)
for x, y, w, h in lic_rects:
	print(x, y, w, h)
	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
cv2.imshow("img", img)
cv2.moveWindow("img", 500,0)
cv2.waitKey(0)
