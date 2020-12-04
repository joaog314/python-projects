n = int(input())
m = int(input())
master_list = []
# master_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
all_values = []

if 1 < m and 1 < n:
    for i in range(n):
        stg_list = []
        for k in range(m):
            t = int(input())
            stg_list.append(t)
            all_values.append(t)
        master_list.append(stg_list)

    for i in range(n):
        for k in range(m):
            master_list[i][k] = master_list[i][k] - max(all_values)
print(master_list)
