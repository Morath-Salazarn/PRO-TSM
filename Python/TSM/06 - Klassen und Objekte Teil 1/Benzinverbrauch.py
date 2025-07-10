#Klassendefinition
class Auto:
    def __init__(self, tankvolumen, tankinhalt, verbrauchPro100km):
        self.tankvolumen = tankvolumen
        self.tankinhalt = tankinhalt
        self.verbrauchPro100km = verbrauchPro100km
    
    def istErreichbar(self, kilometer):
        reichweite = (self.tankinhalt / self.verbrauchPro100km) * 100
        if(reichweite >= kilometer):
            #print("ist erreichbar")
            return True
        else:
            #print("ist nicht erreichbar")
            return False
        
    def tanken(self, liter):
        getankt = self.tankinhalt + liter
        if(getankt <= self.tankvolumen):
            self.tankinhalt = getankt
        else:
            self.tankinhalt = self.tankvolumen

    def fahren(self, km):
        verbrauchPro1km = self.verbrauchPro100km / 100
        reichweite = (self.tankinhalt / self.verbrauchPro100km) * 100
        if(km <= reichweite):
            self.tankinhalt = self.tankinhalt - (verbrauchPro1km * km)
            # print("Sie sind", km,"km gefahren!")
            return self.tankinhalt, True
        else:
            # print("Die Tankfüllung reicht für diese Stecke nicht aus!")
            return False

#Hauptprogramm
A1 = Auto(40, 30, 8)
A2 = Auto(100, 70, 15)

print(A1.istErreichbar(400))
print(A2.istErreichbar(400))

print(A1.fahren(200))
print(A2.fahren(500))