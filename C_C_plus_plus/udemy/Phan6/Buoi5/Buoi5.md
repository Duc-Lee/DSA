## Bài 5: Mảng 2 chiều (Array 2D)

- Trong ngôn ngữ lập trình, chúng ta có thể có mảng đa chiều. Vì vậy về cơ bản chúng ta sử dụng một chiều hoặc 2 chiều, hoặc nhiều nhất là 3 chiều. Nhưng ngôn ngữ lập trình cho phép ta khai báo mảng có nhiều chiều.
- Có 3 phương pháp khai báo mảng 2 chiều.

### a. Khai báo mảng 2 chiều thông thường cùng với tên mảng, kiểu dữ liệu của mảng và kích thước

- Giả sử tôi muốn một mảng có kích thước 3x4, `int A[3][4]`. Vì vậy, chúng ta hình dung rằng một mảng có kích thước 3x4 sẽ được tạo bên trong bộ nhớ chính với 3 hàng, 4 cột.

```cpp
int A[3][4];
```

```text
  A
      0   1   2   3
    ┌───┬───┬───┬───┐
  0 │   │   │   │   │
    ├───┼───┼───┼───┤   │
  1 │   │   │   │   │   │ Số hàng
    ├───┼───┼───┼───┤   ▼
  2 │   │   │   │   │
    └───┴───┴───┴───┘
      ───────────►
         Số cột
```

- Chúng ta biểu diễn một mảng 2 chiều dưới dạng hình chữ nhật giống như một chiếc hộp nhưng thực tế bộ nhớ được phân bổ cho mảng 2 chiều sẽ là tuyến tính.

```text
  A
    ┌───────┬───────┬───────┬───────┐  <-- Địa chỉ (giả sử)
    │ 20011 │ 20012 │ 20013 │ 20014 │      của các phần tử
    ├───────┼───────┼───────┼───────┤      mảng 2 chiều
    │ 20015 │ 20016 │ 20017 │ 20018 │
    ├───────┼───────┼───────┼───────┤  <-- mỗi phần tử có 2
    │ 20019 │ 20020 │ 20021 │ 20022 │      byte do kiểu int
    └───────┴───────┴───────┴───────┘
```

=> Vì vậy, điều này có nghĩa là trong thực tế, bộ nhớ sẽ được phân bổ giống như một mảng 1 chiều với `3 x 4 = 12` (số nguyên `int`).

```text
  A
  ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐
  │       │       │       │       │       │       │       │       │ ...
  └───────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘
    20011   20012   20013   20014   20015   20016   20017   20018
```

- Bộ nhớ sẽ phân bổ giống như một mảng một chiều nhưng trình biên dịch cho phép chúng ta truy cập mảng một chiều đó như mảng 2 chiều có số hàng và số cột.

```cpp
A[1][2] = 15;
```

- Ta truy cập mảng 2 chiều với chỉ số, đó là số hàng và số cột mà trình biên dịch sẽ cho phép chúng ta truy cập như một dữ liệu 2 chiều mặc dù bên trong bộ nhớ chính là 1 chiều.

- Khởi tạo mảng 2 chiều với danh sách các phần tử:

```cpp
int A[3][4] = { {1,2,3,4}, {2,4,6,8}, {3,5,7,9} };
```

=> Mảng 2 chiều `A[3][4]` đã được khởi tạo. Điều này thường gặp trong C và C++. Các cú pháp tương tự được sử dụng và mảng sẽ được tạo bên trong ngăn xếp (stack) vì nó giống như một biến. Không có toán tử mới nào được sử dụng. Vì vậy, khi bạn sử dụng toán tử `new` thì mảng được tạo trên heap.

### b. Tạo mảng 2 chiều bằng cách sử dụng mảng con trỏ

- Chúng ta sử dụng một mảng con trỏ:

```cpp
int *A[3]; // Mang 3 con tro
```

- Giả sử ta muốn mảng 2 chiều kích thước 3x4, ta sẽ lấy mảng có kích thước là 3. Biến thông thường sẽ tạo trên ngăn xếp nhưng đây không phải mảng số nguyên. Đây là mảng con trỏ số nguyên.

```text
    A
    ┌───┐
  0 │   │
    ├───┤
  1 │   │  => Đây đều là con trỏ
    ├───┤
  2 │   │
    └───┘
```

- Tạo một mảng 2 chiều trong heap, mỗi mảng có kích thước là 4 để con trỏ trỏ tới.

```text
      A
        ┌───┐    0   1   2   3
      0 │   │──>┌───┬───┬───┬───┐
        ├───┤   └───┴───┴───┴───┘
      1 │   │──>┌───┬───┬───┬───┐
        ├───┤   └───┴───┴───┴───┘
      2 │   │──>┌───┬───┬───┬───┐
        └───┘   └───┴───┴───┴───┘
```

=> Một mảng có kích thước là 4, phải tạo 3 mảng có kích thước là 4 trong heap. Vậy đây là 1 mảng của mảng. Có 3 mảng và mảng này trỏ tới 3 mảng đó và chúng cùng nhau tạo thành 1 mảng 2 chiều.

```cpp
A[0] = new int[4];
A[1] = new int[4];
A[2] = new int[4];
```

- Tạo 3 mảng ở heap và mảng `A[]` sẽ có trong ngăn xếp (stack).
- Đây là cấu trúc có thể truy cập giống như bình thường.
- Giả sử ta có 1 giá trị 15:

```text
      A
        ┌───┐    0   1   2   3
      0 │   │──>┌───┬───┬───┬───┐
        ├───┤   └───┴───┴───┴───┘
      1 │   │──>┌───┬───┬15 ┬───┐
        ├───┤   └───┴───┴───┴───┘
      2 │   │──>┌───┬───┬───┬───┐
        └───┘   └───┴───┴───┴───┘
```

- Ta truy cập:
```cpp
A[1][2] = 15;
```

### c. Tạo mảng 2 chiều bằng con trỏ kép

- Tạo mảng 2 chiều bằng con trỏ kép:
```cpp
int **A;
```

- `A` là con trỏ kép, giống như một biến được tạo bên trong ngăn xếp.
```cpp
A = new int*[3];
```

```text
        A
      ┌───┐
      │   │
      └───┘
        │ 
        ▼
        ┌───┐    0   1   2   3
      0 │   │──>┌───┬───┬───┬───┐
        ├───┤   └───┴───┴───┴───┘
      1 │   │──>┌───┬───┬───┬───┐
        ├───┤   └───┴───┴───┴───┘
      2 │   │──>┌───┬───┬───┬───┐
        └───┘   └───┴───┴───┴───┘
```

- Khai báo mảng con trỏ `A` có kiểu số nguyên. Vì vậy mảng con trỏ có kiểu số nguyên sẽ được tạo ra với kích thước là 3 và sẽ trỏ tới số này. Mảng con trỏ được tạo trong heap.
- Để tạo ra 3 mảng cho mỗi con trỏ trong `A`:
```cpp
A[0] = new int[4];
A[1] = new int[4];
A[2] = new int[4];
```

- Chỉ có con trỏ kép `A` nằm trong stack.
- Mỗi lần sử dụng toán tử `new`, vì vậy nếu bạn muốn biết cách thực hiện ngôn ngữ C thì sử dụng hàm `malloc` để sử dụng để phân bổ bộ nhớ. Vì vậy, cứ nơi nào dùng `new` thì trong C ta sử dụng `malloc()`, vì `malloc()` là bộ nhớ trong heap.
- Sử dụng hàm `for()` để truy cập phần tử mảng 2 chiều.
  - VD:
    ```cpp
    for(int i = 0; i < 3; i++) { // i hang
        for(int j = 0; j < 4; j++) { // j cot
            // Code
        }
    }
    ```

---


