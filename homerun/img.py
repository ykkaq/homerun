# -*- coding: shift-jis -*-
# �ǂݍ��މ摜���܂Ƃ߂�py

import pygame
import math

from sansho import * 
from data import screen

# �摜�ǂݍ���
## �t�B�[���h
ground = pygame.image.load("pct/ground.png").convert_alpha()
outground = pygame.image.load("pct/outground.png").convert_alpha()

## ����
pitcher = pygame.image.load("pct/baseball_pitcher_woman_fix.png").convert_alpha()
pitcher = pygame.transform.smoothscale(pitcher, (122, 150)) #org

bodyball = pygame.image.load("pct/ball/baseball_ball.png").convert_alpha()
ballShadow = pygame.image.load("pct/ball/baseball_ball_shadow.png").convert_alpha()

shadowDistance = 50

## memo: �o�b�g��-135 to 45


def dispInground():
  screen.blit(ground,[0,0])
  screen.blit(pitcher,[550,10])


def dispOutground():
  screen.blit(outground,[0,0])

'''
def dispBall():
  # �{�[���̉e�̒���
  ballRect = ball.get_rect(center = (ballCenterPosition[0], ballCenterPosition[1]))
  ballShadowRect = ball.get_rect(center = (ballCenterPosition[0], ballCenterPosition[1] + shadowDistance))
  screen.blit(ball, ballRect)
  screen.blit(ballShadow, ballShadowRect)
'''


# �o�b�g�̃X�C���O
class batSprite(pygame.sprite.Sprite):
  def __init__ (self, x, y):
    pygame.sprite.Sprite.__init__(self)
    picFile = "pct/bat/sport_baseball_bat_" #�摜�t�@�C���p�X�̑f
    self.imgScale = 0.3

    self.images = list() #�摜���X�g
    self.numOfImg = 5 #�摜��
    self.index = 0  #�摜index
    self.indexCount = 0 #�摜index�J�E���g
    self.divSwingSpeed = 3  #�o�b�g�̃X�C���O�X�s�[�h�i1[frame] / divSwingSpeed�j 
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

