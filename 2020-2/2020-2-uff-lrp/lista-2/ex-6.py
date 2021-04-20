positions = []
positions_time = []

for k in range(3):
    
    positions.append(int(input()))

if 0 <= positions[0] <= 1000 and 0 <= positions[1] <= 1000 and 0 <= positions[2] <= 1000:
    # andar 1 
    positions_time.append(positions[1]+positions[2]*2)
    # andar 2
    positions_time.append(positions[0]+positions[2])
    # andar 3
    positions_time.append(positions[0]*2+positions[1])

    print(min(positions_time)*2)