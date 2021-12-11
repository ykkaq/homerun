import numpy as np
from sansho import *

# 2 coordinates to 1 numpy.aray
def generateVector(a: coordinate, b: coordinate):
  x = a.x - b.x
  y = a.y - b.y
  return np.matrix([x, y])

# �����蔻��
def collision(point: coordinate, circulRadius ,vecStart: coordinate, vecEnd: coordinate):
  # �x�N�g������
  start2end = generateVector(vecEnd, vecStart) 
  start2point = generateVector(point, vecStart)
  end2point = generateVector(point, vecEnd)
    
  # �~�̒��S�Ɛ����̍ŒZ�����𓱏o
  unitS2E = start2end / np.linalg.norm(start2end)
  vec2point = abs(np.cross(unitS2E, start2point))

  #�ŒZ�����Ɣ��a�̔�r
  if(vec2point > circulRadius):
    return False
  else:
    #�����x�N�g���ƁC�����̗��[����~�̒��S�x�N�g���́C����
    dot1 = np.inner(unitS2E, start2point)
    dot2 = np.inner(unitS2E, end2point)

    ## �e�P�ʃx�N�g��
    normS2E = np.linalg.norm(start2end)
    normS2P = np.linalg.norm(start2point)
    normE2P = np.linalg.norm(end2point)

    ## �����x�N�g���Ɨ��[�x�N�g���̊p�x
    angle1 = np.arccos(dot1/normS2E/normS2P)
    angle2 = np.arccos(dot2/normS2E/normS2P)

    #�e�p�x�̉s�p����
    flag1 = True if np.degrees(angle1) < 90 else False
    flag2 = True if np.degrees(angle2) < 90 else False

    if(flag1 ^ flag2):
      return True
    elif(normS2P < circulRadius or normE2P < circulRadius):
      return True
    else:
      return False


# �{�[�����o�b�g�ɓ��������ꏊ. return �����D
def hitPoint(point: coordinate,vecStart: coordinate, vecEnd: coordinate):
  # �x�N�g������
  start2end = generateVector(vecEnd, vecStart)
  start2point = generateVector(point, vecStart)

  # s2e����Ƃ������x�N�g���̐���
  baseVect = np.concatenate([start2end.T, rotate(90)*(start2end.T)],1)

  # s2p��,s2e�Ƃ����90�x��]�������x�N�g���̕����ɂ킯��
  solve = np.linalg.solve(baseVect, start2point.T)
  
  return solve[0]