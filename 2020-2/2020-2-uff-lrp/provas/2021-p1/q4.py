entr = list(map(int, input().split()))

values = list(map(int, input().split()))

if (1 <= entr[0] <= 1000)  and (1 <= entr[1] <= 100):

    count = 0
    # print(values[i:i+2])
    while values != [entr[1]]*len(values):
        for i in range(len(values)):
            while values[i] != entr[1]:
                if values[i] > entr[1]:
                    values[i:i+2] = [n - 1 for n in values[i:i+2]]
                    count += 1
                elif values[i] < entr[1]:
                    values[i:i+2] = [n + 1 for n in values[i:i+2]] 
                    count += 1
    print(count)