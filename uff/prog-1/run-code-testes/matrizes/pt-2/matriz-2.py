import numpy as np

n = int(input())
master_list = []

if 1 < n:
    for i in range(n):
        stg_list = []
        for k in range(n):
            t = int(input())
            stg_list.append(t)
        master_list.append(stg_list)

    for i in range(n):
        for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r) 