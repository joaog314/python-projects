test_list = []
n = None

while n != 0:
    n = int(input())
    if n !=0:
        test_list.append(n)

c = 1
for value in test_list:
    cedules = [0]*4
    while 0 < value <= 10000: 
        if value//50 > 0: 
            cedules[0] += value//50
            value=value%50
        elif value//10 > 0: 
            cedules[1] += value//10
            value=value%10
        elif value//5 > 0: 
            cedules[2] += value//5
            value=value%5
        elif value//1 > 0: 
            cedules[3] += value//1
            value=value%1
        
    print('Teste '+str(c))
    print(*cedules)
    print('')
    c+=1