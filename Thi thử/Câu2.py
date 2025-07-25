import cv2
import numpy as np
import random

imgs = [cv2.imread(f"image{i}.jpg", 0) for i in range(1, 4)]

def inverse(img):
    return 255 - img

def gamma(img, g):
    table = np.array([(i / 255) ** (1/g) * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(img, table)

def log(img, c):
    img_f = img.astype(np.float32)
    result = c * np.log1p(img_f)
    return np.uint8(np.clip(result / result.max() * 255, 0, 255))

def he(img):
    return cv2.equalizeHist(img)

def stretch(img, r1, r2):
    return cv2.normalize(img, None, r1, r2, cv2.NORM_MINMAX)

def clahe(img):
    return cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)).apply(img)

print("Nhập phím: I, G, L, H, C, A (hoặc Q để thoát)")

while True:
    key = input(">>> ").lower()
    if key == 'q':
        break
    for i, img in enumerate(imgs):
        if key == 'i':
            out = inverse(img)
            name = f"output_inverse_{i+1}.jpg"
        elif key == 'g':
            g = random.uniform(0.5, 2.0)
            out = gamma(img, g)
            name = f"output_gamma_{i+1}.jpg"
        elif key == 'l':
            c = random.uniform(1.0, 5.0)
            out = log(img, c)
            name = f"output_log_{i+1}.jpg"
        elif key == 'h':
            out = he(img)
            name = f"output_histogram_{i+1}.jpg"
        elif key == 'c':
            r1 = random.randint(0, 100)
            r2 = random.randint(150, 255)
            out = stretch(img, r1, r2)
            name = f"output_contrast_{i+1}.jpg"
        elif key == 'a':
            out = clahe(img)
            name = f"output_adaptive_{i+1}.jpg"
        else:
            continue
        cv2.imwrite(name, out)