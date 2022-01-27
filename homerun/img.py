# -*- coding: shift-jis -*-
# 読み込む画像をまとめたpy

import pygame
import math

from sansho import * 
from data import screen

# 画像読み込み
## フィールド
ground = pygame.image.load("pct/ground.png").convert_alpha()
outground = pygame.image.load("pct/outground.png").convert_alpha()

## 投手
pitcher = pygame.image.load("pct/baseball_pitcher_woman_fix.png").convert_alpha()
pitcher = pygame.transform.smoothscale(pitcher, (122, 150)) #org

bodyball = pygame.image.load("pct/ball/baseball_ball.png").convert_alpha()
ballShadow = pygame.image.load("pct/ball/baseball_ball_shadow.png").convert_alpha()

shadowDistance = 50

## memo: バットは-135 to 45


def dispInground():
  screen.blit(ground,[0,0])
  screen.blit(pitcher,[550,10])


def dispOutground():
  screen.blit(outground,[0,0])

'''
def dispBall():
  # ボールの影の調整
  ballRect = ball.get_rect(center = (ballCenterPosition[0], ballCenterPosition[1]))
  ballShadowRect = ball.get_rect(center = (ballCenterPosition[0], ballCenterPosition[1] + shadowDistance))
  screen.blit(ball, ballRect)
  screen.blit(ballShadow, ballShadowRect)
'''


# バットのスイング
class batSprite(pygame.sprite.Sprite):
  def __init__ (self, x, y):
    pygame.sprite.Sprite.__init__(self)
    picFile = "pct/bat/sport_baseball_bat_" #画像ファイルパスの素
    self.imgScale = 0.3

    self.images = list() #画像リスト
    self.numOfImg = 5 #画像数
    self.index = 0  #画像index
    self.indexCount = 0 #画像indexカウント
    self.divSwingSpeed = 3  #バットのスイングスピード（1[frame] / divSwingSpeed） 
    self.batShadow = pygame.image.load("pct/bat/sport_baseball_bat_shadow.png").convert_alpha()
    self.batShadow = pygame.transform.rotozoom(self.batShadow, 0, self.imgScale)
    self.batGuide = pygame.image.load("pct/bat/sport_baseball_bat_guide.png").convert_alpha()
    self.batGuide = pygame.transform.rotozoom(self.batGuide, 0, self.imgScale)

    for i in range(self.numOfImg):
      batFile = picFile + str(i+1) + '.png'
      self.images.append(pygame.image.load(batFile).convert_alpha())
      self.images[i] = pygame.transform.rotozoom(self.images[i], 0, self.imgScale)

    self.width = self.images[0].get_width()
    self.height = self.images[0].get_height()
    self.image = self.images[self.index]

  def draw(self, screen, mouse):
    self.rect = self.image.get_rect(center = (mouse.x, mouse.y))
    self.shadowRect = self.image.get_rect(center = (mouse.x, mouse.y + shadowDistance))
    screen.blit(self.batShadow, self.shadowRect)
    screen.blit(self.batGuide, self.rect)
    screen.blit(self.image, self.rect)


  def update(self):
    self.index = math.floor(self.indexCount / self.divSwingSpeed)
    if self.index < self.numOfImg-1:
      self.indexCount += 1
    self.image = self.images[self.index]


  def reset(self):
    self.indexCount = 0
    self.index = 0
    self.image = self.images[self.index]


# 

