#Cau 1
import imageio.v2 as iio
import numpy as np

# Load the image
img = iio.imread('bird.png')

# Extract color channels
red_channel = img[:, :, 0]
green_channel = img[:, :, 1]
blue_channel = img[:, :, 2]

# Create blank images for each color channel
red_img = np.zeros_like(img)
red_img[:, :, 0] = red_channel

green_img = np.zeros_like(img)
green_img[:, :, 1] = green_channel

blue_img = np.zeros_like(img)
blue_img[:, :, 2] = blue_channel

# Save the images
iio.imwrite('red_bird.png', red_img)
iio.imwrite('green_bird.png', green_img)
iio.imwrite('blue_bird.png', blue_img)