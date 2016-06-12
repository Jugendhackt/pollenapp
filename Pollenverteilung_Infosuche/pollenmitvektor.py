import math
import riesenmatrix as rim
import wind as wind

windstaerke = 5



def rastererstellen(windstaerke):
    raster = []
    for i in range(windstaerke * 2 + 1):
        einzelraster = []
        for x in range(windstaerke * 2 + 1):
            einzelraster.append(0)
        raster.append(einzelraster)
        einzelraster = []
    return raster

def abstand(wind, r1, r2):
    z1 = pow((r1 - wind), 2)
    z2 = pow((r2 - wind), 2)
    abst = math.sqrt(z1 + z2)
    return abst

def abswind(raster, radius, pollenwert):
    if raster == None:
        e = 5
    for r1 in range(len(raster)):
        for r2 in range(len(raster)):
            abst = abstand(windstaerke, r1, r2)
            if abst < radius:
                raster[r1][r2] += pollenwert
    return raster

def windwinkel(raster, wind, windstaerke, pollenwert, winkelgrenze):

    for p1 in range(len(raster)):
        for p2 in range(len(raster)):
            va = []
            vb = []

            va.append(wind[0])
            va.append( wind[1])

            vb.append(p1 - windstaerke)
            vb.append(p2 - windstaerke)

            zwischen1 = va[0] * vb[0] + va[1] * vb[1]
            zwischen2 = pow(va[0], 2) + pow(va[1], 2)
            zwischen3 = pow(vb[0], 2) + pow(vb[1], 2)

            zwischen2 = math.sqrt(zwischen2)
            zwischen3 = math.sqrt(zwischen3)
            if (zwischen2 * zwischen3) == 0:
                continue
            else:
                zwischen4 = min(zwischen1/(zwischen2 * zwischen3), 1)
                zwischen4 = max(zwischen4, -1)
                erg = math.acos(zwischen4)
            if erg > winkelgrenze:
                if raster[p1][p2] > 0:
                    raster[p1][p2] -= pollenwert
    return raster


def baumstempel():
    pollenwert = 0.3
    riesenmatrix_f = rim.matrixErstellen()
    with open('text.txt') as f:

        xein = int(f.readline())
        yein = int(f.readline())
        while xein and yein:

            auswind = wind.windabruf()
            windstaerke = int(auswind[1])
            windv = auswind[0]
            raster = rastererstellen(windstaerke)




            for radius in range(windstaerke, 0, -1):
                raster = abswind(raster, radius, 1)


            for grenze in range(15, 12, -1):
                grenze = math.pi / grenze
                raster = windwinkel(raster, windv, windstaerke, pollenwert, grenze)

            for x in range(len(raster)):
                for y in range(len(raster)):
                    raster[x][y] = round(raster[x][y], 2)

            riesenmatrix_f = rim.matrixplus(int(xein), int(yein), raster, riesenmatrix_f)
            xein = f.readline()
            yein = f.readline()


baumstempel()

