#Cau 3
import imageio.v2 as iio
import numpy as np
import colorsys

# Load the image
img_rgb = iio.imread('bird.png')
img_rgb = img_rgb.astype(np.float32) / 255.0  # Normalize to 0-1 range

# Vectorize the rgb_to_hsv function to apply it to the entire image
rgb_to_hsv_vec = np.vectorize(colorsys.rgb_to_hsv)

# Convert RGB to HSV
h, s, v = rgb_to_hsv_vec(img_rgb[:, :, 0], img_rgb[:, :, 1], img_rgb[:, :, 2])

# Create HSV images
h_img = np.zeros_like(img_rgb)
h_img[:, :, 0] = h
h_img[:, :, 1] = h
h_img[:, :, 2] = h
iio.imwrite('bird_h.png', h_img)

s_img = np.zeros_like(img_rgb)
s_img[:, :, 0] = s
s_img[:, :, 1] = s
s_img[:, :, 2] = s
iio.imwrite('bird_s.png', s_img)

v_img = np.zeros_like(img_rgb)
v_img[:, :, 0] = v
v_img[:, :, 1] = v
v_img[:, :, 2] = v
iio.imwrite('bird_v.png', v_img)