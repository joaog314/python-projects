# entr = list(map(int, input().split()))
# teste = list(map(int, range(min(entr),max(entr))))
entr = [2,12,8,2]
[y,z,v,w] = entr

# x = 1
for x in range(min(entr),max(entr)):
    
    if x%y == 0 and x%z != 0 and (v/x > 1 and v%x == 0) and (w%x != 0):
        print(x)
        break
    else:
        x += 1