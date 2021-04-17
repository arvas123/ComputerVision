import cv2
import numpy as np
import matplotlib.pyplot as plt

# This generates 25 pairs of random numbers. Each (x, y) pair is an integer
# between 0 and 99. Once created, this is converted to an array of
# 32-bit floats because KNearest expects data in that form
trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
# For each data point, randomly assign it to category 0 or category 1
# Convert to 32-bit floats for the same reason
sm = np.sum(trainData, dtype=np.float32, axis=1)
responses  = np.logical_and(sm>=75, sm<=125).astype(np.float32)
red = trainData[responses == 0]  # All data assigned category 0
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')
# Plot category 1 as blue squares
blue = trainData[responses == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')

newPoint = np.random.randint(0, 100, (10, 2)).astype(np.float32)
plt.scatter(newPoint[:, 0], newPoint[:, 1], 80, 'g', 'o')
plt.show()

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
# Report category of new point (based on k=3)
ret, result, neighbors, dist = knn.findNearest(newPoint, 3)
print("result:", result)
print("neighbors:", neighbors)
print("distances:", dist)
