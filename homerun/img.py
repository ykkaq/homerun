# “Ç‚İ‚Ş‰æ‘œ‚ğ‚Ü‚Æ‚ß‚½py

import pygame
from homerun import screen

# ‰æ‘œ“Ç‚İ‚İ
ground = pygame.image.load("pct/ground.png").convert()
pitcher = pygame.image.load("pct/baseball_pitcher_woman_fix.png").convert_alpha()
pitcher = pygame.transform.smoothscale(pitcher, (122, 150)) #orgnSize = 732*800
ball = pygame.image.load("pct/baseball_ball.png").convert_alpha()
ball = pygame.transform.smoothscale(ball, (20, 20))
bat = pygame.image.load("pct/sport_baseball_bat.png").convert_alpha()
bat = pygame.transform.rotozoom(bat, -55 ,0.22) #orgnSize = 479*610

ball_rect = ball.get_rect()

# ‰æ‘œˆÚ“®
def disp(screen, ballC, curse):
  screen.blit(ground,[0,0])
  screen.blit(pitcher,[550,10])
  screen.blit(bat,[curse.x,curse.y])
  screen.blit(ball,[ballC.x,ballC.y]) 