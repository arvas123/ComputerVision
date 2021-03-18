import cv2
import numpy as np
from matplotlib import pyplot as plt
import random

image = cv2.imread("SampleImages/antiqueTractors.jpg")
channels = cv2.split(image)
random.shuffle(channels)
# print(channels)
new_image=cv2.merge(channels)
cv2.imshow("Random Image", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

