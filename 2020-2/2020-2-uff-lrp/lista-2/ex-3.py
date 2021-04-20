
n = int(input())
if (1 <= n <= 500000):
    opr = str(input())

    if '+' in opr:
        opr = list(map(int, opr.split('+')))
        if 0 <= opr[0] <= 1000 and 0 <= opr[1] <= 1000:
            if (opr[0]+opr[1]) <= n:
                print('OK')
            else:
                print('OVERFLOW')
    elif '*' in opr:
        opr = list(map(int, opr.split('*')))
        if 0 <= opr[0] <= 1000 and 0 <= opr[1] <= 1000:
            if (opr[0]*opr[1]) <= n:
                    print('OK')
            else:
                print('OVERFLOW')

    

