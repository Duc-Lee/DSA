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
