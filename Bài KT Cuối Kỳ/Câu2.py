import cv2
import numpy as np
import random

# Danh sách 3 ảnh
images = ["img1.jpg", "img2.jpg", "img3.jpg"]

# Đọc tất cả ảnh
imgs = []
for path in images:
    img = cv2.imread(path)
    if img is None:
        continue
    imgs.append((path, img))

# Menu phím
print("B: Gaussian Blur")
print("M: Median Blur")
print("F: Bilateral Filter")
print("E: Canny Edge Detection")
print("R: Erosion")
print("D: Dilation")

key = input("Choose method (B/M/F/E/R/D): ").upper()

for fname, img in imgs:
    result = None

    if key == "B":
        k = random.choice([3,5,7,9,11])
        result = cv2.GaussianBlur(img, (k, k), 0)
        method = "blur"
        
    elif key == "M":
        k = random.choice([3,5,7,9,11])
        result = cv2.medianBlur(img, k)
        method = "median"

    elif key == "F":
        d = random.randint(5,15)
        sc = random.randint(50,150)
        ss = random.randint(50,150)
        result = cv2.bilateralFilter(img, d, sc, ss)
        method = "bilateral"

    elif key == "E":
        t1 = random.randint(50,100)
        t2 = random.randint(100,150)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        result = cv2.Canny(gray, t1, t2)
        method = "canny"

    elif key == "R":
        k = random.randint(2,5)
        kernel = np.ones((k,k), np.uint8)
        result = cv2.erode(img, kernel)
        method = "erosion"

    elif key == "D":
        k = random.randint(2,5)
        kernel = np.ones((k,k), np.uint8)
        result = cv2.dilate(img, kernel)
        method = "dilation"

    if result is not None:
        outname = f"result_{method}_{fname}"
        cv2.imwrite(outname, result)