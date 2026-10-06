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