# -*- coding: utf8 -*-

'''
作業メモ:12/8
- img.pyの変数で画像の位置を変えるやつ，pygameの機能で移動できそう？
'''

import pygame
from pygame.locals import *
import sys
import numpy as np
import time
import os
from multiprocessing import Pool

from data import screen
import img
import moveBall
import collision
from sansho import *


def main():
  pygameInit()

  ## 変数宣言
  scene = 1
  curse = coordinate(500,650) #マウス座標
  pygame.mouse.set_pos((curse.x,curse.y))  # カーソル初期位置
  clock = pygame.time.Clock() #画面更新頻度
  batSprite = img.batSprite(curse.x, curse.y)
  hitPoint = 0
  hitAngle = 0  
  mouseRightClick = False


  ## while内使用変数
  fnt = [pygame.font.Font(None, 50)] #　文il字フォント
  txt = []
  hitFlag = False
  nextScene = scene
  print(scene, nextScene)
  

  ## 画面更新
  while True:
    pygame.display.update()
    clock.tick(60)
    img.dispInground()

    for event in pygame.event.get():
      ## バツボタン
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      ## マウス右クリ
      if event.type == MOUSEBUTTONDOWN and event.button == 1:
        mouseRightClick = True

      if event.type == MOUSEBUTTONUP and event.button == 1:
        mouseRightClick = False

      # マウスカーソル
      if event.type == MOUSEMOTION:
        curse.x,curse.y = event.pos
      # キー
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()
    
    # 場面表示
    if(scene == 0):
      print('0')
    elif(scene == 1):
      hitPoint, hitAngle, hitFlag = inground(mouseRightClick, hitFlag , batSprite , curse)
      nextScene = dispInground(hitFlag,  batSprite, curse)
    elif(scene == 2):
      dispOutground()
    else:
      exit()
        
    scene = nextScene

# pygame初期設定
def pygameInit():
  pygame.init() #pygame初期化

  pygame.display.set_caption("プニキ") #ウィンドウネーム指定
  
  pygame.mixer.init(frequency = 44100)    # 初期設定
  pygame.mixer.music.load("bgm/main.mid")     # 音楽ファイルの読み込み
  #pygame.mixer.music.play(-1)              # 音楽の再生回数(∞回)

  #pygame.mouse.set_visible(False) # カーソル非表示（）
  pygame.mouse.set_visible(True) 


# 内野処理
def inground(mouseRightClick, hitFlag,  batSprite, curse):
  ball = moveBall.ball() #ボール
  hitPoint = 0
  hitAngle = 0

  ## バットスイング操作
  if(mouseRightClick):
     batSprite.update()
  else:
     batSprite.reset()

  ## 当たり判定
  ### バット
  batGripPoint = np.array([curse.x, curse.y, 0]) #バットグリップの座標
  batEndPoint = np.array([curse.x + batSprite.width/2, curse.y, 0]) #バット先端の座標

  ### ボール
  ballRadius = (ball.width)/2

  if( batSprite.index == 3 and collision.collision(moveBall.ballCenterPosition, ballRadius, batGripPoint, batEndPoint)):
    hitFlag += True

    # バットに当たった位置
    hitPoint = collision.hitPoint(moveBall.ballCenterPosition, batGripPoint, batEndPoint)
    # バットの当たった角度
    hitAngle = collision.hitAngle(moveBall.ballCenterPosition, batGripPoint, batEndPoint)
    time.sleep(0.5)

    print(hitPoint, hitAngle)

  else:
    hitFlag += False

  return hitPoint, hitAngle, hitFlag


# 内野表示
def dispInground(hitFlag,  batSprite, curse):
  if(hitFlag): #打った後のシーン
    img.dispBall()
    batSprite.draw(screen, curse)
    moveBall.hitBallHome()

    # ボールがinground外にあるか
    if(moveBall.outground()):
      global scene
      moveBall.ballCenterPosition[0] = screenWidth/2
      moveBall.ballCenterPosition[1] = screenHeight/2
      return 2


  else:
    # ボールの座標変更
    moveBall.sample()
    
    # 表示
    img.dispBall()
    batSprite.draw(screen, curse)
  
  return 1

# 外野表示
def dispOutground():
  img.dispOutground()


def pygameWhileSetting():
  print('a')
  
        
if __name__ == "__main__":
    main()
