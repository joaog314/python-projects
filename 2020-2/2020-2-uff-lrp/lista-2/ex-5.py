n =  int(input())

test_list = []

q = 0

for i in range(n):

    entr = list(map(int, input().split()))
    if 0 <= entr[0] <= 100 and 0 <= entr[1] <= 100:
        test_list.append(entr)

for tests in test_list:
    if tests[0] > tests[1]:
        q += tests[1]

# if l > c:
#     q += l - c
print(q)