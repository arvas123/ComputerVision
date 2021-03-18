import cv2
from matplotlib import pyplot as plt
import os

curdir = os.getcwd() + '\\SampleImages'
img = cv2.imread(curdir + '\\antiqueTractors.jpg')
cv2.imshow("Images", img)
cv2.waitKey(0)
img = cv2.imread(curdir + '\\beachBahamas.jpg')
cv2.imshow("Images", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
