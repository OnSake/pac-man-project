import pygame
pygame.init()
import sys

ecran = 900, 960
fenetre = pygame.display.set_mode(ecran)


bg_img = pygame.image.load('')


def home_screen():
   pass

while True:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.display.quit()
        sys.exit()

            
      
