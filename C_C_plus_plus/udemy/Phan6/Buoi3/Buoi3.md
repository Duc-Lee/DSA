## Bài 3: Mảng Động và Mảng Tĩnh (Dynamic Array and Static Array)

- **Mảng tĩnh** có nghĩa là kích thước của mảng là tĩnh và **mảng động** có nghĩa là kích thước của mảng là động.
- Tuy nhiên, khi mảng được tạo ra, kích thước của nó không thể thay đổi.

Ví dụ tôi khai báo một hàm `void main` và bên trong hàm:

```c
void main() {
    int A[5];
}
```

- **VD:** Trong C++, tạo 1 biến `n` và `cin >> n`, tức là tôi đang đọc một giá trị đầu vào từ bàn phím, kích thước của mảng là `n`. Sau đó tôi có thể khai báo một mảng có kích thước `n`:

```cpp
void main() {
    int n;
    cin >> n;
    int B[n];
}
```

=> Bởi vì khai báo chấp nhận `n` nào thì kích thước của mảng luôn được quyết định khi chạy. Vì vậy mảng có kích thước đó sẽ được tạo ra bên trong ngăn xếp => **Kích thước của mảng được quyết định tại thời điểm chạy trong C++**.

- Nhưng trong C, nó phải được đề cập đến tại thời điểm biên dịch. Đây là sự khác biệt.

---

## Cách tạo mảng bên trong Heap

- Để quyết định kích thước của mảng vào lúc chạy.
- Để truy cập bất cứ thứ gì từ Heap, ta phải có một **con trỏ**. Vì vậy trước tiên ta phải khai báo con trỏ.
- **VD:** Khai báo con trỏ `p`:

```c
void main() {
    int *p; // con trỏ p
    int A[5];
}
```

- `A` là biến kiểu mảng nên `p` cũng là một biến. Vì vậy điều này cũng sẽ lấy được bộ nhớ bên trong **stack**.

```
┌──────────────────────────────────────────────────────────┐
│ STACK                                                    │
│                                                          │
│       A                                                  │
│    ┌─────┬─────┬─────┬─────┬─────┐      ┌─────┐          │
│    │     │     │     │     │     │      │  ?  │ p        │
│    └─────┴─────┴─────┴─────┴─────┘      └─────┘          │
│       0     1     2     3     4                          │
├──────────────────────────────────────────────────────────┤
│ CODE                                                     │
│    main()                                                │
│    ════════                                              │
│    ════════                                              │
└──────────────────────────────────────────────────────────┘
```

- Trong bất kỳ ngôn ngữ nào, khi khai báo một biến, bộ nhớ dành cho biến đó sẽ chỉ nằm trên **stack**.
- Khi nào nó sẽ được phân bổ trên **heap**?
  - Sử dụng con trỏ để tạo bộ nhớ trong heap, nên gán `p` = mảng số nguyên mới có kích thước là 5. Sau đó bộ nhớ sẽ được tạo bên trong heap và con trỏ `p` này sẽ chỉ đến địa chỉ đó.

```
┌──────────────────────────────────────────────────────────┐
│ HEAP                                                     │
│                                                          │
│      500   502   504   506   508                         │
│    ┌─────┬─────┬─────┬─────┬─────┐                       │
│    │     │     │     │     │     │  ◄── new int[5]       │
│    └─────┴─────┴─────┴─────┴─────┘                       │
│       0     1     2     3     4                          │
│       ▲                                                  │
│       │                                                  │
├───────┼──────────────────────────────────────────────────┤
│ STACK │                                                  │
│       └────────────────────────────────────┐             │
│                                            │             │
│       A                                    │             │
│    ┌─────┬─────┬─────┬─────┬─────┐      ┌──┴──┐          │
│    │     │     │     │     │     │      │ 500 │ p        │
│    └─────┴─────┴─────┴─────┴─────┘      └─────┘          │
│       0     1     2     3     4                          │
├──────────────────────────────────────────────────────────┤
│ CODE                                                     │
│    main()                                                │
│    ════════                                              │
│    ════════                                              │
└──────────────────────────────────────────────────────────┘
```

- Giả sử địa chỉ ô nhớ liền kề đầu tiên của mảng là `500` => `p` lấy địa chỉ `500`.

```cpp
void main() {
    int A[5];
    int *p;
    p = new int[5]; // Khởi tạo bộ nhớ heap bằng con trỏ p
}
```

- Vì vậy bây giờ chương trình có thể truy cập vào heap đó bằng cách đi đến con trỏ, lấy địa chỉ rồi đi đến đó và truy cập vào đó. Vì vậy, **bộ nhớ heap không thể truy cập trực tiếp, nó phải được truy cập gián tiếp**.
- Khi bạn lấy bộ nhớ từ heap: bất cứ khi nào sử dụng `new`, thì đó là dấu hiệu cho thấy bạn lấy bộ nhớ từ heap. Nếu không, tất cả các biến, bất kể bạn khai báo biến gì, chúng chỉ nhận được bộ nhớ bên trong ngăn xếp.

- `new` là một toán tử trong C++, vậy làm sao để làm tương tự trong C => Sử dụng hàm **`malloc`**:

```c
malloc(5 * sizeof(int));
```

=> Đây là cách phổ biến được thực hiện trong ngôn ngữ C. Thay vì đề cập đến 2 byte, chúng ta sẽ đề cập đến kích thước (`sizeof`), do đó tùy thuộc vào hệ thống hoặc trình biên dịch, nó sẽ lấy kích thước đó.

- Hàm `malloc` chỉ phân bổ **bộ nhớ thô**, tức là một khối bộ nhớ. Bây giờ ta muốn sử dụng bộ nhớ đó dưới dạng số nguyên, vì vậy ta phải **ép kiểu** nó thành con trỏ số nguyên:

```c
p = (int*) malloc(5 * sizeof(int));
```

- Vì vậy, mỗi lần mà:
  - Khi bạn khai báo một mảng thông thường thì nó sẽ được tạo bên trong **stack**.
  - Khi bạn muốn tạo mảng trong **heap**, thì ta phải có một con trỏ, sau đó cấp phát bộ nhớ bằng toán tử `new` hoặc hàm `malloc()`. Nó sẽ được tạo ở heap và heap sẽ được truy cập gián tiếp với sự trợ giúp của con trỏ.

- Khi chúng ta đã phân bổ bộ nhớ trong heap và sau một thời gian chương trình đã đến giai đoạn nào đó, nếu bộ nhớ đó không cần thiết nữa thì phải **xóa đi**. Nếu không xóa thì bộ nhớ không sử dụng sẽ gây ra vấn đề **rò rỉ bộ nhớ (memory leak)**.

```cpp
// Trong C++
delete []p;   // [] do p là mảng
```

```c
// Trong C
free(p);
```

---

## Cách truy cập mảng từ Heap

- Đây là một mảng bình thường bên trong ngăn xếp và có 1 mảng bên trong heap:

```cpp
int A[5];
int *p;
p = new int[5];
```

- Truy cập mảng bình thường, tức là `A[5]` trong ngăn xếp như thế nào?

```
┌──────────────────────────────────────────────────────────┐
│ STACK                                                    │
│                                                          │
│       A                                                  │
│    ┌─────┬─────┬─────┬─────┬─────┐      ┌─────┐          │
│    │     │     │     │     │     │      │  ?  │ p        │
│    └─────┴─────┴─────┴─────┴─────┘      └─────┘          │
│       0     1     2     3     4                          │
├──────────────────────────────────────────────────────────┤
│ CODE                                                     │
│    main()                                                │
│    ════════                                              │
└──────────────────────────────────────────────────────────┘
```

- Để truy cập bất kỳ vị trí nào, VD như gán `A[0] = 5`:

```c
int A[5];
A[0] = 5;
```

=> Giá trị 5 được lưu trữ ở `A[]` trong stack.

```
┌──────────────────────────────────────────────────────────┐
│ STACK                                                    │
│                                                          │
│       A                                                  │
│    ┌─────┬─────┬─────┬─────┬─────┐                       │
│    │  5  │     │     │     │     │  ◄── A[0] = 5         │
│    └─────┴─────┴─────┴─────┴─────┘                       │
│       0     1     2     3     4                          │
└──────────────────────────────────────────────────────────┘
```

=> Truy cập mảng `A[]` như bình thường, nó đơn giản như việc truy cập một mảng bên trong ngăn xếp (stack). Với heap: `p[0] = 5`.

- Truy cập mảng từ heap bằng **con trỏ (pointer)**:

```
┌──────────────────────────────────────────────────────────┐
│ HEAP                                                     │
│                                                          │
│      500   502   504   506   508                         │
│    ┌─────┬─────┬─────┬─────┬─────┐                       │
│    │  5  │     │     │     │     │  ◄── p[0] = 5         │
│    └─────┴─────┴─────┴─────┴─────┘                       │
│       0     1     2     3     4                          │
│       ▲                                                  │
│       │                                                  │
├───────┼──────────────────────────────────────────────────┤
│ STACK │                                                  │
│       └────────────────────────────────────┐             │
│                                            │             │
│       A                                    │             │
│    ┌─────┬─────┬─────┬─────┬─────┐      ┌──┴──┐          │
│    │  5  │     │     │     │     │      │ 500 │ p        │
│    └─────┴─────┴─────┴─────┴─────┘      └─────┘          │
│       0     1     2     3     4                          │
└──────────────────────────────────────────────────────────┘
```

=> Con trỏ đóng vai trò như tên một mảng, toàn bộ mảng vẫn có thể truy cập bằng vòng `for`, hoặc có thể truy cập bằng phép tính số học con trỏ (VD: `*(p + 1)`).

---

## Ví dụ

### Tạo mảng tĩnh trên ngăn xếp (stack)

`main.c`

```c
#include <stdio.h>

int main() {
    int A[5] = {2, 4, 6, 8, 10};

    // duyệt mảng trên stack
    for (int i = 0; i < 5; i++) {
        printf("%d", A[i]);
    }
}
```

`main.cpp` < tương tự >

### Tạo mảng động trên heap

`main.c`

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p;
    p = (int*) malloc(5 * sizeof(int));

    // Khởi tạo phần tử trong mảng
    p[0] = 3;
    p[1] = 5;
    p[2] = 7;
    p[3] = 9;
    p[4] = 11;

    // duyệt mảng trên heap
    for (int i = 0; i < 5; i++) {
        printf("%d", p[i]);
    }

    // giải phóng bộ nhớ heap sau khi dùng
    free(p);
}
```

`main.cpp`

```cpp
#include <iostream>
using namespace std;

int main() {
    // cấp phát động mảng
    int *p = new int[5];

    // Khởi tạo phần tử cho mảng
    p[0] = 1;
    p[1] = 3;
    p[2] = 5;
    p[3] = 7;
    p[4] = 9;

    for (int i = 0; i < 5; i++) {
        cout << p[i] << " ";
    }

    delete []p;
}
```
