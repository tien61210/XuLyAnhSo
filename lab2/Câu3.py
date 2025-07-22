import cv2
import numpy as np
import os
import random

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

def run_menu3():
    methods = [image_inverse, gamma_correction, log_transform, histogram_equalization, contrast_stretching]
    folder = 'exercise'
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        channels = list(cv2.split(img))  # <-- CHUYỂN TUPLE THÀNH LIST
        
        for i in range(3):
            func = random.choice(methods)
            channels[i] = func(channels[i])
        
        merged = cv2.merge(channels)
        cv2.imshow('Result', merged)
        cv2.imwrite(f'{folder}/output_randomRGB_{filename}', merged)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

run_menu3()