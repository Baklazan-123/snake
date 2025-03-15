import pygame
from kierunek import Kierunek

class Waz(pygame.sprite.Sprite):
    def __init__(self):
        self.oryginalny_obraz = pygame.image.load("images/head.png")
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)
        self.rect = self.obraz.get_rect(center = (12*32+16, 9*32+16))