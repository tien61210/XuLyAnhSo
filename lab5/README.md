Câu 1: Gán nhãn và hiển thị các đối tượng

Cách hoạt động:

Đọc ảnh geometric.png ở mức xám, phân ngưỡng bằng Otsu để nhị phân hóa ảnh. Sau đó gán nhãn các vùng trắng bằng label().

Ảnh kết quả được lưu thành label_output.jpg. Tiếp theo, vẽ các bounding box quanh từng đối tượng được phát hiện, rồi hiển thị bằng matplotlib.

Câu 2: Dò tìm cạnh theo chiều dọc

Cách hoạt động:

Đọc ảnh geometric.png ở mức xám, sau đó trừ ảnh gốc với phiên bản đã dịch phải 1 pixel theo chiều ngang để phát hiện cạnh dọc.

Kết quả là ảnh biểu diễn các đường biên theo chiều dọc và được hiển thị bằng matplotlib.

Câu 3: Dò tìm cạnh với Sobel Filter

Cách hoạt động:

Đọc ảnh geometric.png, sau đó áp dụng Sobel filter theo cả trục dọc (axis=0) và ngang (axis=1) để phát hiện biên.

Tổng độ lớn gradient theo hai chiều được tính và hiển thị bằng matplotlib để thể hiện rõ các đường biên nổi bật trong ảnh.

Câu 4: Xác định góc của đối tượng

Cách hoạt động:

Đọc ảnh geometric.png, áp dụng thuật toán Harris Corner Detection để phát hiện các góc của đối tượng trong ảnh.

Ảnh đầu ra thể hiện giá trị phản hồi (response) của Harris tại từng điểm, trong đó các điểm sáng nổi bật là các góc đặc trưng.

Câu 5: Dò tìm đường thẳng trong ảnh

Cách hoạt động:

Mã sử dụng kỹ thuật Hough Transform để phát hiện các đường thẳng trong ảnh nhị phân.

Đầu vào là ma trận ảnh, và đầu ra là bản đồ Hough (accumulator) hiển thị sự tích lũy phiếu bầu cho các đường thẳng với từng cặp giá trị (rho, theta).

Chi tiết:

Với mỗi điểm ảnh sáng (giá trị lớn hơn gamma), thuật toán duyệt qua các góc θ từ 0–89 độ.

Tính khoảng cách ρ tương ứng và tăng tích lũy tại vị trí (ρ, θ) trong bản đồ Hough.

Kết quả trực quan cho thấy các điểm sáng trên bản đồ tương ứng với các đường thẳng hiện diện trong ảnh gốc.

Câu 6: Dò tìm đường tròn trong ảnh

Cách hoạt động:

Đoạn mã sử dụng corner Harris detector để xác định các điểm góc (corner) trong ảnh, thường là các vị trí biên có độ cong lớn — nơi các đường cong như đường tròn có thể hiện diện.

Chi tiết:

Ảnh đầu vào 'bird.png' được chuyển sang thang độ xám (rgb2gray).

Áp dụng Harris Corner Detection với hệ số k=0.001 để phát hiện các điểm góc tiềm năng.

Kết quả trả về là một bản đồ độ phản hồi Harris (coordinate), trong đó các điểm có giá trị cao là ứng viên góc — có thể là một phần của các đường tròn.
