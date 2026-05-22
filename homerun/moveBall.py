# -*- coding: utf-8 -*-
import pygame
import random

from sansho import *
from data import *
import img

ballPosition = np.array([0, 0, 0])

class ball:
  def __init__(self, x, y, z):
    self.centerPosition = np.array([x, y, z])
    self.vector = np.array([0, 0, 0])
    self.shadowDistance = 50
    self.ballImg = pygame.transform.smoothscale(img.bodyball, (20, 20))
    self.ballShadowImg = pygame.transform.smoothscale(img.ballShadow, (20, 20))
    self.width = self.ballImg.get_width()
    self.landingPosition = np.array([screenWidth/2, 780, 0])
    self.flightDistance = 0.0
    self.flightProgress = 0.0
    self.flightSpeed = 1.5
    self.outgroundStartY = screenHeight - 80
    self.outgroundTopY = screenHeight / 6
    self.outgroundBottomY = screenHeight * 5 / 6
    self.outgroundEndY = self.outgroundBottomY
    self.defaultShadowDistance = self.shadowDistance
    self.pitchSpeed = random.uniform(3, 8)
    self.isLanded = False

   
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

  def ballOutground(self):
    if self.isLanded:
      self.dispBall()
      return True

    self.flightProgress += self.flightSpeed
    progressRate = min(self.flightProgress / self.flightDistance, 1.0)
    self.centerPosition[0] = screenWidth / 2
    self.centerPosition[1] = self.outgroundStartY + (self.outgroundEndY - self.outgroundStartY) * progressRate

    remainingDistance = max(self.flightDistance - self.flightProgress, 0.0)
    if remainingDistance <= 10:
      self.shadowDistance = self.defaultShadowDistance * (remainingDistance / 10)
    else:
      self.shadowDistance = self.defaultShadowDistance

    if self.flightProgress >= self.flightDistance:
      self.centerPosition = self.landingPosition.copy()
      self.isLanded = True
      self.shadowDistance = 0

    self.dispBall()
    return self.isLanded

  def startOutground(self, flightDistance):
    self.flightDistance = max(flightDistance, 1)
    self.flightProgress = 0.0
    self.shadowDistance = self.defaultShadowDistance
    distanceRate = np.clip((self.flightDistance - 50) / 100, 0.0, 1.0)
    self.outgroundEndY = self.outgroundBottomY + (self.outgroundTopY - self.outgroundBottomY) * distanceRate
    self.centerPosition = np.array([screenWidth/2, self.outgroundStartY, 0])
    self.landingPosition = np.array([screenWidth/2, self.outgroundEndY, 0])
    self.vector = np.array([0, -8, 0])
    self.isLanded = False

  def resetPitch(self):
    self.centerPosition = np.array([screenWidth/2, 50, 0])
    self.vector = np.array([0, 0, 0])
    self.shadowDistance = self.defaultShadowDistance
    self.flightProgress = 0.0
    self.flightDistance = 0.0
    self.isLanded = False
    self.pitchSpeed = random.uniform(3, 8)

  def throwBall(self):
    self.vector = np.array([0, self.pitchSpeed, 0])
    self.centerPosition += self.vector
    if self.centerPosition[1] > screenHeight:
      self.centerPosition[1] = 0
      self.pitchSpeed = random.uniform(3, 8)


def outgroundFlag(ball):
  if(ball.centerPosition[0] < 0 or ball.centerPosition[0] > screenWidth or ball.centerPosition[1] < 0 or ball.centerPosition[1] > screenHeight):
    return True
  else:
    return False


# 打ったボールの飛距離
def flightDistance(hitDistance, ballRadius):
  grazeRate = min(hitDistance / ballRadius, 1.0)
  return 50 + 100 * grazeRate


def flyingPosition(hitPoint, hitAngle, ballClass):
  theta = 1 - abs(hitPoint - 0.8)
  ballPosition[0] += np.cos(hitAngle)
  ballPosition[1] += np.sin(hitAngle)
  ballPosition[2] = np.tan(theta) * ballPosition[0] - np.power(ballPosition[0] / np.cos(theta) / 2, 2)

  return ballPosition  
