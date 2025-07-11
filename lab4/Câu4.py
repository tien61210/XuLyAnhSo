import cv2
import numpy as np

def load_roi(image_path, x=100, y=100, size=100):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Không tìm thấy ảnh.")
        return None
    roi = img[y:y+size, x:x+size]
    return roi

# --- GEOMETRIC TRANSFORMATIONS ---

def coordinate_mapping(img):
    rows, cols = img.shape
    map_x, map_y = np.meshgrid(np.arange(cols), np.arange(rows))
    map_x = map_x.astype(np.float32) + 5 * np.sin(map_y / 10.0)
    map_y = map_y.astype(np.float32) + 5 * np.cos(map_x / 10.0)
    return cv2.remap(img, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

def rotate_image(img, angle=45):
    h, w = img.shape[:2]
    matrix = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
    return cv2.warpAffine(img, matrix, (w, h), borderValue=255)

def scale_image(img, fx=1.5, fy=1.5):
    return cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)

def shift_image(img, dx=30, dy=30):
    h, w = img.shape
    matrix = np.float32([[1, 0, dx], [0, 1, dy]])
    return cv2.warpAffine(img, matrix, (w, h), borderValue=255)

# --- SEGMENTATION ---

def adaptive_thresholding(img):
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 60)

def binary_dilation(img):
    _, mask = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    return cv2.dilate(mask, kernel)

def binary_erosion(img):
    _, mask = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    return cv2.erode(mask, kernel)

def otsu_thresholding(img):
    _, mask = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return mask

# --- MENU ---

def apply_function(code, roi):
    result = None

    if code == "1a":
        result = coordinate_mapping(roi)
    elif code == "1b":
        result = rotate_image(roi)
    elif code == "1c":
        result = scale_image(roi)
    elif code == "1d":
        result = shift_image(roi)
    elif code == "2a":
        result = adaptive_thresholding(roi)
    elif code == "2b":
        result = binary_dilation(roi)
    elif code == "2c":
        result = binary_erosion(roi)
    elif code == "2d":
        result = otsu_thresholding(roi)
    else:
        print(f"Mã không hợp lệ: {code}")
        return

    # Nếu ảnh kết quả là nhị phân → tạo ảnh màu để hiển thị rõ
    if result is not None:
        if len(result.shape) == 2:
            output = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)
            output[result == 0] = [0, 0, 0]
        else:
            output = result

        # Tạo tên file lưu dựa theo code
        filename = f"output_{code}.jpg"
        cv2.imwrite(filename, output)
        cv2.imshow(f"Result {code}", output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def menu():
    print("\n--- MENU ---")
    print("1. geometric_transformation")
    print("    a. coordinate_mapping (1a)")
    print("    b. rotate (1b)")
    print("    c. scale (1c)")
    print("    d. shift (1d)")
    print("2. segment")
    print("    a. adaptive_thresholding (2a)")
    print("    b. binary_dilation (2b)")
    print("    c. binary_erosion (2c)")
    print("    d. otsu (2d)")
    
    choice = input("Nhập lựa chọn (VD: 1a, 2d hoặc 1a+2d): ")

    roi = load_roi("exercise/DaLat.jpg")
    if roi is None:
        return

    if '+' in choice:
        codes = choice.split('+')
        for code in codes:
            apply_function(code.strip(), roi)
    else:
        apply_function(choice.strip(), roi)

# --- Chạy chương trình ---
if __name__ == "__main__":
    menu()
