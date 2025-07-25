import cv2
import numpy as np
import random

# ==== Ảnh 1: Pad mỗi cạnh 35 pixel ====
img1 = cv2.imread("img1.jpg")
if img1 is not None:
    padded = cv2.copyMakeBorder(img1, 35, 35, 35, 35, cv2.BORDER_CONSTANT, value=(0, 0, 0))
    cv2.imwrite("result_padded_img1.jpg", padded)

# ==== Ảnh 2: Xoay 135 độ và lật ngang ====
img2 = cv2.imread("img2.jpg")
if img2 is not None:
    (h, w) = img2.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 135, 1.0)
    rotated = cv2.warpAffine(img2, M, (w, h))
    flipped = cv2.flip(rotated, 1)  # lật ngang
    cv2.imwrite("result_rotated_flipped_img2.jpg", flipped)

# ==== Ảnh 3: Phóng to 5 lần, Gaussian blur, tăng sáng/tương phản ====
img3 = cv2.imread("img3.jpg")
if img3 is not None:
    resized = cv2.resize(img3, None, fx=5, fy=5, interpolation=cv2.INTER_LINEAR)
    blurred = cv2.GaussianBlur(resized, (9, 9), 0)

    alpha = random.uniform(0.5, 2.0)
    beta = random.randint(-50, 50)

    adjusted = np.clip(alpha * blurred + beta, 0, 255).astype(np.uint8)
    cv2.imwrite("result_processed_img3.jpg", adjusted)