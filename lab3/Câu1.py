import numpy as np
from PIL import Image
from scipy.ndimage import map_coordinates
import matplotlib.pyplot as plt

# Bước 1: Đọc ảnh kiwi
image = Image.open("kiwi.jpg")
image = image.convert("RGB")
img_np = np.array(image)

# Bước 2: Tịnh tiến 50 pixel sang phải, 30 pixel xuống dưới
translated = np.zeros_like(img_np)
h, w = img_np.shape[:2]
dx, dy = 50, 30
translated[dy:h, dx:w] = img_np[0:h-dy, 0:w-dx]

# Bước 3: Áp dụng hiệu ứng sóng bằng biến đổi tọa độ
# Tham số sóng có thể điều chỉnh để tạo hiệu ứng khác nhau
x, y = np.meshgrid(np.arange(w), np.arange(h))
x_wave = x + 20 * np.sin(2 * np.pi * y / 100)  # Sóng ngang
y_wave = y + 20 * np.sin(2 * np.pi * x / 100)  # Sóng dọc

# Gộp các tọa độ biến đổi lại
coords = np.array([y_wave, x_wave])

# Duyệt từng kênh màu (RGB) và áp dụng biến đổi
warped = np.zeros_like(img_np)
for i in range(3):
    warped[..., i] = map_coordinates(translated[..., i], coords, order=1, mode='reflect')

# Bước 4: Lưu kết quả
output_img = Image.fromarray(warped)
output_img.save("kiwi_wave.jpg")
print("Đã lưu ảnh kết quả vào kiwi_wave.jpg")
