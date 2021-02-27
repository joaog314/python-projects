n = int(input())
A_MATRIX = []
master_list = []


if 2 < n:
    for i in range(n):
        stg_list = []
        for k in range(n):
            t = int(input())
            stg_list.append(t)
        A_MATRIX.append(stg_list)
    
    r = len(A_MATRIX)


    for i in range (r//2):
        for j in range(r):
            if i < j < (r - i - 1):
                #print(A_MATRIX[i][j])
                master_list.append(A_MATRIX[i][j])

    for k in range (r-1,i,-1):
        for j in range(r-1,0,-1):
            if k > j > (r - k - 1):
                #print(A_MATRIX[k][j])
                master_list.append(A_MATRIX[k][j])
    
    mean = float(sum(master_list)/len(master_list))
    print("%.2f" % mean)