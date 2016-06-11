import math

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




raster = rastererstellen(windstaerke)
for radius in range(windstaerke, 0, -1):
    raster2 = abswind(raster, radius, 1)

for spalte in raster:
    print(spalte)
