values = list(map(int, input().split()))

def diag(h,w):
    c = ((h**2) + (w**2))**(1/2)
    return c

n_checker = 0

for n in values:
    if 0 <= n <= 1000:
        n_checker += 1
    
if n_checker == 4: 

    diag_1 = diag(values[0],values[1])

    diag_2 = diag(values[0],values[2])

    diag_3 = diag(values[2],values[1])

    if (diag_1/2 <= values[3]) and (diag_2/2 <= values[3]) and (diag_3/2 <= values[3]):
        print('S')
    else:
        print('N')    

