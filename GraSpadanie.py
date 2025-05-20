import pygame
import random

class Jajko():
    licznikJajek = 0
    licznikZlapanychJajek = 0

    def __init__(self, x,y,szerokosc,wysokosc,kolor):
        self.x =x
        self.y = y
        self.szerokosc =szerokosc
        self.wysokosc = wysokosc
        self.kolor = kolor
        self.rozbite = False
        Jajko.licznikJajek = Jajko.licznikJajek + 1
        # pygame.draw.ellipse(self.surface, self.color, [0, 0, self.width, self.height])

    def rysuj(self,ekran):
        if not self.rozbite:
            self.y = self.y + 2
        pygame.draw.ellipse(ekran,self.kolor,[self.x,self.y,self.szerokosc,self.wysokosc])
        self.zmianaRozbite(ekran)


    def zmianaRozbite(self,ekran):
        if self.y + self.wysokosc >= ekran.get_height():
            self.kolor = "yellow"
            self.rozbite = True

class Koszyk():

    def __init__(self, x ,ekran):
        self.x = x
        self.y = ekran.get_height()-50
        self.wysokosci = 30
        self.szerokosc = 50
        self.kolor = "brown"
        self.zlapaneJajka = []
        self.ekran = ekran

    def rysuj(self):
        pygame.draw.rect(self.ekran,self.kolor,(self.x,self.y,self.szerokosc,self.wysokosci))

class Gra():

    def __init__(self,szerokosc, wysokosc,kolorTla):
        pygame.init()
        self.kolorTla = kolorTla
        self.ekran = pygame.display.set_mode((szerokosc,wysokosc))
        pygame.display.set_caption("Spadające cosie")
        self.zegar = pygame.time.Clock()
        self.jajka = []

    def rysuj(self):
        ile = 0
        koszyk =Koszyk(50,self.ekran)



        while not self.zwroc_zdarzenia():
            ile  = ile +1
            self.ekran.fill(self.kolorTla)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                if koszyk.x >5:
                    koszyk.x -= 5
            if keys[pygame.K_RIGHT]:
                if koszyk.x <self.ekran.get_width()-koszyk.szerokosc:
                    koszyk.x+=5
            koszyk.rysuj()
            if ile%15 == 0:
                x= random.randint(10,self.ekran.get_width()-10)
                jajko = Jajko(x,10,20,30,"green")
                self.jajka.append(jajko)
            for jajeczko in self.jajka:
                if jajeczko.x > koszyk.x and jajeczko.x <koszyk.x+koszyk.szerokosc and jajeczko.y > self.ekran.get_height() - 50 and jajeczko.y <self.ekran.get_height() -20:
                        self.jajka.remove(jajeczko)
                        koszyk.zlapaneJajka.append(jajeczko)
                else:
                    jajeczko.rysuj(self.ekran)
            self.zegar.tick(60)
            pygame.display.update()

    def zwroc_zdarzenia(self):
        """
        Obsługa zdarzeń:
        zamykanie, kliknięcie myszą lub przyciski klawiatury
        :return: True jeżeli zamykanie
        """
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.QUIT:
                pygame.quit()
                return True

            # inne zdarzenia
        return False

#program główny

gra1 = Gra(500,800,(23,45,234))
gra1.rysuj()