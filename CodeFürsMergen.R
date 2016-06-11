# Ordner festlegen, in dem gearbeitet werden soll. Hier der Desktop
setwd("/Users/MarieLou/Journocoding/pollenapp")

# Die Daten einlesen
baumkataster <- read.csv("Baumkataster_neu.csv", encoding="latin1", sep= ";", dec="-")
allergiebäume <- read.csv("Allergiebäume.csv", encoding="latin1", sep= ";", dec="-")

baumkataster$Baumarten <- baumkataster$Baumgruppe

# Daten ansehen
View(baumkataster)
View(allergiebäume)

allergiebaumkataster <- merge(baumkataster, allergiebäume, by=c("Baumarten"))

View(allergiebaumkataster)

# Neuen Datensatz als csv speichern
write.csv(allergiebaumkataster, file = "Allergiebaumkataster.csv", fileEncoding = "latin1")
