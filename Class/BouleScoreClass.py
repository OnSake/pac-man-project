#-------------------- PROJET PAC MAN --------------------#

#--------------- BOULE SCORE ---------------#

#---------- IMPORT ----------#

import pygame
pygame.init()
from pygame.locals import *
import sys
import time
import random


#---------- CLASS ----------#

class Boule_Score:
    def __init__(self, carre_x, carre_y):
        self.__x__ = carre_x
        self.__y__ = carre_y
        self.__eat__ = False



    #-------- Get et Set --------#

    def get_posx(self):
        return self.__x__

    def set_posx(self, valeur):
        self.__x__ = valeur

    def get_posy(self):
        return self.__y__

    def set_posy(self, valeur):
        self.__y__ = valeur

    def get_eat(self):
        return self.__eat__

    def set_eat(self, valeur):
        self.__eat__ = valeur

    #-------- Méthodes --------#

    def draw(self):
        pass
