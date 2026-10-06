# Kỹ thuật hai con trỏ (Two Pointers Technique)

## 1. Giới thiệu tổng quan

**Kỹ thuật hai con trỏ (Two Pointers Technique)** là một chiến lược giải thuật đơn giản nhưng vô cùng mạnh mẽ. Trong kỹ thuật này, ta sử dụng hai chỉ số (hoặc con trỏ) để duyệt qua một cấu trúc dữ liệu tuyến tính (như mảng, danh sách hoặc chuỗi) theo:
- **Hướng ngược chiều nhau (Opposite Direction):** Một con trỏ bắt đầu từ đầu ($left = 0$), một con trỏ bắt đầu từ cuối ($right = n - 1$) và di chuyển dần lại gần nhau.
- **Cùng hướng (Same Direction / Fast & Slow Pointers):** Hai con trỏ cùng xuất phát và di chuyển về cùng một phía với tốc độ hoặc điều kiện khác nhau (kỹ thuật Rùa và Thỏ, Cửa sổ trượt).

Kỹ thuật này giúp tối ưu hóa độ phức tạp thời gian từ $O(n^2)$ (vét cạn bằng 2 vòng lặp lồng nhau) xuống còn **$O(n)$**.

### Các bài toán kinh điển áp dụng:
- **Two Sum (mảng đã sắp xếp):** Tìm hai phần tử có tổng bằng giá trị mục tiêu.
- **3Sum / 4Sum:** Tìm bộ ba, bộ bốn phần tử có tổng thỏa mãn điều kiện.
- **Tổng hai phần tử gần nhất (Closest Pair).**
- **Trapping Rain Water (Bẫy nước mưa).**
- **Kiểm tra chuỗi đối xứng (Palindrome), đảo ngược mảng/chuỗi.**

---

## 2. Khi nào nên sử dụng kỹ thuật hai con trỏ?

- **Dữ liệu đầu vào đã được sắp xếp (Sorted Array/List):**  
  Nếu mảng hoặc danh sách đã sắp xếp (hoặc có thể sắp xếp trước trong $O(n \log n)$), hai con trỏ có thể tìm các cặp hoặc phạm vi một cách tối ưu trong $O(n)$.  
  *Ví dụ:* Tìm hai số trong mảng đã sắp xếp có tổng bằng số mục tiêu (`target`).

- **Bài toán xử lý cặp phần tử hoặc mảng con (Pairs / Subarrays):**  
  Khi bài toán yêu cầu làm việc với hai đầu của một mảng hoặc một phạm vi thay vì các phần tử đơn lẻ.  
  *Ví dụ:* Kiểm tra xem một chuỗi có phải là chuỗi đối xứng (palindrome) hay không, dồn các số 0 về cuối mảng.

- **Bài toán cửa sổ trượt (Sliding Window):**  
  Khi cần duy trì một "cửa sổ" các phần tử có thể mở rộng hoặc thu hẹp dựa trên điều kiện bài toán.  
  *Ví dụ:* Tìm mảng con ngắn nhất có tổng $\ge K$, chuỗi con dài nhất không có ký tự lặp lại.

- **Danh sách liên kết (Con trỏ chậm - nhanh / Floyd's Cycle Detection):**  
  Sử dụng hai con trỏ di chuyển với tốc độ khác nhau để phát hiện chu trình (vòng lặp), tìm điểm giữa của danh sách liên kết.

---

## 3. Bài toán minh họa: Tổng của cặp số bằng giá trị mục tiêu (Two Sum)

### Đề bài
Cho một mảng số nguyên `arr` đã được **sắp xếp theo thứ tự tăng dần** và một giá trị `target`. Hãy xác định xem có tồn tại cặp phần tử `(arr[i], arr[j])` (với $i \ne j$) sao cho:
$$\text{arr}[i] + \text{arr}[j] = \text{target}$$

### Ví dụ minh họa (Test cases)

- **Ví dụ 1:**
  - **Đầu vào (Input):** `arr = [10, 20, 35, 50]`, `target = 70`
  - **Đầu ra (Output):** `true`
  - **Giải thích:** Tồn tại cặp `(20, 50)` có tổng: $20 + 50 = 70$.

- **Ví dụ 2:**
  - **Đầu vào (Input):** `arr = [10, 20, 30]`, `target = 70`
  - **Đầu ra (Output):** `false`
  - **Giải thích:** Không tồn tại cặp số nào có tổng bằng $70$.

- **Ví dụ 3:**
  - **Đầu vào (Input):** `arr = [-8, 1, 4, 6, 10, 45]`, `target = 16`
  - **Đầu ra (Output):** `true`
  - **Giải thích:** Tồn tại cặp `(6, 10)` có tổng: $6 + 10 = 16$.

---

### Phương pháp đơn giản - Thời gian O($n^2$) và Không gian O(1)

- Cách tiếp cận cơ bản nhất là tạo ra tất cả các cặp có thể và kiểm tra xem có cặp nào cộng lại bằng giá trị mục tiêu hay không. Để tạo ra tất cả các cặp, chúng ta chỉ cần chạy hai vòng lặp lồng nhau.

```python 
# Khoi tao ham tinh 
def two_pointers(arr, target):
    #  duyet qua 2 vong lap 
    # dong thoi kiem tra arr[i] + arr[j] == target?
    for i in range(len(arr)):
        # duyet tu i + 1
        for j in range(i+1,len(arr)):
            if(arr[i] + arr[j] == target): 
                # dung thi tra ve True
                return True
    # Sai thi false 
    return False 

if __name__ == "__main__" : 
    # khoi tao array va khoa target
    arr = [10,20,30,40]
    target = 70
    # IN ra ket qua
    print(two_pointers(arr,target))
```

### Ý tưởng giải thuật bằng Hai con trỏ:
1. Đặt `left = 0` (đầu mảng) và `right = len(arr) - 1` (cuối mảng).
2. Lặp lại khi `left < right`:
   - Tính `current_sum = arr[left] + arr[right]`.
   - Nếu `current_sum == target`: Tìm thấy cặp số $\to$ Trả về `true`.
   - Nếu `current_sum < target`: Tổng đang nhỏ hơn mục tiêu, cần tăng tổng lên bằng cách tăng con trỏ trái: `left += 1`.
   - Nếu `current_sum > target`: Tổng đang lớn hơn mục tiêu, cần giảm tổng xuống bằng cách giảm con trỏ phải: `right -= 1`.
3. Nếu hết vòng lặp mà không tìm thấy $\to$ Trả về `false`.

```python
# Tinh voi O(n)
def sum_pointers(arr, target):
    # khoi tao con tro dau 
    left = 0
    # khoi tao con tro cuoi 
    right = len(arr)-1
    while(left < right):
        # tinh tong hien tai 
        sum_curr = arr[left] + arr[right]
        # neu dang bang nhau tra ve True
        if(sum_curr == target):
            return True
        # Neu tong dang lon hon thi giam right di 
        # de giam tong xuong
        elif(sum_curr > target):
            right -= 1
        elif(sum_curr < target):
            left += 1
    # neu khong co ket qua nao duoc tim thay 
    return False 

if __name__ == "__main__" : 
    # khoi tao array va khoa target
    arr = [10,20,35,50]
    target = 70
    # IN ra ket qua
    print(sum_pointers(arr,target))
```