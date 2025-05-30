#Cau 6
import imageio.v2 as iio
import numpy as np
import scipy.ndimage as ndimage
import os

# Directory containing the images
image_dir = 'Exercise/'
output_dir = 'Exercise_Denoised/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Denoising filters
filters = {
    'mean': lambda img: ndimage.convolve(img, np.ones((5, 5)) / 25),
    'median': lambda img: ndimage.median_filter(img, size=5),
    'maximum': lambda img: ndimage.maximum_filter(img, size=5),
    'minimum': lambda img: ndimage.minimum_filter(img, size=5)
}

# Process each image in the directory
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        image_path = os.path.join(image_dir, filename)
        img = iio.imread(image_path)

        # Apply each filter and save the result
        for filter_name, filter_func in filters.items():
            if len(img.shape) > 2:
                filtered_img = np.zeros_like(img)
                for i in range(img.shape[2]):
                    filtered_img[:, :, i] = filter_func(img[:, :, i])
            else:
                filtered_img = filter_func(img)

            output_filename = f'{filter_name}_{filename}'
            output_path = os.path.join(output_dir, output_filename)
            iio.imwrite(output_path, filtered_img.astype(np.uint8))

print('Denoising completed.')
#Filer khử nhiễu tốt nhất là median