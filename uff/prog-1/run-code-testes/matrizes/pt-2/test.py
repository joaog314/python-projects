A_MATRIX = [[6, 4, 2, 3], [7, 7, 4, 10], [5, 6, 5, 6], [4, 2, 9, 5]]
r = len(A_MATRIX)
master_list = []


for i in range (r//2):
    for j in range(r):
        if i < j < (r - i - 1):
            print(A_MATRIX[i][j])

for k in range (r-1,i,-1):

    for j in range(r-1,0,-1):
        #print((r - i - 1))
        print('k =', k, 'j =', j, '(r - k - 1) = ', (r + k - 1))
        if k > j > (r - k - 1):
            print(A_MATRIX[k][j])
