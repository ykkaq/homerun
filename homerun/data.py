# -*- coding: shift-jis -*-

import pygame
#import img

# 初期化とか
screenWidth = 1200 #画面横
screenHeight = 900 #画面縦
screen = pygame.display.set_mode((screenWidth,screenHeight))  #ウィンドウの大きさ指定

#　仮
'''
class ball():
  def __int__(self, img):
    self.objectCenterPoint = np.array([0, 0, 0])
    self.dispCenterPoint = np.array([0, 0])
    self.vector = np.array([0, 0, 0])
    self.imageSize = 20
    self.image = pygame.transform.smoothscale(img, (imgSize, imgSize))
    self.magnification

  def move(self):
    self.centerPoint += self.vector

  def disp(self, magnification):
    self.ballImg = pygame.transform.rotozoom(self.image, 0, magnification)


class uniteBall():
  class bodyBall():
    def __init__(self, img.bodyball):
      super.__init__()


  def __init__(self):
    self.ball = ball(img.ball)
    self.shadow = ball(img.ballShadow)

class collision():




class ball():
  def __init__(self):
    self.centerPoint = np.array([0, 0, 0])
    self.vector = np.array([0, 0, 0])
    self.flyingPosition = np.array([0, 0, 0])

    self.magnification = 1
    self.imgSize = 20
    self.shadowDistance = 50
    self.ballImg = pygame.transform.smoothscale(img.ball, (imgSize, imgSize))
    self.ballShadowImg = pygame.transform.smoothscale(img.ballShadow, (imgSize, imgSize))

  def move(self):
    self.centerPoint += self.vector

  def disp(self, magnification):
    self.ballImg = pygame.transform.rotozoom(self.ballImg, 0, magnification)
    self.ballImg = pygame.transform.rotozoom(self.ballImg, 0, magnification)


    # 画像を正方形で管理
    ballRect = self.ballImg.get_rect(center = (self.centerPosition[0], self.centerPosition[1]))
    ballShadowRect = self.ballImg.get_rect(center = (self.centerPosition[0], self.centerPosition[1] + self.shadowDistance))
    # 画像表示
    screen.blit(self.ballImg, ballRect)
    screen.blit(self.ballShadowImg, ballShadowRect)
'''

