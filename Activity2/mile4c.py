from morphing import *
from blurring import *
import os
from matplotlib import pyplot as plt

l = os.listdir('SampleImages/PuzzlesAndGames')
for i in l:
	# print(i)
	img = cv2.imread(f'SampleImages/PuzzlesAndGames/{i}')
	# h,w,d = img.shape
	# img = cv2.resize(img, (w//2,h//2))
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	blurred = gauss(gray, 5, 5)
	thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
	cannyImg = cv2.Canny(gray, 50, 200)
	# cv2.imshow("Canny", cannyImg)
	# cv2.waitKey(0)
	contrs, hier = cv2.findContours(cannyImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contrs:
		area = cv2.contourArea(cnt)
		if area > 60:
			approx = cv2.approxPolyDP(cnt,
									  0.009 * cv2.arcLength(cnt, True), True)

			# Checking if the no. of sides of the selected region is 7.
			if len(approx)==4:
				cv2.drawContours(img, [approx], 0, (0, 0, 255), 3)
	cv2.imshow("Contours", img)
	cv2.waitKey(0)

	cv2.destroyAllWindows()
