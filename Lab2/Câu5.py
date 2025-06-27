from PIL import Image, ImageFilter
from scipy.ndimage import rotate, gaussian_filter, map_coordinates
import numpy as np

def load_image():
    print("Chọn ảnh:")
    print("1. img1.jpg")
    print("2. img2.jpg")
    print("3. img3.jpg")
    choice = input("Nhập số (1-3): ")
    path = f"img{choice}.jpg"
    return Image.open(path).convert("RGB")

def translate(img):
    dx = int(input("Nhập số pixel dịch theo trục X: "))
    dy = int(input("Nhập số pixel dịch theo trục Y: "))
    arr = np.array(img)
    result = np.zeros_like(arr)
    h, w = arr.shape[:2]
    result[dy:h, dx:w] = arr[0:h-dy, 0:w-dx]
    return Image.fromarray(result)

def rotate_image(img):
    angle = float(input("Nhập góc xoay (độ): "))
    reshape = input("Cho reshape? (y/n): ").lower() == 'y'
    arr = np.array(img)
    rotated = rotate(arr, angle=angle, reshape=reshape, mode='reflect')
    return Image.fromarray(rotated.astype(np.uint8))

def zoom_image(img):
    factor = float(input("Nhập hệ số zoom (ví dụ: 2 để phóng to, 0.5 để thu nhỏ): "))
    new_size = (int(img.width * factor), int(img.height * factor))
    return img.resize(new_size, Image.LANCZOS)

def gaussian_blur(img):
    sigma = float(input("Nhập giá trị sigma cho Gaussian blur: "))
    arr = np.array(img)
    blurred = gaussian_filter(arr, sigma=(sigma, sigma, 0))
    return Image.fromarray(blurred.astype(np.uint8))

def wave_effect(img):
    amplitude = float(input("Nhập biên độ sóng: "))
    arr = np.array(img)
    h, w = arr.shape[:2]
    x, y = np.meshgrid(np.arange(w), np.arange(h))
    x_wave = x + amplitude * np.sin(2 * np.pi * y / 100)
    coords = np.array([y, x_wave])
    warped = np.zeros_like(arr)
    for i in range(3):
        warped[..., i] = map_coordinates(arr[..., i], coords, order=1, mode='reflect')
    return Image.fromarray(warped)

def main():
    img = load_image()
    print("\nChọn phép biến đổi:")
    print("1. Tịnh tiến")
    print("2. Xoay")
    print("3. Phóng to / Thu nhỏ")
    print("4. Làm mờ Gaussian")
    print("5. Biến đổi sóng")

    choice = input("Nhập số (1-5): ")

    if choice == '1':
        result = translate(img)
    elif choice == '2':
        result = rotate_image(img)
    elif choice == '3':
        result = zoom_image(img)
    elif choice == '4':
        result = gaussian_blur(img)
    elif choice == '5':
        result = wave_effect(img)
    else:
        print("Lựa chọn không hợp lệ.")
        return

    result.save("result.jpg")
    print("✅ Ảnh đã được lưu thành result.jpg")

if __name__ == "__main__":
    main()
