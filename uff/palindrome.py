def palind_ver(word):

    letters = word.split() # separação de letras para criação de uma lista.

    list_str = list(','.join(letters)) # criação de lista com as letras da palavra a ser avaliada.

    n = len(list_str) # variável com o tamanho da palavra a ser iterada.

    p = 0 # contador de iterações com resultado verdadeiro.

    # iteração para palíndrome pura.
    for i in range(n//2):
        if (list_str[i] == list_str[n-i-1]) == True:
            p = p + 1
    if p == n//2:
        return('palíndrome pura')

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
        return( 'palíndrome quebrada')
    else:
        return('não é uma palíndrome')

start = 1
while start == 1:
    word = str(input('Digite uma palavra, ou s para sair: ')).upper()
    if word == 'S':
        print('fim do programa...')
        start = 0
    elif len(word) >= 3:
        print(palind_ver(word))
    else:
        print('palavra curta demais')

# AAAEAEAEAAA
# SUBINOONIBUS