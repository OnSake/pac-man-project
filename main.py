#-------------------- PROJET PAC MAN --------------------#

#--------------- MAIN ---------------#

#---------- IMPORT ----------#
import pygame 
pygame.init()
from pygame.locals import *
import sys
import time

#---------- IMPORT CLASS ----------#
from Class.PacmanClass import Pacman
from Class.MapClass import Map
from Class.FantomeClass import Fantome


#---------- VARIABLE ----------#
ecran = 900, 960
fenetre = pygame.display.set_mode(ecran)
pygame.display.set_caption("Pac Man")



pac_man =  Pacman(1, 60, 60)
fantome_red = Fantome(ecran[0]//2+30, ecran[1]//2, 0, 'red', (ecran[0]//2, ecran[1]//2), 'right')
fantome_orange = Fantome(ecran[0]//2, ecran[1]//2, 0, 'orange', (ecran[0]//2, ecran[1]//2), 'left')
fantome_blue = Fantome(ecran[0]//2, ecran[1]//2, 0, 'blue', (ecran[0]//2, ecran[1]//2), 'top')
fantome_pink = Fantome(ecran[0]//2, ecran[1]//2, 0, 'pink', (ecran[0]//2, ecran[1]//2), 'bottom')
fantomes = [fantome_red, fantome_orange, fantome_blue, fantome_pink]


can_eat = False
police = pygame.font.SysFont("alef" ,30)

#Sound effects
original_sound = f'Musique/PacMan_Original_Theme.mp3'
pacman_dying_sound = f'Musique/PacMan_Dying.mp3'
pacman_eating_sound = f'Musique/PacMan-Eating.mp3'
pacman_eating_ghost_sound = f'Musique/PacMan_Eating_Ghost.mp3'


map = Map(1, (120, 132, 240))

pygame.mixer.music.load(original_sound)
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1, 0.5, 500)
# ------------ GAME ------------#

while map.game_finish(pac_man.get_vie()) == False:
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
        can_eat = True
        pygame.mixer.music.load(pacman_eating_sound)
        pygame.mixer.music.play(-1, 0.5, 500)
        tps_zero = pygame.time.get_ticks()
        pac_man.set_can_eat(False)


    if can_eat == True and (pygame.time.get_ticks() - tps_zero) <=8000 :
        for i in range(len(fantomes)):
            fantomes[i].set_malade(True)
        if (pygame.time.get_ticks() - tps_zero) >= 5000:
            for i in range(len(fantomes)):
                fantomes[i].set_finish_heal(True)
    else : 

        for i in range(len(fantomes)):
            fantomes[i].set_malade(False)
            can_eat = False
            fantomes[i].set_finish_heal(False)


    for i in range(len(fantomes)):
        pac_man.check_eat_ghost(fantomes[i].get_posx(), fantomes[i].get_posy(), ecran)
        fantomes[i].check_collision(ecran, map.get_map_select())
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