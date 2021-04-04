from blurring import *
from morphing import *

img1 = cv2.imread("SampleImages/CardsAndSIgns/Door1.jpg")
img = np.copy(img1)
grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImg = gauss(grayImg, 21, 21)
res, thresh = cv2.threshold(grayImg, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("gray", thresh)
goodFeats = cv2.goodFeaturesToTrack(thresh, 100, 0.1, 5)
for i in goodFeats:
	x, y = i[0, 0], i[0, 1]
	x = x.astype('uint32')
	y = y.astype('uint32')
	cv2.circle(img1, (x, y), 5, (0, 255, 0), 2)
cv2.imshow("good", img1)
# cv2.imshow("Original 1", img)
# # create a FAST object, that can run the FAST algorithm.
fast = cv2.FastFeatureDetector_create()
# detect features
# res, thresh =
keypts = fast.detect(thresh, None)
img2 = cv2.drawKeypoints(img, keypts, None, (255, 0, 0), 4)
cv2.imshow("Keypoints 1", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
