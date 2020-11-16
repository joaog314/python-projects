n = int(input())
A = []

# A list
for i in range(n):
    p = int(input())
    A.append(p)

B = sorted(A)

if A == B:
    print('sim')
else:
    print('não')