#Cau 2
import imageio.v2 as iio
import numpy as np

# Load the image
img = iio.imread('bird.png')

# Swap Red and Green channels
img_swap_rg = img.copy()
img_swap_rg[:, :, 0], img_swap_rg[:, :, 1] = img[:, :, 1].copy(), img[:, :, 0].copy()
iio.imwrite('bird_swap_rg.png', img_swap_rg)

# Swap Green and Blue channels
img_swap_gb = img.copy()
img_swap_gb[:, :, 1], img_swap_gb[:, :, 2] = img[:, :, 2].copy(), img[:, :, 1].copy()
iio.imwrite('bird_swap_gb.png', img_swap_gb)

# Swap Red and Blue channels
img_swap_rb = img.copy()
img_swap_rb[:, :, 0], img_swap_rb[:, :, 2] = img[:, :, 2].copy(), img[:, :, 0].copy()
iio.imwrite('bird_swap_rb.png', img_swap_rb)