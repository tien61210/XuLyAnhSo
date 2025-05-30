#Cau5
import imageio.v2 as iio
import numpy as np
import scipy.ndimage as ndimage
import os

# Directory containing the images
image_dir = 'Exercise/'
output_dir = 'Exercise_MeanFiltered/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Mean filter size
filter_size = 5
kernel = np.ones((filter_size, filter_size)) / (filter_size * filter_size)

# Process each image in the directory
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        image_path = os.path.join(image_dir, filename)
        img = iio.imread(image_path)

        # Apply mean filter to each color channel separately if it's a color image
        if len(img.shape) > 2:
            filtered_img = np.zeros_like(img)
            for i in range(img.shape[2]):
                filtered_img[:, :, i] = ndimage.convolve(img[:, :, i], kernel)
        else:
            filtered_img = ndimage.convolve(img, kernel)

        # Save the filtered image
        output_path = os.path.join(output_dir, f'mean_{filename}')
        iio.imwrite(output_path, filtered_img.astype(np.uint8))

print("Mean filtering completed.")