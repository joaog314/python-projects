n = int(input())
m = int(input())
master_list = []
all_values = []

if 1 < m and 1 < n:
    for i in range(n):
        stg_list = []
        for k in range(m):
            t = int(input())
            stg_list.append(t)
            all_values.append(t)
        master_list.append(stg_list)

    for k in range(m):
        for i in range(n):
            master_list[i][k] = max(all_values)
            all_values.remove(max(all_values))

    print(master_list)
    