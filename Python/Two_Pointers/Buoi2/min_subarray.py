from bisect import bisect_right

# Phuong phap tong tien to 
def min_subarray(arr, x) :
    # khoi tao chieu dai mang 
    n = len(arr)
    min_len = float('inf')
    # KHoi tao mang tien to 
    # voi kich thuoc n + 1 ptu
    prefix_sum = [0] * (n + 1)
    for i in range(1,n+1) : 
        # tinh tong tien to 
        prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

    # duyet qua mang 
    for i in range(n):
        # khoi tao bien tim kiem 
        # lam sao de bien tong tien to lon hon x 
        to_find = prefix_sum[i] + x
        # tim kiem ben phai mang prefix
        # neu co thi tra ve index
        bound = bisect_right(prefix_sum, to_find) 
        if bound <= n : 
            # tinh do dai nho nhat 
            min_len = min(min_len, bound - i) 
    # Neu khong tim thay mang con thoa man thi tra ve 0
    return min_len if min_len != float('inf') else 0

if __name__ == "__main__":
    print(min_subarray([1, 4, 45, 6, 0, 19], 51)) 
    print(min_subarray([1, 10, 5, 2, 7], 100))  