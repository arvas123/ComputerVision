import cv2
import numpy as np
import matplotlib.pyplot as plt

faceCascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt0.xml")
eyeCascade = cv2.CascadeClassifier("haarcascades/haarcascade_eye1.xml")
vid = cv2.VideoCapture(0)
prevrect = False
while True:
	ret, frame = vid.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
	gray = cv2.equalizeHist(gray)
	# break
	face_rects = faceCascade.detectMultiScale(gray, 1.3, 5)
	done=False
	for (x, y, w, h) in face_rects:
		# print(x, y, w, h)
		gray_roi = gray[y:y + h, x:x + w]
		eye_rects = eyeCascade.detectMultiScale(gray_roi, minNeighbors=10)
		for (ax, ay, aw, ah) in eye_rects:
			if aw*ah<=2000:
				continue
			cv2.rectangle(frame, (x + ax, y + ay), (x + ax + aw, y + ay + ah), (0, 255, 0), 3)
			prevrect=[(x + ax, y + ay), (x + ax + aw, y + ay + ah)]
			done=True

	if not done and prevrect:
		cv2.rectangle(frame, prevrect[0],prevrect[1],(0,255,0),3)
	cv2.imshow("FD", frame)
	v = cv2.waitKey(20)
	c = chr(v & 0xFF)
	if c == 'c':
		break
vid.release()
cv2.destroyAllWindows()
