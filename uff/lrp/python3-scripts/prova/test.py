t = [4, 6, 6]
max_value_list = []
for i in range(len(t)):
    if t[i] == max(t):
       max_value_list.append(i)

print(max(max_value_list)) 