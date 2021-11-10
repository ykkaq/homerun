import pygame
from pygame.locals import *
import sys
import os

imgGround = pygame.image.load("pct/ground.png")
imgPitcher = pygame.image.load("pct/baseball_pitcher_woman_fix.png")
imgPitcher = pygame.transform.smoothscale(imgPitcher, (122, 150)) #orgnSize = 732*800
imgBall = pygame.image.load("pct/baseball_ball.png")
imgBall = pygame.transform.smoothscale(imgBall, (20, 20))
imgBat = pygame.image.load("pct/sport_baseball_bat.png")
imgBat = pygame.transform.rotozoom(imgBat, -50 ,0.22) #orgnSize = 479*610


class coordinate:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  def add(self,num):
    self+=num

def disp(screen, ball, curse):
  screen.blit(imgGround,[0,0])
  screen.blit(imgPitcher,[550,10])
  screen.blit(imgBat,[curse.x,curse.y])
  screen.blit(imgBall,[ball.x,ball.y]) 


def main():
  pygame.init()

  ## 変数宣言
  width = 1200 #画面横
  height = 900 #画面縦
  m = [width/2,100] #マウス(x,y)座標
  curse = coordinate(width/2,100)
  ball = coordinate(600,0)

  pygame.display.set_caption("テスト")
  screen = pygame.display.set_mode((width,height))
  clock = pygame.time.Clock()
  
  pygame.mixer.init(frequency = 44100)    # 初期設定
  pygame.mixer.music.load("bgm/main.mid")     # 音楽ファイルの読み込み
  pygame.mixer.music.play(-1)              # 音楽の再生回数(1回)

  #pygame.mouse.set_visible(False) # カーソル非表示（）
  pygame.mouse.set_visible(True)
  pygame.mouse.set_pos((curse.x,curse.y))  # カーソル初期位置


  ## while内使用変数
  owl_plus = True
  owl_count = [0,-5,5]
  owl_vari = 20

  while True:
    ball_y = disp(screen, ball, curse)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == MOUSEMOTION:
        curse.x,curse.y = event.pos
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()

    
    pygame.display.update()
    clock.tick(60)

    ## 座標変更
    ### ボール
    if(owl_plus):
      ball.x+=owl_vari
      owl_count[0]+=1
    else:
      ball.x-=owl_vari
      owl_count[0]-=1
    if(owl_count[0]==owl_count[1]):
      owl_plus=True
    if(owl_count[0]==owl_count[2]):
      owl_plus=False

    ball.y = (ball.y + 10) % 900

    print(curse.x,curse.y)
    print()

        
if __name__ == "__main__":
    main()
