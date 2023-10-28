#-------------------- PROJET PAC MAN --------------------#

#--------------- MAIN ---------------#

#---------- IMPORT ----------#
import pygame 
pygame.init()
from pygame.locals import *
import sys
import time
from math import pi
from Class.PacmanClass import Pacman
from Class.MapClass import Map
from Class.FantomeClass import Fantome


ecran = 900, 960
fenetre = pygame.display.set_mode(ecran)


#---------- VARIABLE ----------#
pac_man =  Pacman(1, 60, 60)
fantome_red = Fantome(ecran[0]//2, ecran[1]//2, 0, 'red', (ecran[0]//2, ecran[1]//2), 'right')
fantome_orange = Fantome(ecran[0]//2, ecran[1]//2, 0, 'orange', (ecran[0]//2, ecran[1]//2), 'right')
fantome_blue = Fantome(ecran[0]//2, ecran[1]//2, 0, 'blue', (ecran[0]//2, ecran[1]//2), 'right')
fantome_pink = Fantome(ecran[0]//2, ecran[1]//2, 0, 'pink', (ecran[0]//2, ecran[1]//2), 'right')
fantomes = [fantome_red, fantome_orange, fantome_blue, fantome_pink]



police = pygame.font.SysFont("alef" ,30)



map = Map(1, (120, 132, 240))



# ------------ GAME ------------#

while True:

    fenetre.fill([0,0,0])
    image_score = police.render("Score : " + str(pac_man.get_score()), 1, (255, 255, 255))
    map.dessiner_map(ecran, fenetre)
    # fenetre.blit(image_pt_de_vie, (50, 50))
    fenetre.blit(image_score, (0, 0))
    pygame.display.flip()



    pac_man.check_collision(ecran, map.get_map_select())
    pac_man.move()
    pac_man.draw(fenetre)
    pac_man.check_score(ecran, map.get_map_select())
    pac_man.check_malade(ecran, map.get_map_select())

    if pac_man.get_can_eat():
        for i in range(len(fantomes)):
            fantomes[i].set_malade(True)
            #fantomes[i].finish_heal()


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