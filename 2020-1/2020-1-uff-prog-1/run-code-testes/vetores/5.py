n = int(input())
m = int(input())

A = []
B = []
C = []

if 1 <= n <= m:
    while len(A) < n:
        a = int(input())
        A.append(a)   
    
    while len(B) < m:
        b = int(input())
        B.append(b)
    

    i = 0
    while len(C) < m + n:
        if i < n:
            C.append(A[i])
        C.append(B[i])
        i = i + 1 

    print(C)