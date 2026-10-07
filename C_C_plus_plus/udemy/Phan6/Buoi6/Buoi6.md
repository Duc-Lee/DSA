## Bài 6: Trình biên dịch biểu diễn mảng

- Tìm hiểu về trình biên dịch xử lí mảng và quản lí mảng, những vấn đề này sẽ giải quyết những gì?

- Ví dụ ta có biến đơn giản, tức là biến vô hướng:
  ```cpp
  int x = 10;
  ```
  ```text
        x
      ┌────┐
      │ 10 │
      └────┘
    100/101  <-- Địa chỉ (Giả sử int chiếm 2 bytes)
  ```

- Trong chương trình, ta sử dụng tên biến (`x`) để biểu diễn một số dữ liệu nhưng khi trình biên dịch dịch sang mã máy, mã máy sẽ không có khái niệm "tên biến".
- Giả sử trong quá trình thực thi, biến `x` có địa chỉ `100`/`101` và giá trị `10` được lưu trữ ở vị trí đó. Về cơ bản, mã máy sẽ tham chiếu theo địa chỉ chứ không phải theo tên.
- Trình biên dịch sẽ chuyển đổi tên thành địa chỉ. Khi biết được địa chỉ thì sẽ định vị được ô nhớ.
  ```text
    100: lưu byte đầu tiên
    101: lưu byte thứ 2
    => Lưu địa chỉ trong thanh RAM
  ```

- Ví dụ ta có mảng 1 chiều:
  ```cpp
  int A[5] = {3, 5, 8, 4, 2};
  ```
  ```text
    A
      ┌─────┬─────┬─────┬─────┬─────┐
      │  3  │  5  │  8  │  4  │  2  │
      └─────┴─────┴─────┴─────┴─────┘
      200/1 202/3 204/5 206/7 208/9
  ```

- **Mảng là một biến vector** (lưu trữ tập hợp các giá trị).

### Tính địa chỉ phần tử mảng 1 chiều (Chỉ số từ 0)

- Để lấy địa chỉ của phần tử `A[i]`:
  > **Địa chỉ (A[i]) = L₀ + (i × W)**

- Trong đó:
  - **L₀ (Base Address / Địa chỉ cơ sở)**: Là địa chỉ của phần tử đầu tiên `A[0]` (ví dụ bài này là `200`, giá trị cụ thể sẽ được cấp phát khi chương trình chạy và OS cấp phát bộ nhớ).
  - **i (Index)**: Chỉ số phần tử cần truy cập.
  - **W (Data size)**: Kích thước của kiểu dữ liệu tính bằng byte (Ví dụ: `char` = 1 byte, `int` = 2 bytes hoặc 4 bytes tùy hệ thống, ở ví dụ này đang giả sử `int` = 2 bytes).

- **Ví dụ**: Tìm địa chỉ `A[3]` khi L₀ = 200, mỗi phần tử `int` chiếm 2 bytes:
  - Địa chỉ `A[3]` = 200 + (3 × 2) = **206**

### Tại sao C/C++ luôn bắt đầu mảng từ index 0?

Nếu một ngôn ngữ cho phép mảng đánh chỉ số từ 1 đến n, để truy cập phần tử thứ `i`, công thức tính địa chỉ phải lùi lại 1 bước:
  > **Địa chỉ (A[i]) = L₀ + (i - 1) × W**

**Ví dụ**: Cần truy cập phần tử thứ 3 (`A[3]`) theo hệ thống đếm từ 1:
- Địa chỉ `A[3]` = 200 + (3 - 1) × 2 = **204**

**So sánh số lượng phép tính số học mà CPU phải thực thi**:
- Mảng bắt đầu từ **0**: `L₀ + i × W` => Cần **2 phép tính** (Cộng `+` và Nhân `×`).
- Mảng bắt đầu từ **1**: `L₀ + (i - 1) × W` => Cần **3 phép tính** (Cộng `+`, Trừ `-` và Nhân `×`).

**=> Lý do tối ưu hiệu suất**:
- Hệ thống đếm mảng (Array) bắt đầu từ 1 sẽ bị dư 1 phép trừ (`i - 1`). Khi thao tác duyệt mảng hàng triệu phần tử lặp đi lặp lại nhiều lần, phép tính thừa này sẽ tích tụ và làm chậm chương trình.
- Do đó, C/C++ chọn cách đánh chỉ số từ `0` để **tiết kiệm đúng 1 phép toán**, giúp CPU đạt tốc độ tối đa ở mức phần cứng.

- Trong bộ nhớ, `L₀` nằm ở ngay ô địa chỉ đầu tiên:
  - Phần tử đầu tiên nằm tại vạch xuất phát: cách `L₀` đúng **0** bước.
  - Phần tử 1 cách `L₀` **1** bước.
  - Phần tử 2 cách `L₀` **2** bước.

**=> Công thức tự nhiên của phần cứng tính địa chỉ luôn là**:
  > **Địa chỉ = Điểm xuất phát (L₀) + (Độ lệch × W)**
  *(Độ lệch chính là offset `i`)*

- Khi quy ước phần tử đầu tiên có index là `0`, chỉ số `i` chính là độ chênh lệch (offset). CPU chỉ việc lấy trực tiếp:
  `Địa chỉ = L₀ + i × W`

### Trình biên dịch xử lí địa chỉ bộ nhớ như thế nào?

- Khi bạn viết code, tên biến là `x` hay `A` (Array) nhưng CPU và mã máy không biết chữ cái hay tên biến là gì. Chúng chỉ hiểu và làm việc với **địa chỉ ô nhớ** (Memory address).
- **Thời điểm biên dịch (Compile time)**: Chương trình chưa chạy, Hệ điều hành (OS) chưa cấp phát RAM nên trình biên dịch chưa biết địa chỉ cụ thể sẽ nằm ở đâu. Thay vì nhúng một "địa chỉ cứng", trình biên dịch sẽ tạo ra một **công thức tính địa chỉ tương đối** (dựa trên địa chỉ gốc L₀) để chương trình tự tính toán ra địa chỉ thật vào lúc chạy (Run time).