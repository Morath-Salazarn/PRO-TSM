def max(zahl1, zahl2, *zahlen):
    groesste = int
    kleinste = int
    if zahl1 > zahl2:
        groesste = zahl1
        kleinste = zahl2
    else:
        groesste = zahl2
        kleinste = zahl1
    for zahl in zahlen:
        if zahl > groesste:
            groesste = zahl
        if zahl < kleinste:
            kleinste = zahl
    return groesste, kleinste

print(max(1,2,5,7,2,8,6,1))