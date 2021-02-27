o1, o2, o3 = map(int, input().split())

if 1 <= o1 <= 1000 and 1 <= o2 <= 1000 and 1 <= o3 <= 1000 :
    if o1 == o2 or o1 == o3 or o2 == o3 or o1 == o2+o3 or o2 == o1+o3 or o3 == o1+o2:
        print("S")
    else:
        print("N")
else:
    print("N")