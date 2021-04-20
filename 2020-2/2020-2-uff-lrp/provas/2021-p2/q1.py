[n,c,m] = list(map(int, input().split()))

# if (1 <= n <= 100) and (1 <= c <= n/2) and (1 <= m <= 300):

nowner = 0

esp_coll = list(map(int, input().split()))
own_coll = list(map(int, input().split()))
# print(len(esp_coll),c,len(own_coll),  m)
    
unique_coll = []

for book in own_coll:
    if 1 <= book and book not in unique_coll:
        unique_coll.append(book)

# print(unique_coll)

for bk in unique_coll:
    # print(bk,nowner)
    if 1 <= bk and bk in esp_coll and bk <= n:
        nowner += 1

print(c-nowner)


