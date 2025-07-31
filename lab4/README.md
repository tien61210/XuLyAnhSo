Câu 1: Chọn và xử lý vùng đỉnh LangBiang

Cách hoạt động:

Chương trình đọc ảnh DaLat.jpg, cắt một vùng 100x100 pixel từ vị trí (100, 100), áp dụng phương pháp phân ngưỡng Otsu để tạo mask và giữ lại vùng đối tượng sáng, phần nền được đặt màu đen.

Kết quả được lưu thành ảnh lang_biang.jpg.

Kết quả:

Tạo ảnh mới hiển thị riêng vùng đỉnh LangBiang với phần nền đã được loại bỏ.

Câu 2: Xoay và xử lý vùng Hồ Xuân Hương

Cách hoạt động:

Chương trình đọc ảnh DaLat.jpg, cắt vùng 100x100 pixel tại (100, 100), xoay vùng này 45 độ, sau đó áp dụng phương pháp phân ngưỡng thích nghi (adaptive threshold) để tách đối tượng.

Kết quả được tô màu và lưu lại thành ho_xuan_huong.jpg.

Kết quả:

Tạo ảnh mới hiển thị vùng Hồ Xuân Hương đã xoay, rõ nét các chi tiết vùng sáng.

Câu 3: Biến đổi tọa độ và làm mịn Quảng Trường Lâm Viên

Cách hoạt động:

Chương trình cắt vùng 100x100 tại (100,100) từ ảnh DaLat.jpg, áp dụng biến dạng lưới tọa độ để tạo hiệu ứng sóng nhẹ. Sau đó, ảnh được nhị phân hóa và xử lý đóng (morphological closing) để làm mịn vùng sáng.

Kết quả cuối được che nền và lưu thành quan_truong_lam_vien.jpg.

Kết quả:

Hiển thị vùng quảng trường bị biến dạng nhẹ, nổi bật các chi tiết chính, nền đã được loại bỏ.

Câu 4: Biến đổi hình học và phân đoạn ảnh

1. Đọc ảnh và cắt ROI (load_roi)

Đọc ảnh mức xám từ đường dẫn.

Cắt một vùng nhỏ (ROI) kích thước 100x100 từ tọa độ (x=100, y=100) để thực hiện xử lý.

2. Biến đổi hình học (Geometric Transformations)

coordinate_mapping(img)

Biến đổi tọa độ từng điểm ảnh theo dạng sóng sinusoidal, tạo hiệu ứng uốn lượn ảnh.

rotate_image(img)

Xoay ảnh quanh tâm một góc mặc định 45 độ, dùng phép biến đổi affine.

scale_image(img)

Phóng to ảnh theo tỷ lệ fx=1.5, fy=1.5 bằng nội suy tuyến tính.

shift_image(img)

Tịnh tiến ảnh sang phải và xuống dưới 30 pixel bằng ma trận tịnh tiến.

3. Phân đoạn ảnh (Segmentation)


adaptive_thresholding(img)

Phân ngưỡng cục bộ ảnh bằng phương pháp trung bình động, xử lý tốt vùng sáng tối không đều.

binary_dilation(img)

Áp dụng phép co giãn (dilate) nhị phân, làm dày các vùng trắng bằng kernel 3x3.

binary_erosion(img)

Áp dụng phép xói mòn (erode), làm mỏng vùng trắng trong ảnh nhị phân.

otsu_thresholding(img)

Phân ngưỡng toàn cục tự động bằng phương pháp Otsu để tách foreground và background.

4. Menu lựa chọn và xử lý (menu, apply_function)

Hiển thị danh sách lựa chọn các thao tác từ 1a → 2d.

Người dùng nhập mã thao tác (ví dụ: 1b, 2a+2b).

Áp dụng từng hàm tương ứng lên ảnh ROI.

Nếu ảnh đầu ra là nhị phân → tô đen vùng mask để hiển thị rõ hơn.

Lưu và hiển thị kết quả bằng OpenCV.

