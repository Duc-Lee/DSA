# Bài toán cấp độ dễ 

## Bài 1: Two Sum II - Tìm cặp số có tổng bằng Target trong mảng đã sắp xếp

Cho một mảng số nguyên `arr[]` đã được sắp xếp theo thứ tự không giảm (tăng dần) với **chỉ số bắt đầu từ 1 (1-based index)** và một số nguyên `target`. 

Hãy tìm hai phần tử trong mảng sao cho tổng của chúng bằng `target`.
- Nếu tồn tại: Trả về chỉ số của hai phần tử đó theo thứ tự tăng dần `[index1, index2]` (với $1 \le \text{index1} < \text{index2} \le n$).
- Nếu không tồn tại: Trả về `[-1, -1]`.

---

### Ví dụ minh họa:

- **Ví dụ 1:**
  - **Đầu vào (Input):** `arr = [2, 7, 11, 15]`, `target = 9`
  - **Đầu ra (Output):** `[1, 2]`
  - **Giải thích:** Vì mảng được đánh số từ 1, nên $\text{arr}[1] + \text{arr}[2] = 2 + 7 = 9$.

- **Ví dụ 2:**
  - **Đầu vào (Input):** `arr = [1, 3, 4, 6, 8, 11]`, `target = 10`
  - **Đầu ra (Output):** `[3, 4]`
  - **Giải thích:** Vì mảng được đánh số từ 1, nên $\text{arr}[3] + \text{arr}[4] = 4 + 6 = 10$.

- **Ví dụ 3:**
  - **Đầu vào (Input):** `arr = [1, 2, 3, 5]`, `target = 10`
  - **Đầu ra (Output):** `[-1, -1]`
  - **Giải thích:** Không có cặp số nào trong mảng có tổng bằng 10.

### Cách 1 : Thử tất cả các cặp - Thời gian O($n^2$) và Không gian O(1)

Ý tưởng là kiểm tra mọi cặp phần tử có thể có bằng cách sử dụng hai vòng lặp lồng nhau. Nếu bất kỳ cặp nào cộng lại bằng giá trị mục tiêu, chúng ta sẽ trả về chỉ số bắt đầu từ 1 của chúng ngay lập tức.

```python 
# khoi tao tao ham duyet 2 lan 
def two_sum(arr, target):
    # duyet 2 lan 
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            # neu tong bang target ban dau 
            # tra ve index 2 so do trong arr
            if(arr[i] + arr[j] == target) : 
                return [i+1,j+1]
    # Neu khong tim thay thi tra [-1,-1]
    return [-1,-1]

print(two_sum([2, 7, 11, 15], 9))  
print(two_sum([1, 3, 4, 6, 8, 11], 10))  
print(two_sum([1, 2, 3, 5], 10))  
```

### Cách 2 : Sử dụng hai con trỏ - Thời gian O(n) và Không gian O(1)
- Bài toán có thể được giải quyết bằng kỹ thuật hai con trỏ . Ta có thể duy trì hai con trỏ, left = 0 và right = n - 1, và tính tổng của chúng S = arr[left] + arr[right].
    - Nếu S = mục tiêu, thì trả về bên trái và bên phải.
    - Nếu S < mục tiêu, thì ta cần tăng tổng S, vì vậy ta sẽ tăng left = left + 1.
    - Nếu S > mục tiêu, thì ta cần giảm tổng S, vì vậy ta sẽ giảm right = right - 1.
- Nếu tại bất kỳ điểm nào, bên trái >= bên phải, thì không tìm thấy cặp nào có tổng bằng mục tiêu.

```python
# Tinh tong bang 2 con tro 
def two_sum(arr, target):
    # khoi tao con tro dau mang 
    left = 0
    # khoi tao con tro cuoi mang 
    right = len(arr) - 1
    while(left < right ) : 
        # khoi tao bien tinh tong hien tai 
        sum_curr = arr[left] + arr[right]
        # kiem tra dieu kien 
        if(sum_curr == target) : 
            return [left + 1, right + 1]
        # neu khong thi kiem tra xem 
        # neu tong lon hon 
        elif(sum_curr > target) : 
            right -= 1
        elif(sum_curr < target) :
            left += 1

    return [-1,-1]

if __name__ == "__main__" :
    print(two_sum([2, 7, 11, 15], 9))  
    print(two_sum([1, 3, 4, 6, 8, 11], 10))  
    print(two_sum([1, 2, 3, 5], 10)) 
```

## Bài 2: Mảng con nhỏ nhất có tổng lớn hơn một giá trị cho trước

Cho một mảng số nguyên `arr[]` và một số nguyên `x`, nhiệm vụ là tìm độ dài của mảng con nhỏ nhất có tổng lớn hơn `x`.
- Nếu tồn tại: Trả về độ dài của mảng con nhỏ nhất có tổng lớn hơn `x`.
- Nếu không tồn tại: Trả về `0`.

---

### Ví dụ minh họa:

- **Ví dụ 1:**
  - **Đầu vào (Input):** `arr = [1, 4, 45, 6, 0, 19]`, `x = 51`
  - **Đầu ra (Output):** `3`
  - **Giải thích:** Mảng con có độ dài nhỏ nhất là `[4, 45, 6]` (tổng là $4 + 45 + 6 = 55 > 51$).

- **Ví dụ 2:**
  - **Đầu vào (Input):** `arr = [1, 10, 5, 2, 7]`, `x = 100`
  - **Đầu ra (Output):** `0`
  - **Giải thích:** Không tồn tại mảng con nào có tổng lớn hơn 100.

### Cách 1 : Sử dụng hai vòng lặp lồng nhau - Thời gian O($n^2$) và Không gian O(1)

Ý tưởng là sử dụng hai vòng lặp lồng nhau:
- Vòng lặp ngoài chọn một phần tử bắt đầu.
- Vòng lặp trong duyệt qua tất cả các phần tử (ở phía bên phải của phần tử bắt đầu hiện tại) làm phần tử kết thúc.
- Bất cứ khi nào tổng các phần tử giữa phần tử bắt đầu và kết thúc hiện tại lớn hơn `x`, hãy cập nhật kết quả nếu độ dài hiện tại nhỏ hơn độ dài nhỏ nhất đã tìm thấy cho đến nay.

```python 
def min_subarray(arr, x):
    n = len(arr)
    # Khoi tao min_len bang mot gia tri lon hon do dai mang
    min_len = n + 1
    
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            # Kiem tra dieu kien tong lon hon x
            if curr_sum > x:
                min_len = min(min_len, j - i + 1)
                break
                
    # Neu khong tim thay mang con nao thoa man thi tra ve 0
    return min_len if min_len <= n else 0

if __name__ == "__main__":
    print(min_subarray([1, 4, 45, 6, 0, 19], 51))  # Output: 3
    print(min_subarray([1, 10, 5, 2, 7], 100))     # Output: 0
```

### Cách 2 : Tổng tiền tố và tìm kiếm nhị phân - Thời gian O($n \log n$) và Không gian O($n$)

- **Ý tưởng:** Lưu trữ tổng tiền tố vào một mảng `preSum[]`. Vì các phần tử là số nguyên dương nên mảng tiền tố có thứ tự tăng dần (đã sắp xếp). Với mỗi chỉ số `i`, ta thực hiện **tìm kiếm nhị phân** trong phạm vi `[i + 1, n]` để tìm chỉ số `j` nhỏ nhất sao cho:
  $$\text{preSum}[j] > \text{preSum}[i] + x$$

- **Các bước thực hiện chi tiết:**
  1. **Tính tổng tiền tố:** Xây dựng mảng `preSum[]` với kích thước $n + 1$ (với `preSum[0] = 0`), trong đó `preSum[k]` lưu tổng của $k$ phần tử đầu tiên.
  2. **Tìm kiếm nhị phân:** Duyệt qua từng chỉ số `i` và tìm chỉ số `j` đầu tiên trong `preSum[]` sao cho $\text{preSum}[j] > \text{preSum}[i] + x$ (sử dụng tìm kiếm nhị phân / hàm `bisect_right`).
  3. **Cập nhật kết quả:** 
     - Nếu tìm thấy chỉ số `j` thỏa mãn, độ dài mảng con tương ứng là $j - i$.
     - Cập nhật `min_len = min(min_len, j - i)`.
  4. **Trả về kết quả:** Nếu tìm thấy ít nhất một mảng con thỏa mãn thì trả về `min_len`, ngược lại trả về `0`.

```python 
from bisect import bisect_right

def min_subarray(arr, x): 
    n = len(arr) 
    # Khoi tao bien do dai min 
    min_len = float('inf')
    
    # Khoi tao mang prefix_sum[] co kich thuoc n + 1
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        # Tong tien to
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
        
    # Duyet qua cac vi tri bat dau cua mang con (chi so tu 0 den n - 1)
    for i in range(n):
        # Tim gia tri prefix_sum can vuot qua (vi yeu cau tong > x)
        to_find = prefix_sum[i] + x
        # Index c
        bound = bisect_right(prefix_sum, to_find)
        
        # Neu tim thay vi tri hop le trong mang prefix_sum
        # bound - i la 
        if bound <= n:
            min_len = min(min_len, bound - i)
            
    # Neu khong tim thay mang con thoa man thi tra ve 0
    return min_len if min_len != float('inf') else 0

if __name__ == "__main__":
    print(min_subarray([1, 4, 45, 6, 0, 19], 51)) 
    print(min_subarray([1, 10, 5, 2, 7], 100))    
```

### Cách 3 :  Sử dụng cửa sổ trượt - Thời gian O(n) và không gian O(1)

## Bài 3: Loại bỏ các phần tử trùng lặp khỏi mảng đã sắp xếp

Cho một mảng đã được sắp xếp `arr[]` có kích thước $n$, mục tiêu là sắp xếp lại mảng sao cho tất cả các phần tử khác nhau (phân biệt) xuất hiện ở đầu theo thứ tự đã sắp xếp. Ngoài ra, hãy trả về độ dài của mảng con gồm các phần tử khác nhau này.

> **Lưu ý:** Các phần tử sau các phần tử phân biệt có thể xuất hiện theo bất kỳ thứ tự nào và mang bất kỳ giá trị nào, vì chúng không ảnh hưởng đến kết quả.

---

### Ví dụ minh họa:

- **Ví dụ 1:**
  - **Đầu vào (Input):** `arr = [2, 2, 2, 2, 2]`
  - **Đầu ra (Output):** `[2]`
  - **Giải thích:** Tất cả các phần tử đều là 2, vì vậy chỉ giữ lại một lần xuất hiện của số 2.

- **Ví dụ 2:**
  - **Đầu vào (Input):** `arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]`
  - **Đầu ra (Output):** `[1, 2, 3, 4, 5]`
  - **Giải thích:** Loại bỏ các phần tử trùng lặp, chỉ giữ lại các phần tử duy nhất theo thứ tự tăng dần.

- **Ví dụ 3:**
  - **Đầu vào (Input):** `arr = [1, 2, 3]`
  - **Đầu ra (Output):** `[1, 2, 3]`
  - **Giải thích:** Không có thay đổi vì tất cả các phần tử đều đã khác nhau.

### Cách 1 : Tập hợp đã sắp xếp - Cũng hoạt động với tập hợp chưa sắp xếp - Thời gian O(n) và không gian O(n)

Duyệt qua mảng đã được sắp xếp và chèn từng phần tử vào một tập hợp.
Tập hợp không cho phép các giá trị trùng lặp, do đó các phần tử lặp lại sẽ tự động bị loại bỏ.
Cuối cùng, chuyển tập hợp đó thành mảng/danh sách và trả về.

```python 
from typing import List 

def removeDuplicate(arr : List[int]) -> List : 
    # chuyen het vè set 
    st = set(arr)
    # tra ve danh sach da duoc sap xep 
    # luu y nho ep lai kieu list 
    return list(st) 

if __name__ == "__main__" : 
    print(removeDuplicate([1, 1, 2, 2, 3, 3])) 
    print(removeDuplicate([1, 2, 2, 3, 4, 4, 4, 5, 5]))
    print(removeDuplicate([1, 2, 3]))
```

### Cách 3 : Duyệt một lần - Thời gian O(n) và Không gian O(1)
Vì mảng đã được sắp xếp, nên tất cả các lần xuất hiện của một phần tử sẽ liên tiếp nhau.

Chúng ta chủ yếu cần kiểm tra xem phần tử hiện tại có giống với phần tử trước đó hay không.

Thực hiện từng bước:

- Lặp qua mảng với i từ 0 đến n-1. Tại mỗi chỉ số i, nếu arr[i]khác với arr[i-1], hãy cộng nó vào kết quả.
- Sau vòng lặp, kết quả chứa phần tử duy nhất.

```python 
from typing import List 

def removeDuplicate(arr : List[int]) -> List : 
    n = len(arr)
    # khoi tao mang con 
    result = []
    # cho phan tu dau tien vao truoc 
    result.append(arr[0]) 
    for i in range(1,n) : 
        if(arr[i] == arr[i-1]) :
            # nhay qua phan tu trung lap 
            continue
        else : 
            result.append(arr[i])
    return result 

if __name__ == "__main__" :
    print(removeDuplicate([1, 1, 2, 2, 3, 3])) 
    print(removeDuplicate([1, 2, 2, 3, 4, 4, 4, 5, 5]))
    print(removeDuplicate([1, 2, 3]))
```

## Bài 4: Câu đối xứng

Cho một chuỗi câu `s`, hãy xác định xem nó có phải là câu đối xứng hay không. Một câu được coi là đối xứng nếu chuỗi ký tự đọc xuôi và đọc ngược hoàn toàn giống nhau sau khi:
- Chuyển đổi tất cả các chữ cái viết hoa thành chữ cái viết thường.
- Loại bỏ tất cả các ký tự không phải chữ cái hoặc chữ số (tức là bỏ qua khoảng trắng, dấu chấm câu và ký hiệu).

---

### Ví dụ minh họa:

- **Ví dụ 1:**
  - **Đầu vào (Input):** `s = "Too hot to hoot."`
  - **Đầu ra (Output):** `true`
  - **Giải thích:** Nếu ta loại bỏ tất cả các ký tự không phải chữ cái hoặc số và chuyển tất cả các chữ cái viết hoa thành chữ cái viết thường, chuỗi `s` sẽ trở thành `"toohottohoot"`, đây là một chuỗi đối xứng.

- **Ví dụ 2:**
  - **Đầu vào (Input):** `s = "Abc 012..## 10cbA"`
  - **Đầu ra (Output):** `true`
  - **Giải thích:** Nếu ta loại bỏ tất cả các ký tự không phải chữ cái hoặc số và chuyển tất cả các chữ cái viết hoa thành chữ cái viết thường, chuỗi `s` sẽ trở thành `"abc01210cba"`, đây là một chuỗi đối xứng.

- **Ví dụ 3:**
  - **Đầu vào (Input):** `s = "ABC $. def01ASDF.."`
  - **Đầu ra (Output):** `false`
  - **Giải thích:** Nếu ta loại bỏ tất cả các ký tự không phải chữ cái hoặc số và chuyển tất cả các chữ cái viết hoa thành chữ cái viết thường, chuỗi `s` sẽ trở thành `"abcdef01asdf"`, đây không phải là một chuỗi đối xứng.

### Cách 1 : Chuẩn hóa và kiểm tra ngược - Thời gian O(n) và Không gian O(n)

Ý tưởng là xử lý trước câu đã cho bằng cách lọc bỏ tất cả các ký tự không phải chữ cái hoặc số và chuyển đổi tất cả các chữ cái viết hoa thành chữ cái viết thường. Điều này đảm bảo rằng phép so sánh không bị ảnh hưởng bởi khoảng trắng, dấu chấm câu hoặc kiểu chữ. Sau khi chuỗi được chuẩn hóa, chúng ta chỉ cần so sánh nó với chuỗi đảo ngược của nó. Nếu cả hai giống hệt nhau, câu đó là một câu đối xứng; ngược lại, nó không phải là câu đối xứng.

```python 
def isPalinset(s)  : 
    # khoi tao mang con 
    s1 = []
    for ch in s : 
        # neu la so hoac chu 
        if ch.isalnum() : 
            # them phan tu ay vo 
            s1.append[ch]
    # chuyen list lai thanh string 
    s1 = " ".join(s1)
    # gan ham nguoc 
    rev = s1[::-1]
    return s1 == rev

if __name__ == "__main__" :
    print(isPalinset("A man, a plan, a canal: Panama"))  
    print(isPalinset("race a car"))  
    print(isPalinset(" "))  
```

### Cách 2 : Hai con trỏ - Thời gian O(n) và không gian O(1)

Ý tưởng là sử dụng phương pháp hai con trỏ để kiểm tra xem một câu có phải là câu đối xứng hay không. Chúng ta đặt một con trỏ ở đầu và con trỏ kia ở cuối chuỗi, di chuyển chúng lại gần nhau trong khi so sánh các ký tự. 
Chúng ta bỏ qua bất kỳ ký tự nào không phải là chữ cái hoặc số và chuyển đổi chữ cái viết hoa thành chữ cái viết thường để đảm bảo so sánh không phân biệt chữ hoa chữ thường. Nếu các ký tự tại cả hai con trỏ không khớp, chúng ta trả về false. Nếu các con trỏ giao nhau mà không có sự không khớp, câu đó là câu đối xứng.

```python 
def isPalinset(s) : 
    left  = 0 
    right = len(s) -1 
    while (left < right ) : 
        # kiem tra phan tu dau tien neu la chu or so
        # tang bien left len neu khong phai 
        # neu no la ki tu dac biet
        if not s[left].isalnum() : 
            left += 1
        # tiep tuc kiem tra ca phan tu ben right
        # neu no la ki tu dac biet thi giam right 
        elif not s[right].isalnum() : 
            right -= 1
        # kiem tra xem 2 phan bang nhau khong
        # xem co doi xung khong 
        elif s[left].lower() == s[right].lower() :
            left += 1
            right -= 1
        # neu tat ca cac truong hop deu khong xay ra
        # tuc la mang bat doi xung
        else : 
            return False
    return True

if __name__ == "__main__" :
    print(isPalinset("A man, a plan, a canal: Panama")) 
    print(isPalinset("race a car")) 
    print(isPalinset("abdce sae")) 
```