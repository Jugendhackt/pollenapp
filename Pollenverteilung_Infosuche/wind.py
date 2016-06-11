import urllib.request
import re

seite = urllib.request.urlopen('https://www.zamg.ac.at/cms/de/wetter/wetterwerte-analysen/wien')
quelltext = seite.read()
erg = re.findall('(Nordost|Nordwest|Südost|Südwest|West|Nord|Ost|S&uumld)', str(quelltext))
erg2 = re.findall('[0-9]* km', str(quelltext))
print(erg2)
z = 0
for x in erg2:
    if z % 2 != 0:
        erg2[z] = "FEHLER"
        b = 4
    z += 1


for x in erg2:
    if x == "FEHLER":
        erg2.remove(x)
print(erg)
print(erg2)