numbers = []
mean_dif = []
for i in range(5):
    n = float(input())
    if n >= 0:
        numbers.append(n)

mean = sum(numbers)/5 
mean_dif[:] = [abs((number - mean)) for number in numbers]
result = numbers[mean_dif.index(min(mean_dif))]

print("%.2f" % result)