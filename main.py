#-------------------- PROJET PAC MAN --------------------#

#--------------- MAIN ---------------#

#---------- IMPORT ----------#
import pygame
from pygame.locals import *
import sys
import time
pygame.init()

#---------- IMPORT CLASS ----------#
from Class.PacmanClass import Pacman
from Class.MapClass import Map
from Class.FantomeClass import Fantome


#---------- VARIABLE ----------#
ecran = 900, 960
fenetre = pygame.display.set_mode(ecran)
pygame.display.set_caption("Pac Man")



pac_man =  Pacman(2, 60, 60)
fantome_red = Fantome(ecran[0]//2, ecran[1]//2, 0, 'red', (ecran[0]//2, ecran[1]//2), 'right')
fantome_orange = Fantome(ecran[0]//2, ecran[1]//2, 0, 'orange', (ecran[0]//2, ecran[1]//2), 'left')
fantome_blue = Fantome(ecran[0]//2, ecran[1]//2, 0, 'blue', (ecran[0]//2, ecran[1]//2), 'top')
fantome_pink = Fantome(ecran[0]//2, ecran[1]//2, 0, 'pink', (ecran[0]//2, ecran[1]//2), 'bottom')
fantomes = [fantome_red, fantome_orange, fantome_blue, fantome_pink]


can_eat = False
police = pygame.font.SysFont("arial" ,30)

# ---- Sound effects ---- #
pacman_original_sound = pygame.mixer.Sound('Musique\PacMan_Original_Theme.mp3')
pacman_dying_sound = pygame.mixer.Sound('Musique\PacMan_Dying.mp3')
pacman_eating_sound = pygame.mixer.Sound('Musique\PacMan-Eating.mp3')
pacman_eating_ghost_sound = pygame.mixer.Sound('Musique\PacMan_Eating_Ghost.mp3')

pac_man.set_touch(False)
map = Map(1, (120, 132, 240))
#------------ GAME ------------#
    #-------- GAME SETUP --------#

pygame.mixer.music.set_volume(0.2)
pacman_original_sound.play(-1)

pac_man.set_posx(60), pac_man.set_posy(60)

for i in range(len(fantomes)):
    fantomes[i].set_orientation("top")

    #-------- GAME LAUNCHED --------#

while map.game_finish(pac_man.get_touch(), pacman_dying_sound) == False:
    
    fenetre.fill([0,0,0])
    image_score = police.render("Score : " + str(pac_man.get_score()), 1, (255, 255, 255))
    image_pt_de_vie = police.render("Vie : " + str(pac_man.get_vie()), 1, (255, 255, 255))
    map.dessiner_map(ecran, fenetre)
    fenetre.blit(image_pt_de_vie, (800, 0))
    fenetre.blit(image_score, (10, 0))
    pygame.display.flip()



    pac_man.check_collision(ecran, map.get_map_select())
    pac_man.move()
    pac_man.draw(fenetre)
    pac_man.check_score(ecran, map.get_map_select())
    pac_man.check_malade(ecran, map.get_map_select())


    if pac_man.get_can_eat():
        pacman_eating_sound.play(-1)
        pacman_original_sound.set_volume(0.0)
        can_eat = True
        tps_zero = pygame.time.get_ticks()
        pac_man.set_can_eat(False)

    if can_eat == True and (pygame.time.get_ticks() - tps_zero) <=8000 :
        for i in range(len(fantomes)):
            fantomes[i].set_malade(True)
        if (pygame.time.get_ticks() - tps_zero) >= 5000:
            for i in range(len(fantomes)):
                fantomes[i].set_finish_heal(True)
    else :

        pacman_original_sound.set_volume(1.0)
        pacman_eating_sound.stop()
        for i in range(len(fantomes)):
            fantomes[i].set_malade(False)
            can_eat = False
            fantomes[i].set_finish_heal(False)


    for i in range(len(fantomes)):
        pac_man.check_eat_ghost(fantomes[i], ecran, pacman_eating_ghost_sound)
        #fantomes[i].check_collision(ecran, map.get_map_select())
        fantomes[i].mvt()
        fantomes[i].draw(fenetre)
        fantomes[i].change_direction(fantomes[i].check_collision(ecran, map.get_map_select()))       
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