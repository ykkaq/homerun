import pygame

from sansho import *
from data import *
import img

ballPosition = np.array([0, 0, 0])

class ball:
  def __init__(self, x, y, z):
    self.centerPosition = np.array([x, y, z])
    self.vector = np.array([0, 0, 0])
    self.shadowDistance = 50
    self.ballImg = pygame.transform.smoothscale(img.ball, (20, 20))
    self.ballShadowImg = pygame.transform.smoothscale(img.ballShadow, (20, 20))
    self.width = self.ballImg.get_width()

   
  # 表示
  def dispBall(self):
    # 画像を正方形で管理
    ballRect = self.ballImg.get_rect(center = (self.centerPosition[0], self.centerPosition[1]))
    ballShadowRect = self.ballImg.get_rect(center = (self.centerPosition[0], self.centerPosition[1] + self.shadowDistance))
    # 画像表示
    screen.blit(self.ballImg, ballRect)
    screen.blit(self.ballShadowImg, ballShadowRect)

  def hitBallInground(self):
    self.vector = np.array([0, -10, 0])
    self.centerPosition += self.vector

  def hitBallOutground(self):
    # 影の調整 (0 <= z <= max) する
    defaultImgSize = 8

    self.ballImg = pygame.transform.smoothscale(img.ball, (defaultImgSize, defaultImagSize))
    self.ballShadowImg = pygame.transform.smoothscale(img.ballShadow, (defaultImgSize, defaultImagSize))
    
    magnification = (1+z)/50
    self.BallImag = pygame.transform.smoothscale(self.ballImg, 1, magnification)
    self.BallShadowImag = pygame.transform.smoothscale(self.ballImgShadow, 1, magnification)
    dispBall()

  def throwBall(self):
    self.vector = np.array([0, 5, 0])
    self.centerPosition += self.vector
    self.centerPosition[1] %= screenHeight


def outgroundFlag(ball):
  if(ball.centerPosition[0] < 0 or ball.centerPosition[0] > screenWidth or ball.centerPosition[1] < 0 or ball.centerPosition[1] > screenHeight):
    return True
  else:
    return False


# 打ったボールの飛距離
def flyingPosition(hitPoint, hitAngle, ballClass):
  theta = 1 - abs(hitPoint - 0.8)
  ballPosition[0] += np.cos(hitAngle)
  ballPosition[1] += np.sin(hitAngle)
  ballPosition[2] = np.tan(theta) * ballPosition[0] - np.power(ballPosition[0] / np.cos(theta) / 2, 2)

  return ballPosition  
