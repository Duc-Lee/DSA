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