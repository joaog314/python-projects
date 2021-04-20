test = str(input()) 
word = str(input())
# test = 'iohmunlcaywgdfbqpvxzerwsyt'
key_cr = []
# word = 'lvimeihib'
for chars in test:
    key_cr.append(chars)

test_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# word = 'lvimeihib'
desc = ['']
for w in word:
    desc[0] += test_list[key_cr.index(w)]
print(*desc)