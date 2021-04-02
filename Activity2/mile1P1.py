from blurring import *

blurdir = 2
vid = cv2.VideoCapture(0)
ret, frame = vid.read()
h, w, d = frame.shape
Min = (3, 3)
Max = min(h, w)
hi, wid = 1, 1
print('1 to change blur mode')
print('w/s to increase/decrease height')
print('d/a to increase/decrease width')
mode = 0
while True:
	ret, frame = vid.read()
	frame = frame[:, ::-1, :]
	if mode == 0:
		gauss(frame, hi, wid)
	else:
		regular(frame, hi, wid)
	ch = cv2.waitKey(10)
	ch = chr(ch & 255)
	if ch == 'c':
		break
	elif ch == 'w':
		hi += blurdir
	elif ch == 's':
		hi += blurdir
	elif ch == 'd':
		wid += blurdir
	elif ch == 'a':
		wid -= blurdir
	elif ch == '1':
		mode += 1
		mode %= 2

cv2.destroyAllWindows()
