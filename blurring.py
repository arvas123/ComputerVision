import cv2
import numpy


def blur_display(img, wid, h, type):
	cv2.putText(img, f"{type} wid = {wid}, Height = {h}", (5, 15),
				cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0))
	cv2.imshow("BlurredImage", img)


def gauss(img, wid, h):
	blur_img = cv2.GaussianBlur(img, (wid, h), 0)
	return blur_img
	# blur_display(blur_img, wid, h, "Gaussian Blur")


def regular(img, wid, h):
	blur_img = cv2.blur(img, (wid, h))
	return blur_img
	# blur_display(blur_img, wid, h, "Regular Blur")


