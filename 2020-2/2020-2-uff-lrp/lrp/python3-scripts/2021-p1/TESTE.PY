direction = 'EXEC 1'
list_test = [2,3,4,5]
if 'EXEC' in direction: 
    list_test.append(list_test[int(direction[5]) - 1])
    print(list_test)


    # l1 = list(map(int, input().split()))

# print(l1)