#-------------------- PROJET PAC MAN --------------------#

#--------------- END SCREEN ---------------#

#---------- IMPORT ----------#

import pygame
pygame.init()
import sys

#---------- FONCTION ----------#

def end_screen(win_statut, score, ecran, fenetre, police):

  
  end_text_win = police.render("Bravo ! Vous avez réussi le niveau", 1, (110, 255, 51)) 
  end_text_lose = police.render("Perdu", 1, (255, 51, 51)) 
  score_text = police.render("Vous avez fait " + str(score) + " points", 1 ,(255, 255, 255))
  
  retry_button = pygame.image.load('Texture/Buttons/Retry_Button.png')
  retry_button_pressed = pygame.image.load('Texture/Buttons/Retry_Button_pressed.png')
  quit_button = pygame.image.load('Texture/Buttons/Quit_Button.png')
  quit_button_pressed = pygame.image.load('Texture/Buttons/Quit_Button_pressed.png')

  retry_button_rect = retry_button.get_rect()
  quit_button_rect = quit_button.get_rect()


  #Position du Rect Retry_Button
  retry_button_rect.x = ecran[0]//5
  retry_button_rect.y = ecran[0]//1.8
  #Position du Rect Quit_Button
  quit_button_rect.x = 2.5*(ecran[0]//5)
  quit_button_rect.y = ecran[0]//1.8


  while True:
    fenetre.fill([0,23,80])

    
    if win_statut: 
        end_text = end_text_win
        fenetre.blit(end_text, (ecran[0]//2 - 175, ecran[1]//2 - 150))
    else : 
        end_text = end_text_lose
        fenetre.blit(end_text, (ecran[0]//2 - 50, ecran[1]//2 - 150))
    fenetre.blit(score_text, (ecran[0]//2 - 125, ecran[1]//2 - 100))
    
    if retry_button_rect.collidepoint(pygame.mouse.get_pos()):
      fenetre.blit(retry_button_pressed, retry_button_rect)
    else :  fenetre.blit(retry_button, retry_button_rect)
    
    if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
      fenetre.blit(quit_button_pressed, quit_button_rect)
    else : fenetre.blit(quit_button, quit_button_rect)

    pygame.display.flip() 

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.display.quit()
        sys.exit()

      elif event.type == pygame.MOUSEBUTTONDOWN:
        if retry_button_rect.collidepoint(pygame.mouse.get_pos()):
          return True
        if quit_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.display.quit()
            sys.exit()
            
      
