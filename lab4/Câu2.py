import cv2
import numpy as np

def rotate_image(img, angle):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)

    # Tính ma trận xoay
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, matrix, (w, h), borderValue=255)
    return rotated

def select_ho_xuan_huong(image_path):
    # Đọc ảnh grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Không tìm thấy ảnh. Kiểm tra lại đường dẫn.")
        return

    # Cắt vùng 100x100 từ vị trí (100, 100)
    x, y, size = 100, 100, 100
    roi = img[y:y+size, x:x+size]

    # Xoay vùng chọn 45 độ
    rotated_roi = rotate_image(roi, 45)

    # Áp dụng Adaptive Thresholding
    mask = cv2.adaptiveThreshold(rotated_roi, 255,
                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 11, 60)

    # Tạo ảnh màu để hiển thị rõ
    output = cv2.cvtColor(rotated_roi, cv2.COLOR_GRAY2BGR)
    output[mask == 0] = [0, 0, 0]

    # Lưu và hiển thị kết quả
    cv2.imwrite("ho_xuan_huong.jpg", output)
    cv2.imshow("Ho Xuan Huong", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Gọi hàm
if __name__ == "__main__":
    select_ho_xuan_huong("exercise/DaLat.jpg")
