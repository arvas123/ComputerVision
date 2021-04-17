'''
Maximum overall accuracy for neighbours = 5 Max accuracy = 91.76
Max Accuracy for digit: 0 is with neighbours = 3 Max accuracy = 98.8
Max Accuracy for digit: 1 is with neighbours = 3 Max accuracy = 99.2
Max Accuracy for digit: 2 is with neighbours = 5 Max accuracy = 86.4
Max Accuracy for digit: 3 is with neighbours = 7 Max accuracy = 93.2
Max Accuracy for digit: 4 is with neighbours = 7 Max accuracy = 87.6
Max Accuracy for digit: 5 is with neighbours = 3 Max accuracy = 90.8
Max Accuracy for digit: 6 is with neighbours = 5 Max accuracy = 98.4
Max Accuracy for digit: 7 is with neighbours = 3 Max accuracy = 93.2
Max Accuracy for digit: 8 is with neighbours = 3 Max accuracy = 84.8
Max Accuracy for digit: 9 is with neighbours = 11 Max accuracy = 93.2

'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('digits.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cells = np.array([np.hsplit(row, 100) for row in np.vsplit(gray_img, 50)])

trainCols = 50
train = cells[:, :trainCols]
test = cells[:, trainCols:100]
trainPerDigit = 500 / (100 / trainCols)
testPerDigit = 500 / (100 / (100 - trainCols))
og_train = np.copy(train)
og_test = np.copy(test)
print(og_test.shape)
# img = cv2.resize(train[0][0],(200,200))
# cv2.imshow("pic", img)
#
# cv2.moveWindow("pic", 100,100)
# cv2.waitKey(0)
train = train.reshape(-1, 400).astype(np.float32)
test = test.reshape(-1, 400).astype(np.float32)

digitCats = np.arange(10)
train_labels = np.repeat(digitCats, trainPerDigit)[:, np.newaxis]
test_labels = np.repeat(digitCats, testPerDigit)[:, np.newaxis]
# print(train[0], train_labels)
knn = cv2.ml.KNearest_create()
knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, 5)
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * 100.0 / result.size
# num = 0
for i in range(10):
	cor = 0
	cnt = 0
	num=0
	for idx, j in enumerate(test_labels):
		num += 1
		if j == i:
			if j == result[idx]:
				cor += 1
			else:
				row = num//50
				col = num%50

				img = cv2.resize(og_test[row][col],(200,200))
				cv2.imshow("badpic", img)

				cv2.waitKey(0)
			cnt += 1
	acc = cor / cnt * 100
