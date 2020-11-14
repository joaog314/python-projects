Na = int(input())

Nb = int(input())

Nc = int(input())

d_ab = 1
d_ac = 2
d_bc = 1

cost = []

if (0 <= Na <= 10000) and (0 <= Nb <= 10000) and (0 <= Nb <= 10000):
    
    #Na
    cost.append(Nb*2*d_ab+Nc*2*d_ac)
    
    #Nb
    cost.append(Na*2*d_ab+Nc*2*d_bc)

    #Nc
    cost.append(Na*2*d_ac+Nb*2*d_bc)

print(min(cost))
