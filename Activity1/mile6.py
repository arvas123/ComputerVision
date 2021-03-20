import cv2
import numpy as np

im1 = cv2.imread("SampleImages/canyonlands.jpg")
im2 = cv2.imread("SampleImages/mightyMidway.jpg")
h, w, d = im1.shape
h1, w1, d1 = im2.shape
minh = min(h, h1)
minw = min(w, w1)
new_im1 = im1[0:minh, 0:minw]
new_im2 = im2[0:minh, 0:minw]
# blending 2 images

blended = cv2.addWeighted(new_im1, 0.5, new_im2, 0.5, 0)
cv2.imshow("blended", blended)
cv2.waitKey(10)
# cv2.destroyAllWindows()
# blending video
video = cv2.VideoCapture(0)
ret, vid = video.read()
h2, w2, d2 = vid.shape
newh = min(h, h2)
neww = min(w, w2)
new_im = im1[0:newh, 0:neww]
while True:
	ret, vid = video.read()
	vid = vid[:, ::-1, :]
	vid = vid[0:newh, 0:neww]
	blended_vid = cv2.addWeighted(vid, 0.5, new_im, 0.5, 0)
	cv2.imshow("blendedvid", blended_vid)
	char = cv2.waitKey(10)
	if char == ord('c'): break
cv2.destroyAllWindows()

# echo effect
frames = []
while True:
	ret, vid = video.read()
	vid = vid[:, ::-1, :]
	if len(frames)<5:
		cv2.imshow("blendedvid", vid)
		frames.append(vid)
		continue
	prev_frame = frames[0]
	blended_vid = cv2.addWeighted(vid, 0.1, prev_frame, 0.9, 0)
	cv2.imshow("blendedvid", blended_vid)
	frames.pop(0)
	frames.append(vid)
	char = cv2.waitKey(10)
	if char == ord('c'): break
cv2.destroyAllWindows()