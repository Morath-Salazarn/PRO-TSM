class ticketautomat:
    def __init__(self, __preis, ticketname):
        self.ticketname = str(ticketname)
        
        if int(__preis) > 0:
            self.__preis = int(__preis)
        else:
            self.__preis = 0
            self.ticketname = "ungueltig"

        if len(ticketname) > 3:
            self.ticketname = ticketname
        else:
            self.__preis = 0
            self.ticketname = "ungueltig"

        self.bisherGezahlt = 0
        self.gesamtSumme = 0

    
    def geldEinwerfen(self, betrag):
        if betrag >= 0:
            self.bisherGezahlt += betrag
        else:
            print("Fehler")

    def ticketAusgeben(self):
        
        

            if self.bisherGezahlt >= self.__preis:
                print("""
                *********************
                * Einheitsticket
                * """+ str(self.ticketname) +"""
                *
                * """+ str(self.__preis) +""" ct
                *********************
                """)
                self.bisherGezahlt -= self.__preis
                print("Restgeld: " + str(self.bisherGezahlt) + " Cent")
        
            
t1 = ticketautomat(2000, "Python Kurs")
t1.geldEinwerfen(3000)
t1.ticketAusgeben()