## Bài 7: Công thức tính địa chỉ cho mảng 2 chiều

### Bản chất của mảng 2 chiều trong phần cứng

```cpp
int A[3][4];
```

**Mô hình mảng 2 chiều (Góc nhìn logic):**
```text
      A     0     1     2     3
         ┌─────┬─────┬─────┬─────┐
      0  │ a00 │ a01 │ a02 │ a03 │
         ├─────┼─────┼─────┼─────┤
      1  │ a10 │ a11 │ a12 │ a13 │
         ├─────┼─────┼─────┼─────┤
      2  │ a20 │ a21 │ a22 │ a23 │
         └─────┴─────┴─────┴─────┘
```

**Bản chất trên bộ nhớ RAM (Góc nhìn vật lý):**
```text
  A  00 01 02 03 10 11 12 13 20 21 22 23
   ┌──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┐
   │  │  │  │  │  │  │  │  │  │  │  │  │
   └──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┴──┘
  200/1 202 204 206 ...
```

- Con người sẽ nhìn mảng 2 chiều dưới dạng **lưới và cột** (ma trận `M x N`).
- Nhưng thực tế trên phần cứng, bộ nhớ RAM là một dãy tuyến tính (1D). Mọi mảng 2 chiều kích thước `M x N` đều phải được trải phẳng thành `M x N` ô nhớ liên tiếp.

Có 2 cách trải phẳng mảng 2 chiều xuống RAM:
1. **Row-major Order (Ánh xạ theo hàng)**:
   - Lưu hết hàng `0`, rồi đến hàng `1`, hàng `2`...
   - Được sử dụng trong các ngôn ngữ: **C/C++, Python...**
2. **Column-major Order (Ánh xạ theo cột)**:
   - Lưu hết cột `0`, rồi đến cột `1`, cột `2`...
   - Được sử dụng trong các phần mềm/ngôn ngữ: **Matlab, Fortran...**

---

### Tính địa chỉ theo hàng (Row-major Order)

- Xét ma trận `A[m][n]` (gồm `m` hàng, `n` cột). Để truy cập đến phần tử `A[i][j]`, con trỏ bộ nhớ phải:
  1. **Bỏ qua `i` hàng đầu tiên**: Mỗi hàng có `N` phần tử => Số phần tử cần nhảy qua là `i × N`.
  2. **Đi tiếp `j` bước trong hàng hiện tại**: Nhảy thêm `j` phần tử.
  3. Nhân tổng số phần tử cần lệch với kích thước dữ liệu `W` (byte) rồi cộng với địa chỉ gốc `L₀`.

> **Địa chỉ ( A[i][j] ) = L₀ + [ (i × N) + j ] × W**

**Ví dụ**: Xét `A[1][2]` (mảng `A[3][4]`), `L₀ = 200`, `W = 2`:
- Địa chỉ ( A[1][2] ) = 200 + [ (1 × 4) + 2 ] × 2 = **212**

- Nếu index bắt đầu từ **1** thì công thức sẽ là:
> **Địa chỉ ( A[i][j] ) = L₀ + [ (i - 1) × N + (j - 1) ] × W**

**So sánh hiệu suất tính toán địa chỉ:**
- Mảng bắt đầu từ **0** => Cần **4 phép tính** (2 nhân, 2 cộng).
- Mảng bắt đầu từ **1** => Cần **6 phép tính** (2 nhân, 2 cộng, 2 trừ).

=> Khi duyệt qua ma trận hàng triệu phần tử trong tính toán khoa học hoặc xử lí đồ họa, 2 phép trừ dư thừa này sẽ gây suy giảm hiệu năng rõ rệt. C/C++ giữ nguyên đánh số từ `0` để tối ưu hóa tốc độ CPU.
