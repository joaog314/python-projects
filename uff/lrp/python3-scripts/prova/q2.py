def verify_func(list_input,n_iter):
    c = 0
    for i in range(n_iter):  
        if 1 <= list_input[i] <= 1000:
            c = c + 1
    if 1 < n_iter <= 3 and c == n_iter:
        return True 
    else:
        return False

list_input = list(map(int, input().split()))

n_iter = len(list_input)

road = 0

if verify_func(list_input,n_iter) == True:
    for k in range(n_iter):
        if k % 2 == 0:
            road = road + list_input[k]
        else:
            road = road - list_input[k]
    if road == 1: 
        print('S')  
    else:
        print('N') 
else:
    print('N')  




