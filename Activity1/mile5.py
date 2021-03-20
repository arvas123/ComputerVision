import cv2
import numpy as np
import os

dir = os.getcwd() + '\\Screenshots'
video = cv2.VideoCapture(0)
num = 0
try:
	fname = (os.listdir(dir))[-1]
	fname = fname[10:]
	num = ''
	i = 0
	while fname[i].isdigit():
		num += fname[i]
		i += 1
	num = int(num)
except IndexError:
	pass
while True:
	ret, img = video.read()
	img = img[:, ::-1, :]
	cv2.imshow("Webcam", img)
	inp = cv2.waitKey(10)
	if inp == ord('c'):
		break
	elif inp == ord('s'):
		fname = dir + '\\screenshot' + str(num) + '.png'
		cv2.imwrite(fname, img)
		print('Saving Screenshot...')
		num += 1
cv2.destroyAllWindows()
video.release()
