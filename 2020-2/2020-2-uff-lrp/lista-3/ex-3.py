test = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
# entr = [22,5,22]
# entr = [31, 110, 79]
# entr = [45, 8, 7]
entr = list(map(int, input().split()))
tests_lists = []
for opt in test:
    i = 0 
    sub_list = []
    for k in opt:
        sub_list.append(k*entr[i])
        i += 1
    tests_lists.append(sum(sub_list))

for h in tests_lists:
    if h in entr or h == 0:
        v = 'S'
        break
    else:
        v = 'N'
# print(tests_lists)
print(v)