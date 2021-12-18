numarr = [ 0 for i in range(9) ]

for x in range(9) :
    numarr[x] = int(input())

max = max(numarr)
for y in range(9) :
    if numarr[y] == max :
        where = y + 1

print(max)
print(where)
