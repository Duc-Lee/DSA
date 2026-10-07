## Bài 8: Công thức cột chính của mảng 2 chiều

- **Biểu diễn mảng 2 chiều (Ánh xạ cột) trong phần cứng:**
  - Mảng 2 chiều kích thước `M x N` được lưu phẳng trên RAM 1 chiều bằng cách lưu trữ theo từng cột.

```cpp
int A[3][4]; // M x N
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

**Lưu trữ tuyến tính theo Column-major Order:**
- Lưu hết cột 0, sau đó đến cột 1, cột 2, cột 3.

```text
  A   00  10  20  01  11  21  02  12  22  03  13  23
    ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
    │   │   │   │   │   │   │   │   │   │   │   │   │
    └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
     200 202 204 206 208 ...
    |___col 1___|___col 2___|___col 3___|___col 4___|
```

- **Tính địa chỉ:**
  *(Chờ chép tiếp)*
