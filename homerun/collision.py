# -*- coding: shift-jis -*-

import numpy as np
from numpy.lib.function_base import angle

from sansho import *
import data

# 2 coordinates to 1 numpy.aray
def generateVector(a: coordinate, b: coordinate):
  x = a.x - b.x
  y = a.y - b.y
  return np.array([x, y])

# 当たり判定
def collision(ballPoint: np.ndarray, circulRadius ,vecStart: np.ndarray, vecEnd: np.ndarray):
  # ベクトル生成
  start2end = vecEnd - vecStart #バットの"グリップ"から"先"へのベクトル
  start2point = ballPoint - vecStart #"バットのグリップ"から"球の中心"へのベクトル
  end2point = ballPoint - vecEnd  #"バットの先"から"球の中心"へのベクトル

  limitAngle_xy = np.radians(0)
  limitAngle_xz = np.radians(0)
  
  normS2E = np.linalg.norm(start2end)
  normS2P = np.linalg.norm(start2point)

  S2E_xy = np.delete(start2end, 2)
  S2E_xz = np.delete(start2end, 1)
  S2P_xy = np.delete(start2point, 2)
  S2P_xz = np.delete(start2point, 1)

  angle_xy = np.arccos( np.dot(S2E_xy, S2P_xy) / np.linalg.norm(S2E_xy) / np.linalg.norm(S2P_xy))
  angle_xz = np.arccos( np.dot(S2E_xz, S2P_xz) / np.linalg.norm(S2E_xz) / np.linalg.norm(S2P_xz))


  if(normS2E > normS2P and angle_xy < limitAngle_xy and angle_xz < limitAngle_xz):
    return True

'''
  # 円の中心と線分の最短距離を導出
  unitS2E = start2end / np.linalg.norm(start2end) #ベクトルの単位化
  vec2point = np.linalg.norm(np.cross(unitS2E, start2point)) #球の中心とバットベクトルの距離
  
  #最短距離と半径の比較
  if(vec2point > circulRadius):
    return False  
  else:
    #線分ベクトルと，線分の両端から円の中心ベクトルの内積
    dot1 = np.inner(unitS2E, start2point)
    dot2 = np.inner(unitS2E, end2point)

    ## 各ノルム
    normS2E = np.linalg.norm(start2end)
    normS2P = np.linalg.norm(start2point)
    normE2P = np.linalg.norm(end2point)

    ## 線分ベクトルと両端ベクトルの角度
    angle1 = np.arccos(dot1/normS2E/normS2P)
    angle2 = np.arccos(dot2/normS2E/normS2P)

    #各角度の鋭角判定
    flag1 = True if np.degrees(angle1) < 90 else False
    flag2 = True if np.degrees(angle2) < 90 else False
    
    print(np.degrees(angle1), np.degrees(angle2))

    if(flag1 ^ flag2):
      return True
    elif(normS2P < circulRadius or normE2P < circulRadius):
      return True
    else:
      return False

'''


# ボールがバットに当たった場所. return 割合．
def hitPoint(point: np.ndarray ,vecStart: np.ndarray , vecEnd: np.ndarray):
  # ベクトル生成
  start2end = vecEnd - vecStart #バットの"グリップ"から"先"へのベクトル
  start2point = point - vecStart #"バットのグリップ"から"球の中心"へのベクトル

  # 次元調整
  start2end = np.delete(start2end, 2)
  start2point = np.delete(start2point, 2)

  # s2eを基準とした基底ベクトルの生成
  baseVect = np.concatenate([np.matrix(start2end).T, rotate(90) @ np.matrix(start2end).T], 1) #2x2dim

  # s2pを,s2eとそれを90度回転させたベクトルの方向にわける
  solve = np.linalg.solve(baseVect, start2point.T)
  
  return solve[0], solve[1]

  
def hitAngle(ballCenterPoint: np.ndarray, vecStart: np.ndarray, vecEnd: np.ndarray):
  start2end = vecEnd - vecStart #バットの"グリップ"から"先"へのベクトル
  start2point = ballCenterPoint - vecStart #"バットのグリップ"から"球の中心"へのベクトル

  # x,yベクトルのみにする
  S2E_xy = np.delete(start2end, 2)
  S2P_xy = np.delete(start2point, 2)

  # angle = arccos(S2E_xy ・ S2P_xy / |S2E_xy| / |S2P_xy|)
  angle_xy = np.arccos( np.dot(S2E_xy, S2P_xy) / np.linalg.norm(S2E_xy) / np.linalg.norm(S2P_xy))

  return angle_xy
