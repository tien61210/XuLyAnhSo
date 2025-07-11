import cv2
import numpy as np
import os

def select_langbiang(image_path):
    # Đọc ảnh dưới dạng grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("Không tìm thấy ảnh. Kiểm tra lại đường dẫn.")
        return

    # Cắt vùng 100x100 pixel từ vị trí (100, 100)
    x, y, size = 100, 100, 100
    roi = img[y:y+size, x:x+size]

    # Áp dụng Otsu Thresholding
    _, mask = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Tạo ảnh màu từ vùng roi để áp dụng mask
    output = cv2.cvtColor(roi, cv2.COLOR_GRAY2BGR)
    output[mask == 0] = [0, 0, 0]  # Đặt nền là đen

    # Lưu ảnh và hiển thị
    cv2.imwrite("lang_biang.jpg", output)
    cv2.imshow("LangBiang Area", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Gọi hàm chính
if __name__ == "__main__":
    # Đảm bảo file ảnh gốc nằm trong thư mục 'exercise'
    select_langbiang("exercise/DaLat.jpg")
