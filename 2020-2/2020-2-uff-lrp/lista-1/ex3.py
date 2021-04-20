entr = list(map(float, input().split()))
xm = entr[0]
ym = entr[1]
xr = entr[2]
yr = entr[3]
if 0 <= xm <= 1000 and 0 <= ym <= 1000 and 0 <= xr <= 1000 and 0 <= yr <= 1000:
    print(int(abs(xr-xm)+abs(yr-ym)))