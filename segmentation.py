import cv2
import matplotlib.pyplot as plt
import numpy as np


car = cv2.imread('./imgs/00116571.png')
hsv_car = cv2.cvtColor(car, cv2.COLOR_BGR2HSV)

min_grey = (0, 0, 70)
max_grey = (255, 15, 115)

# plt.imshow(hsv_car)
# plt.show()


mask = cv2.inRange(hsv_car, min_grey, max_grey)
# plt.imshow(mask)
# plt.show()

row = mask[300,:]
# print(y)
# for i in range(len(y)):
#     if y[i] == 255:
#         print(i)
print(np.array([row]))

plt.subplot(121), plt.imshow(np.array([row]).repeat(100, axis=0))
plt.subplot(122), plt.imshow(mask)
plt.show()

output = cv2.connectedComponentsWithStats(row, 4)

num_labels = output[0]
# The second cell is the label matrix
labels = output[1]
# The third cell is the stat matrix
stats = output[2]
# The fourth cell is the centroid matrix
centroids = output[3]

area = stats[:, cv2.CC_STAT_AREA]
print("area", area)
x = stats[:, cv2.CC_STAT_LEFT]
y = stats[:, cv2.CC_STAT_TOP]
w = stats[:, cv2.CC_STAT_WIDTH]
h = stats[:, cv2.CC_STAT_HEIGHT]

print("left", x)
print("top", y)
print(w)
print(h)