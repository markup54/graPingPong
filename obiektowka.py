class Osoba():
    licznikOsob = 0 #pole statyczne

    def __init__(self,imie,wiek,plec):
        self.imie = imie
        self.wiek = wiek
        self.plec =plec
        Osoba.licznikOsob += 1

    def przedstawSie(self):
        print("Mam na imię "+self.imie)

print ("mamy ",Osoba.licznikOsob," obiektów")
osobaJas = Osoba("Jan",12,"M")
print(osobaJas.imie)
print ("mamy ",Osoba.licznikOsob," obiektów")
osobaJas.przedstawSie()
osobaMalgosia = Osoba("Małgorzata",11,"K")
osobaMalgosia2 = Osoba("Małgorzata",11,"K")
print ("mamy ",Osoba.licznikOsob," obiektów")