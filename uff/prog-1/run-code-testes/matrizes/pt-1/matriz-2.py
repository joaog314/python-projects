n = int(input())
master_list = []
# master_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def list_reverse(rev_list): 
    new_rev_list = rev_list[::-1] 
    return new_rev_list 

if 1 < n:
    for i in range(n):
        stg_list = []
        for k in range(n):
            t = int(input())
            stg_list.append(t)
        master_list.append(stg_list)

    for i in range(n):
            for k in range(n):
                if i == k:
                    temp = master_list[i][k]
                    master_list[i][k] = master_list[i][n-k-1]
                    master_list[i][n-k-1] = temp
    
    rev_list = master_list[0]
    master_list[0] = list_reverse(rev_list)

    print(master_list)



