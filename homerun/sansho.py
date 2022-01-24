# memo:ファイル名は仮．後で変更する．
import numpy as np

# 座標クラス
class coordinate:
  def __init__(self,x,y):
    self.x = x
    self.y = y

def crdAdd(a: coordinate, b: coordinate):
  return coordinate(a.x + b.x , a.y + b.y)

def crdSub(a: coordinate, b: coordinate):
  return coordinate(a.x + b.x , a.y + b.y)

def rotate(theta):
  theta = np.radians(theta)
  ret = np.array([
    [np.cos(theta), -1*np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
  ])

  return ret

def crd2mat(a: coordinate):
  return np.numpy([a.x , a.y])

def mat2crd(m: np.array):
  return coordinate(m[0,0], m[0,1])