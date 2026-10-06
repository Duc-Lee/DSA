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