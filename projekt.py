import pygame
import random
import time
from jablko import Jablko
from kierunek import Kierunek
from waz import Waz

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608

tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))

#25x19
for i in range(25):
    for j in range (19):
        obraz = pygame.image.load("images/background.png")
        maska = (random.randrange(0,20), random.randrange(0,20), random.randrange(0,20))

        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        tlo.blit(obraz, (i*32, j*32))

pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

waz = Waz()

PORUSZ_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZ_WEZEM, 200)

jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)

gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    ekran.blit(tlo, (0,0))

    ekran.blit(waz.obraz, waz.rect)
    
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)

    pygame.display.flip()

    zegar.tick(30)

time.sleep(3)
pygame.quit()

