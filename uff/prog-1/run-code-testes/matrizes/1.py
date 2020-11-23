def bubbleSort(nlist):
    c = 0
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    c = c+1
    return c


n = int(input())

list_final = []

if n >= 1:
    for k in range(n):
        list_stg = []
        for l in range(5):
            list_stg.append(int(input())) 
        list_final.append(list_stg)    
 

nlist = list_final[1]
print(bubbleSort(nlist))