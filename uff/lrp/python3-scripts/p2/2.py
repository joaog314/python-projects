l, n = map(int, input().split())

placas = [[0 for x in range(2)] for y in range(n)] 

for i in range(n):
    inicio, largura = map(int, input().split())
    placas[i][0] = inicio
    placas[i][1] = largura