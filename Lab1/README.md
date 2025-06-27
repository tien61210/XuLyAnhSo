### <a name="Cau 1"></a> Câu 1: Nạp ảnh và tách kênh màu
**Cách hoạt động:**
Đọc ảnh, tách thành 3 mảng (Red, Green, Blue), lưu mỗi mảng thành ảnh.
**Kết quả:**
Chương trình tạo ra 3 ảnh mới: `red_bird.png` (chỉ có màu Red), `green_bird.png` (chỉ có màu Green), và `blue_bird.png` (chỉ có màu Blue).

### <a name="Cau 2"></a> Câu 2: Viết chương trình nạp một ảnh và hoán đổi giá trị các màu. Lưu các ảnh vào máy.
**Cách hoạt động:**
Đọc ảnh, tạo 3 bản sao, hoán đổi cặp kênh màu (RG, GB, RB) trong mỗi bản sao, lưu ảnh.
**Kết quả:**
Chương trình tạo ra 3 ảnh mới: màu sắc bị thay đổi do hoán đổi kênh.

### <a name="Cau 3"></a> Câu 3: Viết chương trình nạp một ảnh, chuyển thành hệ màu HSV và lưu 3 ảnh với 3 màu khác nhau.
**Cách hoạt động:**
Đọc ảnh, chuyển từ RGB sang HSV, tạo 3 ảnh từ kênh H, S, V.
**Kết quả:**
Chương trình tạo ra 3 ảnh: thể hiện thông tin Hue, Saturation, Value của ảnh gốc.

### <a name="Cau 4"></a> Câu 4: Viết chương trình nạp một ảnh, chuyển sang hệ màu HSV. Lưu ảnh mới với kênh  $H_{new}=1/3$ $H_{old}$. $V_{new}=\frac{3}{4}V_{old}$.
**Cách hoạt động:**
Đọc ảnh, chuyển sang HSV, thay đổi H và V theo công thức, chuyển lại RGB, lưu ảnh.
**Kết quả:**
Chương trình tạo 1 ảnh: màu sắc và độ sáng thay đổi.

### <a name="Cau 5"></a> Câu 5: Viết chương trình sử dụng mean filter cho các hình trong thư mục Exercise
**Cách hoạt động:**
Đọc ảnh từ thư mục, áp dụng mean filter (làm mờ), lưu ảnh đã lọc vào thư mục mới.
**Kết quả:**
Chương trình tạo ảnh mờ hơn ảnh gốc.

### <a name="Cau 6"></a> Câu 6: Viết chương trình sử dụng các filter khử nhiễu đã thực hành cho các hình trong thư mục Exercise. Cho biết filter nào khử nhiễu tốt nhất?
**Cách hoạt động:**
Đọc ảnh từ thư mục, áp dụng các filter (mean, median, max, min), lưu ảnh đã lọc.
**Kết quả:**
Chương trình tạo nhiều ảnh, mỗi ảnh được lọc bằng một filter khác nhau, mức độ khử nhiễu khác nhau.

### <a name="Cau 7"></a> Câu 7: Viết chương trình sử dụng các filter xác định biên của các hình trong thư mục Exercise. Lưu các hình vào máy. (Khử nhiễu trước khi xác định biên)
**Cách hoạt động:**
Đọc ảnh từ thư mục, khử nhiễu, áp dụng các filter dò biên (Sobel, Prewitt, Canny), lưu ảnh.
**Kết quả:**
Chương trình tạo ảnh chỉ hiển thị các cạnh của vật thể.

### <a name="Cau 8"></a> Câu 8: Viết chương trình đổi màu RGB ngẫu nhiên của các hình trong thư mục Exercise. Lưu hình mới vào máy. (Khử nhiễu trước khi đổi màu)
**Cách hoạt động:**
Đọc ảnh từ thư mục, khử nhiễu, nhân ngẫu nhiên ma trận màu, lưu ảnh.
**Kết quả:**
Chương trình tạo ảnh có màu sắc thay đổi ngẫu nhiên.

### <a name="Cau 9"></a> Câu 9: Viết chương trình đổi màu HSV ngẫu nhiên nhưng không trùng của các hình trong thư mục Exercise. Lưu hình mới vào máy. (Khử nhiễu trước khi đổi màu)
**Cách hoạt động:**
Đọc ảnh từ thư mục, khử nhiễu, chuyển sang HSV, thay đổi HSV ngẫu nhiên, chuyển lại RGB, lưu ảnh.
**Kết quả:**
Chương trình tạo ảnh có màu sắc, độ bão hòa, độ sáng thay đổi ngẫu nhiên.
