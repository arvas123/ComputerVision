import cv2
from matplotlib import pyplot as plt
import os

curdir = os.getcwd() + '\\SampleImages'
dirs = (next(os.walk(os.getcwd() + '\\SampleImages')))
fnames = dirs[2]
for i in range(len(fnames)):
	fnames[i] = curdir + '\\' + fnames[i]
fnames = fnames[1:]
for fname in fnames:
	# w/ matplotlib
	pic = cv2.imread(fname)
	pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
	plt.imshow(pic)
	plt.draw()
	plt.waitforbuttonpress(0)
	plt.close()
	# w/cv2
	'''
	pic = cv2.imread(fname)
	cv2.imshow("current image", pic)
	cv2.waitKey(0)
	'''

cv2.destroyAllWindows()
