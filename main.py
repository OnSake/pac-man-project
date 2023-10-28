#-------------------- PROJET PAC MAN --------------------#

#--------------- MAIN ---------------#

#---------- IMPORT ----------#
import pygame 
pygame.init()
from pygame.locals import *
import sys
import time
from math import pi
from PacmanClass import Pacman
from map_1 import map 
from FantomeClass import Fantome


ecran = 900, 960
fenetre = pygame.display.set_mode(ecran)


#---------- VARIABLE ----------#
pac_man =  Pacman(1, 60, 60, 10)
fantome_red = Fantome(ecran[0]//2, ecran[1]//2, 0, 'red', (ecran[0]//2, ecran[1]//2), 'right')
fantome_orange = Fantome(ecran[0]//2, ecran[1]//2, 0, 'orange', (ecran[0]//2, ecran[1]//2), 'right')
fantome_blue = Fantome(ecran[0]//2, ecran[1]//2, 0, 'blue', (ecran[0]//2, ecran[1]//2), 'right')
fantome_pink = Fantome(ecran[0]//2, ecran[1]//2, 0, 'pink', (ecran[0]//2, ecran[1]//2), 'right')
fantomes = [fantome_red, fantome_orange, fantome_blue, fantome_pink]

fantome_pink.set_malade(True)

police = pygame.font.SysFont("alef" ,15)



map_1 = map
couleur_ligne = (120, 132, 240)



# ------------ MAP ------------#
def dessiner_map():
   y_space = ecran[0]//30 #On crée des maps en 30x32 donc on divise la largeur de l'écran par 30
   x_space = ecran[1]//32 #On crée des maps en 30x32 donc on divise la hauteur de l'écran par 32

   #On lit le tableau par liste, puis par élément. Donc par ligne puis par colonne
   for i in range(len(map_1)):
      for j in range(len(map_1[i])):

        if map_1[i][j] == 1:
            pygame.draw.rect(fenetre, (0, 0, 0), (j * x_space, i * y_space, 30, 30))
            pygame.draw.circle(fenetre, (255, 255, 255), (j * x_space + (x_space/2), i * y_space + (y_space/2)), 5) #Ici, on calcule la position de départ x et y et on ajoute la moitié pour que la boule soit centrée
        elif map_1[i][j] == 2:
            pygame.draw.rect(fenetre, (0, 0, 0), (j * x_space, i * y_space, 30, 30))
            pygame.draw.circle(fenetre, (255, 255, 255), (j * x_space + (x_space/2), i * y_space + (y_space/2)), 10)

        elif map_1[i][j] == 3:
           pygame.draw.rect(fenetre, couleur_ligne, (j * x_space, i * y_space, 29, 29))

        elif map_1[i][j] == 9:
                      pygame.draw.rect(fenetre, (255, 255, 255), (j * x_space, i * y_space, 30, 30))





while True:

    fenetre.fill([0,0,0])
    dessiner_map()
    image_score = police.render("Score : " + str(pac_man.get_score()), 1, (255, 0, 0))

    # fenetre.blit(image_pt_de_vie, (50, 50))
    fenetre.blit(image_score, (100, 0))
    pygame.display.flip()

    pac_man.check_collision(ecran, map_1)
    pac_man.move()
    pac_man.draw(fenetre)
    pac_man.check_score(ecran, map_1)

    for i in range(len(fantomes)):
        fantomes[i].mvt()
        fantomes[i].draw(fenetre)



    # routine pour pouvoir fermer «proprement» la fenêtre Pygame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()    

    # Bouger le PAC MAN
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                pac_man.set_orientation("top")
            elif event.key == K_RIGHT:
                pac_man.set_orientation("right")
            elif event.key == K_DOWN:
                pac_man.set_orientation("bottom")
            elif event.key == K_LEFT:
                pac_man.set_orientation("left")


    pygame.display.update()
    time.sleep(0.1)

pygame.quit() 