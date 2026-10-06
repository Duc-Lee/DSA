# Hash Functions (Hàm băm)

**Hàm băm (Hash Function)** là một hàm nhận đầu vào (được gọi là *khóa* hoặc *key*) có kích thước tùy ý và chuyển đổi nó thành một giá trị có kích thước cố định (thường là số nguyên), được gọi là **giá trị băm** (*hash value*) hoặc **mã băm** (*hash code*).

Ví dụ đơn giản sử dụng phép toán modulo:
$$h(x) = x \bmod 10$$

![](../Hashing/image/a1.png)

---

## 1. Các ví dụ minh họa về hàm băm

Dưới đây là các ví dụ minh họa cách các khóa đầu vào (*keys*) được ánh xạ tới các giá trị băm (*hash values*) để lưu trữ và truy xuất hiệu quả.

### Ví dụ 1: Sử dụng số điện thoại làm khóa (Key)
Giả sử ta sử dụng **hai chữ số cuối** của số điện thoại làm giá trị băm:
$$h(k) = k \bmod 100$$

- **Kích thước bảng băm:** Bảng có kích thước là 100, do đó các chỉ số (index) hợp lệ nằm trong khoảng từ `0` đến `99`. Việc lấy hai chữ số cuối đảm bảo kết quả luôn nằm trong phạm vi này.
 
  > **Tại sao không lấy hai chữ số đầu tiên?**  
  > Nhiều số điện thoại có cùng đầu số nhà mạng (ví dụ `09...`, `08...`, `03...`). Nếu lấy hai chữ số đầu sẽ dẫn đến phân bố không đồng đều và gây ra rất nhiều trường hợp trùng lặp (va chạm). Ngược lại, các chữ số cuối có độ phân tán ngẫu nhiên tốt hơn nhiều.

---

### Ví dụ 2: Sử dụng chuỗi ký tự viết thường làm khóa (Key)
Giả sử ta quy ước giá trị cho các chữ cái tiếng Anh: `'a' = 1, 'b' = 2, ..., 'z' = 26`.

#### Cách 1: Tính tổng giá trị các ký tự
Cộng giá trị của tất cả các ký tự lại và lấy phần dư theo kích thước bảng:
$$h(s) = \left(\sum \text{giá\_trị}(s[i])\right) \bmod 100$$

- **Hạn chế:** Các chuỗi ký tự khác nhau có thể tạo ra cùng một giá trị băm, dẫn đến **va chạm (collision)**.
  - `"ad"`: $1 + 4 = 5 \implies 5 \bmod 100 = 5$
  - `"bc"`: $2 + 3 = 5 \implies 5 \bmod 100 = 5$
  - Thậm chí các chuỗi hoán vị như `"ad"` và `"da"` cũng cho cùng kết quả.

#### Cách 2: Phương pháp cải tiến (Tổng có trọng số - Weighted Sum)
Để khắc phục vấn đề hoán vị và giảm thiểu va chạm, ta gán trọng số theo vị trí cho từng ký tự:
$$h(s) = \left(\sum_{i} \text{giá\_trị}(s[i]) \times \text{trọng\_số}[i]\right) \bmod 100$$

- **Ý nghĩa:** Mỗi ký tự đóng góp khác nhau tùy thuộc vào vị trí của nó trong chuỗi (ví dụ: dùng lũy thừa của một cơ số nguyên tố $p^i$). Điều này giúp cải thiện đáng kể sự phân bố giá trị băm và giảm va chạm.

---

## 2. Các thuộc tính của một hàm băm tốt

Một hàm băm tốt cần đáp ứng các tiêu chuẩn sau để đảm bảo lưu trữ, truy xuất và bảo mật dữ liệu hiệu quả:

- **Tính xác định (Determinism):** Cùng một đầu vào phải luôn luôn tạo ra cùng một giá trị băm duy nhất.
- **Kích thước đầu ra cố định (Fixed Output Size):** Đầu ra luôn có kích thước cố định, bất kể kích thước dữ liệu đầu vào lớn hay nhỏ.
- **Tính toán hiệu quả (Efficiency):** Hàm băm cần tính toán rất nhanh (thời gian $O(1)$ hoặc tuyến tính theo độ dài khóa).
- **Tính đồng nhất (Uniformity):** Phân phối các giá trị băm đồng đều trên toàn bộ không gian bảng băm để tránh hiện tượng tập trung cục bộ (clustering).
- **Hiệu ứng tuyết lở (Avalanche Effect):** Một thay đổi nhỏ ở dữ liệu đầu vào (dù chỉ là 1 bit hoặc 1 ký tự) cũng tạo ra giá trị băm khác biệt đáng kể.
- **Khả năng kháng tiền ảnh (Pre-image Resistance):** Khó/bất khả thi về mặt tính toán để suy ngược lại dữ liệu đầu vào ban đầu khi chỉ biết giá trị băm (dành cho hàm băm mật mã).
- **Khả năng kháng va chạm (Collision Resistance):** Rất khó để tìm ra hai đầu vào khác nhau $x \ne y$ sao cho $h(x) = h(y)$.

---

## 3. Ứng dụng của hàm băm

Hàm băm được ứng dụng rộng rãi trong khoa học máy tính:

- **Bảng băm (Hash Table / Hash Map):** Ứng dụng phổ biến nhất trong DSA, cho phép lưu trữ, tìm kiếm, chèn và xóa dữ liệu với độ phức tạp trung bình $O(1)$.
- **Kiểm tra tính toàn vẹn dữ liệu (Data Integrity):** Tạo mã kiểm tra (checksum, CRC32, MD5) để xác minh dữ liệu không bị hỏng hoặc bị sửa đổi trong quá trình truyền tải.
- **Mật mã học & Bảo mật (Cryptography):** Băm mật khẩu người dùng (bcrypt, argon2), chữ ký số, chứng thực thông điệp và công nghệ Blockchain (SHA-256).
- **Cấu trúc dữ liệu nâng cao:** Bộ lọc Bloom (Bloom Filter), HyperLogLog, cây Merkle (Merkle Tree).

---

## 4. Các phương pháp xây dựng hàm băm phổ biến

### 4.1. Phương pháp chia (Division Method)
Tính giá trị băm bằng phần dư khi chia khóa $k$ cho kích thước bảng $m$:
$$h(k) = k \bmod m$$
*(Trong đó $k$ là khóa và $m$ thường được chọn là một **số nguyên tố** không quá gần lũy thừa của 2 hoặc 10).*

- **Ưu điểm:**
  - Cực kỳ đơn giản, dễ cài đặt và tính toán nhanh.
  - Hoạt động rất tốt khi chọn $m$ là số nguyên tố phù hợp.
- **Nhược điểm:**
  - Phân bố kém nếu chọn $m$ không khéo (ví dụ: nếu chọn $m = 2^p$, giá trị băm chỉ phụ thuộc vào $p$ bit cuối cùng của $k$).

---

### 4.2. Phương pháp nhân (Multiplication Method)
Khóa $k$ được nhân với một hằng số thực $A$ ($0 < A < 1$), lấy phần thập phân của kết quả rồi nhân với kích thước bảng $m$ và làm tròn xuống:
$$h(k) = \lfloor m \cdot ((k \cdot A) \bmod 1) \rfloor$$
*(Trong đó $\lfloor \dots \rfloor$ là hàm làm tròn xuống (floor), và $(k \cdot A) \bmod 1$ biểu thị phần thập phân của $k \cdot A$. Nhà khoa học Donald Knuth đề xuất hằng số vàng $A \approx \frac{\sqrt{5} - 1}{2} \approx 0.6180339887$).*

- **Ưu điểm:**
  - Ít phụ thuộc vào việc lựa chọn $m$ (có thể chọn $m = 2^p$ để tối ưu tính toán bằng phép dịch bit).
  - Phân phối giá trị băm đồng đều trong nhiều trường hợp thực tế.
- **Nhược điểm:**
  - Phép tính số thực phức tạp hơn một chút so với phương pháp chia.

---

### 4.3. Phương pháp bình phương lấy giữa (Mid-Square Method)
Phương pháp này gồm các bước:
1. **Bình phương khóa:** Tính $k^2$.
2. **Trích xuất phần giữa:** Lấy các chữ số ở giữa của giá trị bình phương để làm giá trị băm (có thể modulo theo kích thước bảng nếu cần).

*Việc bình phương khóa giúp phân bổ đều các chữ số, vì tất cả các chữ số của khóa ban đầu đều đóng góp vào việc tạo nên các chữ số ở giữa kết quả bình phương.*

- **Ưu điểm:**
  - Tạo ra sự phân bố giá trị băm rất tốt và ngẫu nhiên.
- **Nhược điểm:**
  - Với khóa $k$ lớn, phép bình phương có thể gây tràn số và tốn chi phí tính toán.

---

### 4.4. Phương pháp gấp (Folding Method)
Trong phương pháp này, khóa được chia thành nhiều đoạn nhỏ bằng nhau (hoặc gần bằng nhau), sau đó các đoạn này được cộng lại để tạo ra giá trị băm:
1. Chia khóa $k$ thành các đoạn nhỏ có kích thước cố định.
2. Cộng tất cả các đoạn lại với nhau để được tổng trung gian.
3. Áp dụng phép modulo theo kích thước bảng băm: $h(k) = \text{tổng} \bmod m$.
*(Tùy chọn: Có thể đảo ngược các đoạn xen kẽ trước khi cộng - gọi là Fold-boundary - để tăng độ phân tán).*

- **Ưu điểm:**
  - Đơn giản, dễ thực hiện.
  - Rất phù hợp với các khóa có kích thước lớn (như số CMND/CCCD, ISBN, số thẻ tín dụng).
- **Nhược điểm:**
  - Chất lượng phân bố phụ thuộc vào cách phân chia khóa; nếu các đoạn có cấu trúc tương tự nhau, va chạm vẫn có thể xảy ra nhiều.

---

### 4.5. Các hàm băm mật mã (Cryptographic Hash Functions)
Các hàm băm này được thiết kế ưu tiên tính **bảo mật** và **kháng tấn công** hơn là tốc độ tính toán thuần túy.
- **Ví dụ tiêu biểu:** SHA-256, SHA-512, SHA-3.
- **Đặc điểm:** Đảm bảo nghiêm ngặt tính kháng tiền ảnh, kháng tiền ảnh thứ hai và kháng va chạm.
- **Ưu điểm:**
  - Độ tin cậy và bảo mật cực cao, không thể giải mã ngược.
- **Nhược điểm:**
  - Tốc độ tính toán chậm hơn nhiều so với các hàm băm thông thường dùng trong bảng băm.

---

### 4.6. Băm phổ quát (Universal Hashing)
Thay vì sử dụng một hàm băm cố định, băm phổ quát chọn **ngẫu nhiên** một hàm băm từ một họ các hàm băm được thiết kế cẩn thận tại thời điểm chạy:
$$h_{a, b}(k) = ((a \cdot k + b) \bmod p) \bmod m$$
*(Trong đó $a, b$ là các hằng số ngẫu nhiên với $1 \le a < p$, $0 \le b < p$; $p$ là số nguyên tố lớn hơn $m$, và $k$ là khóa).*

- **Ưu điểm:**
  - Giảm thiểu xác suất va chạm xuống mức tối đa (không vượt quá $1/m$).
  - Chống lại các cuộc tấn công có chủ đích từ dữ liệu xấu nhất (Hash DoS).
- **Nhược điểm:**
  - Cần thêm tài nguyên lưu trữ tham số ngẫu nhiên và tính toán phức tạp hơn.

---

### 4.7. Hàm băm hoàn hảo (Perfect Hashing)
Băm hoàn hảo là kỹ thuật xây dựng hàm băm cho một **tập hợp khóa tĩnh (cố định)** đã biết trước, đảm bảo rằng mỗi khóa ánh xạ tới một chỉ mục duy nhất mà **hoàn toàn không xảy ra va chạm** (thời gian tìm kiếm đảm bảo chắc chắn là $O(1)$ trong trường hợp xấu nhất).

- **Phân loại:**
  - **Băm hoàn hảo tối thiểu (Minimal Perfect Hashing):** Kích thước bảng đúng bằng số lượng khóa ($m = n$).
  - **Băm hoàn hảo không tối thiểu:** Kích thước bảng lớn hơn số lượng khóa ($m > n$).
- **Ưu điểm:**
  - Triệt tiêu 100% va chạm, không cần cơ chế xử lý va chạm.
- **Nhược điểm:**
  - Chỉ áp dụng được cho tập dữ liệu tĩnh (không hỗ trợ thêm/xóa phần tử động).
  - Chi phí thiết kế và xây dựng hàm băm ban đầu khá phức tạp.