# 読み込む画像をまとめたpy

import pygame
from homerun import screen,screenHeight
from sansho import * 
import moveBall

# 画像読み込み
ground = pygame.image.load("pct/ground.png").convert()
pitcher = pygame.image.load("pct/baseball_pitcher_woman_fix.png").convert_alpha()
pitcher = pygame.transform.smoothscale(pitcher, (122, 150)) #orgnSize = 732*800
ball = pygame.image.load("pct/baseball_ball.png").convert_alpha()
ball = pygame.transform.smoothscale(ball, (20, 20))
bat = pygame.image.load("pct/sport_baseball_bat.png").convert_alpha()
bat = pygame.transform.rotozoom(bat, 0 , 0.3)

batLeng = bat.get_width()/2

## memo: バットは-135 to 45

def dispBase():
  screen.blit(ground,[0,0])
  screen.blit(pitcher,[550,10])

def dispBat(batGrip: coordinate, angel):
  batRotate = pygame.transform.rotate(bat, angel)
  batRect = batRotate.get_rect(center = (batGrip.x, batGrip.y))
  screen.blit(batRotate, batRect)

def dispBall(ballCenter: coordinate):
  ballCenter = moveBall.sample(ballCenter)
  ballRect = ball.get_rect(center = (ballCenter.x, ballCenter.y))
  #ballRect.center = (ballCenter.x, ballCenter.y)
  screen.blit(ball, ballRect)
  pygame.draw.rect(screen,(0,80,0),ballRect,1)
  pygame.draw.circle(screen, 'orange', ballRect.center, 2, width = 0)
