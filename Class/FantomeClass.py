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
        self.__malade__ = False 
        self.__finish_heal__ = False
        self.__liste_orientation__= ["left", "top", "right", "bottom", "None"]

    #-------- Get et Set --------#
    def get_liste_orientation(self):
        return self.__liste_orientation__

    def get_finish_heal(self):
        return self.__finish_heal__
    
    def set_finish_heal(self, valeur):
        self.__finish_heal__ = valeur

    def get_malade(self):
        return self.__malade__
    
    def set_malade(self, valeur):
        self.__malade__ = valeur

    def get_posx(self):
        return self.__pos_x__

    def set_posx(self,valeur):
        self.__pos_x__ = valeur

    def get_posy(self):
        return self.__pos_y__

    def set_posy(self,valeur):
        self.__pos_y__ = valeur

    def get_orientation(self):
        return self.__orientation__

    def set_orientation(self, valeur):
        self.__orientation__ = valeur

    def get_couleur(self):
        return self.__couleur__


    #-------- Méthodes --------#

    def mvt(self):


            if self.get_orientation() == "left":
                self.min_posx(15)
            elif self.get_orientation() == "top":
                self.add_posy(15)
            elif self.get_orientation() == "right":
                self.add_posx(15)
            elif self.get_orientation() == "bottom":
                self.min_posy(15)


    def draw(self, fenetre):

        if self.get_malade() == False :
            if self.get_couleur() == 'red':
                fenetre.blit(fantome[0], (self.get_posx(), self.get_posy()))
            elif self.get_couleur() == 'orange':
                fenetre.blit(fantome[1], (self.get_posx(), self.get_posy()))
            elif self.get_couleur() == 'blue':
                fenetre.blit(fantome[2], (self.get_posx(), self.get_posy()))
            elif self.get_couleur() == 'pink':
                fenetre.blit(fantome[3], (self.get_posx(), self.get_posy()))
        else : 
            if self.get_finish_heal():
                fenetre.blit(fantome[5], (self.get_posx(), self.get_posy()))
            else : fenetre.blit(fantome[4], (self.get_posx(), self.get_posy()))
        
        pygame.display.flip()


    def finish_heal(self):
        self.set_finish_heal(False)
        self.set_malade(False)

    def check_collision(self, ecran, map):
        orientation = self.get_liste_orientation()
        num1 = ecran[1]//32
        num2 = ecran[0]//30
        if 0 < self.get_posx() < 850 and 0 < self.get_posy() < 900:
            if map[self.get_posy()//num1][(self.get_posx() + 30)//num2] == 3 and self.get_orientation() == "right":
                self.set_orientation(orientation[randint(0, 3)])
            
            if map[self.get_posy()//num1][(self.get_posx() - 15)//num2] == 3 and self.get_orientation() == "left":
                self.set_orientation(orientation[randint(0, 3)])

            if map[(self.get_posy() - 15)//num1][self.get_posx()//num2] == 3 and self.get_orientation() == "top":
                self.set_orientation(orientation[randint(0, 3)])

            if map[(self.get_posy() + 30)//num1][self.get_posx()//num2] == 3 and self.get_orientation() == "bottom":
                self.set_orientation(orientation[randint(0, 3)])
        else: 
            self.set_posy(ecran[1]//2)
            self.set_posx(ecran[0]//2)

            
 
        

    def add_posx(self, valeur):
        self.set_posx(self.get_posx() + valeur)

    def min_posx(self, valeur):
        self.set_posx(self.get_posx() - valeur)

    def add_posy(self, valeur):
        self.set_posy(self.get_posy() + valeur)

    def min_posy(self, valeur):
        self.set_posy(self.get_posy() - valeur)






fantome_1 = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/red.gif'), (25, 25))
fantome_2 = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/orange.gif'), (25, 25))
fantome_3 = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/blue.gif'), (25, 25))
fantome_4 = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/pink.gif'), (25, 25))
fantome_malade = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/malade.gif'), (25, 25))
fantome_malade_finish = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/malade_finish.gif'), (25, 25))

fantome = [fantome_1, fantome_2, fantome_3, fantome_4, fantome_malade, fantome_malade_finish]