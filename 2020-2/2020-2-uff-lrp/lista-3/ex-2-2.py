a,v = None,None

airpt_res = []

while [a,v] != [0,0]:
    
    [a,v] = list(map(int, input().split()))
    
    if 0 < a <= 100 and 0 < v <= 10000:
        airpt_rank = [0]*a
        for i in range(v):
            [x,y] = list(map(int, input().split()))
            if 1 <= x <= a and 1 <= y <= a and x != y:
                for n in [x,y]:
                   airpt_rank[n-1] += 1 
        airpt_res.append(airpt_rank)

# print(airpt_res)
k = 1 
for test_group in airpt_res:
    
    list_rank = []
    for i in range(len(test_group)):
        if test_group[i] == max(test_group):
            list_rank.append(i+1)
            i += 1
    
    print('Teste '+str(k))
    print(*list_rank,'')
    print('')
    k += 1
