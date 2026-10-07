## Bài 2: Khai báo mảng (Declarations of Array)

- Khi tôi khai báo một mảng tên `A` và có kích thước là 5 thì mảng này sẽ phân bổ không gian cho 5 số nguyên, index từ 0 đến 4.

```
            +-----+-----+-----+-----+-----+
int A[5]; A |  ?  |  ?  |     |     |     |
            +-----+-----+-----+-----+-----+
               0     1     2     3     4
                     garbage
```

-  Khi chưa khởi tạo giá trị thì các phần tử trong mảng `A[]` sẽ mang **giá trị rác**, nghĩa là các giá trị không xác định. Sẽ có những giá trị ngẫu nhiên không được chúng ta khởi tạo, do đó chúng không có ích cho chúng ta. Vì vậy, chúng ta gọi nó là **giá trị rác (garbage)**.

- Bây giờ, tôi muốn khởi tạo các giá trị thì tôi sẽ khai báo:

```c
int A[5] = {2, 4, 6, 8, 10};
```

=> Mảng `A[5]` sẽ được tạo trong thời gian chạy và tất cả các giá trị sẽ được khởi tạo trong mảng này.

```
    +-----+-----+-----+-----+-----+
  A |  2  |  4  |  6  |  8  | 10  |
    +-----+-----+-----+-----+-----+
       0     1     2     3     4
```

=> Đây là phương pháp khai báo đi kèm với phần khởi tạo trong một mảng.

- **Cách thứ 3:** Tôi sẽ khai báo một mảng nhưng không muốn khởi tạo tất cả các giá trị, chỉ muốn một số giá trị được khởi tạo. Khi đó một mảng có kích thước là 5 sẽ được tạo ra với các chỉ số từ 0 đến 4 và chỉ có 2 giá trị được đề cập:

```c
int A[5] = {2, 4};
```

=> Mảng `A[]` có 5 phần tử, 2 phần tử đầu được khởi tạo là 2 và 4, **3 phần tử còn lại được khởi tạo bằng số 0**.

```
    +-----+-----+-----+-----+-----+
  A |  2  |  4  |  0  |  0  |  0  |
    +-----+-----+-----+-----+-----+
       0     1     2     3     4
```

- **+)** Bởi vì khi quá trình khởi tạo được bắt đầu, nó sẽ cố gắng khởi tạo tất cả các phần tử. Vì vậy các giá trị còn lại không được cung cấp nên nó sẽ khởi tạo chúng bằng số 0.

- Vì vậy, ngay cả khi mảng số nguyên `A[]` có kích thước là 5 và chỉ khởi tạo `0`, điều này sẽ tạo ra một mảng, khởi tạo phần tử đầu tiên bằng số 0 và nó sẽ tiếp tục khởi tạo các phần tử còn lại bằng 0.

```
    +-----+-----+-----+-----+-----+
  A |  0  |  0  |  0  |  0  |  0  |
    +-----+-----+-----+-----+-----+
       0     1     2     3     4
```

```c
int A[5] = {0};
```

---

## Truy cập các phần tử trong mảng

- Khởi tạo một mảng `A[5] = {2, 5, 4, 9, 8}` đã được khởi tạo với các phần tử. Vì vậy trong thời gian chạy, mảng sẽ được tạo như thế này và các phần tử sẽ được lưu trữ tại các vị trí này cùng với địa chỉ của chúng. Tôi có thể đề cập rằng các địa chỉ sẽ **liền kề nhau**.

```c
int A[5] = {2, 5, 4, 9, 8};
```

```
     20011 20013 20015 20017 20019
    +-----+-----+-----+-----+-----+
  A |  2  |  5  |  4  |  9  |  8  |
    +-----+-----+-----+-----+-----+
       0     1     2     3     4
```

> Mỗi `int` chiếm 2 byte nên địa chỉ các phần tử cách nhau 2.

- Bây giờ, làm sao để truy cập các phần tử đó?
  - **+)** Muốn in ra giá trị của bất kỳ phần tử nào thì sử dụng `tên_mảng[index của phần tử đó]`:

    ```c
    printf("%d", A[0]); // truy cập phần tử đầu tiên
    ```

  - **+)** Dùng biến để dễ dàng thay đổi:

    ```c
    printf("%d", A[i]);
    ```

- **Duyệt qua một mảng**, tức là duyệt qua từng phần tử mỗi lần. Vì vậy nếu tôi phải duyệt qua các phần tử, tôi sẽ sử dụng vòng lặp `for` chạy từ 0 đến 4:

```cpp
for (int i = 0; i < 5; i++) {
    printf("%d", A[i]); // Truy cập = Index
}
```

- Ngoài ra, có thể truy cập mảng `A[]` bằng **con trỏ** qua phép tính số học con trỏ để truy cập vào phần tử đó:

```cpp
printf("%d", *(A + 2)); // A[2] = 4

// Duyệt mảng
for (int i = 0; i < 5; i++) {
    printf("%d", *(A + i)); // Truy cập bằng con trỏ
}
```

=> Bản chất mảng là một tập hợp các ô nhớ liên tiếp, nó chỉ hoạt động như một con trỏ khi tham gia vào các biểu thức tính toán học hoặc khi truyền vào hàm, do cơ chế **Array Decay**.
