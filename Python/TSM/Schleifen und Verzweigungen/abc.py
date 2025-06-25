a = input("Geben Sie einen Wert für a ein: ")
b = input("Geben Sie einen Wert für b ein: ")
c = input("Geben Sie einen Wert für c ein: ")

if((int(b)**2-4*int(a)*int(c))**0.5 < 0):
    print("Für x gibt es keine Werte")
elif((int(b)**2-4*int(a)*int(c))**0.5 == 0):
    x1 = (-int(b) + (int(b)**2 - 4 * int(a) * int(c))**0.5) / (2 * int(a))
    print("Für x gibt es genau einen Wert: ",x1)
elif((int(b)**2-4*int(a)*int(c))**0.5 > 0):
    x1 = (-int(b) + (int(b)**2 - 4 * int(a) * int(c))**0.5) / (2 * int(a))
    x2 = (-int(b) - (int(b)**2 - 4 * int(a) * int(c))**0.5) / (2 * int(a))
    print("Die Werte für x sind: ",x1," und ",x2)
