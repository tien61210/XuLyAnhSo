Câu 1: Tịnh tiến ảnh và áp dụng hiệu ứng sóng

Cách hoạt động:

Đọc ảnh kiwi, tịnh tiến 50 pixel sang phải và 30 pixel xuống dưới.

Áp dụng hiệu ứng sóng ngang & dọc bằng cách biến đổi tọa độ điểm ảnh với hàm sin.

Biến đổi được thực hiện cho từng kênh màu R, G, B bằng map_coordinates.

Kết quả là ảnh bị uốn lượn theo dạng sóng mềm mại.

Ảnh đầu ra được lưu dưới tên kiwi_wave.jpg.


Câu 2: Chuyển ảnh sang màu gradient và ghép ảnh

Cách hoạt động:

Đọc 2 ảnh papaya.jpg và watermelon.jpg, resize về 300×300.

Áp dụng hiệu ứng gradient màu bằng cách nội suy từ màu đầu đến màu cuối dựa trên độ sáng ảnh gốc:

Đu đủ: từ đỏ → xanh lá

Dưa hấu: từ vàng → tím

Ghép 2 ảnh lên 1 nền trong suốt bằng chế độ RGBA.

Kết quả được lưu thành ảnh ghép fruit_composite.png.


Câu 3: Xoay ảnh và tạo phản chiếu

Cách hoạt động:

Đọc ảnh mountain.jpg và boat.jpg, resize về 300×300.

Xử lý từng ảnh:

Xoay 45 độ nhưng giữ nguyên kích thước.

Tạo ảnh phản chiếu theo chiều dọc (lật từ trên xuống).

Ghép 2 ảnh kết quả lên một nền trắng kích thước 700×350.

Kết quả: Ảnh cuối được lưu dưới tên mountain_boat_mirror.jpg.


Câu 4: Phóng to và làm cong ảnh

Cách hoạt động:

Đọc ảnh pagoda.jpg và phóng to 5 lần.

Áp dụng biến đổi hình học kiểu uốn cong theo trục Y bằng hàm sin của X (giống sóng ngang).

Biến đổi được áp dụng cho từng kênh màu (R, G, B).

Kết quả: Ảnh đầu ra có hiệu ứng cong mềm mại, được lưu với tên pagoda_warped.jpg.


Câu 5: Menu tương tác áp dụng các phép biến đổi

Cách hoạt động:

Người dùng chọn một ảnh (img1.jpg, img2.jpg, img3.jpg) và chọn 1 trong 5 phép biến đổi:

Tịnh tiến ảnh theo X, Y

Xoay ảnh theo góc bất kỳ, cho phép reshape

Phóng to / thu nhỏ theo hệ số

Làm mờ Gaussian với sigma tùy chọn

Biến dạng sóng sin theo trục X

Kết quả: Ảnh sau biến đổi được lưu lại với tên result.jpg.
