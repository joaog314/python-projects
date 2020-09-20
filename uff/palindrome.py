def palind_ver(word):
    letters = entry.split()
    list_str = list(','.join(letters))
    n = len(list_str) 
    p = 0

    for i in range(n//2):
        if (list_str[i] == list_str[n-i-1]) == True:
            p = p + 1
    if p == n//2:
        return('palíndrome pura')

    for i in range(n//2):
        if (list_str[i] < list_str[n-i-1]) == True:
            p = p + 1
    if p == n//2:
        return('palíndrome quebrada')
    else:
        return('não é palíndrome')

start = 1
while start == 1:
    word = str(input('Digite uma palavra, ou s para sair: ')).upper()
    if word == 'S':
        start = 0
    elif len(word) >= 3:
        print(palind_ver(word))
    else:
        print('palavra curta demais')
