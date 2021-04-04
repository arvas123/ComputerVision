from morphing import *
from matplotlib import pyplot as plt

img = cv2.imread("SampleImages/CardsandSIgns/Exit1.jpg")
img = cv2.resize(img, (800, 500))
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width, depth = img.shape

Mask = np.zeros((height, width, 1), np.uint8)
Mask[305: 430, 248:626] = 255
maskedImg = cv2.bitwise_and(img, img, mask=Mask)

graymask = cv2.cvtColor(maskedImg, cv2.COLOR_BGR2GRAY)
res, threshmask = cv2.threshold(graymask, 180, 255, cv2.THRESH_BINARY)
maskedImg1 = cv2.bitwise_and(graymask, graymask, mask=threshmask)
cv2.imshow("Threshold Mask", maskedImg1)
# cv2.moveWindow("Threshold Mask", 800, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()
