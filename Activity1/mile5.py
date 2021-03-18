import cv2
from matplotlib import pyplot as plt
import numpy as np
video=cv2.VideoCapture(0)
for i in range(300):
	ret,img=video.read()
	# img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	# plt.imshow(img)
	# plt.draw()
	# plt.pause(1/100000)
	img2=img[:,::-1,:]
	cv2.imshow("Webcam",img2)
	cv2.waitKey(10)
cv2.destroyAllWindows()
video.release()