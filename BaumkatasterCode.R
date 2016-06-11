# Ordner festlegen, in dem gearbeitet werden soll. Hier der Desktop
setwd("/Users/MarieLou/Desktop")

# Die Daten einlesen
baum <- read.csv("Baumkatalog_clean2.csv", encoding="latin1", sep= ";", dec="-")

# ein Paket zur Datenmanipulation laden
if(!require(dplyr)) {
  install.packages("dplyr", repos="http://cran.us.r-project.org")
  require(dplyr)
}

# Nur die Zeilen zu einem neuen Datensatz zusammenfügen, die in der Spalte "Baumgruppe" unsere Allergiebäume enthalten
Bäume <- baum %>% 
  filter(Baumgruppe %in% c("Birke", "Buche", "Eiche", "Erle", "Esche", "Hainbuche", "Hasel", "Kiefer", "Pappel", "Weide")) 

# Neuen Datensatz als csv speichern
write.csv(Bäume, file = "Baumkataster_neu.csv", fileEncoding = "latin1")
