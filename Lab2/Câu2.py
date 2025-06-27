from PIL import Image
import numpy as np

def apply_gradient(image, start_color, end_color):
    """Đổi ảnh thành ảnh dạng gradient từ start_color đến end_color"""
    img = image.convert("L")  # Chuyển sang ảnh xám
    img_np = np.array(img).astype(np.float32) / 255.0

    # Nội suy tuyến tính giữa 2 màu
    gradient = np.zeros((img_np.shape[0], img_np.shape[1], 3), dtype=np.uint8)
    for i in range(3):
        gradient[..., i] = (start_color[i] + (end_color[i] - start_color[i]) * img_np).astype(np.uint8)

    return Image.fromarray(gradient)

# Load ảnh đu đủ và dưa hấu
papaya = Image.open("papaya.jpg").resize((300, 300))
watermelon = Image.open("watermelon.jpg").resize((300, 300))

# Đổi màu:
# Đu đủ: Đỏ -> Xanh lá (RGB: (255,0,0) -> (0,255,0))
papaya_gradient = apply_gradient(papaya, (255, 0, 0), (0, 255, 0))

# Dưa hấu: Vàng -> Tím (RGB: (255,255,0) -> (128,0,128))
watermelon_gradient = apply_gradient(watermelon, (255, 255, 0), (128, 0, 128))

# Tạo nền trong suốt (alpha = 0)
background = Image.new("RGBA", (700, 400), (0, 0, 0, 0))

# Thêm alpha cho 2 ảnh đã đổi màu
papaya_rgba = papaya_gradient.convert("RGBA")
watermelon_rgba = watermelon_gradient.convert("RGBA")

# Ghép ảnh lên nền trong suốt
background.paste(papaya_rgba, (50, 50), papaya_rgba)
background.paste(watermelon_rgba, (400, 50), watermelon_rgba)

# Lưu kết quả
background.save("fruit_composite.png")
print("Đã lưu ảnh kết quả vào fruit_composite.png")
