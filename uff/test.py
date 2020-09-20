word = 'SUBINOONIBUS'

letters = word.split() # separação de letras para criação de uma lista.

list_str = list(','.join(letters)) # criação de lista com as letras da palavra a ser avaliada.

n = len(list_str) # variável com o tamanho da palavra a ser iterada.

result = 0 # varíavel para avaliação de resultados das iterações.

p = 0 # contador de iterações com resultado verdadeiro.

# iteração para palíndrome pura.
for i in range(n//2):
    if (list_str[i] == list_str[n-i-1]) == True:
        p = p + 1
if p == n//2:
    result = result + 1

p = 0
# iteração para palíndrome quebrada.
for i in range(n//2):
    if (
            ((list_str[i] < list_str[i+1]) and (list_str[n-i-2] > list_str[n-i-1])) == True 
        
            or ((list_str[i] > list_str[i+1]) and (list_str[n-i-2] < list_str[n-i-1])) == True
        
            or ((list_str[i] == list_str[i+1]) and (list_str[n-i-2] == list_str[n-i-1])) == True
        ):
        p = p + 1

if p == n//2:
    result = result + 2

if result == 1: 
    print('palíndrome pura')
elif result == 2:
    print( 'palíndrome quebrada')
elif result == 3:
    print( 'palíndrome pura & quebrada')
else:
    print( 'não é uma palíndrome')

# BIT
# AAAEAEAEAAA
# SUBINOONIBUS
# TIPOERROTUDO
# ERAREHUMANO