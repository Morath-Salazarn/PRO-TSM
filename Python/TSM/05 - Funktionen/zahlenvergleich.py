def max(zahl1, zahl2, *zahlen):
    groesste = 0
    if zahl1 > zahl2:
        groesste = zahl1
    else:
        groesste = zahl2

    for zahl in zahlen:
        if zahl > groesste:
            groesste = zahl
    return groesste

print(max(1,2,5,7,2,8,6,1))