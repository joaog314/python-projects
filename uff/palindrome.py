# Verificação de palíndromes puras e quebradas

# Uma cadeia de caracteres é chamada de palíndrome pura se a sequência de caracteres da esquerda
# para a direita é igual à sequência de caracteres da direita para a esquerda (uma outra definição é
# que o primeiro caractere da cadeia deve ser igual ao último caractere, o segundo caractere seja
# igual ao penúltimo caractere, o terceiro caractere seja igual ao antepenúltimo caractere, e assim
# por diante). Por exemplo, as cadeias de caracteres ‘MIM’, ‘AXXA’ e ‘ANANAGANANA’ são
# palíndromes puras.

# Uma outra definição de palíndrome utiliza comparações entre caracteres, considerando que os
# caracteres são ordenados crescentemente de A até Z, ou seja, A < B < C < ... < Z. Uma cadeia de
# caracteres é chamada de palíndrome quebrada se a sequência de resultados da comparação entre o
# primeiro e o segundo caracteres é igual ao resultado da comparação entre o último e o penúltimo
# caractere, e o resultado da comparação entre o segundo e o terceiro caracteres é igual ao resultado
# da comparação entre o penúltimo e o antepenúltimo caracteres, e assim por diante. Por exemplo,
# as cadeias ‘MIN’ e ‘ASSOCFUUS’ são palíndromes quebradas. Obviamente, toda cadeia que é
# palíndrome pura é também palíndrome quebrada.

# Função para verificação de palíndromes.
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


# Qual das seguintes cadeias é palíndrome quebrada:
# (A) TODOS R: palíndrome quebrada
# (B) AZULMARINHO R: não é uma palíndrome
# (C) NAOMARQUEAQUI R: não é uma palíndrome
# (D) PROGRAMAR R: não é uma palíndrome
# (E) FIM R: não é uma palíndrome

# 2. Considere as seguintes cadeias:
# (i) BIT R: não é uma palíndrome
# (ii) AAAEAEAEAAA R: palíndrome pura
# (iii) SUBINOONIBUS R: palíndrome pura
# (iv) TIPOERROTUDO R: palíndrome quebrada
# (v) ERAREHUMANO não é uma palíndrome

# Qual das seguintes afirmações é correta?
# (A) (i) e (ii) são palíndromes puras. F
# (B) (iv) e (v) são palíndromes quebradas F
# (C) (ii) não é palíndrome pura. F
# (D) (iii) é palíndrome pura e (iv) é palíndrome quebrada. V
# (E) (v) é palíndrome quebrada F