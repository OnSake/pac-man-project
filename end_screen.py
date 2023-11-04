import pygame
pygame.init()
import time
import sys

ecran = 900, 960
fenetre = pygame.display.set_mode(ecran)
police = pygame.font.SysFont("dubai" ,30)

win = True
score = 80
fenetre.fill([0,23,80])
end_text_win = police.render("Bravo ! Vous avez réussi le niveau", 1, (110, 255, 51)) 
end_text_lose = police.render("Perdu", 1, (255, 51, 51)) 
score_text = police.render("Vous avez fait " + str(score) + " points", 1 ,(255, 255, 255))
retry_button = pygame.transform.scale(pygame.image.load('Texture/Buttons/Retry_Button.png'), (300, 300))
quit_button = pygame.transform.scale(pygame.image.load('Texture/Buttons/Quit_Button.png'), (300, 300))



if win: 
    end_text = end_text_win
    fenetre.blit(end_text, (ecran[0]//2 - 175, ecran[1]//2 - 150))
else : 
    end_text = end_text_lose
    fenetre.blit(end_text, (ecran[0]//2 - 50, ecran[1]//2 - 150))
fenetre.blit(score_text, (ecran[0]//2 - 125, ecran[1]//2 - 100))

retry_button_rect = retry_button.get_rect()
quit_button_rect = quit_button.get_rect()


while True:

  # if retry_button.get_rect().collidepoint(pygame.mouse.get_pos()):
  #   retry_button = pygame.transform.scale(pygame.image.load('Texture/Buttons/Retry_Button_Pressed.png'), (300, 300))
  #   print('ok')
  # if retry_button.get_rect().collidepoint(pygame.mouse.get_pos()):
  #   quit_button = pygame.transform.scale(pygame.image.load('Texture/Buttons/Quit_Button_Pressed.png'), (300, 300))
  #   print('ok')


  fenetre.blit(retry_button, (0.5*(ecran[0]//5), ecran[1]*(2/5)))
  fenetre.blit(quit_button, (2.7*(ecran[0]//5), ecran[1]*(2/5)))
  pygame.display.flip() 

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.display.quit()
      sys.exit()

    elif event.type == pygame.MOUSEBUTTONDOWN:
       if retry_button_rect.collidepoint(pygame.mouse.get_pos()):
          print('retry')  
    
       
