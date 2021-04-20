def numbers(n):
    return (2**n + 1)**2

entr = None
i = 1
test_list = []
while entr!=-1:

    entr = int(input())
    if -1 < entr <= 15:
        test_list.append(entr)

for n in test_list:
    print('Teste '+str(i))
    print(numbers(n))
    print('')
    i += 1