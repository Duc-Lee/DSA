# Bài toán cấp độ Trung bình

## Bài 1: Triplet Sum in Array - Tìm bộ ba có tổng bằng Target

Cho một mảng số nguyên `arr[]` và một số nguyên `target`. Hãy xác định xem có tồn tại **một bộ ba** phần tử trong mảng có tổng bằng `target` hay không.

- Nếu tồn tại: Trả về `true`.
- Nếu không tồn tại: Trả về `false`.

---

### Ví dụ minh họa:

- **Ví dụ 1:**
  - **Đầu vào (Input):** `arr = [1, 4, 45, 6, 10, 8]`, `target = 13`
  - **Đầu ra (Output):** `true`
  - **Giải thích:** Bộ ba `[1, 4, 8]` có tổng $1 + 4 + 8 = 13$.

- **Ví dụ 2:**
  - **Đầu vào (Input):** `arr = [1, 2, 4, 3, 6, 7]`, `target = 10`
  - **Đầu ra (Output):** `true`
  - **Giải thích:** Hai bộ ba `[1, 3, 6]` và `[1, 2, 7]` đều có tổng bằng 10.

- **Ví dụ 3:**
  - **Đầu vào (Input):** `arr = [40, 20, 10, 3, 6, 7]`, `target = 24`
  - **Đầu ra (Output):** `false`
  - **Giải thích:** Không có bộ ba nào trong mảng có tổng bằng 24.

### Cách 1 : Tạo ra tất cả các bộ ba - Thời gian O($n^3$) và Không gian O(1)

Ý tưởng là tạo ra tất cả các bộ ba có thể có bằng **ba vòng lặp lồng nhau** và so sánh tổng của mỗi bộ ba với `target`.
- Nếu tổng bằng `target` → trả về `true`.
- Nếu duyệt hết mà không tìm thấy → trả về `false`.

```python 
def tripleSum(arr, target) : 
    n = len(arr) 
    for i in range(n-2) : 
        for j in range(i+1,n-1) : 
            for k in range(j+1,n) : 
                if( arr[i] + arr[j] + arr[k]) == target : 
                    return True
    return False

if __name__ == "__main__" : 
    print(tripleSum([1, 4, 45, 6, 10, 8], 13)) 
    print(tripleSum([1, 2, 4, 3, 6, 7], 10))  
    print(tripleSum([40, 20, 10, 3, 6, 7], 24))  
```

### Cách 2 : Tập hợp băm - Thời gian O($n^2$) và Không gian O(n)

Phương pháp từng bước:

- Lặp qua mảng, cố định phần tử đầu tiên (arr [i] ) cho bộ ba.
- Đối với mỗi arr [i] , hãy sử dụng một Hash Set để lưu trữ các phần tử thứ hai tiềm năng và chạy một vòng lặp khác bên trong đó cho j từ i+1 đến n-1.
- Bên trong một vòng lặp lồng nhau, hãy kiểm tra xem tổng đã cho - arr[i] - arr[j] có tồn tại trong tập băm hay không. Nếu có, thì in bộ ba đó ra.
- Nếu không tìm thấy bộ ba nào trong toàn bộ mảng, hàm sẽ trả về false.

```python 
def tripleSum(arr, target) : 
    n = len(arr) 
    for i in range(n-1) :
        # khoi tao set rong  
        st = set() 
        # duyet qua mang lan nua 
        for j in range(i+1,n) :
            # khoi tao bien arr[k]
            second = target - arr[i] - arr[j]
            # tim kiem xem phan tu nay co trong bam khong
            # arr[j] la tham so thay doi lien tuc
            if second in st : 
                return True 
            # khong thi add vo set 
            st.add(arr[j]) 
    # neu sau khong co j tuc la false 
    return False 

if __name__ == "__main__" : 
    print(tripleSum([1, 4, 45, 6, 10, 8], 13)) 
    print(tripleSum([1, 2, 4, 3, 6, 7], 10))  
    print(tripleSum([40, 20, 10, 3, 6, 7], 24))  
```

### Cách 3  : Sắp xếp và hai con trỏ - Thời gian O($n^2$) và Không gian O(1)

Chúng ta hãy cùng hiểu qua ví dụ này:
arr[] = [1, 4, 45, 6, 10, 8], target = 13

- Sắp xếp mảng: arr = [1, 4, 6, 8, 10, 45].
- Đặt i = 0, cố định phần tử đầu tiên là 1, sao cho tổng của hai phần tử còn lại phải bằng 12.
- Khởi tạo l = 1 (4) và r = 5 (45).
- 4 + 45 = 49, lớn hơn 12, nên dịch r sang trái để giảm tổng.
- 4 + 10 = 14, vẫn lớn hơn 12, vậy nên dịch chuyển r sang trái một lần nữa.
- 4 + 8 = 12, trùng với tổng cần tìm.
Bộ ba (1, 4, 8) cộng lại bằng 13, vì vậy hàm trả về true.

```python 
def tripleSum(arr, target) : 
    n = len(arr)
    # sap xep mang  
    arr.sort() 
    for i in range(n-1) : 
        # i la con tro dau mang 
        # no chay sau
        # khoi tao bien tro 2 dau mang 
        l , r = i+1, n - 1 
        # bh tim tong arr[l] + arr[r] == second
        second = target - arr[i]
        while(l < r) :
            if arr[l] + arr[r] == second : 
                return True 
            elif arr[l] + arr[r] < second : 
                l += 1 
            elif arr[l] + arr[r] > second : 
                r -= 1
    return False 

if __name__ == "__main__" : 
    print(tripleSum([1, 4, 45, 6, 10, 8], 13)) 
    print(tripleSum([1, 2, 4, 3, 6, 7], 10))  
    print(tripleSum([40, 20, 10, 3, 6, 7], 24))  
```

## Bài 2 :  Vấn đề của người nổi tiếng

# Vấn đề người nổi tiếng

Cho ma trận vuông `mat[][]` có kích thước `n x n`, trong đó `mat[i][j] == 1` nghĩa là người `i` biết người `j`, và `mat[i][j] == 0` nghĩa là người `i` không biết người `j`. Hãy tìm **người nổi tiếng**.

**Định nghĩa người nổi tiếng**:

- Ai cũng biết người này.
- Người này không biết người khác (ngoại trừ chính bản thân).

Trả về chỉ số của người nổi tiếng nếu tồn tại, nếu không trả về `-1`.

> Lưu ý: Đảm bảo rằng `mat[i][i] == 1` cho tất cả `i`.

### Ví dụ minh họa

```python
# Ví dụ 1
mat = [[1, 1, 0],
       [0, 1, 0],
       [0, 1, 1]]
# Đầu ra: 1
# Giải thích: Người 0 và 2 đều biết người 1 → người 1 là người nổi tiếng.
```

```python
# Ví dụ 2
mat = [[1, 1],
       [1, 1]]
# Đầu ra: -1
# Giải thích: Hai người đều biết nhau, không có người nổi tiếng.
```

```python
# Ví dụ 3 (trường hợp không hợp lệ)
mat = []  # hoặc cấu trúc sai
# Đầu ra: 0
```

### Cách 1 : Sử dụng danh sách kề - Thời gian O(n² ) và không gian O(n)

Hướng dẫn thực hiện từng bước:

Tạo hai mảng `indegree` và `outdegree` để lưu trữ bậc vào và bậc ra.
Chạy một vòng lặp lồng nhau, vòng lặp ngoài từ 0 đến n và vòng lặp trong từ 0 đến n.
Với mỗi cặp i, j, hãy kiểm tra xem i có quen biết j hay không, sau đó tăng bậc ra của i và bậc vào của j.
Với mỗi cặp i, j, hãy kiểm tra xem j có quen biết i hay không, sau đó tăng bậc ra của j và bậc vào của i.
Chạy một vòng lặp từ 0 đến n và tìm ID mà tại đó bậc vào là n và bậc ra là 1.

```python 
def celebrity(mat): 
    n = len(mat) 
    # khoi tao 2 mang luu tru bac vao va bac ra
    # indegree[i] la so nguoi biet i 
    indegree = [0] * n
    # outdegree[i] la so nguoi i biet 
    outdegree = [0] * n
    # Chỉ cộng khi mat[i][j] == 1
    for i in range(n): 
        for j in range(n): 
            if mat[i][j] == 1:
                outdegree[i] += 1 
                indegree[j] += 1           
    # Vi dụ mat = [[1,1,0], [0,1,0], [0,1,1]]:
    # outdegree = [2, 1, 2]
    # indegree  = [1, 3, 1]
    # nguoi 1 biet it nguoi nhat (1) va duoc nhieu nguoi biet nhat (3)
    for i in range(n): 
        # Nguoi i biet it nguoi nhat (outdegree == 1) 
        # va duoc nhieu nguoi biet nhat (indegree == n)
        if outdegree[i] == 1 and indegree[i] == n: 
            return i          
    return -1 

if __name__ == "__main__": 
    mat = [
        [1, 1, 0], 
        [0, 1, 0], 
        [0, 1, 1]
    ]
    print(celebrity(mat))  
```