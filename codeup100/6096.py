arrX = []

for x in range(19) :
    arrX.append(input().split(sep = " "))
for x in range(19) : 
    for y in range(19) :
        arrX[x][y] = int(arrX[x][y])

casenum = int(input())

corX = [ 0 for i in range(casenum)]
corY = [ 0 for i in range(casenum)]

for x in range(casenum) :
    a,b = input().split(sep=" ")
    corX[x] = int(a)-1
    corY[x] = int(b)-1

for x in range(casenum) :
    for y in range(19) : 
        if arrX[y][corY[x]] == 0 :
            arrX[y][corY[x]] = 1
        else :
            arrX[y][corY[x]] = 0
    for y in range(19) :
        if arrX[corX[x]][y] == 0 :
            arrX[corX[x]][y] = 1
        else :
            arrX[corX[x]][y] = 0

for x in range(19) :
    for y in range(19) :
        print(arrX[x][y],end=" ")
    print("")
