import cv2
import numpy as np

def coordinate_mapping(img):
    rows, cols = img.shape
    # Tạo lưới tọa độ ban đầu
    map_x, map_y = np.meshgrid(np.arange(cols), np.arange(rows))
    map_x = map_x.astype(np.float32)
    map_y = map_y.astype(np.float32)

    # Áp dụng biến đổi (dịch chuyển nhẹ từng pixel)
    map_x += 5 * np.sin(map_y / 10.0)
    map_y += 5 * np.cos(map_x / 10.0)

    # Mapping
    warped = cv2.remap(img, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return warped

def binary_closing(mask):
    kernel = np.ones((5, 5), np.uint8)
    closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    return closed

def select_quang_truong(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Không tìm thấy ảnh.")
        return

    # Chọn vùng 100x100 từ (100,100)
    x, y, size = 100, 100, 100
    roi = img[y:y+size, x:x+size]

    # Bước 1: Coordinate Mapping
    warped = coordinate_mapping(roi)

    # Bước 2: Nhị phân hóa và đóng (closing)
    _, binary = cv2.threshold(warped, 127, 255, cv2.THRESH_BINARY)
    closed = binary_closing(binary)

    # Bước 3: Tạo ảnh màu để che nền
    output = cv2.cvtColor(warped, cv2.COLOR_GRAY2BGR)
    output[closed == 0] = [0, 0, 0]

    # Lưu và hiển thị
    cv2.imwrite("quan_truong_lam_vien.jpg", output)
    cv2.imshow("Quang Truong Lam Vien", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Gọi hàm
if __name__ == "__main__":
    select_quang_truong("exercise/DaLat.jpg")