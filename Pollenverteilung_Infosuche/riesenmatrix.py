from copy import deepcopy

latWien = 10000
lonWien = 15000

xrMatrix =1000
yrMatrix = 1000
rMatrix = []
baumMatrix = [[1,2,3],[1,2,3],[55,6,5]]
xBaum = 3
yBaum = 4

def matrixErstellen():
    for x in range(xrMatrix):
        einzel = []
        for y in range(yrMatrix):
            einzel.append(0)
        rMatrix.append(einzel)
    return rMatrix



def matrixplus(xBaum, yBaum, matrixBaum, rMatrix):
    startx = xBaum - int((len(matrixBaum) / 2 - 0.5))
    starty = yBaum - int((len(matrixBaum) / 2 - 0.5))
    xKopie = deepcopy(startx)

    for x in range(len(matrixBaum)):
        for y in range(len(matrixBaum)):
            rMatrix[startx][starty] += matrixBaum[x][y]
            startx += 1
        startx = xKopie
        starty += 1
    return rMatrix

matrix = matrixErstellen()
matrix = matrixplus(xBaum,yBaum,baumMatrix,matrix)

