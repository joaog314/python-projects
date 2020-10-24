x = int(input())
y = int(input())
anos = 0

while x < y and x >= 2:
    x = x*1.5
    y = y*1.3
    anos = anos + 1 

print(anos)