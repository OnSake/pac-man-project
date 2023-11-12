import pygame
pygame.init()
import sys

#Code couleur 1) = #00113B 2) = #004F89



def home_screen(fenetre):
  """
      Affiche l'écran d'accueil du jeu Pac-Man.

      Cette fonction crée un écran d'accueil pour le jeu Pac-Man en utilisant Pygame.

      @arguments :
      - fenetre (pygame.Surface) : La surface Pygame sur laquelle l'écran d'accueil sera affiché.

      @returns :
      - bool : Retourne True si le bouton "Play" est cliqué, indiquant que le joueur souhaite commencer le jeu.

      La fonction effectue les actions suivantes :
      1. Charge la police de caractères et la musique d'arrière-plan.
      2. Affiche le fond d'écran, le texte de bienvenue et les informations sur le projet.
      3. Affiche un bouton "Play" qui réagit au survol de la souris.
      4. Gère les événements, tels que la fermeture de la fenêtre ou le clic sur le bouton "Play".
      5. Arrête la musique lorsque le bouton "Play" est cliqué.
    """

  title_font = pygame.font.Font("Fonts/NEW UPDATED VERSION/horizon.otf" ,60)
  subtitle_font = pygame.font.Font("Fonts/NEW UPDATED VERSION/horizon.otf" ,45)
  text_font = pygame.font.Font("Fonts/NEW UPDATED VERSION/horizon.otf" ,25)



  play_button = pygame.image.load('Texture/Buttons/Play_Button.png')
  play_button_pressed = pygame.image.load('Texture/Buttons/Play_Button_Pressed.png')


  play_button_rect = play_button.get_rect()
  play_button_rect.x = 330
  play_button_rect.y = 480


  welcome_text = title_font.render("Welcome", 3,  (255, 199, 0))
  to_text = text_font.render("TO", 3, (255, 255, 255))
  pacman_text = subtitle_font.render("pacman", 3, ((255, 199, 0)))
  team_text = text_font.render("BY Jules - cédric - thibault", 1, (255, 255, 255))

  while True:
      fenetre.fill([0, 17, 59])
      fenetre.blit(welcome_text, (225, 145))
      fenetre.blit(to_text, (430, 258))
      fenetre.blit(pacman_text, (300, 316))
      fenetre.blit(team_text, (180, 765))
      
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
        
   
      
