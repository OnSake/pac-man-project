#-------------------- PROJET PAC MAN --------------------#

#--------------- MAP ---------------#

#---------- IMPORT ----------#

import pygame
from pygame.locals import *
from Maps.map_1 import map_edited as map_1
from Maps.map_1 import map_origin as map_1_origin
from Maps.map_2 import map as map_2
pygame.init()

maps = [map_1, map_2]
maps_origin = [map_1_origin]
#---------- CLASS ----------#
class Map:
  def __init__(self, level, couleur):
    self.__level__ = level - 1
    self.__map_select__ = maps[self.get_level()]
    self.__couleur__ = couleur
    self.__map_origin__ = maps_origin[self.get_level()]

  #-------- Get et Set --------#
  def get_map_origin(self):
     return self.__map_origin__

  def get_level(self):
    return self.__level__

  def set_level(self, valeur):
    self.__level__ = valeur

  def get_couleur(self):
    return self.__couleur__

  def set_couleur(self, valeur):
    self.__couleur__ = valeur

  def set_map_select(self, valeur):
     self.__map_select__ = valeur

  def get_map_select(self):
     return self.__map_select__


    #-------- Méthodes --------#

  def dessiner_map(self, ecran, fenetre):
    """
    Dessine la carte sur l'écran spécifié.
    @arguments:
        self (Class Map): Instance de la classe Map.
        ecran (tuple): Tuple contenant les dimensions de l'écran (largeur, hauteur).
        fenetre (Surface): Surface pygame sur laquelle dessiner la carte.

    Description:
        Cette fonction prend en entrée les dimensions de l'écran ainsi qu'une surface pygame
        sur laquelle la carte sera dessinée. Elle parcourt ensuite les éléments de la carte
        et les dessine en fonction de leur type.

        Les éléments de la carte sont représentés par des entiers correspondant à leur type :
        - 1 représente un élément de type 1 avec un rectangle noir et un cercle blanc de rayon 5.
        - 2 représente un élément de type 2 avec un rectangle noir et un cercle blanc de rayon 10.
        - 3 représente un élément de type 3 avec un rectangle de couleur définie par la méthode get_couleur().
        - 4 représente un élément de type 4 avec un rectangle blanc.

        Les dimensions de chaque élément sont déterminées en fonction de l'espace disponible sur l'écran.
    """
    y_space = ecran[0]//30 #On crée des maps en 30x32 donc on divise la largeur de l'écran par 30
    x_space = ecran[1]//32 #On crée des maps en 30x32 donc on divise la hauteur de l'écran par 32

    #On lit le tableau par liste, puis par élément. Donc par ligne puis par colonne
    for i in range(len(self.get_map_select())):
      for j in range(len(self.get_map_select()[i])):

        if self.get_map_select()[i][j] == 1:
            pygame.draw.rect(fenetre, (0, 0, 0), (j * x_space, i * y_space, 30, 30))
            pygame.draw.circle(fenetre, (255, 255, 255), (int(j * x_space + (x_space/2)), int(i * y_space + (y_space/2))), 5)#Ici, on calcule la position de départ x et y et on ajoute la moitié pour que la boule soit centrée

        elif self.get_map_select()[i][j] == 2:
            pygame.draw.rect(fenetre, (0, 0, 0), (j * x_space, i * y_space, 30, 30))
            pygame.draw.circle(fenetre, (255, 255, 255), (int(j * x_space + (x_space/2)), int(i * y_space + (y_space/2))), 10)


        elif self.get_map_select()[i][j] == 3:
            pygame.draw.rect(fenetre, self.get_couleur(), (j * x_space, i * y_space, 30, 30))

        elif self.get_map_select()[i][j] == 4:
                      pygame.draw.rect(fenetre, (255, 255, 255), (j * x_space, i * y_space, 30, 30))

  def game_finish(self, objet_pacman):
    """
    Vérifie les conditions de fin de jeu et met à jour les attributs en conséquence.

    @arguments:
        self (object): L'instance de la classe à laquelle cette méthode appartient.
        objet_pacman (object): L'objet représentant le personnage principal du jeu.

    Returns:
        bool: True si le jeu est terminé, False sinon.
    """
    if objet_pacman.get_touch() == True and objet_pacman.get_vie() < 1:
      objet_pacman.set_win(False)
      self.set_map_select(self.get_map_origin())
      return True

    for i in range(len(self.get_map_select())):
        if 1 in self.get_map_select()[i]:
           return False
    objet_pacman.set_win(True)
    self.set_map_select(self.get_map_origin())
    return True