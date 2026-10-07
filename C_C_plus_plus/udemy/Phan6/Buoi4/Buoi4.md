## Bài 4: Cách tăng kích thước mảng

- Tạo 1 mảng có kích thước là 5 được tạo trong **heap** và con trỏ đang trỏ tới mảng đó. Con trỏ `p` nằm trong ngăn xếp (**stack**).

```cpp
int *p = new int[5];
```

```
┌──────────────────────────────────────────────────────────┐
│ HEAP                                                     │
│                                                          │
│    ┌─────┬─────┬─────┬─────┬─────┐                       │
│    │  5  │  8  │  3  │  6  │  9  │  ◄── new int[5]       │
│    └─────┴─────┴─────┴─────┴─────┘                       │
│       0     1     2     3     4                          │
│       ▲                                                  │
│       │                                                  │
├───────┼──────────────────────────────────────────────────┤
│ STACK │                                                  │
│       │                                                  │
│    ┌──┴──┐                                               │
│    │  ●  │ p                                             │
│    └─────┘                                               │
└──────────────────────────────────────────────────────────┘
```

- Bây giờ ta muốn **tăng kích thước mảng** lên thì làm sao?
  - Giả sử lấy thêm một con trỏ `q` và tạo mảng mới có kích thước lớn hơn theo yêu cầu. Giả sử ta muốn kích thước là 10:

```cpp
int *q = new int[10];
```

```
┌──────────────────────────────────────────────────────────┐
│ HEAP                                  ◄── new int[10]    │
│                                                          │
│     ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐            │
│     │   │   │   │   │   │   │   │   │   │   │            │
│     └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘            │
│       0   1   2   3   4   5   6   7   8   9              │
│       ▲                                                  │
│       │                                                  │
├───────┼──────────────────────────────────────────────────┤
│ STACK │                                                  │
│       │                                                  │
│    ┌──┴──┐                                               │
│    │  ●  │ q                                             │
│    └─────┘                                               │
└──────────────────────────────────────────────────────────┘
```

- Sơ đồ minh họa quá trình tăng kích thước mảng:

```text
         p                            delete []p
       ┌───┐                  ┌───┬───┬───┬───┬───┐
       │   │ ─ ─ ─ ─ ─ ─ ─ ─X>│ 5 │ 8 │ 9 │ 6 │ 4 │ (Mảng cũ bị xóa)
       └───┘                  └───┴───┴───┴───┴───┘
         │
         │ (Gán p = q)
         ▼
                   
         q                    ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
       ┌───┐                  │ 5 │ 8 │ 9 │ 6 │ 4 │   │   │   │   │   │
delete │ X │ ───────────────> └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
       └───┘                    0   1   2   3   4   5   6   7   8   9
(Gán q = NULL)                 (Mảng mới kích thước 10)
```


1. **Khởi tạo mảng động mới `q`** (kích thước lớn hơn) và sao chép các phần tử từ mảng cũ sang mảng mới:
   ```cpp
   // Sao chép các giá trị
   for (int i = 0; i < 5; i++) {
       q[i] = p[i];
   }
   ```
   *(Trong ngôn ngữ C/C++ có thể dùng hàm `memcpy()` để sao chép mảng)*.

2. **Giải phóng mảng cũ**: Xóa mảng cũ mà `p` đang trỏ tới để tránh rò rỉ bộ nhớ.
   ```cpp
   // Xóa mảng p hiện tại (mảng 5 phần tử)
   delete []p;
   ```

3. **Cập nhật lại con trỏ**: Gán con trỏ `p` trỏ sang vùng nhớ của mảng mới `q`. Sau đó gán `q = NULL` (tương ứng với chữ "delete q" bị gạch chéo trong hình) để `q` không còn trỏ vào mảng mới nữa.
   ```cpp
   // Gán p bằng địa chỉ q
   p = q;

   // Gán q bằng NULL
   q = NULL;
   ```

- **Lưu ý quan trọng**: 
  - Quy trình phải được thực hiện **tuần tự** như trên mã code (phải `delete []p;` trước khi gán `p = q;`) để giải phóng đúng vùng nhớ không dùng và tránh làm mất vùng nhớ vừa được cấp cho mảng mới.
  - Gán `q = NULL` để `q` không còn trỏ vào mảng có 10 phần tử nữa, để lúc lỡ gọi `delete []q;` không xóa nhầm vùng nhớ ấy (do lúc này `q` đang cùng trỏ vào mảng đó với `p`).

---

### Tại sao kích thước mảng không thể tự động tăng lên trực tiếp?

- Ta **không thể tăng kích thước trực tiếp của mọi mảng**.
- Bởi vì **bộ nhớ của một mảng phải liên tiếp (liền kề) nhau**.

Giả sử ta cấp phát:
```cpp
int *p = new int[4];
int *x = new int[5]; // Một biến khác được cấp phát sau đó
```

Mô phỏng bộ nhớ:
```text
      p                               x
    ┌───┐     ┌───┬───┬───┬───┐     ┌───┐
    │ ● │──>  │ 1 │ 2 │ 3 │ 4 │     │ 5 │ (Có giá trị 5)
    └───┘     └───┴───┴───┴───┘     └───┘
             5001 5002 5003 5004   5005
```

- Giả sử thật không may biến `x` tạo vùng nhớ có giá trị `5` để lưu trữ ở ngay địa chỉ `5005` liền kề mảng `p`.
- Nếu muốn tăng kích thước mảng `p` lên 5 phần tử (mở rộng ngay tại chỗ), thì phần tử thứ 5 sẽ bị đè lên vùng nhớ của biến `x`.
- **=> Kết luận:** Ta muốn tăng kích thước mảng lớn hơn nhưng **chưa biết vùng nhớ tiếp theo đó có trống (free) hay không** nên không có gì để đảm bảo an toàn.
- **=> Phương pháp giải quyết:** Là **tạo một mảng lớn hơn** (ở một vị trí khác) và **dịch chuyển (sao chép)** các phần tử từ mảng cũ sang mảng mới.

---

### Chi tiết cách triển khai trong C++

- **Chuyển các giá trị phần tử của `p` sang `q`**:
  - File `main.cpp`:
    ```cpp
    // Sao chép các giá trị
    for (int i = 0; i < 5; i++) {
        q[i] = p[i];
    }
    ```
  - *(Lưu ý trong ảnh: Trong ngôn ngữ C có hàm `memset()` để sao chép phần tử như vậy. Tuy nhiên, hàm dùng để sao chép mảng thực tế thường là `memcpy()` hoặc `memmove()`)*.

- **Minh họa con trỏ `q` sau khi nhận giá trị**:
  ```text
        q             0   1   2   3   4   5   6   7   8   9
      ┌───┐         ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
      │   │ ──────> │ 5 │ 8 │ 9 │ 6 │ 4 │   │   │   │   │   │
      └───┘         └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘
  ```

- **Muốn tăng kích thước của `p`?**
  - File `main.cpp`:
    ```cpp
    int *p = new int[5];
    int *q = new int[10];
    
    // sao chép giá trị
    for (int i = 0; i < 5; i++) {
        q[i] = p[i];
    }
    
    // xóa mảng p hiện tại 5 phần tử max
    delete []p;
    
    // Gán p bằng địa chỉ q
    p = q;
    
    // Gán q cho NULL
    q = NULL;
    
    // Giải phóng q
    delete []q;
    ```
