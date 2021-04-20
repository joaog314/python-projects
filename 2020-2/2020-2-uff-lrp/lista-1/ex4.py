entr = list(map(int, input().split()))
# entr = [ 1, 2, 3, 5, 6]

if len(entr) == 5:
    asc = sorted(entr, reverse=False)
    desc = sorted(entr, reverse=True)
        
    if entr==asc:
        print('C')
    elif entr==desc:
        print('D') 
    else:
        print('N') 