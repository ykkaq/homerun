import pygame

from sansho import *
from data import screen, screenHeight, screenWidth
import img

ballSetPosition_y = 50
ballCenterPosition = np.array([600, ballSetPosition_y, 0]) #�{�[�����W

class ball:
  ## �{�[���摜
  ballImg = pygame.image.load("pct/ball/baseball_ball.png").convert_alpha()
  ballImg = pygame.transform.smoothscale(ballImg, (20, 20))
  ## �{�[���̉e�摜
  ballShadowImg = pygame.image.load("pct/ball/baseball_ball_shadow.png").convert_alpha()
  ballShadowImg = pygame.transform.smoothscale(ballShadowImg, (20, 20))

  def __init__(self):
    self.centerPosition = np.array([screenWidth/2, 50, 0])
    self.vector = np.array([0, 0, 0])

    self.width = self.ballImg.get_width()
    

  def dispBall(self):
    # �e�̒��� (max(z) = 1 �Ƃ���)
    shadowDistance = 50
    # �摜�𐳕��`�ŊǗ�
    ballRect = self.ball.get_rect(center = (self.centerPosition[0], self.centerPosition[1]))
    ballShadowRect = img.ball.get_rect(center = (self.centerPosition[0], self.centerPosition[1] + shadowDistance))
    # �摜�\��
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



# �O��̃V�[���Ɉڂ邩����
def outground():
  if(ballCenterPosition[0] < 0 or ballCenterPosition[0] > homerun.screenWidth or ballCenterPosition[1] < 0 or ballCenterPosition[1] > homerun.screenHeight):
    return True
  else:
    return False

# �����{�[���̈ړ��v�Z
def sample():
  ballSpeed = 5

  ballCenterPosition[1] = ((ballCenterPosition[1] + ballSpeed) % homerun.screenHeight)

# �ł����{�[���̈ړ��v�Z
def hitBallHome():
  ballSpeed = -5
  ballCenterPosition[1] = ((ballCenterPosition[1] + ballSpeed))


# �ł����{�[���̔򋗗�
def hitBall(hitSpot, hitAngle):
  # (x,y) = (v0 t + cos(t), v0 t + 1/2 v t^2)
  # d(x,y)/dt = v0 - sint, v0 + 

  # ����x���s����2�����̔򋗗� & ���E�̊p�x -> �ɍ��W�\��
  #hitSpot -> �򋗗�, hitAngle -> ���E�̃u��
  # �Ƃ肠�����C���`�Ƃ���.

  # �����i�{�[���̊g�k�����������Ă݂�j

  maxDistance = 150

  hitDistance = maxDistance * ( 1 - np.abs(hitSpot -0.8) ) * (1 - hitAngle) 

  print(hitDistance)

