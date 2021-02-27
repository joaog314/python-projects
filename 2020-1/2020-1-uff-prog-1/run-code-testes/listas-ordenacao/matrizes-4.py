n = int(input())
list_key = []
list_rate = []
ordered = []

if n >= 1:

    for i in range(n):
        t = int(input())
        list_key.append(t)

    for i in range(n):
        t = float(input())
        list_rate.append(t)

    list_sorted = sorted(list_rate)

    indexes = []
    for i in range(n):
        #print(sorted_a[i])
        indexes.append(list_rate.index(list_sorted[i]))

    for i in indexes:
        ordered.append(list_key[i])

    print(ordered)