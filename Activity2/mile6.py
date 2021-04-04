import cv2
img1 = cv2.imread("bookpic.jpeg")
# img2 = cv2.imread("SampleImages/Coins/dollarCoin.jpg")
orb = cv2.ORB_create()
bfMatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
kp1, des1 = orb.detectAndCompute(img1, None)
vid = cv2.VideoCapture(0)
while True:
	ret, img2 = vid.read()
	img2 = img2[:,::-1,:]
	kp2, des2 = orb.detectAndCompute(img2, None)
	# Find all stable matches
	matches = bfMatcher.match(des1, des2)
	# Sort matches by distance (best matches come first in the list)
	matches.sort(key = lambda x: x.distance)
	# Find index where matches start to be over threshold
	m=0
	for i in range(len(matches)):

		if matches[i].distance > 10.0:
			break
		m+=1

	# Draw good-quality matches up to the threshold index
	img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:m], None)
	cv2.imshow("Matches", img3)
	if cv2.waitKey(10) & 0xFF==ord('c'): break
cv2.destroyAllWindows()
