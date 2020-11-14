numbers = []
position = []

for i in range(10):
    n = int(input())
    if n >= 0:
        numbers.append(n)

for i in range(10):
    l = numbers[i] // 5
    position.append(l)

print(position)