# test_list = [5, 5, 12, 5, 10, 10, 10, 10, 10, 10, 5, 5, 5]
# test_list = [1]
t = int(input())
test_list = list(map(int, input().split()))

unique_values = []
values_frequency = []

for n in test_list:
    if n not in unique_values:
        unique_values.append(n)
        check_list = []
        for i in range(t):
            if n == test_list[i]:
                check_list.append(i)
        values_frequency.append(check_list)
# print(unique_values, values_frequency)

mf = []
for freq in values_frequency:
    v = 1
    for l in range(len(freq)-1):      
        if freq[l+1] - freq[l] == 1:
            v += 1
    mf.append(v)

print(max(mf))
