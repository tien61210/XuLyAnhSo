Câu 1.

Mục đích:
Lọc nhiễu, phát hiện biên, xử lý màu.

Code và giải thích:

img = cv2.imread("hoa.jpg")

if img is None: exit()

→ Đọc ảnh, kiểm tra nếu ảnh rỗng thì thoát.

median = cv2.medianBlur(img, 5)

cv2.imwrite("hoa_median.jpg", median)

→ Lọc trung vị 5x5 để giảm nhiễu.

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

sobel = cv2.magnitude(sx, sy)

sobel = np.uint8(np.clip(sobel, 0, 255))

cv2.imwrite("hoa_sobel.jpg", sobel)

→ Chuyển ảnh xám → phát hiện biên bằng Sobel → lưu kết quả.

swapped = img[:, :, [1, 2, 0]]

cv2.imwrite("hoa_swapped.jpg", swapped)

→ Hoán đổi thứ tự kênh màu: G-R-B.

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

l, a, b = cv2.split(lab)

cv2.imwrite("hoa_L.jpg", l)

cv2.imwrite("hoa_A.jpg", a)

cv2.imwrite("hoa_B.jpg", b)

→ Chuyển ảnh sang LAB → tách và lưu từng kênh.

Câu 2.

Mục đích:
Thực hiện một trong các bộ lọc: Gaussian, Median, Bilateral, Canny, Erosion, Dilation – trên danh sách nhiều ảnh.

Code và giải thích:

images = ["img1.jpg", "img2.jpg", "img3.jpg"]

→ Danh sách tên ảnh cần xử lý.

for path in images:

    img = cv2.imread(path)
    
    ...
→ Đọc từng ảnh, lưu vào danh sách imgs.

key = input(...)  # Người dùng chọn phương pháp

→ Nhập lựa chọn từ bàn phím: B, M, F, E, R, D.

Các phương pháp xử lý:

"B": Gaussian Blur với kernel ngẫu nhiên (3–11) → làm mờ mượt.

"M": Median Blur → lọc nhiễu muối tiêu.

"F": Bilateral Filter → làm mờ giữ biên.

"E": Canny Edge Detection → phát hiện biên.

"R": Erosion → co vùng trắng, xóa nhiễu nhỏ.

"D": Dilation → giãn vùng trắng, nối vật thể.

cv2.imwrite(...)  # Lưu kết quả theo tên file mới

→ Lưu ảnh đầu ra theo tên result_<method>_<filename>.

Câu 3.

Mục đích:
Thực hiện 3 thao tác khác nhau trên 3 ảnh: pad viền, xoay+lật, phóng to+blur+chỉnh sáng.

Code và giải thích:

cv2.copyMakeBorder(..., 35, 35, 35, 35, ...)

→ Thêm viền đen 35px mỗi cạnh cho ảnh img1.jpg.

cv2.getRotationMatrix2D(...) → xoay

cv2.flip(..., 1) → lật ngang

→ Xử lý img2.jpg bằng cách xoay 135 độ quanh tâm ảnh rồi lật ngang.

cv2.resize(..., fx=5, fy=5)

cv2.GaussianBlur(..., (9, 9), 0)

alpha = hệ số tương phản (0.5–2.0), beta = độ sáng (-50 → 50)

→ img3.jpg được phóng to 5 lần, làm mờ Gaussian, rồi chỉnh sáng và tương phản bằng công thức:

adjusted = alpha * ảnh + beta
