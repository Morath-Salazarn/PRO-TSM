import os
import csv
os.path.isfile()
with open("/home/maxi-leidl/Documents/PRO Code/PRO-TSM/Python/TSM/03 - Textdateien und Datenformate auswerten/ppDaten.csv", "w", newline="", encoding="utf-8") as csvfile:
    for line in csvfile:
        print(line)

        # Zähler für die Nummern 1, 2, 3 in der ersten Spalte
        count_1 = 0
        count_2 = 0
        count_3 = 0

        # Variablen für höchste und niedrigste Zahl in der dritten Spalte
        max_value = None
        min_value = None
        max_name = ""
        min_name = ""

        with open("/home/maxi-leidl/Documents/PRO Code/PRO-TSM/Python/TSM/03 - Textdateien und Datenformate auswerten/ppDaten.csv", "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if not row:
                    continue
                nummer = row[0].strip()
                name = row[1].strip()
                try:
                    wert = float(row[2].replace(",", "."))
                except (IndexError, ValueError):
                    continue

                if nummer == "1":
                    count_1 += 1
                elif nummer == "2":
                    count_2 += 1
                elif nummer == "3":
                    count_3 += 1

                if (max_value is None) or (wert > max_value):
                    max_value = wert
                    max_name = name
                if (min_value is None) or (wert < min_value):
                    min_value = wert
                    min_name = name

        print(f"Anzahl 1: {count_1}")
        print(f"Anzahl 2: {count_2}")
        print(f"Anzahl 3: {count_3}")
        print(f"Höchster Wert: {max_value} (Name: {max_name})")
        print(f"Niedrigster Wert: {min_value} (Name: {min_name})")
