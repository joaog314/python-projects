# Números
# Escreva um programa que permita que o usuário indique um número de inteiros N a serem
# lidos (os N números fornecidos estão entre 0 e 100, pode acreditar). Após a leitura dos N
# números, escreva na tela a média, a soma, o produto, o menor valor e o maior valor. Utilizar
# laços contáveis.
# ENTRADA: número N (inteiro), seguido por N números (inteiros) entre 0 e 100 (pode acreditar)
# SAIDA: 5 números (real, inteiro, inteiro, inteiro e inteiro), um por linha, representando a média ,
# a soma, o produto, o menor valor e o maior valor. O número real terá duas casas decimais
import numpy as np

numbers_list = []
k = int(input())

for i in range(k):
    n = int(input())
    if 0 <= n <= 100:
        numbers_list.append(n)    

print("%.2f" % (sum(numbers_list)/len(numbers_list)))
print(sum(numbers_list))
print(np.prod(numbers_list))
print(min(numbers_list))
print(max(numbers_list))