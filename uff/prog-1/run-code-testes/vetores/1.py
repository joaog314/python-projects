numbers = []
position = []

for i in range(11):
    n = int(input())
    if i == 10:
        l = n
    else:
        numbers.append(n)

for i in range(10):
    if numbers[i] == l:
        position.append(i)

print(position)
