#Cau 4
import imageio.v2 as iio
import numpy as np
import colorsys

# Load the image
img_rgb = iio.imread('bird.png')
img_rgb = img_rgb.astype(np.float32) / 255.0

# Vectorize conversion functions
rgb_to_hsv_vec = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb_vec = np.vectorize(colorsys.hsv_to_rgb)

# Convert RGB to HSV
h, s, v = rgb_to_hsv_vec(img_rgb[:, :, 0], img_rgb[:, :, 1], img_rgb[:, :, 2])

# Modify H and V channels
h_new = h / 3.0
v_new = v * 3.0 / 4.0

# Convert HSV back to RGB
r, g, b = hsv_to_rgb_vec(h_new, s, v_new)
img_new_rgb = np.stack((r, g, b), axis=-1)

img_new_rgb = (np.clip(img_new_rgb, 0, 1) * 255).astype(np.uint8) # Ensure values are within 0-255

# Save the new image
iio.imwrite('bird_modified_hsv.png', img_new_rgb)