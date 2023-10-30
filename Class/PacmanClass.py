#-------------------- PROJET PAC MAN --------------------#

#--------------- PAC MAN ---------------#

#---------- IMPORT ----------#

import pygame 
pygame.init()
from pygame.locals import *
import time

#---------- CLASS ----------#

class Pacman:
    def __init__(self, vie, pos_x, pos_y, orientation = "None"):
        self.__vie__ = vie
        self.__pos_x__ = pos_x
        self.__pos_y__ = pos_y
        self.__can_eat__ = False
        self.__orientation__ = orientation
        self.__couleur__ = (255, 255, 0)
        self.__score__ = 0
        self.__check_collision__ = [False, False, False, False]

    #-------- Get et Set --------#
    def get_collision(self, index):
        return self.__check_collision__[index]

    def set_collision(self, index, valeur):
        self.__check_collision__[index] = valeur

    def get_vie(self):
        return self.__vie__

    def set_vie(self, valeur):
        self.__vie__ = valeur

    def get_posx(self):
        return self.__pos_x__

    def set_posx(self, valeur):
        self.__pos_x__ = valeur

    def get_posy(self):
        return self.__pos_y__

    def set_posy(self, valeur):
        self.__pos_y__ = valeur

    def get_can_eat(self):
        return self.__can_eat__

    def set_can_eat(self, valeur):
        self.__can_eat__ = valeur

    def get_orientation(self):
        return self.__orientation__

    def set_orientation(self, valeur):
        self.__orientation__ = valeur

    def get_couleur(self):
        return self.__couleur__

    def set_couleur(self, valeur):
        self.__couleur__ = valeur

    def get_score(self):
        return self.__score__

    def set_score(self, valeur):
        self.__score__ += valeur


    #-------- Méthodes --------#

    def draw(self, surface):
        if self.get_orientation() == "None":
            surface.blit(pac_man_img_neutre, (self.get_posx(), self.get_posy()))
        elif self.get_orientation() == "right":
            surface.blit(pac_man_img, (self.get_posx(), self.get_posy()))
        elif self.get_orientation() == "top":
            surface.blit(pygame.transform.rotate(pac_man_img, 90), (self.get_posx(), self.get_posy()))
        elif self.get_orientation() == "bottom":
            surface.blit(pygame.transform.rotate(pac_man_img, -90), (self.get_posx(), self.get_posy()))
        elif self.get_orientation() == "left":
            surface.blit(pygame.transform.flip(pac_man_img, True, False), (self.get_posx(), self.get_posy()))  


    def move(self):
        if self.get_posx() < -30:
            self.set_posx(900)
        elif self.get_posx() > 910:
            self.set_posx(-20)
        if self.get_orientation() == "left" and self.get_collision(0):
                self.min_posx(15)
        elif self.get_orientation() == "top" and self.get_collision(1):
                self.min_posy(15)
        elif self.get_orientation() == "right" and self.get_collision(2):
                self.add_posx(15)
        elif self.get_orientation() == "bottom" and self.get_collision(3):
                self.add_posy(15)
        else:
            self.add_posx(0)
            self.add_posy(0)
            self.min_posx(0)
            self.min_posy(0)
    
    
    def check_collision(self, ecran, map):
        num1 = ecran[1]//32
        num2 = ecran[0]//30

        #if self.get_posy()%30 == 0 and self.get_posx()%30:
        self.set_collision(0, False)
        self.set_collision(1, False)
        self.set_collision(2, False)
        self.set_collision(3, False)
    
        if self.get_orientation() == "right":
            if self.get_posx() < 870: #Pour éviter le "out of range"
                if map[self.get_posy()//num1][(self.get_posx() + 30) // num2] < 3:
                    self.set_collision(2, True)
                else : self.__check_collision__[2] = False
            else : self.set_collision(2, True)

        elif self.get_orientation() == "left":
            if map[self.get_posy()//num1][(self.get_posx() - 15) // num2] < 3:
                self.set_collision(0, True)
            else : self.__check_collision__[0] = False

        elif self.get_orientation() == "top":
            if map[(self.get_posy() - 15)//num1][self.get_posx() // num2] < 3:
                self.set_collision(1, True)
            else : self.__check_collision__[1] = False

        elif self.get_orientation() == "bottom":
            if map[(self.get_posy() + 30)//num1][self.get_posx() // num2] < 3:
                self.set_collision(3, True)
            else : self.__check_collision__[3] = False


    def check_score(self, ecran, map):
        num1 = ecran[1]//32
        num2 = ecran[0]//30

        if 0 < self.get_posx() < 900 : #Eviter le out of range
            if map[self.get_posy() // num1][self.get_posx() // num2] == 1:
                self.set_score(10)
                map[self.get_posy() // num1][self.get_posx() // num2] = 0
            
            
    def check_malade(self, ecran, map):
        a = 0
        num1 = ecran[1]//32
        num2 = ecran[0]//30
        if 0 < self.get_posx() < 900 : #Eviter le out of range
            if map[self.get_posy() // num1][self.get_posx() // num2] == 2:
                self.set_can_eat(True)
                self.set_score(50)
                map[self.get_posy() // num1][self.get_posx() // num2] = 0
        


            
    


       

    #-------- Méthodes pour modifier les coordonées x et y (pour faire bouger le pac man) --------#

    def add_posx(self, valeur):
        self.set_posx(self.get_posx() + valeur)

    def min_posx(self, valeur):
        self.set_posx(self.get_posx() - valeur)

    def add_posy(self, valeur):
        self.set_posy(self.get_posy() + valeur)

    def min_posy(self, valeur):
        self.set_posy(self.get_posy() - valeur)



pac_man_img = pygame.transform.scale(pygame.image.load(f'Texture/Pacman/pacman.gif'), (30, 30))
pac_man_img_neutre = pygame.transform.scale(pygame.image.load(f'Texture/Pacman/pac_man_neutre.gif'), (30, 30))