# -*- coding: utf8 -*-

'''
作業メモ:12/8
- img.pyの変数で画像の位置を変えるやつ，pygameの機能で移動できそう？
'''

import pygame
from pygame import image
from pygame.locals import *
import sys
import os

import collision
import img
from sansho import coordinate

# 初期化とか
screenWidth = 1200 #画面横
screenHeight = 900 #画面縦
screen = pygame.display.set_mode((screenWidth,screenHeight))  #ウィンドウの大きさ指定


def main():
  pygame.init() #pygame初期化

  ## 変数宣言
  curse = coordinate(500,650) #マウス座標
  ballC = coordinate(600,0) #ボール座標

  pygame.display.set_caption("テスト") #ウィンドウネーム指定
  clock = pygame.time.Clock() #画面更新頻度
  
  pygame.mixer.init(frequency = 44100)    # 初期設定
  pygame.mixer.music.load("bgm/main.mid")     # 音楽ファイルの読み込み
  #pygame.mixer.music.play(-1)              # 音楽の再生回数(∞回)

  #pygame.mouse.set_visible(False) # カーソル非表示（）
  pygame.mouse.set_visible(True) 
  pygame.mouse.set_pos((curse.x,curse.y))  # カーソル初期位置


  ## while内使用変数
  owl_plus = True
  owl_count = [0,-5,5]
  owl_vari = 20
  font = pygame.font.Font(None, 100)  #　文字フォント


  ## 画面更新
  while True:
    pygame.display.update()
    clock.tick(60)

    img.disp(screen, ballC, curse)

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
    

    ## 当たり判定
    ### バット
    batGripEnd = coordinate(curse.x, curse.y + img.bat.get_height() /2)
    pygame.draw.line(screen, 'White', (batGripEnd.x, batGripEnd.y), (batGripEnd.x + img.bat.get_width(), batGripEnd.y),5)

    ### ボール
    ballCenterPosition = coordinate(ballC.x + img.ball.get_width()/2 , ballC.y + img.ball.get_height()/2)
    ballRadius = img.ball.get_width()/2
    pygame.draw.circle(screen, 'Red', (ballCenterPosition.x, ballCenterPosition.y), ballRadius ,width = 3)

    ### 本文



    ## 文字表示

    text = font.render("HIT", True, (0,0,0))
    screen.blit(text, [0, 0])# 文字列の表示位置


    ## 座標変更
    ### ボール
    '''
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
    '''
    
    ballC.y = (ballC.y + 5) % screenHeight
    #img.ball.top = (img.ball.top+5) % screenHeight

    print(curse.x,curse.y)
    print()


        
if __name__ == "__main__":
    main()
