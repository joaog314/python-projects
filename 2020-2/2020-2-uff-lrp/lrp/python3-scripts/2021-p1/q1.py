r1 = list(map(int, input().split()))

r2 = list(map(int, input().split()))

# # r1 = [0,0,30,30]
# # r2 = [2,2,32,53]

# r1 = [0,0,30,30]
# r2 = [50,50,90,90]

p1 = r1[:2]
p2 = r1[2:4]
    
p3 = r2[:2]
p4 = r2[2:4]

#print(p1,p2,p3,p4)

xmin = min([p1[0],p2[0]])
ymin = min([p1[1],p2[1]])
xmax = max([p1[0],p2[0]])
ymax = max([p1[1],p2[1]])
#print(xmin,ymin,xmax,ymax)

x1min = min([p3[0],p4[0]])
y1min = min([p3[1],p4[1]])
x1max = max([p3[0],p4[0]])
y1max = max([p3[1],p4[1]])
#print(x1min,y1min,x1max,y1max)

if (xmax >= x1min) and (x1max >= xmin) and (ymax >= y1min) and (y1max >= ymin):
    print(1)
else:
    print(0)
