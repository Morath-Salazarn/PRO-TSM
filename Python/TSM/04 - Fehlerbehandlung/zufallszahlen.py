import random

# 10 Zufallszahlen im Bereich 0-100 erzeugen
zahlen = []

while len(zahlen)<10:
    zufallszahl = random.randint(0, 100)
    zahlen.append(zufallszahl)

# Zahlen > 90 filtern
groesser_90 = [zahl for zahl in zahlen if zahl > 90]

# Durchschnitt berechnen, falls vorhanden
if groesser_90:
    durchschnitt = sum(groesser_90) / len(groesser_90)
    print("Durchschnitt der Zahlen > 90:", durchschnitt)
else:
    print("Keine Zahlen größer als 90 vorhanden.")