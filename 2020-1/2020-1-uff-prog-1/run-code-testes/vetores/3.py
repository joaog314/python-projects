import math

n = int(input())
A = []
B = []

# A list
for i in range(n):
    p = int(input())
    A.append(p)
A.reverse()

# B list
for i in range(n):
    if A[i] < 0:
        B.append(A[i])
    else:
        B.append(math.factorial(A[i]))

print(B)