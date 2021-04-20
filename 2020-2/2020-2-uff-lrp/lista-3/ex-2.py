a,v = -1, -1
airports_fls = []
airpts_n = []

while a != 0 and v != 0:

    entr1 = list(map(int, input().split()))
    
    a,v = entr1[0], entr1[1]
    airpts_n.append(a)

    if a != 0 and v != 0:
        test_fl = []
        for i in range(v):
            fls = list(map(int, input().split()))
            if fls[0] != fls[1] and 1<= fls[0] <= a and 1<= fls[1] <= a:
                for n in fls:
                    test_fl.append(n)
        airports_fls.append(test_fl)

t = 0

for test_group in airports_fls:
    
    l = airpts_n[t]
    check_airpts = [0]*l
    airpts_rank = []

    for i in range(l):
        check_airpts[i] += airports_fls[t].count(i+1)

    for k in range(l):
        if check_airpts[k] == max(check_airpts):
            airpts_rank.append(k+1) 
    
    print('Teste '+str(t+1))
    print(*sorted(airpts_rank))
    print('')
    t += 1