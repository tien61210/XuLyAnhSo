import numpy as np
from PIL import Image
from scipy.ndimage import map_coordinates

# Bước 1: Đọc ảnh và phóng to 5 lần
img = Image.open("pagoda.jpg").convert("RGB")
img = img.resize((img.width * 5, img.height * 5), Image.LANCZOS)
img_np = np.array(img)

# Bước 2: Tạo biến đổi hình học "uốn cong"
h, w = img_np.shape[:2]
x, y = np.meshgrid(np.arange(w), np.arange(h))

# Biến đổi hình học cong (warp cong trục Y theo sin của X)
x_new = x
y_new = y + 40 * np.sin(2 * np.pi * x / 300)  # Điều chỉnh biên độ và tần số sóng

coords = np.array([y_new, x_new])

# Bước 3: Áp dụng biến đổi cho từng kênh
warped = np.zeros_like(img_np)
for i in range(3):
    warped[..., i] = map_coordinates(img_np[..., i], coords, order=1, mode='reflect')

# Bước 4: Lưu kết quả
Image.fromarray(warped).save("pagoda_warped.jpg")
print("Đã lưu ảnh pagoda_warped.jpg thành công!")
