import numpy as np

n = int(input())
list_numbers = []

if n >= 1:
    for i in range(n):
        t = int(input())
        list_numbers.append(t)

print(sorted(np.unique(list_numbers)))