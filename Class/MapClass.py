#-------------------- PROJET PAC MAN --------------------#

#--------------- MAP ---------------#

#---------- IMPORT ----------#

import pygame
from pygame.locals import *
from Maps.map_1 import map as map_1
from Maps.map_2 import map as map_2
pygame.init()

maps = [map_1, map_2]
#---------- CLASS ----------#
class Map:
  def __init__(self, level, couleur):
    self.__level__ = level - 1
    self.__map_select__ = maps[self.get_level()]
    self.__couleur__ = couleur

  #-------- Get et Set --------#
  def get_level(self):
    return self.__level__

  def set_level(self, valeur):
    self.__level__ = valeur

  def get_couleur(self):
    return self.__couleur__

  def set_couleur(self, valeur):
    self.__couleur__ = valeur

  def get_map_select(self):
     return self.__map_select__


    #-------- Méthodes --------#

  def dessiner_map(self, ecran, fenetre):
    y_space = ecran[0]//30 #On crée des maps en 30x32 donc on divise la largeur de l'écran par 30
    x_space = ecran[1]//32 #On crée des maps en 30x32 donc on divise la hauteur de l'écran par 32

    #On lit le tableau par liste, puis par élément. Donc par ligne puis par colonne
    for i in range(len(self.get_map_select())):
      for j in range(len(self.get_map_select()[i])):

        if self.get_map_select()[i][j] == 1:
            pygame.draw.rect(fenetre, (0, 0, 0), (j * x_space, i * y_space, 30, 30))
            pygame.draw.circle(fenetre, (255, 255, 255), (j * x_space + (x_space/2), i * y_space + (y_space/2)), 5) #Ici, on calcule la position de départ x et y et on ajoute la moitié pour que la boule soit centrée
        elif self.get_map_select()[i][j] == 2:
            pygame.draw.rect(fenetre, (0, 0, 0), (j * x_space, i * y_space, 30, 30))
            pygame.draw.circle(fenetre, (255, 255, 255), (j * x_space + (x_space/2), i * y_space + (y_space/2)), 10)

        elif self.get_map_select()[i][j] == 3:
            pygame.draw.rect(fenetre, self.get_couleur(), (j * x_space, i * y_space, 30, 30))

        elif self.get_map_select()[i][j] == 4:
                      pygame.draw.rect(fenetre, (255, 255, 255), (j * x_space, i * y_space, 30, 30))

  def game_finish(self, touch_pacman):
    if touch_pacman == True: 
       return True
    
    for i in range(len(self.get_map_select())):   
        if 1 in self.get_map_select()[i]:
           return False
    return True