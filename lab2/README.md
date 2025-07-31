Câu 1: Biến đổi ảnh bằng 5 phương pháp nâng cao

Cách hoạt động:

Đọc ảnh trong thư mục exercise, cho người dùng chọn kiểu biến đổi sau:

I – Inverse: Đảo ngược màu bằng công thức 255 - pixel

G – Gamma correction: Làm sáng ảnh không tuyến tính theo tham số gamma

L – Log transform: Tăng cường vùng tối bằng hàm logarit

H – Histogram equalization: Cân bằng độ sáng tổng thể ảnh (kênh Y nếu là ảnh màu)

C – Contrast stretching: Kéo dãn độ tương phản dựa trên giá trị min–max của ảnh

Kết quả được hiển thị và lưu dưới dạng output_<phép biến đổi>_<tên ảnh gốc>.

Câu 2: Biến đổi ảnh bằng Fourier và bộ lọc Butterworth

Cách hoạt động:

F – Fourier: Hiển thị phổ biên độ bằng biến đổi Fourier 2D.

L – Lowpass: Làm mịn ảnh bằng bộ lọc thông thấp Butterworth (ngăn tần số cao).

H – Highpass: Làm nổi chi tiết bằng bộ lọc thông cao Butterworth (ngăn tần số thấp).

Phổ được tính bằng fft2 + fftshift, bộ lọc được nhân trực tiếp trong miền tần số rồi biến đổi ngược về ảnh.

Câu 3: Biến đổi ngẫu nhiên từng kênh màu RGB

Cách hoạt động:

Đọc ảnh và tách thành 3 kênh R, G, B.

Áp dụng ngẫu nhiên 1 trong 5 phép biến đổi lên mỗi kênh:

Negative (ảnh âm)

Logarithmic

Gamma Correction

Histogram Equalization

Contrast Stretching

Ghép 3 kênh lại và hiển thị ảnh kết quả.

Kết quả tạo ra ảnh có hiệu ứng màu sắc thay đổi đa dạng, mỗi lần chạy cho kết quả khác nhau.

Câu 4: Lọc tần số ngẫu nhiên từng kênh màu với Butterworth

Cách hoạt động:

Đọc ảnh, tách thành 3 kênh màu R, G, B.

Mỗi kênh được áp dụng ngẫu nhiên một trong hai lọc tần số:

Butterworth Low-pass (làm mờ, giữ tần số thấp)

Butterworth High-pass (làm sắc nét, giữ tần số cao)

Các phép lọc thực hiện trong miền tần số với FFT.

Ghép 3 kênh lại và lưu ảnh kết quả.

Ảnh đầu ra cho hiệu ứng lọc khác nhau trên từng kênh, tạo kết quả thị giác độc đáo.
