[y,z,v,w] = list(map(int, input().split()))
# entr = [2,12,8,2]
# [y,z,v,w] = entr

q = 0
numbers = list(range(min([y,z,v,w]),max([y,z,v,w])+1))
# print(numbers)
for x in numbers:
    
    if x%y == 0 and x%z != 0 and (v/x > 1 and v%x == 0) and (w%x != 0):
        q = x
        print(x)
        break
        
if q == 0:
    print(-1)
