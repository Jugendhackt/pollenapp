import urllib.request
import requests
import re

def windabruf():
    seite = requests.get('https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/wien')
    quelltext = seite.text
    erg = re.findall('(Nordost|Nordwest|Süldost|Südwest|West|Nord|Ost|S&uumld)', str(quelltext))
    erg2 = re.findall('[0-9]* km', str(quelltext))
    erg2[0] = re.sub(" km","", erg2[0])
    z = 0
    for x in erg2:
        if z % 2 != 0:
            erg2[z] = "FEHLER"
            b = 4
        z += 1


    for x in erg2:
        if x == "FEHLER":
            erg2.remove(x)

    richtung = windrichtung(erg[0])
    return [richtung,erg2[0]]

def windrichtung(richtung):
    if richtung == "Nordost":
        return [1,1]
    elif richtung == "Nordwest":
        return [1, -1]
    elif richtung == "Südost":
        return [-1,1]
    elif richtung == "Nord":
        return [-1, 0]
    elif richtung == "Süd":
        return [0, -1]
    elif richtung == "West":
        return [-1, 0]
    elif richtung == "Osten":
        return [1, 0]
    elif richtung == "Südwest":
        return [-1,-1]
    else:
        return [0,0]

windabruf()