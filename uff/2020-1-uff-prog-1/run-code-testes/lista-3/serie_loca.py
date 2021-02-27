a = 3 
b = 7
n = int(input())
s = n 
for i in range(1,100,1):
    if i % 2 > 0:
        s = s + n*(a/b)
        a = a + 5
        b = b + 2     
    else: 
        s = s - n*(a/b)
        a = a + 5
        b = b + 2

print("%.3f" % s)