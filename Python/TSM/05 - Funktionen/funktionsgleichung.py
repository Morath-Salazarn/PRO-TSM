import math

def loese_quadratische_gleichung(a, b, c):
    if a == 0:
        # Lineare Gleichung bx + c = 0
        if b == 0:
            return (None, None)
        else:
            x = -c / b
            return (x, None)
    else:
        diskriminante = b**2 - 4*a*c
        if diskriminante > 0:
            x1 = (-b + math.sqrt(diskriminante)) / (2*a)
            x2 = (-b - math.sqrt(diskriminante)) / (2*a)
            return (x1, x2)
        elif diskriminante == 0:
            x = -b / (2*a)
            return (x, None)
        else:
            return (None, None)

# Beispielaufruf im Hauptprogramm
if __name__ == "__main__":
    a = 1
    b = -3
    c = 2
    loesungen = loese_quadratische_gleichung(a, b, c)
    print("Lösungen:", loesungen)