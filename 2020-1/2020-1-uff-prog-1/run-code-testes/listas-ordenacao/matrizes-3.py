n = int(input())
list_odd = []
list_even = []

if n >= 1:
    for i in range(n):
        t = int(input())
        if t % 2 > 0:
            list_odd.append(t)
        else: 
            list_even.append(t)

list_odd.sort(reverse=True)
list_even.sort()

print(list_even + list_odd)
