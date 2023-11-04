#-------------------- PROJET PAC MAN --------------------#

#--------------- MAIN ---------------#

#---------- IMPORT ----------#
import pygame
from pygame.locals import *
import sys
import time
from random import randint
pygame.init()

#---------- IMPORT CLASS ----------#
from Class.PacmanClass import Pacman
from Class.MapClass import Map
from Class.FantomeClass import Fantome


#---------- VARIABLE ----------#
ecran = 900, 960
fenetre = pygame.display.set_mode(ecran)
pygame.display.set_caption("Pac Man")
pacman_x_spawn, pacman_y_spawn = 60, 60

#---------- OBJETS ----------#
pac_man =  Pacman(1, pacman_x_spawn, pacman_y_spawn)
fantome_red = Fantome(ecran[0]//2, ecran[1]//2, 0, 'red', (ecran[0]//2, ecran[1]//2), 'right')
fantome_orange = Fantome(ecran[0]//2, ecran[1]//2, 0, 'orange', (ecran[0]//2, ecran[1]//2), 'left')
fantome_blue = Fantome(ecran[0]//2, ecran[1]//2, 0, 'blue', (ecran[0]//2, ecran[1]//2), 'top')
fantome_pink = Fantome(ecran[0]//2, ecran[1]//2, 0, 'pink', (ecran[0]//2, ecran[1]//2), 'bottom')
fantomes = [fantome_red, fantome_orange, fantome_blue, fantome_pink]
can_eat = False


map = Map(1, (120, 132, 240))
police = pygame.font.SysFont("dubai" ,30)

#---------- SOUNDS EFFECTS ----------#
pacman_original_sound = pygame.mixer.Sound('Musique\PacMan_Original_Theme.mp3')
pacman_dying_sound = pygame.mixer.Sound('Musique\PacMan_Dying.mp3')
pacman_eating_sound = pygame.mixer.Sound('Musique\PacMan-Eating.mp3')
pacman_eating_ghost_sound = pygame.mixer.Sound('Musique\PacMan_Eating_Ghost.mp3')

pac_man.set_touch(False)


#------------ GAME ------------#

    #-------- GAME SETUP --------#

game_statut = True
pygame.mixer.music.set_volume(0.2)
pacman_original_sound.play(-1)


pac_man.set_posx(pacman_x_spawn), pac_man.set_posy(pacman_y_spawn)
pac_man.set_posx(60), pac_man.set_posy(60)


for i in range(len(fantomes)):
    fantomes[i].set_start_movement(True)

    #-------- GAME LAUNCHED --------#
def game(game_statut, can_eat):
    while game_statut:
        
        if map.game_finish(pac_man):
            game_statut = False

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



        #Quand pacman est touché par un fantome sans powerBall
        if pac_man.get_touch():
            pacman_dying_sound.play()
            pacman_original_sound.stop()
            pac_man.set_posx(pacman_x_spawn)
            pac_man.set_posy(pacman_y_spawn)
            pac_man.set_orientation("None")
            for i in range(len(fantomes)):
                fantomes[i].set_start_movement(True)
                fantomes[i].set_posx(ecran[0]//2)
                fantomes[i].set_posy(ecran[1]//2)

            time.sleep(pacman_dying_sound.get_length())
            pac_man.set_touch(False)
            pacman_original_sound.play()


        if pac_man.get_can_eat():
            pacman_eating_sound.play(-1)
            pacman_original_sound.set_volume(0.0)
            can_eat = True
            tps_zero = pygame.time.get_ticks()
            pac_man.set_can_eat(False)
        
        
        #Timer pour manger 
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
            if fantomes[i].get_start_movement(): #Si le fantome est mort, il revient donc à son point de respawn et doit aller vers le haut
                if fantomes[i].check_collision_top(ecran, map.get_map_select()) == False:
                    fantomes[i].set_orientation("top")
                else :     
                    if randint(0, 1) == 0:
                        fantomes[i].set_orientation("right")
                    else : fantomes[i].set_orientation("left")  
                    fantomes[i].set_start_movement(False)
            fantomes[i].change_direction(fantomes[i].check_collision(ecran, map.get_map_select()))       
            fantomes[i].mvt()
            fantomes[i].draw(fenetre)
        

        # routine pour pouvoir fermer «proprement» la fenêtre Pygame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
        # Bouger le PAC MAN

            if event.type == KEYDOWN:
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
    
#------------ GAME SCREEN ------------#


game(game_statut, can_eat)    
pygame.mixer.stop()

#------------ END GAME SCREEN ------------#



game(game_statut, can_eat)    
pygame.mixer.stop()

#------------ END GAME SCREEN ------------#

fenetre.fill([0,23,80])
pac_man.set_win(True)
end_text_win = police.render("Bravo ! Vous avez réussi le niveau", 1, (110, 255, 51)) 
end_text_lose = police.render("Perdu", 1, (255, 51, 51)) 
score_text = police.render("Vous avez fait " + str(pac_man.get_score()) + " points", 1 ,(255, 255, 255))

if pac_man.get_win(): 
    end_text = end_text_win
else : end_text = end_text_lose
fenetre.blit(end_text, (ecran[0]//2 - 150, ecran[1]//2 - 50))
fenetre.blit(score_text, (ecran[0]//2 - 150, ecran[1]//2))
pygame.display.flip()
time.sleep(3)


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
