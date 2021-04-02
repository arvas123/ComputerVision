import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("SampleImages/snowLeo2.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.draw()
# plt.waitforbuttonpress(0)
# plt.close()
cv2.circle(img, (125, 128), 80, (255, 0, 0))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "snowLeo2.jpg", (10, 30), font, 1, (250, 0, 0))
cv2.line(img, (564, 131), (599, 346), [255] * 3, 10)
cv2.ellipse(img, (123, 385), (48, 28), 0, 0, 180, (0, 250, 0), 10)
cv2.ellipse(img, (452, 404), (48, 25), -30, 180, 0, (0, 0, 250), 10)
plt.imshow(img)
plt.draw()
plt.waitforbuttonpress(0)
plt.close()
