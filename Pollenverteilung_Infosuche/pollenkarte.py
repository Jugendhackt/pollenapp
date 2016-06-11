#!/usr/bin/env python3
# Erzeugt eine Heatmap aus einer riesigen Matrix.


import png

def erzeuge_pollenkarte(matrix):
    breite = len(matrix)
    hoehe = len(matrix[0])

    matrix2 = []
    for x in range(breite):
        zeile = []
        for y in range(hoehe):
            wert = matrix[x][y]
            #rgba = (wert, wert, wert, 0.1)
            #zeile.append(rgba)
            zeile.append(0xCC)
            zeile.append(0)
            zeile.append(0)
            zeile.append(wert)
        matrix2.append(zeile)

    image = png.from_array(matrix2, 'RGBA')

    image.save('pollenkarte.png')

#    png_file = open('pollenkarte.png', 'wb')
#    png_writer = png.Writer(width=breite, height=hoehe, alpha=True, bitdepth=8)
#            #greyscale=True,
#    #for daten in matrix:
#    #    png_writer.write(png_file, daten)
#    png_writer.write(png_file, matrix2)
#    png_file.close()



import random
liste = []

#m = [[1,2,3],[34,2,4],[2,34,45]]
m = [[1,0,1],[1,1,0],[1,0,0]]
n = [1,2,3,34,2,4,2,34,45]
for x in range(600):
    einzel = []
    for y in range(600):
        zahl =random.randint(0, 255)
        einzel.append(zahl)
    liste.append(einzel)
erzeuge_pollenkarte(liste)
