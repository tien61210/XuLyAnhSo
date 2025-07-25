import cv2
import numpy as np
import random

# Đọc ảnh gốc
img = cv2.imread("a.jpg")

# 1.1 Mean filter
mean_filtered = cv2.blur(img, (5, 5))
cv2.imwrite("a_mean.jpg", mean_filtered)

# 1.2 Biên ảnh (sử dụng Sobel)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
edge = cv2.magnitude(sobelx, sobely)
edge = np.uint8(np.clip(edge, 0, 255))
cv2.imwrite("a_edge.jpg", edge)

# 1.3 Đổi màu RGB ngẫu nhiên
channels = list(cv2.split(img))
random.shuffle(channels)
random_color = cv2.merge(channels)
cv2.imwrite("a_random_color.jpg", random_color)

# 1.4 Chuyển HSV và tách kênh
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
cv2.imwrite("a_hue.jpg", h)
cv2.imwrite("a_saturation.jpg", s)
cv2.imwrite("a_value.jpg", v)