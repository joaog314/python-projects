n = int(input())
m = int(input())

master_list = []

if 1 < n and 1 < m:

    for i in range(n):
        stg_list = []
        for k in range(m):
            t = int(input())
            stg_list.append(t)
        master_list.append(stg_list)

    min_list = []
    for k in range(m):
        stg_list = []
        for i in range(n):
            stg_list.append(abs(master_list[i][k]))
        min_list.append(min(stg_list))

    for k in range(m):
        for i in range(n):
            master_list[i][k] = master_list[i][k] + min_list[k]

    print(master_list)