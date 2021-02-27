#Sortudo

l1 = list(map(int, input().split()))

N = l1[0] 
T = l1[1]

if T <= 1000 and 1 <= N:
    
    l2 = list(map(int, input().split()))
    
    total = [0]*N
    
    c = 0
    while c < len(l2):
     for i in range(T):
         for k in range(N):
            total[k] = total[k] + l2[c]
            c = c + 1 

max_value_list = []
for i in range(len(total)):
    if total[i] == max(total):
       max_value_list.append(i)

print(max(max_value_list)+1) 
