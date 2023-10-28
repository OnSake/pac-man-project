# Créé par thibault.rigallaud, le 16/10/2023 en Python 3.7
from random import randint
import pygame
import sys
import time

class Fantome:

    def __init__(self,positionx,positiony,mort_fantome,couleur,respawn,orientation):
        self.__pos_x__ = positionx
        self.__pos_y__ = positiony
        self.__mort__ = mort_fantome
        self.__couleur__ = couleur
        self.__respawn__ = respawn
        self.__orientation__ = orientation

    def get_posx (self):
        return self.__pos_x__

    def set_posx(self,valeur):
        self.__pos_x__ = valeur

    def get_posy (self):
        return self.__pos_y__

    def set_posy(self,valeur):
        self.__pos_y__ = valeur

    def get_orientation(self):
        return self.__orientation__

    def set_orientation(self, valeur):
        self.__orientation__ = valeur

    def get_couleur(self):
        return self.__couleur__

    def mvt(self):
            liste_orientation=["left", "top", "right", "bottom"]
            self.set_orientation(liste_orientation[randint(0, 3)])

            if self.get_orientation() == "left":
                self.min_posx(10)
            elif self.get_orientation() == "top":
                self.add_posy(10)
            elif self.get_orientation() == "right":
                self.add_posx(10)
            elif self.get_orientation() == "bottom":
                self.min_posy(10)


    def draw(self):
        pygame.draw.circle(fenetre, self.get_couleur(), (self.get_posx(), self.get_posy()), 30)


    def add_posx(self, valeur):
        self.set_posx(self.get_posx() + valeur)

    def min_posx(self, valeur):
        self.set_posx(self.get_posx() - valeur)

    def add_posy(self, valeur):
        self.set_posy(self.get_posy() + valeur)

    def min_posy(self, valeur):
        self.set_posy(self.get_posy() - valeur)

pygame.init()


ecran = 640, 480
pygame.display.init()
fenetre = pygame.display.set_mode(ecran)
police = pygame.font.SysFont("arial" ,15)

fantome = Fantome(ecran[0]//2, ecran[1]//2, 0, (86, 177, 105), 0, "left")

while True:
    fenetre.fill([0, 0, 0])

    fantome.mvt()
    fantome.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

    pygame.display.update()
    time.sleep(0.1)






