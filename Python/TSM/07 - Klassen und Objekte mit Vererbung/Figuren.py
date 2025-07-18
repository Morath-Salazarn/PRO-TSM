import math

# *** Klassendefinition für die Figur ***
class Figur:        
    def __init__(self,x,y,farbe):
        self.farbe = farbe
        self.x = x
        self.y = y
        
    def print(self):
        print("Das ist ein",type(self)," an Position ",self.x,",",self.y,"mit der Farbe",self.farbe)

# *** Die Klasse Kreis erbt alles von der Figur ***
class Kreis(Figur):
    # Konstruktor vom Kreis braucht ein neues Attribut radius -
    # die anderen Attribute müssen auch initialisiert werden
    def __init__(self,x,y,farbe,radius=10):
        #super ruft den Konstruktor der Elternklasse auf und übergibt die nötigen Werte
        super().__init__(x,y,farbe)
        # Jetzt muss nur noch der Radius definiert werden
        self.radius = radius
        #neue Methode
    def flaeche(self):
        return self.radius*self.radius*math.pi    
# *** Hauptprogramm: Zwei Kreise, ein Quadrat und eine Figur ***

# Konstruktion von 3 unterschiedlichen Objekten
f1 = Figur(20,20,"gruen")
k1 = Kreis(30,30,"rot",10)
k2 = Kreis(60,60,"blau",20)

#Ausgabe: durch den Aufruf der Methode print() von oben.
f1.print() #ausgabe: Das ist ein/e <class '__main__.Figur'> an Position 20 , 20 mit der Farbe gruen   
k1.print() #ausgabe: Das ist ein/e <class '__main__.Kreis'> an Position 30 , 30 mit der Farbe rot
k2.print() #ausgabe: Das ist ein/e <class '__main__.Kreis'> an Position 60 , 60 mit der Farbe blau

# Alle Objekte können auch in einer Liste verwaltet werden
""" figuren = []
figuren.append(f1)
figuren.append(k1)
figuren.append(k2)

for figur in figuren:
    figur.print() """