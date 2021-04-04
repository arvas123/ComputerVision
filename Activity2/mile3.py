from morphing import *
from blurring import *
import os

l = os.listdir('SampleImages/Coins')
for i in l:
	origIm = cv2.imread(f'SampleImages/Coins/{i}')
	origIm = cv2.resize(origIm, (800, 800))
	gl = np.array([70, 70, 70])
	gh = np.array([200, 200, 200])
	mask = cv2.inRange(origIm, gl, gh)
	res = cv2.bitwise_and(origIm, origIm, mask=mask)
	res = dilate(res, 5)
	imgray = cv2.GaussianBlur(cv2.cvtColor(res, cv2.COLOR_BGR2GRAY), (5, 5), -1)
	cv2.imshow("res", imgray)
	cv2.waitKey(0)
	ret, thresh = cv2.threshold(imgray, 120, 255, 0)
	contrs, hier = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(origIm, contrs, -1, (0, 255, 0), 3)
	cv2.imshow('Contours', origIm)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
