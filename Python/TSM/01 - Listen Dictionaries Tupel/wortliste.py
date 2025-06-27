eingabe = ""
wortliste = []

while eingabe != "Ende":
    eingabe = input("Geben Sie ein Wort ein, zum beenden 'Ende' eingeben: ")
    if (eingabe == "Ende"):
        print(wortliste)
        print(len(wortliste))
        print(wortliste[::2])
    else:
        if(eingabe in wortliste):
            print("Dieses Wort existiert bereits in der Liste!")
        else:
            wortliste.append(eingabe)
            wortliste.sort()
            print(wortliste)


