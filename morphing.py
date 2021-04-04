import cv2
import numpy as np


def display(img, operation, structElem, size, iters):
	# print(operation)
	cv2.putText(img, 'operation: ' + operation, (10, 20),
				cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))
	cv2.putText(img, 'structure: ' + structElem, (10, 40),
				cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))
	cv2.putText(img, 'ksize: %d  iters: %d' % (size, iters), (10, 60),
				cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255))
	cv2.imshow('morphology', img)


def get_ElementName(num):
	names = ['ellipse', 'rect', 'cross']
	num %= 3
	return names[num]


def whichStructElem(structMode):
	structElems = {'ellipse': cv2.MORPH_ELLIPSE,
				   'rect': cv2.MORPH_RECT,
				   'cross': cv2.MORPH_CROSS}
	return structElems[structMode]


def whichOper(op):
	operations = {'erode': cv2.MORPH_ERODE,
				  'dilate': cv2.MORPH_DILATE,
				  'open': cv2.MORPH_OPEN,
				  'close': cv2.MORPH_CLOSE,
				  'blackhat': cv2.MORPH_BLACKHAT,
				  'tophat': cv2.MORPH_TOPHAT,
				  'gradient': cv2.MORPH_GRADIENT}
	return operations[op]


def dilate(img, size=0, structMode=0, iters=1):
	if size > 0:
		oper = whichOper('dilate')
		opername = 'dilate'
	else:
		oper = whichOper('erode')
		opername = 'erode'
	size = abs(size)
	size += (size + 1) % 2
	structName = get_ElementName(structMode)
	structElem = whichStructElem(structName)
	st = cv2.getStructuringElement(structElem, (size, size))
	res = cv2.morphologyEx(img, oper, st, iterations=iters)
	return res
	# display(res, opername, structName, size, iters)


def Open(img, size=0, structMode=0, iters=1):
	if size > 0:
		oper = whichOper('open')
	else:
		oper = whichOper('close')
	size = abs(size)
	size += (size + 1) % 2
	structName = get_ElementName(structMode)
	structElem = whichStructElem(structName)
	st = cv2.getStructuringElement(structElem, (size, size))
	res = cv2.morphologyEx(img, oper, st, iterations=iters)
	return res
	# display(res, oper, structName, size, iters)


def Hat(img, size=0, structMode=0, iters=1):
	if size > 0:
		oper = whichOper('tophat')
	else:
		oper = whichOper('blackhat')
	size = abs(size)
	size += (size + 1) % 2
	structName = get_ElementName(structMode)
	structElem = whichStructElem(structName)
	st = cv2.getStructuringElement(structElem, (size, size))
	res = cv2.morphologyEx(img, oper, st, iterations=iters)
	return res
	# display(res, oper, structName, size, iters)


def gradient(img, size=0, structMode=0, iters=1):
	oper = whichOper('gradient')
	size = abs(size)
	size += (size + 1) % 2
	structName = get_ElementName(structMode)
	structElem = whichStructElem(structName)
	st = cv2.getStructuringElement(structElem, (size, size))
	res = cv2.morphologyEx(img, oper, st, iterations=iters)
	return res
	# display(res, oper, structName, size, iters)


