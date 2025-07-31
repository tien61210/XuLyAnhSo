Câu 1.

Mục đích:
Làm mờ ảnh, phát hiện biên, trộn kênh màu RGB ngẫu nhiên, chuyển sang HSV và tách kênh.

Code và giải thích:

img = cv2.imread("a.jpg")

→ Đọc ảnh từ tệp a.jpg.

mean_filtered = cv2.blur(img, (5, 5))

cv2.imwrite("a_mean.jpg", mean_filtered)

→ Làm mờ ảnh bằng bộ lọc trung bình (mean filter) với kernel 5x5 và lưu ảnh kết quả.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

edge = cv2.magnitude(sobelx, sobely)

edge = np.uint8(np.clip(edge, 0, 255))

cv2.imwrite("a_edge.jpg", edge)

→ Chuyển ảnh sang thang xám, áp dụng Sobel để phát hiện biên theo 2 hướng, tính biên độ tổng và lưu kết quả.

channels = list(cv2.split(img))

random.shuffle(channels)

random_color = cv2.merge(channels)

cv2.imwrite("a_random_color.jpg", random_color)

→ Tách ảnh thành 3 kênh B, G, R → trộn ngẫu nhiên thứ tự → ghép lại và lưu ảnh mới.

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

cv2.imwrite("a_hue.jpg", h)

cv2.imwrite("a_saturation.jpg", s)

cv2.imwrite("a_value.jpg", v)

→ Chuyển ảnh sang không gian HSV → tách 3 kênh Hue, Saturation, Value và lưu từng kênh.

Câu 2.

Mục đích:
Thực hiện các phép biến đổi tăng cường ảnh: âm bản, gamma correction, logarit, cân bằng histogram, giãn mức xám, và CLAHE – trên 3 ảnh đầu vào.

Code và giải thích:

imgs = [cv2.imread(f"image{i}.jpg", 0) for i in range(1, 4)]

→ Đọc 3 ảnh xám: image1.jpg, image2.jpg, image3.jpg.

def inverse(img):

    return 255 - img

→ Trả về ảnh âm bản bằng cách đảo giá trị pixel.

def gamma(img, g):

    table = np.array([(i / 255) ** (1/g) * 255 for i in range(256)]).astype("uint8")
    
    return cv2.LUT(img, table)

→ Thực hiện biến đổi gamma với hệ số ngẫu nhiên g ∈ [0.5, 2.0].

def log(img, c):

    img_f = img.astype(np.float32)
    
    result = c * np.log1p(img_f)
    
    return np.uint8(np.clip(result / result.max() * 255, 0, 255))

→ Biến đổi logarit với hệ số c, giúp tăng chi tiết vùng tối.

def he(img):

    return cv2.equalizeHist(img)

→ Cân bằng histogram (HE) – phân bố lại mức xám để tăng độ tương phản.

def stretch(img, r1, r2):

    return cv2.normalize(img, None, r1, r2, cv2.NORM_MINMAX)

→ Giãn mức xám về khoảng [r1, r2] để tăng độ tương phản.

def clahe(img):

    return cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)).apply(img)

→ CLAHE (Cân bằng histogram cục bộ) – tăng cường tương phản theo từng vùng nhỏ.

while True:

    key = input(">>> ").lower()
    
    ...

→ Người dùng nhập lệnh (I, G, L, H, C, A) để chọn kỹ thuật xử lý tương ứng. Ảnh sau xử lý sẽ được lưu với tên phù hợp (output_...jpg). Lặp lại cho cả 3 ảnh.

Câu 3.

1. Tăng kích thước ảnh bằng viền sao chép

Cách hoạt động: Đọc ảnh colorful-ripe-tropical-fruits.jpg, thêm viền dày 30 pixel ở 4 phía bằng cách sao chép mép ảnh, rồi lưu thành fruit_resized.jpg.

2. Xoay 45 độ và lật ngang ảnh

Cách hoạt động: Đọc ảnh quang-ninh.jpg, xoay 45 độ quanh tâm ảnh, sau đó lật ngang rồi lưu thành quangninh_rotated_flipped.jpg.

3. Phóng to và làm mờ Gaussian ảnh

Cách hoạt động: Đọc ảnh pagoda.jpg, phóng to gấp 5 lần rồi làm mờ bằng Gaussian (7x7), lưu kết quả thành pagoda_enlarged_blurred.jpg.

4. Thay đổi độ sáng và tương phản ảnh

Cách hoạt động: Đọc lại ảnh pagoda.jpg, áp dụng hệ số alpha (độ tương phản) và beta (độ sáng) ngẫu nhiên, sau đó lưu ảnh kết quả thành pagoda_brightness_contrast.jpg.
