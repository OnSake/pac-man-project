#-------------------- PROJET PAC MAN --------------------#

#--------------- END SCREEN ---------------#

#---------- IMPORT ----------#

import pygame
pygame.init()
import sys

#---------- FONCTION ----------#



def end_screen(win_statut, score, ecran, fenetre):
  """
    Affiche un écran de fin de jeu avec le résultat et des boutons de réessai et de sortie.

    @arguments:
    win_statut (bool): Indique si le joueur a gagné (True) ou perdu (False).
    score (int): Le score obtenu par le joueur.
    ecran (tuple): Un tuple contenant les dimensions de l'écran (largeur, hauteur).
    fenetre (pygame.Surface): La surface de la fenêtre de jeu où l'écran de fin sera affiché.
    police (pygame.Font): La police de caractères utilisée pour le texte.

    @returns:
    bool: True si le joueur choisit de réessayer, sinon False.

    Remarques:
    Cette fonction affiche un écran de fin de jeu avec un message de victoire ou de défaite en fonction de win_statut.
    Elle affiche également le score du joueur et des boutons de réessai et de sortie.
    La fonction renvoie True si le joueur choisit de réessayer en cliquant sur le bouton de réessai,
    sinon elle renvoie False si le joueur choisit de quitter en cliquant sur le bouton de sortie.
    La fonction s'exécute dans une boucle infinie tant que l'écran de fin est ouvert. Pour quitter, l'utilisateur peut fermer la fenêtre.
    """

  title_font = pygame.font.Font("Fonts/NEW UPDATED VERSION/horizon.otf" ,60)
  score_font = pygame.font.Font("Fonts/NEW UPDATED VERSION/horizon.otf" ,60)
  text_font = pygame.font.Font("Fonts/NEW UPDATED VERSION/horizon.otf" ,20)

  end_text_win = title_font.render("Gagné", 1, (255, 199, 0)) 
  end_text_lose = title_font.render("Perdu", 1, (255, 199, 0))
  text = text_font.render("Vous avez fait", 1, (255, 255, 255)) 
  score_text = score_font.render(str(score) + " points", 1 ,(255, 255, 255))
  
  retry_button = pygame.image.load('Texture/Buttons/Retry_Button.png')
  retry_button_pressed = pygame.image.load('Texture/Buttons/Retry_Button_pressed.png')
  quit_button = pygame.image.load('Texture/Buttons/Quit_Button.png')
  quit_button_pressed = pygame.image.load('Texture/Buttons/Quit_Button_pressed.png')

  retry_button_rect = retry_button.get_rect()
  quit_button_rect = quit_button.get_rect()


  #Position du Rect Retry_Button
  retry_button_rect.x = 112
  retry_button_rect.y = 600
  #Position du Rect Quit_Button
  quit_button_rect.x = 531
  quit_button_rect.y = 600


  while True:
    fenetre.fill([0,23,80])

    
    if win_statut: 
        end_text = end_text_win
        fenetre.blit(end_text, (280, 255))
    else : 
        end_text = end_text_lose
        fenetre.blit(end_text, (280, 255))
    fenetre.blit(text, (315, 380))
    fenetre.blit(score_text, (210, 440))
    
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
            