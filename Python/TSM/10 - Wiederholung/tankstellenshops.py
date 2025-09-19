maxUmsatz= 0
maxUmsatzName = ""

minUmsatz = 500000
minUmsatzName = ""

gesamtUmsatz = 0
gesamtMini = 0
gesamtMidi = 0
gesamtMaxi = 0

dateiname = "/home/maxi-leidl/Documents/PRO Code/PRO-TSM/Python/TSM/10 - Wiederholung/ppDaten.csv"
with open(dateiname, "r") as datei:
    for line in datei:
        spalten = line.strip().split(";")

        paechterNr = spalten[0]
        shopTyp = int(spalten[1])
        name = spalten[2]
        umsatz = int(spalten[3])

        #Maximaler Umsatz
        if umsatz > maxUmsatz:
            maxUmsatz = umsatz
            maxUmsatzName = name

        #Minimaler Umsatz
        if umsatz < minUmsatz:
            minUmsatz = umsatz
            minUmsatzName = name
        
        #Gesamt Umsatz
        gesamtUmsatz += umsatz

        if shopTyp == 1:
            gesamtMini += umsatz
        if shopTyp == 2:
            gesamtMidi += umsatz
        if shopTyp == 3:
            gesamtMaxi += umsatz

        anteilMini = round((gesamtMini / gesamtUmsatz) * 100, 2)
        anteilMidi = round((gesamtMidi / gesamtUmsatz) * 100, 2)
        anteilMaxi = round((gesamtMaxi / gesamtUmsatz) * 100, 2)
        
print("Auswertung")
print("------------")
print("Pächter mit dem größten Umsatz... Name: " + str(maxUmsatzName))
print("höchster Umsatz: " + str(maxUmsatz) + " Euro")
print("Pächter mit dem niedrigster Umsatz... Name: " + str(minUmsatzName))
print("niedrigster Umsatz: " + str(minUmsatz) + " Euro")
print("\n" + "Der Gesamtumsatz: " + str(gesamtUmsatz) + " Euro teilt sich auf in:")
print("---------------------------------------")
print("Mini-Shop: " + str(gesamtMini) + " Euro / Anteil am Gesamtumsatz: " + str(anteilMini) + "%")
print("Midi-Shop: " + str(gesamtMidi) + " Euro / Anteil am Gesamtumsatz: " + str(anteilMidi) + "%")
print("Maxi-Shop: " + str(gesamtMaxi) + " Euro / Anteil am Gesamtumsatz: " + str(anteilMaxi) + "%")