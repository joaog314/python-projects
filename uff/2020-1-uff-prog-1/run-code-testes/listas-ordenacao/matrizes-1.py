def bubbleSort(alist):
    c = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                c = c + 1
    return c

n = int(input())
master_list = []

if n >= 1:
    for i in range(n):
        stg_list = []
        for k in range(5):
            t = int(input())
            stg_list.append(t)
        master_list.append(stg_list)

for i in range(n):
    print(bubbleSort(master_list[i]))


