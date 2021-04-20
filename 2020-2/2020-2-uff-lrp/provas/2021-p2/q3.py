# entr = list(map(int, input().split()))
entr = [2,12,8,2]
[y,z,v,w] = entr

test = list(range(1, 10**9))

if 1 < y < 10**9 and 1 < z < 10**9 and 1 < v < 10**9 and 1 < w < 10**9:
    s = None
    for n in test:
        # print(i)
        if (n%y == 0) and (n%z != 0) and (v%n == 0) and (w%n != 0):
            print(n)
            s = n 
            break 
    if s == None:
        print(-1)
            


