from PIL import Image
from scipy.ndimage import rotate
import numpy as np

# Đọc ảnh
mountain = Image.open("mountain.jpg").convert("RGBA").resize((300, 300))
boat = Image.open("boat.jpg").convert("RGBA").resize((300, 300))

# Hàm xoay ảnh giữ nguyên kích thước
def rotate_image(img, angle):
    arr = np.array(img)
    rotated = rotate(arr, angle=angle, reshape=False, mode='nearest')
    return Image.fromarray(rotated.astype(np.uint8))

# Hàm tạo phản chiếu dọc
def vertical_mirror(img):
    return img.transpose(Image.FLIP_TOP_BOTTOM)

# Xử lý ảnh núi
mountain_rotated = rotate_image(mountain, 45)
mountain_mirrored = vertical_mirror(mountain_rotated)

# Xử lý ảnh thuyền
boat_rotated = rotate_image(boat, 45)
boat_mirrored = vertical_mirror(boat_rotated)

# Tạo canvas trắng để ghép ảnh
canvas_width = 700
canvas_height = 350
canvas = Image.new("RGB", (canvas_width, canvas_height), (255, 255, 255))

# Ghép ảnh lên canvas
canvas.paste(mountain_mirrored.convert("RGB"), (50, 25))
canvas.paste(boat_mirrored.convert("RGB"), (400, 25))

# Lưu ảnh kết quả
canvas.save("mountain_boat_mirror.jpg")
print("Đã lưu ảnh thành công: mountain_boat_mirror.jpg")
