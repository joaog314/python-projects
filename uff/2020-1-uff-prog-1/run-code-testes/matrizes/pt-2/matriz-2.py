n = int(input())
A_MATRIX = []
B_MATRIX = []
C_MATRIX = []

if 1 < n:
    for i in range(n):
        stg_list = []
        zeros_shape = []
        for k in range(n):
            t = int(input())
            stg_list.append(t)
            zeros_shape.append(0)
        A_MATRIX.append(stg_list)
        B_MATRIX.append(zeros_shape)
        C_MATRIX.append(zeros_shape)        

    for u in range(len(A_MATRIX)):
        for v in range(len(A_MATRIX[0])):
            C_MATRIX[v][u] = A_MATRIX[u][v]

    for i in range(len(A_MATRIX)):
        for j in range(len(A_MATRIX[0])):
            for k in range(len(A_MATRIX)):
                B_MATRIX[i][j] += A_MATRIX[i][k] * A_MATRIX[k][j]
          
    print(B_MATRIX)
