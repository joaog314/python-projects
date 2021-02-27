N = 0
t = 1
while N != -1:
    N = int(input())
    N_out = (2**N + 1)**2       
    if N != -1 and 0 <= N <= 20:
        print("Teste",t)
        print(N_out)
        print('')
        t = t + 1