import cv2
import numpy as np
import random

# 1. Tăng kích thước ảnh colorful-ripe-tropical-fruits.jpg
img1 = cv2.imread("colorful-ripe-tropical-fruits.jpg")
resized_img1 = cv2.copyMakeBorder(img1, 30, 30, 30, 30, cv2.BORDER_REPLICATE)
cv2.imwrite("fruit_resized.jpg", resized_img1)

# 2. Xoay 45 độ + lật ngang ảnh quang-ninh.jpg
img2 = cv2.imread("quang-ninh.jpg")
(h2, w2) = img2.shape[:2]
center = (w2 // 2, h2 // 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img2, M, (w2, h2))
flipped = cv2.flip(rotated, 1)
cv2.imwrite("quangninh_rotated_flipped.jpg", flipped)

# 3. Tăng kích thước pagoda.jpg 5 lần + làm mịn Gaussian
img3 = cv2.imread("pagoda.jpg")
img3_large = cv2.resize(img3, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
blurred = cv2.GaussianBlur(img3_large, (7, 7), 0)
cv2.imwrite("pagoda_enlarged_blurred.jpg", blurred)

# 4. Biến đổi độ sáng và tương phản cho ảnh pagoda.jpg
img4 = cv2.imread("pagoda.jpg")
alpha = round(random.uniform(0.5, 2.0), 2)
beta = random.randint(-50, 50)
adjusted = cv2.convertScaleAbs(img4, alpha=alpha, beta=beta)
cv2.imwrite("pagoda_brightness_contrast.jpg", adjusted)