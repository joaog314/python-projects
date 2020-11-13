
for i in range(2):
    
    numbers_verify = False
    while numbers_verify != True:
        numbers = list(map(int, input('numbers').split()))
        print(0 <= numbers[0] <= 5, 0 <= numbers[1] <= 5)
        if (0 <= numbers[0] <= 5) and (0 <= numbers[1] <= 5):
            numbers_verify = True