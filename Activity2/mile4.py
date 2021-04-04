from morphing import *
from blurring import *
import os
from matplotlib import pyplot as plt
l = os.listdir('SampleImages/Coins')
for i in l:
	# print(i)
	img = cv2.imread(f'SampleImages/Coins/{i}')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blurred = gauss(gray, 5, 5)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
	cannyImg = cv2.Canny(gray, 50, 200)
	cv2.imshow("Canny", cannyImg)
	cv2.waitKey(0)
	contrs, hier = cv2.findContours(cannyImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	for cont in contrs:
		hull = cv2.convexHull(cont)
		cv2.drawContours(img, [hull], -1, (0, 255, 0), 3)
	cv2.imshow("Contours", img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
