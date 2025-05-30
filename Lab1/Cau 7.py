#Cau 7
import imageio.v2 as iio
import numpy as np
import scipy.ndimage as ndimage
from skimage import filters
import os

# Directory containing the images
image_dir = 'Exercise/'
output_dir = 'Exercise_EdgeDetected/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Edge detection filters
edge_filters = {
    'sobel': filters.sobel,
    'prewitt': filters.prewitt,
    'canny': lambda img: filters.canny(img, sigma=1)
}

# Process each image in the directory
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        image_path = os.path.join(image_dir, filename)
        img = iio.imread(image_path)

        # Convert to grayscale if necessary
        if len(img.shape) > 2:
            img_gray = np.mean(img, axis=2)  # Simple grayscale conversion
        else:
            img_gray = img.copy()

        # Denoise the image before edge detection
        img_denoised = ndimage.median_filter(img_gray, size=3)

        # Apply each edge detection filter and save the result
        for filter_name, filter_func in edge_filters.items():
            img_edges = filter_func(img_denoised)
            output_filename = f'{filter_name}_{filename}'
            output_path = os.path.join(output_dir, output_filename)
            iio.imwrite(output_path, (img_edges * 255).astype(np.uint8))  # Scale to 0-255

print('Edge detection completed.')