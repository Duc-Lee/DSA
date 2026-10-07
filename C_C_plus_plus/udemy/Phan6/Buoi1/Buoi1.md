## Bài 1: Giới thiệu về Mảng

**\*** Trước khi vào Mảng (Array) là gì? thì ta sẽ đi tìm hiểu về **biến** là gì?

- Mọi ngôn ngữ lập trình đều hỗ trợ biến và các biến sẽ có 1 số kiểu dữ liệu.
- **VD:** Khi mình khai báo một biến `int x` muốn lưu giá trị 10:

```c
int x = 10;
```

- Sau đó, ta biết rõ ràng tại thời điểm chạy, biến `x` sẽ nhận được một số bộ nhớ:

```
                      x
                  +--------+
int x = 10  --->  |   10   |   2 byte
                  +--------+
                   1001101
```

=> 2 byte bộ nhớ (memory) sẽ được phân bổ cho `x` và có địa chỉ là `1001101` (ví dụ).

=> Đây là loại **biến đơn**, có thể lưu trữ một giá trị duy nhất. Các biến giá trị đơn này còn được gọi là **biến vô hướng (scalar variable)**.

- Vô hướng nghĩa là chỉ có độ lớn => `int x = 10` nghĩa là đây là độ lớn, giá trị là 10.

---

## I. Mảng là gì?

- Chúng ta có thể lưu trữ nhiều giá trị, tức là danh sách các giá trị hoặc tập hợp các giá trị.

=> **Mảng** là tập hợp các phần tử và tất cả các phần tử đều có **cùng kiểu**. Vì vậy, mảng là tập hợp các phần tử dữ liệu tương tự được nhóm lại dưới **một tên**.

- Giả sử biến chỉ lưu một giá trị, nếu tôi phải lưu trữ danh sách các giá trị, tôi có thể khai báo một mảng.

- **Ví dụ:** Giả sử tôi khai báo một mảng kiểu số nguyên có tên là `A` và kích thước là 5. Vì vậy điều này sẽ cung cấp cho tôi một mảng có kích thước là 5:

```
             0     1     2     3     4
int A[5]  A +-----+-----+-----+-----+-----+
            |     |     |     |     |     |
            +-----+-----+-----+-----+-----+
               ^
```

> Nơi có thể lưu 5 số nguyên, mỗi số được lưu vào 1 ô nhớ có kích thước `int` (2 byte) liên tiếp với chỉ số bắt đầu từ 0 đến 4.

- Nếu `int x = 10` là một **biến vô hướng** có thể lưu 1 giá trị thì `int A[5]` là một **biến vector** cũng có 1 chiều duy nhất. Vì vậy tôi có thể lưu trữ tổng cộng 5 giá trị trong mảng kia.

=> **Mảng là một biến vector.**

```
         20011 20013 20015 20017 20019
        +-----+-----+-----+-----+-----+
int A[] |     |     |     |     |     |
        +-----+-----+-----+-----+-----+
           0     1     2     3     4
```

- **\*)** Đối với mảng `A[]` sẽ có tổng bộ nhớ được phân bổ là **10 byte** do mỗi ô nhớ là 2 byte.
- **\*)** Nếu phần tử đầu tiên `A[0]` có địa chỉ `20011` (ví dụ) thì các phần tử tiếp theo có địa chỉ lần lượt là `20013, 20015, 20017, 20019` (mỗi phần tử cách nhau 2 byte vì `int` chiếm 2 byte) do các phần tử được lưu trữ **liền kề nhau** dưới dạng một khối duy nhất.

- Để phân biệt các phần tử trong mảng với nhau thì sẽ nhờ vào **chỉ mục (index)**:

```
        +-----+-----+-----+-----+-----+
int A[] |     |     | 15  |     |     |
        +-----+-----+-----+-----+-----+
           0     1     2     3     4
```

- Giả sử lưu giá trị 15 ở ô thứ 3 thì ta truy cập ô nhớ đó để lấy giá trị bằng cách lấy index (chỉ số) được gán giá trị 15:

```c
printf("%d", A[2]); // 15
```

=> Với index, ta có thể truy cập bất kỳ phần tử nào của mảng với độ phức tạp **O(1)**.
