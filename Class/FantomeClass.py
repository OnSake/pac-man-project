# Créé par thibault.rigallaud, le 16/10/2023 en Python 3.7
from random import randint
import pygame


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
        self.__start_movement__ = False

    #-------- Get et Set --------#
    def get_start_movement(self):
        return self.__start_movement__

    def set_start_movement(self, valeur):
        self.__start_movement__ = valeur

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

    def get_mort(self):
        return self.__mort__

    def set_mort(self, valeur):
        self.__mort__ = valeur

    #-------- Méthodes --------#

    def mvt(self):


            if self.get_orientation() == "left":
                self.min_posx(15)
            elif self.get_orientation() == "top":
                self.min_posy(15)
            elif self.get_orientation() == "right":
                self.add_posx(15)
            elif self.get_orientation() == "bottom":
                self.add_posy(15)


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


    def check_collision(self, ecran, map):
        liste_collision = [True, True, True, True] #R, L, T, B

        if self.check_collision_right(ecran, map) == True:
            liste_collision[0] = False
        else : liste_collision[0] = True

        if self.check_collision_left(ecran, map) == True:
            liste_collision[1] = False  
        else : liste_collision[1] = True  

        if self.check_collision_top(ecran, map) == True:
            liste_collision[2] = False  
        else : liste_collision[2] = True  

        if self.check_collision_bottom(ecran, map) == True:
            liste_collision[3] = False  
        else : liste_collision[3] = True  

        return liste_collision


    def change_direction(self, liste_collision):
        #R = 0, L = 1, T = 2, B = 3
        direction_possible = []
        if liste_collision[0] == False and self.get_orientation() == "right": 
            for i in range(len(liste_collision)):
                if i == 1 and liste_collision[i] == True:
                    direction_possible.append(1)

                if i == 2 and liste_collision[i] == True:
                    direction_possible.append(2)
                
                if i == 3 and liste_collision[i] == True: 
                    direction_possible.append(3)
        
        if liste_collision[1] == False and self.get_orientation() == "left": 
            for i in range(len(liste_collision)):
                if i == 0 and liste_collision[i] == True:
                    direction_possible.append(0)

                if i == 2 and liste_collision[i] == True:
                    direction_possible.append(2)
                
                if i == 3 and liste_collision[i] == True: 
                    direction_possible.append(3)
        
        if liste_collision[2] == False and self.get_orientation() == "top": 
            for i in range(len(liste_collision)):
                if i == 1 and liste_collision[i] == True:
                    direction_possible.append(1)

                if i == 0 and liste_collision[i] == True:
                    direction_possible.append(0)
                
                if i == 3 and liste_collision[i] == True: 
                    direction_possible.append(3)
        
        if liste_collision[3] == False and self.get_orientation() == "bottom": 
            for i in range(len(liste_collision)):
                if i == 1 and liste_collision[i] == True:
                    direction_possible.append(1)

                if i == 2 and liste_collision[i] == True:
                    direction_possible.append(2)
                
                if i == 0 and liste_collision[i] == True: 
                    direction_possible.append(0)

        if len(direction_possible) != 0:
            direction_random = direction_possible[randint(0, len(direction_possible) - 1)]
            if direction_random == 0:
                self.set_orientation("right")        
            elif direction_random == 1:
                self.set_orientation("left")
            elif direction_random == 2:
                self.set_orientation("top")
            elif direction_random == 3: 
                self.set_orientation("bottom")

    """
    def start_movement(self, ecran, map):
        self.set_orientation("top")
        if self.check_collision_top(ecran, map):
            if randint(0, 1) == 0: 
                self.set_orientation("right")
            else : self.set_orientation("left")
        self.set_start_movement(False)  
    """



    def add_posx(self, valeur):
        self.set_posx(self.get_posx() + valeur)

    def min_posx(self, valeur):
        self.set_posx(self.get_posx() - valeur)

    def add_posy(self, valeur):
        self.set_posy(self.get_posy() + valeur)

    def min_posy(self, valeur):
        self.set_posy(self.get_posy() - valeur)


    def check_collision_right(self, ecran, map):
        num1 = ecran[1]//32
        num2 = ecran[0]//30
        if map[self.get_posy()//num1][(self.get_posx() + 30)//num2] == 3:
            return True
        return False

    def check_collision_left(self, ecran, map):
        num1 = ecran[1]//32
        num2 = ecran[0]//30
        if map[self.get_posy()//num1][(self.get_posx() - 15)//num2] == 3:
            return True
        return False

    def check_collision_top(self, ecran, map):
        num1 = ecran[1]//32
        num2 = ecran[0]//30
        if map[(self.get_posy() - 15)//num1][self.get_posx()//num2] == 3:
            return True
        return False

    def check_collision_bottom(self, ecran, map):
        num1 = ecran[1]//32
        num2 = ecran[0]//30
        if map[(self.get_posy() + 30)//num1][self.get_posx()//num2] == 3:
            return True
        return False





fantome_1 = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/red.gif'), (25, 25))
fantome_2 = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/orange.gif'), (25, 25))
fantome_3 = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/blue.gif'), (25, 25))
fantome_4 = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/pink.gif'), (25, 25))
fantome_malade = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/malade.gif'), (25, 25))
fantome_malade_finish = pygame.transform.scale(pygame.image.load(f'Texture/Fantome/malade_finish.gif'), (25, 25))

fantome = [fantome_1, fantome_2, fantome_3, fantome_4, fantome_malade, fantome_malade_finish]