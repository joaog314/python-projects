n = int(input())

p1 = str(input())
p2 = str(input())

result = []

while n != 0:

    for i in range(n):
        l1 = list(map(int, input().split()))
        result.append(sum(l1))

    for r in result:
        if r % 2 == 0 : print(p1)
        else: print(p2)
    
    n = int(input())