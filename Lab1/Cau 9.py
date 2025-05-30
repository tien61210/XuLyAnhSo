#Cau 9
import imageio.v2 as iio
import numpy as np
import scipy.ndimage as ndimage
import colorsys
import random
import os

# Directory containing the images
image_dir = 'Exercise/'
output_dir = 'Exercise_RandomHSV/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def random_hsv(img):
    """Applies a random but non-identical HSV transformation."""

    if len(img.shape) < 3:
        return img  # Skip grayscale images

    hsv_img = np.zeros_like(img, dtype=float)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            r, g, b = img[i, j] / 255.0
            h, s, v = colorsys.rgb_to_hsv(r, g, b)

            # Generate random but distinct shifts
            h_shift = random.uniform(-0.1, 0.1)
            s_scale = random.uniform(0.5, 1.5)
            v_scale = random.uniform(0.5, 1.5)

            hsv_img[i, j] = (h + h_shift) % 1, np.clip(s * s_scale, 0, 1), np.clip(v * v_scale, 0, 1)

    rgb_img = np.zeros_like(img, dtype=np.uint8)
    for i in range(hsv_img.shape[0]):
        for j in range(hsv_img.shape[1]):
            h, s, v = hsv_img[i, j]
            r, g, b = colorsys.hsv_to_rgb(h, s, v)
            rgb_img[i, j] = np.clip(np.array([r, g, b]) * 255, 0, 255).astype(np.uint8)
    return rgb_img

# Process each image
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        image_path = os.path.join(image_dir, filename)
        img = iio.imread(image_path)

        # Denoise
        if len(img.shape) > 2:
            for i in range(img.shape[2]):
                img[:, :, i] = ndimage.median_filter(img[:, :, i], size=3)
        else:
            img = ndimage.median_filter(img, size=3)

        # Apply random HSV transformation
        transformed_img = random_hsv(img.copy())
        output_filename = f'random_hsv_{filename}'
        output_path = os.path.join(output_dir, output_filename)
        iio.imwrite(output_path, transformed_img)

print('Random HSV transformation completed.')