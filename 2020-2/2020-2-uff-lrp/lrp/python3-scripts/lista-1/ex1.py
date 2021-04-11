
def min_cel(n):
    s = [0]*4
    while n != 0:
        if(n//50) > 0:
            s[0] += (n//50)
            n = n%50
        elif(n//10) > 0:
            s[1] += (n//10)
            n = n%10
        elif(n//5) > 0:
            s[2] += (n//5)
            n = n%5
        elif(n//1) > 0:
            s[3] += (n//1)
            n = n%1
    return print(*s)

entr = -1
test = []

while entr != 0:
    
    entr = int(input())
    if  0 < entr <= 10000:
        test.append(entr)

if len(test) > 0:
    for amount in test:
        min_cel(amount)