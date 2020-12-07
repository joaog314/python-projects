l1 = list(map(int, input().split()))
print(l1)

N = l1[0] 
T = l1[1]

if T <= 1000 and 1 <= N:
    
    l2 = list(map(int, input().split()))
    
    total = [0]*N



l = [200,100,200]

p = [50,0,350]
f = []
for i in range(3):
    f.append(p[i]+l[i])

print(f)