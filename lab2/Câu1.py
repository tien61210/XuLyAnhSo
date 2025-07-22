import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

def image_inverse(img):
    return 255 - img

def gamma_correction(img, gamma=2.0):
    look_up_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(img, look_up_table)

def log_transform(img):
    c = 255 / np.log(1 + np.max(img))
    log_image = c * (np.log(img + 1))
    return np.array(log_image, dtype=np.uint8)

def histogram_equalization(img):
    if len(img.shape) == 2:
        return cv2.equalizeHist(img)
    else:
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

def contrast_stretching(img):
    a, b = np.min(img), np.max(img)
    return ((img - a) / (b - a) * 255).astype(np.uint8)

def run_menu1():
    folder = 'exercise'
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        key = input("Chọn I, G, L, H, C: ").upper()
        if key == 'I':
            result = image_inverse(img)
        elif key == 'G':
            result = gamma_correction(img)
        elif key == 'L':
            result = log_transform(img)
        elif key == 'H':
            result = histogram_equalization(img)
        elif key == 'C':
            result = contrast_stretching(img)
        else:
            continue
        
        cv2.imshow("Result", result)
        cv2.imwrite(f'{folder}/output_{key}_{filename}', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

run_menu1()