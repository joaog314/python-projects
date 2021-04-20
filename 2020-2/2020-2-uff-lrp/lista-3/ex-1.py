n = int(input())
words_output = []

for i in range(n):  

    entr = str(input())
    l1 = list(map(str, entr.split(' ')))
    word = str()
    for words in l1: 
        if words not in '% %':
            # print(words)
            word = word+words[0]
    words_output.append(word)

for words_2 in words_output:
    print(words_2)