n = int(input())
if 1 <= n <= 500: 

    for k in range(n):
            
        c = int(input())
        if 1 <= n <= 200:
            
            cmd_list = [] 

            for i in range(c):
                direction = str(input())
                if direction == 'ESQ':
                    cmd_list.append(-1)
                elif direction == 'DIR':
                    cmd_list.append(1)
                elif 'EXEC' in direction:
                    cmd_list.append(cmd_list[int(direction[5]) - 1])
            print(sum(cmd_list))
        
