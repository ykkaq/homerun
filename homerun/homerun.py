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

import collision
import img
from sansho import *

# 初期化とか
screenWidth = 1200 #画面横
screenHeight = 900 #画面縦
screen = pygame.display.set_mode((screenWidth,screenHeight))  #ウィンドウの大きさ指定


def main():
  pygame.init() #pygame初期化

  ## 変数宣言
  curse = coordinate(500,650) #マウス座標
  ballCenterPosition = coordinate(600,0) #ボール座標
  batDeg = 0

  pygame.display.set_caption("テスト") #ウィンドウネーム指定
  clock = pygame.time.Clock() #画面更新頻度
  
  pygame.mixer.init(frequency = 44100)    # 初期設定
  pygame.mixer.music.load("bgm/main.mid")     # 音楽ファイルの読み込み
  #pygame.mixer.music.play(-1)              # 音楽の再生回数(∞回)

  #pygame.mouse.set_visible(False) # カーソル非表示（）
  pygame.mouse.set_visible(True) 
  pygame.mouse.set_pos((curse.x,curse.y))  # カーソル初期位置


  ## while内使用変数
  fnt = [pygame.font.Font(None, 50)] #　文字フォント
  txt = []
  thp = ""
  thit = ""

  ## 画面更新
  while True:
    pygame.display.update()
    clock.tick(60)
    img.dispBase()

    batDeg = (batDeg + 1) % 360


    for event in pygame.event.get():
      ## バツボタン
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      ## マウス右クリ
      if event.type == MOUSEBUTTONDOWN and event.button == 1:
        tmc = fnt[0].render("Mouse Crick!", True, (0,0,0))
        screen.blit(tmc, [0,0])
      if event.type == MOUSEMOTION:
        curse.x,curse.y = event.pos
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()


    ## 当たり判定
    ### バット
    batGrip = coordinate(curse.x, curse.y)
    batEndPoint = coordinate(curse.x + img.batLeng, curse.y)
    G2Evec = collision.generateVector(batEndPoint, batGrip)
    G2ERotate = (rotate(-1*batDeg) * G2Evec.T)
    batEnd = crd2mat(batGrip) + G2ERotate.T
    batEnd = mat2crd(batEnd)

    ### ボール
    ballRadius = img.ball.get_width()/2
    

    ### 当たり判定.main
    if(collision.collision(ballCenterPosition, ballRadius, batGrip, batEnd)):
      # バットに当たった位置
      hitPoint = collision.hitPoint(ballCenterPosition, batGrip, batEnd)
      thp = str(hitPoint)
      time.sleep(0.5)
      # 文字表示
      thit = "HIT"
    else:
      thit = ""

    txt.append(fnt[0].render(thp, True, (0,0,0)))
    txt.append(fnt[0].render(thit, True, (0,0,0)))

    ## 座標変更
    ### ボール
    #img.ball.top = (img.ball.top+5) % screenHeight

    tms = str(curse.x)+" , "+str(curse.y)
    txt.append(fnt[0].render(tms, True, (0,0,0)))
    txt.append(fnt[0].render(str(batDeg), True, (0,0,0)))
    # 表示
    img.dispBat(batGrip, batDeg) 
    img.dispBall(ballCenterPosition)
    pygame.draw.line(screen, 'White', (batGrip.x, batGrip.y), (batEnd.x, batEnd.y)  ,5)
    pygame.draw.circle(screen, 'Red', (ballCenterPosition.x, ballCenterPosition.y), ballRadius ,width = 3)
    pygame.draw.circle(screen, 'Pink', (ballCenterPosition.x, ballCenterPosition.y), 2, width = 0)
    
    for i,t in enumerate(txt):
      screen.blit(t, [0,i*50])
    txt = []


        
if __name__ == "__main__":
    main()
