n =  int(input())

if 0 <= n <= 100:
    
    if n == 0:
        print('E')
    elif 1 <= n <= 35:
        print('D')
    elif 36 <= n <= 60:
        print('C')
    elif 61 <= n <= 85:
        print('B')
    elif 86 <= n <= 100:
        print('A')