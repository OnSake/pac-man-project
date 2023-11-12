#-------------------- PROJET PAC MAN --------------------#

#--------------- PAC MAN ---------------#

#---------- IMPORT ----------#

import pygame 
pygame.init()
from pygame.locals import *


#---------- CLASS ----------#

class Pacman:
    def __init__(self, vie, pos_x, pos_y, orientation = "None"):
        self.__vie__ = vie
        self.__pos_x__ = pos_x
        self.__pos_y__ = pos_y
        self.__can_eat__ = False
        self.__orientation__ = orientation
        self.__score__ = 0
        self.__check_collision__ = [False, False, False, False]
        self.__touch__ = False
        self.__win__ = False

    #-------- Get et Set --------#
    def get_win(self):
        return self.__win__

    def set_win(self, valeur):
        self.__win__ = valeur

    def get_touch(self):
        return self.__touch__

    def set_touch(self, valeur):
        self.__touch__ = valeur

    def get_collision(self, index):
        return self.__check_collision__[index]

    def set_collision(self, index, valeur):
        self.__check_collision__[index] = valeur

    def get_vie(self):
        return self.__vie__

    def set_vie(self, valeur):
        self.__vie__ += valeur

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

    def get_score(self):
        return self.__score__

    def set_score(self, valeur):
        self.__score__ += valeur


    #-------- Méthodes --------#

    def draw(self, surface):
        """
    Cette fonction est utilisée pour dessiner un personnage (probablement Pac-Man) sur une surface spécifiée en fonction de son orientation.

    @arguments:
        self: L'instance de l'objet PacMan ou du personnage que vous souhaitez dessiner.
        surface: La surface (généralement une fenêtre de jeu) sur laquelle le personnage doit être dessiné.

    @remarques:
    - Cette fonction examine l'orientation du personnage (gauche, droite, haut, bas ou neutre) en fonction de laquelle elle choisit l'image appropriée à afficher.
    - Les images utilisées pour le personnage dépendent des variables globales 'pac_man_img', 'pac_man_img_neutre', etc., qui doivent être définies ailleurs dans votre code.
    - Lorsque l'orientation est "top" ou "bottom", la fonction effectue des rotations d'image pour afficher le personnage dans la direction correcte.
    - Lorsque l'orientation est "left", la fonction effectue une inversion horizontale de l'image pour afficher le personnage dans la direction correcte.

    
    Cette fonction est essentielle pour afficher correctement le personnage dans un jeu et doit être appelée régulièrement pour mettre à jour l'apparence du personnage en fonction de son orientation.
        """
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
        """
    Cette fonction est responsable de déplacer un objet dans un environnement de jeu. Elle vérifie la position actuelle
    de l'objet, son orientation et les éventuelles collisions, puis effectue le déplacement en conséquence.

    Conditions de déplacement :
    - Si la position en x de l'objet est inférieure à -30, l'objet est déplacé à la position 900 pour simuler un rebond à droite.
    - Si la position en x de l'objet est supérieure à 910, l'objet est déplacé à la position -20 pour simuler un rebond à gauche.
    - Selon l'orientation de l'objet (gauche, haut, droite, bas) et les informations de collision, l'objet peut être déplacé
      ou son mouvement peut être restreint.

    Les fonctions utilisées dans cette méthode sont des méthodes de l'objet actuel, telles que get_posx(), set_posx(),
    get_orientation(), get_collision(), add_posx(), add_posy(), min_posx(), min_posy(). Il est recommandé de consulter
    la documentation de ces méthodes pour une compréhension approfondie de leur fonctionnement.

    Remarques :
    - L'objet est autorisé à se déplacer horizontalement (posx) ou verticalement (posy) en fonction de son orientation et
      de la détection de collision.
    - Si aucune condition de collision ou d'orientation n'est remplie, les positions de l'objet en x et y ne sont pas modifiées.

        """

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
        """
    Cette fonction permet de vérifier les collisions entre un objet représenté par une instance de la classe à laquelle cette méthode appartient
    et une carte de jeu.

    @arguments :
    - self : L'objet lui-même, une instance de la classe à laquelle cette méthode appartient.
    - ecran : Une liste contenant les dimensions de l'écran de jeu, généralement au format [largeur, hauteur].
    - map : Une matrice représentant la carte de jeu où chaque case contient une valeur indiquant la nature de l'obstacle ou du terrain.

    Attributs mis à jour :
    - Collision en direction de la droite (indice 2) : Indique s'il y a une collision à droite de l'objet.
    - Collision en direction de la gauche (indice 0) : Indique s'il y a une collision à gauche de l'objet.
    - Collision en direction du haut (indice 1) : Indique s'il y a une collision en haut de l'objet.
    - Collision en direction du bas (indice 3) : Indique s'il y a une collision en bas de l'objet.

    Remarque :
    Les collisions sont détectées en fonction de la position de l'objet par rapport à la carte de jeu et de son orientation.

        """
        num1 = ecran[1]//32
        num2 = ecran[0]//30

        self.set_collision(0, False)
        self.set_collision(1, False)
        self.set_collision(2, False)
        self.set_collision(3, False)

        if map[self.get_posy()//num1][self.get_posx() // num2] < 3:
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
        """
    Vérifie et met à jour le score du joueur en fonction de sa position sur l'écran et la carte du jeu.

    @arguments:
    - self: L'objet représentant le joueur.
    - ecran: Une liste ou un tuple contenant les dimensions de l'écran sous la forme (largeur, hauteur).
    - map: Une liste à deux dimensions représentant la carte du jeu. Cette carte contient des valeurs binaires où 1 signifie un élément collectible, et 0 signifie qu'il a déjà été collecté.

    Description:
    Cette fonction vérifie la position actuelle du joueur sur l'écran et détermine s'il est en train de collecter un élément sur la carte du jeu. Si la position du joueur est dans les limites de l'écran (0 < self.get_posx() < 900), la fonction examine la case correspondante sur la carte du jeu (map) pour voir si elle contient un élément collectible (valeur 1). Si c'est le cas, le score du joueur est augmenté de 10 points, et la case de la carte du jeu est mise à zéro pour indiquer que l'élément a été collecté.
        """
        num1 = ecran[1]//32
        num2 = ecran[0]//30

        if 0 < self.get_posx() < 900 : #Eviter le out of range
            if map[self.get_posy() // num1][self.get_posx() // num2] == 1:
                self.set_score(10)
                map[self.get_posy() // num1][self.get_posx() // num2] = 0
            
            
    def check_malade(self, ecran, map):
        """
    Vérifie si le personnage est sur une case malade de la carte et effectue des actions en conséquence.

    Cette fonction prend en compte la position du personnage sur l'écran (ecran) et la carte du jeu (map) pour déterminer s'il se trouve sur une case malade.
    
    @arguments :
        - ecran (tuple) : Un tuple contenant les coordonnées (x, y) de l'écran où se trouve le personnage.
        - map (list) : Une liste bidimensionnelle représentant la carte du jeu, où chaque case contient une valeur numérique (2 pour une case malade, 0 pour une case vide, etc.).

    Actions effectuées :
        - Si la position du personnage est à l'intérieur des limites de l'écran (0 < self.get_posx() < 900), la fonction vérifie la case correspondante sur la carte (map).
        - Si la case sur la carte est égale à 2, cela signifie que le personnage se trouve sur une case malade.
        - Dans ce cas, la fonction définira la capacité du personnage à manger sur True en utilisant "self.set_can_eat(True)".
        - Elle augmentera également le score du personnage de 50 points en utilisant "self.set_score(50)".
        - Elle mettra à jour la valeur de la case sur la carte en la mettant à 0 pour indiquer que la case a été "mangée" ou "traitée".

        """
        num1 = ecran[1]//32
        num2 = ecran[0]//30
        if 0 < self.get_posx() < 900 : #Eviter le out of range
            if map[self.get_posy() // num1][self.get_posx() // num2] == 2:
                self.set_can_eat(True)
                self.set_score(50)
                map[self.get_posy() // num1][self.get_posx() // num2] = 0
        

    def check_eat_ghost(self, objet_fantome, ecran, ghost_eat_object ):
        """
    Vérifie si le personnage du jeu peut manger un fantôme.

    Cette fonction prend en compte plusieurs conditions pour déterminer si le personnage du jeu peut manger un fantôme. Les paramètres de la fonction sont utilisés comme suit :
    
    @arguments:
        objet_fantome (Fantome): L'objet représentant le fantôme à vérifier.
        ecran (tuple): Un tuple contenant les dimensions de l'écran de jeu (largeur, hauteur).
        ghost_eat_object (objet_sonore): Un objet sonore à jouer lorsque le personnage mange un fantôme.

    Conditions de vérification:
    - Si le fantôme est malade et se déplace vers la droite et le personnage est suffisamment proche horizontalement, le personnage mange le fantôme et gagne des points.
    - Si le fantôme est malade et se déplace vers la gauche et le personnage est suffisamment proche horizontalement, le personnage mange le fantôme, mais perd une vie.
    - Si le fantôme est malade et se déplace vers le haut et le personnage est suffisamment proche verticalement, le personnage mange le fantôme, mais perd une vie.
    - Si le fantôme est malade et se déplace vers le bas et le personnage est suffisamment proche verticalement, le personnage mange le fantôme, mais perd une vie.
    - Si le fantôme est malade et se trouve à proximité horizontale et verticale du personnage, le personnage mange le fantôme, mais perd une vie.
    - Si le fantôme n'est pas malade, mais se trouve à proximité du personnage dans la même cellule de la grille de jeu, le personnage perd une vie et est marqué comme touché.

    Notes:
    - La fonction met également à jour la position du fantôme, le remet au centre de l'écran et redémarre son mouvement si le personnage le mange.

        """
        num1 = ecran[1]//32
        num2 = ecran[0]//30

        if objet_fantome.get_malade() == True:

            if objet_fantome.get_orientation() == "right":
                if objet_fantome.get_posx() - 25 <= self.get_posx() <= objet_fantome.get_posx() + 50 and objet_fantome.get_posy() - 25 <= self.get_posy() <= objet_fantome.get_posy() + 25:
                    ghost_eat_object.play()
                    self.set_score(200)
                    objet_fantome.set_malade(False)
                    objet_fantome.set_posx(ecran[0]//2)
                    objet_fantome.set_posy(ecran[1]//2)
                    objet_fantome.set_start_movement(True)

            elif objet_fantome.get_orientation() == "left":
                if objet_fantome.get_posx() - 50 <= self.get_posx() <= objet_fantome.get_posx() + 25 and objet_fantome.get_posy() - 25 <= self.get_posy() <= objet_fantome.get_posy() + 25:
                    ghost_eat_object.play()
                    self.set_score(200)
                    objet_fantome.set_malade(False)
                    objet_fantome.set_posx(ecran[0]//2)
                    objet_fantome.set_posy(ecran[1]//2)
                    objet_fantome.set_start_movement(True)
            
            elif objet_fantome.get_orientation() == "top":
                if objet_fantome.get_posx() - 25 <= self.get_posx() <= objet_fantome.get_posx() + 25 and objet_fantome.get_posy() - 50 <= self.get_posy() <= objet_fantome.get_posy() + 25:
                    ghost_eat_object.play()
                    self.set_score(200)
                    objet_fantome.set_malade(False)
                    objet_fantome.set_posx(ecran[0]//2)
                    objet_fantome.set_posy(ecran[1]//2)
                    objet_fantome.set_start_movement(True)

            elif objet_fantome.get_orientation() == "bottom":
                if objet_fantome.get_posx() - 25 <= self.get_posx() <= objet_fantome.get_posx() + 25 and objet_fantome.get_posy() - 25 <= self.get_posy() <= objet_fantome.get_posy() + 50:
                    ghost_eat_object.play()
                    self.set_score(200)
                    objet_fantome.set_malade(False)
                    objet_fantome.set_posx(ecran[0]//2)
                    objet_fantome.set_posy(ecran[1]//2)
                    objet_fantome.set_start_movement(True)


            if  objet_fantome.get_posx() - 25 <= self.get_posx() <= objet_fantome.get_posx() + 25 and objet_fantome.get_posy() - 25 <= self.get_posy() <= objet_fantome.get_posy() + 25:
                ghost_eat_object.play()
                self.set_score(200)
                objet_fantome.set_malade(False)
                objet_fantome.set_posx(ecran[0]//2)
                objet_fantome.set_posy(ecran[1]//2)
                objet_fantome.set_start_movement(True)


        else:
                if self.get_posx()//num2 == objet_fantome.get_posx()//num2 and self.get_posy()//num1 == objet_fantome.get_posy()//num1:
                    self.set_vie(-1)
                    self.set_touch(True)
                
       

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