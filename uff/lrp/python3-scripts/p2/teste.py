l1 = list(map(int, input().split()))

N = l1[0] 
L = l1[1]


l = [200,200,200]

p = [50,0,350]
f = []
for i in range(3):
    f.append(p[i]+l[i])

sort_p = []
sort_l = []
sort_f = []
for i in range(3):
    sort_p.append(min(p))
    sort_l.append(l[(p.index(min(p)))])
    sort_f.append(f[(p.index(min(p)))])
    p.remove(min(p))
    l.remove(sort_l[i])
    f.remove(sort_f[i])
print(sort_p, sort_l,sort_f)

stg = []
for i in range(3):
    if i < 2:
        if sort_p[i+1] < sort_f[i]:
            p.append(sort_p[i])
            f.append(sort_f[i+1])
            sort_p.remove(sort_p[i+1])
            sort_p.append(0)
        else:
            p.append(sort_p[i])
            f.append(sort_f[i])
    if i == 2:
        if sort_p[i] > sort_f[i-1]:
            p.append(sort_p[i])
            f.append(sort_f[i])

print(600 - size)
size = 0

for i in range(len(p)):
    size = size + f[i] - p[i]

print(600 - size)

