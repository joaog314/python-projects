def palind_ver(word):

    # separação de letras para criação de uma lista.
    letters = word.split()
    # criação de lista com as letras da palavra a ser avaliada.
    list_str = list(','.join(letters))
    # variável com o tamanho da palavra a ser iterada.
    n = len(list_str)

    # contador de iterações com resultado verdadeiro.
    p = 0

    # iteração para palíndrome pura.
    for i in range(n//2):
        if (list_str[i] == list_str[n-i-1]) is True:
            p = p + 1
    if p == n//2:
        return('palíndrome pura')

    p = 0
    # iteração para palíndrome quebrada.
    for i in range(n//2):
        if (
                (
                    (list_str[i] < list_str[i+1])
                    and (list_str[n-i-2] > list_str[n-i-1])
                ) is True

                or
                (
                    (list_str[i] > list_str[i+1])
                    and (list_str[n-i-2] < list_str[n-i-1])
                ) is True

                or
                (
                    (list_str[i] == list_str[i+1])
                    and (list_str[n-i-2] == list_str[n-i-1])
                ) is True
           ):
            p = p + 1

    if p == n//2:
        return('palíndrome quebrada')
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

# Qual das seguintes cadeias é palíndrome quebrada:
# (A) AAAEAEAEAAA
# (B) AZULMARINHO
# (C) NAOMARQUEAQUI
# (D) PROGRAMAR
# (E) FIM

# 2. Considere as seguintes cadeias:
# (i) BIT
# (ii) AAAEAEAEAAA
# (iii) SUBINOONIBUS
# (iv) TIPOERROTUDO
# (v) ERAREHUMANO
# Qual das seguintes afirmações é correta?
# (A) (i) e (ii) são palíndromes puras.
# (B) (iv) e (v) são palíndromes quebradas
# (C) (ii) não é palíndrome pura.
# (D) (iii) é palíndrome pura e (iv) é palíndrome quebrada.
# (E) (v) é palíndrome quebrada