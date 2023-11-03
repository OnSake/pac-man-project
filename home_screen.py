import pygame
pygame.init()
import time
import sys

ecran = 900, 960
fenetre = pygame.display.set_mode(ecran)
police = pygame.font.SysFont("dubai" ,30)

win = False
score = 80
fenetre.fill([0,23,80])
end_text_win = police.render("Bravo ! Vous avez réussi le niveau", 1, (110, 255, 51)) 
end_text_lose = police.render("Perdu", 1, (255, 51, 51)) 
score_text = police.render("Vous avez fait " + str(score) + " points", 1 ,(255, 255, 255))

if win: 
    end_text = end_text_win
    fenetre.blit(end_text, (ecran[0]//2 - 200, ecran[1]//2 - 50))
else : 
    end_text = end_text_lose
    fenetre.blit(end_text, (ecran[0]//2 - 50, ecran[1]//2 - 50))
fenetre.blit(score_text, (ecran[0]//2 - 150, ecran[1]//2))
pygame.display.flip()
time.sleep(3)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.display.quit()
      sys.quit()
