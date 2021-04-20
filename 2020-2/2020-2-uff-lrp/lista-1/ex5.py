c = int(input())
l = int(input())

if 1 <= c <= 1000 and 1 <= l <= 1000:

    teste_out = []
    for k in range(c):
        teste_list = [0]*l
        for i in range(l):      
            if k%2== 0 and i%2 == 0:
                teste_list[i] = 1
            elif k%2!= 0 and i%2 != 0:
                teste_list[i] = 1
        teste_out.append(teste_list)

    print(teste_out[c-1][l-1])

