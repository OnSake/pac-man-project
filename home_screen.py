import pygame
pygame.init()
import sys

def home_screen(ecran, fenetre):
  police = pygame.font.SysFont("dubai", 50)
  police_1 = pygame.font.SysFont("dubai" ,20)

  musique = pygame.mixer.Sound('Musique/PacMan_Home_Screen.mp3')
  musique.set_volume(1)
  musique.play(-1, 0, 500)

  bg_img = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Texture/Background.jpg'), ecran), True, False)
  play_button = pygame.image.load('Texture/Buttons/Play_Button.png')
  play_button_pressed = pygame.image.load('Texture/Buttons/Play_Button_Pressed.png')


  play_button_rect = play_button.get_rect()
  play_button_rect.x = ecran[0]//2.75
  play_button_rect.y = ecran[1]//1.5


  project_text = police_1.render("Projet NSI", 1, (255, 255, 255))
  project_text_1 = police_1.render("Jules MULLER - Thibault REGALLAUD - Cédric GUIGNER", 1, (255, 255, 255))
  welcome_text = police.render("Bienvenue sur PACMAN", 3,  (255, 255, 0))
  while True:
      fenetre.blit(bg_img, (0, -100))
      fenetre.blit(welcome_text, (ecran[0]//3.5, 150))
      fenetre.blit(project_text, (0, 0))
      fenetre.blit(project_text_1, (0, 25))
      
      if play_button_rect.collidepoint(pygame.mouse.get_pos()):
        fenetre.blit(play_button_pressed, play_button_rect)
      else : fenetre.blit(play_button, play_button_rect)

      pygame.display.flip()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.display.quit()
          sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
          if play_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mixer.stop()
            return True
        
   
      
