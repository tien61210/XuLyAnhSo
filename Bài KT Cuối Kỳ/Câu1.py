import cv2
import numpy as np

img = cv2.imread("hoa.jpg")
if img is None:
    exit()

# Median filter
median = cv2.medianBlur(img, 5)
cv2.imwrite("hoa_median.jpg", median)

# Sobel filter
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sx, sy)
sobel = np.uint8(np.clip(sobel, 0, 255))
cv2.imwrite("hoa_sobel.jpg", sobel)

# Hoán đổi kênh màu
swapped = img[:, :, [1, 2, 0]]
cv2.imwrite("hoa_swapped.jpg", swapped)

# Chuyển LAB và tách kênh
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(lab)
cv2.imwrite("hoa_L.jpg", l)
cv2.imwrite("hoa_A.jpg", a)
cv2.imwrite("hoa_B.jpg", b)