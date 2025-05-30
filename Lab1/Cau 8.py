#Cau 8
import imageio.v2 as iio
import numpy as np
import scipy.ndimage as ndimage
import random
import os

# Directory containing the images
image_dir = 'Exercise/'
output_dir = 'Exercise_RandomRGB/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def random_rgb(img):
    """Applies a random RGB transformation to the image."""

    if len(img.shape) < 3:
        return img  # Skip grayscale images

    random_matrix = np.random.rand(3, 3)
    transformed_img = np.zeros_like(img, dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pixel = img[i, j, :].astype(float)
            new_pixel = np.dot(random_matrix, pixel)
            transformed_img[i, j, :] = np.clip(new_pixel, 0, 255).astype(np.uint8)
    return transformed_img

# Process each image in the directory
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        image_path = os.path.join(image_dir, filename)
        img = iio.imread(image_path)

        # Denoise the image
        if len(img.shape) > 2:
            for i in range(img.shape[2]):
                img[:, :, i] = ndimage.median_filter(img[:, :, i], size=3)
        else:
            img = ndimage.median_filter(img, size=3)

        # Apply random RGB transformation and save
        transformed_img = random_rgb(img.copy())  # Apply to a copy
        output_filename = f'random_rgb_{filename}'
        output_path = os.path.join(output_dir, output_filename)
        iio.imwrite(output_path, transformed_img)

print('Random RGB transformation completed.')