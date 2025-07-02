import os
if not os.path.isfile("/home/maxi-leidl/Documents/PRO Code/PRO-TSM/Python/TSM/01 - Listen Dictionaries Tupel/woerterbuch.txt"):
    print ("Das Wörterbuch gibt es nicht")
datei = open("/home/maxi-leidl/Documents/PRO Code/PRO-TSM/Python/TSM/01 - Listen Dictionaries Tupel/woerterbuch.txt","r")
deutsch = []
englisch = []
franzoesisch = []
italienisch = []
spanisch = []
for zeile in datei:
    spalten = zeile.split(";")
    deutsch.append(spalten[0])
    englisch.append(spalten[1])
    franzoesisch.append(spalten[2])
    italienisch.append(spalten[3])
    spanisch.append(spalten[4])
datei.close()

wort = input("Geben Sie ein Wort ein: ")

