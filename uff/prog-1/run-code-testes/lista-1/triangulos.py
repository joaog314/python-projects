x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())

a = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
b = ((x3 - x2)**2 + (y3 - y2)**2)**(1/2)
c = ((x1 - x3)**2 + (y1 - y3)**2)**(1/2)

if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
    print('inexistente')
else: 
    if a == b == c:
        print("equilátero")
    elif a==b or b==c or c==a:
        print("isósceles")
    else:
        print("escaleno")
     
