n = int(input())
master_list = []

mean = 0
sum_num = 0
count = 0 

if 1 < n:
    for i in range(n):
        stg_list = []
        for k in range(n):
            t = int(input())
            stg_list.append(t)
        master_list.append(stg_list)


    for i in range(n):
        for k in range(n):
             if i < k:
                sum_num = sum_num + master_list[i][k]

    for i in range(n):
        for k in range(n):
                mean = mean + master_list[i][k]
    
    mean = float(mean)/n**2
    
    for i in range(n):
        for k in range(n):
            if master_list[i][k] < mean:
                count = count + 1

print(sum_num)
print(count)
