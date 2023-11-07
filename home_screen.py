import pygame
pygame.init()
import sys

#Code couleur 1) = #00113B 2) = #004F89



def home_screen(ecran, fenetre):
  """
      Affiche l'écran d'accueil du jeu Pac-Man.

      Cette fonction crée un écran d'accueil pour le jeu Pac-Man en utilisant Pygame.

      @arguments :
      - ecran (tuple) : Un tuple contenant les dimensions de l'écran du jeu (largeur, hauteur).
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

  police = pygame.font.Font("Fonts/NEW UPDATED VERSION/horizon.otf" ,30)
  police_1 = pygame.font.Font("Fonts/NEW UPDATED VERSION/horizon.otf" ,15)


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
        
   
      
