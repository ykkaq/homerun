import numpy as np
from sansho import *

# 2 coordinates to 1 numpy.aray
def generateVector(a: coordinate, b: coordinate):
  x = a.x - b.x
  y = a.y - b.y
  return np.matrix([x, y])

# 当たり判定
def collision(point: coordinate, circulRadius ,vecStart: coordinate, vecEnd: coordinate):
  # ベクトル生成
  start2end = generateVector(vecEnd, vecStart) 
  start2point = generateVector(point, vecStart)
  end2point = generateVector(point, vecEnd)
    
  # 円の中心と線分の最短距離を導出
  unitS2E = start2end / np.linalg.norm(start2end)
  vec2point = abs(np.cross(unitS2E, start2point))

  #最短距離と半径の比較
  if(vec2point > circulRadius):
    return False
  else:
    #線分ベクトルと，線分の両端から円の中心ベクトルの，内積
    dot1 = np.inner(unitS2E, start2point)
    dot2 = np.inner(unitS2E, end2point)

    ## 各単位ベクトル
    normS2E = np.linalg.norm(start2end)
    normS2P = np.linalg.norm(start2point)
    normE2P = np.linalg.norm(end2point)

    ## 線分ベクトルと両端ベクトルの角度
    angle1 = np.arccos(dot1/normS2E/normS2P)
    angle2 = np.arccos(dot2/normS2E/normS2P)

    #各角度の鋭角判定
    flag1 = True if np.degrees(angle1) < 90 else False
    flag2 = True if np.degrees(angle2) < 90 else False

    if(flag1 ^ flag2):
      return True
    elif(normS2P < circulRadius or normE2P < circulRadius):
      return True
    else:
      return False


# ボールがバットに当たった場所. return 割合．
def hitPoint(point: coordinate,vecStart: coordinate, vecEnd: coordinate):
  # ベクトル生成
  start2end = generateVector(vecEnd, vecStart)
  start2point = generateVector(point, vecStart)

  # s2eを基準とした基底ベクトルの生成
  baseVect = np.concatenate([start2end.T, rotate(90)*(start2end.T)],1)

  # s2pを,s2eとそれを90度回転させたベクトルの方向にわける
  solve = np.linalg.solve(baseVect, start2point.T)
  
  return solve[0]