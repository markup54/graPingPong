import pygame
import random
class Platforma():
    def __init__(self,ekran):
        self.ekran = ekran
        self.x = random.randint(10,ekran.get_width()//4*3)
        self.y = 0
        self.wysokosc = 30
        self.szerokosc = random.randint(80,200)
        self.kolor = (23,234,100)
    def rysuj(self):
        pygame.draw.rect(self.ekran,self.kolor,(self.x,self.y,self.szerokosc,self.wysokosc))


class Lawa():
    pass

class Gra():
    def __init__(self, wysokosc , szerokosc, kolorTla):
        pygame.init()
        self.wysokosc =wysokosc
        self.szerokosc = szerokosc
        self.kolor_tla = kolorTla
        self.ekran = pygame.display.set_mode((wysokosc,szerokosc))
        pygame.display.set_caption("Lawa")
        self.zegar = pygame.time.Clock()
        self.platformy = []

    def rysuj(self):
        licznikcykniec = 0
        while True:
            for zdarzenie in pygame.event.get():
                if zdarzenie.type == pygame.QUIT:
                    pygame.quit()
                    return True
            self.ekran.fill(self.kolor_tla)
            if licznikcykniec%50 == 0:
                platforma = Platforma(self.ekran)
                self.platformy.append(platforma)
            for platforma in self.platformy:
                platforma.y +=2
                platforma.rysuj()

            self.zegar.tick(60)
            licznikcykniec +=1
            pygame.display.update()



gra = Gra(500,700,(34,56,78))
gra.rysuj()


class Ludzik():
    pass

