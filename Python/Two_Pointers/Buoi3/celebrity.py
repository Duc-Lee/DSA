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
    # In ra để bạn thấy giá trị thực tế:
    # Với mat = [[1,1,0], [0,1,0], [0,1,1]]:
    # outdegree = [2, 1, 2]
    # indegree  = [1, 3, 1]
    for i in range(n): 
        # Người i chỉ biết bản thân (out == 1) và được cả n người biết (in == n)
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