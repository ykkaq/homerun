import pygame

from sansho import *
from data import screen, screenHeight, screenWidth
import img

ballSetPosition_y = 50
ballCenterPosition = np.array([600, ballSetPosition_y, 0]) #ボール座標

class ball:
  ## ボール画像
  ballImg = pygame.image.load("pct/ball/baseball_ball.png").convert_alpha()
  ballImg = pygame.transform.smoothscale(ballImg, (20, 20))
  ## ボールの影画像
  ballShadowImg = pygame.image.load("pct/ball/baseball_ball_shadow.png").convert_alpha()
  ballShadowImg = pygame.transform.smoothscale(ballShadowImg, (20, 20))

  def __init__(self):
    self.centerPosition = np.array([screenWidth/2, 50, 0])
    self.vector = np.array([0, 0, 0])

    self.width = self.ballImg.get_width()
    

  def dispBall(self):
    # 影の調整 (max(z) = 1 とする)
    shadowDistance = 50
    # 画像を正方形で管理
    ballRect = self.ball.get_rect(center = (self.centerPosition[0], self.centerPosition[1]))
    ballShadowRect = img.ball.get_rect(center = (self.centerPosition[0], self.centerPosition[1] + shadowDistance))
    # 画像表示
    screen.blit(img.ball, ballRect)
    screen.blit(img.allShadow, ballShadowRect)

  def hitBallInground(self):
    self.vector = np.array([-5, 0, 0])
    self.centerPosition = (self.enterPosition + self.vector)



def outgroundFlag(ball):
  if(ball.centerPosition[0] < 0 or ball.centerPosition[0] > screenWidth or ball.centerPosition[1] < 0 or ball.centerPosition[1] > screenHeight):
    return True
  else:
    return False



# 外野のシーンに移るか判定
def outground():
  if(ballCenterPosition[0] < 0 or ballCenterPosition[0] > homerun.screenWidth or ballCenterPosition[1] < 0 or ballCenterPosition[1] > homerun.screenHeight):
    return True
  else:
    return False

# 投球ボールの移動計算
def sample():
  ballSpeed = 5

  ballCenterPosition[1] = ((ballCenterPosition[1] + ballSpeed) % homerun.screenHeight)

# 打ったボールの移動計算
def hitBallHome():
  ballSpeed = -5
  ballCenterPosition[1] = ((ballCenterPosition[1] + ballSpeed))


# 打ったボールの飛距離
def hitBall(hitSpot, hitAngle):
  # (x,y) = (v0 t + cos(t), v0 t + 1/2 v t^2)
  # d(x,y)/dt = v0 - sint, v0 + 

  # 高さx奥行きの2次元の飛距離 & 左右の角度 -> 極座標表示
  #hitSpot -> 飛距離, hitAngle -> 左右のブレ
  # とりあえず，線形とする.

  # 高さ（ボールの拡縮だけ実装してみる）

  maxDistance = 150

  hitDistance = maxDistance * ( 1 - np.abs(hitSpot -0.8) ) * (1 - hitAngle) 

  print(hitDistance)

