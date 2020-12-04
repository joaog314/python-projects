import numpy as np

n = int(input())
m = int(input())

master_list = []

if 1 < m and 1 < n:
    
    all_values = []
    
    for i in range(n*m):
        t = int(input())
        all_values.append(t)

    # for k in range(m):
    #     for i in range(n):
    #         master_list[i][k] = max(stg_list)
    #         stg_list.remove(max(stg_list))

    for i in range(n):
        stg_list = []
        for k in range(m):
            stg_list.append(max(all_values))
            all_values.remove(max(all_values))
        master_list.append(stg_list)

    print(master_list)