from morphing import *

blurdir = 2
vid = cv2.VideoCapture(0)
ret, frame = vid.read()
h, w, d = frame.shape
Min = 3
Max = min(h, w)
size = 3
currStruct = 0
funcNames = ['dilate', 'Open', 'Hat', 'gradient']
currmorph = 0
iters = 1
print('1 to change filter')
print('2 to change struct')
print('w to increase size')
print('s to reduce size')
print('d to increase iters')
print('a to reduce iters')
while True:
	ret, frame = vid.read()
	frame = frame[:, ::-1, :]
	func = funcNames[currmorph]

	locals()[func](frame, size, currStruct, iters)
	# eval(call)
	cv2.namedWindow("morphology")

	ch = cv2.waitKey(10)
	ch = chr(ch & 0xFF)
	if ch == 'c':
		break
	elif ch == '1':
		currmorph += 1
	elif ch == '2':
		currStruct += 1
	elif ch == 'w':
		size += blurdir
	elif ch == 's':
		size -= blurdir
	elif ch == 'd':
		iters += 1
	elif ch == 'a':
		iters -= 1
	iters = max(iters, 0)
	iters = min(iters, 20)
	size = max(size, Min)
	size = min(size, Max)
	currStruct %= 3
	currmorph %= 4
cv2.destroyAllWindows()
