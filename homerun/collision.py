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

# �����蔻��
def collision(ballPoint: np.ndarray, circulRadius ,vecStart: np.ndarray, vecEnd: np.ndarray):
  # �x�N�g������
  start2end = vecEnd - vecStart #�o�b�g��"�O���b�v"����"��"�ւ̃x�N�g��
  start2point = ballPoint - vecStart #"�o�b�g�̃O���b�v"����"���̒��S"�ւ̃x�N�g��
  end2point = ballPoint - vecEnd  #"�o�b�g�̐�"����"���̒��S"�ւ̃x�N�g��

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
  # �~�̒��S�Ɛ����̍ŒZ�����𓱏o
  unitS2E = start2end / np.linalg.norm(start2end) #�x�N�g���̒P�ʉ�
  vec2point = np.linalg.norm(np.cross(unitS2E, start2point)) #���̒��S�ƃo�b�g�x�N�g���̋���
  
  #�ŒZ�����Ɣ��a�̔�r
  if(vec2point > circulRadius):
    return False  
  else:
    #�����x�N�g���ƁC�����̗��[����~�̒��S�x�N�g���̓���
    dot1 = np.inner(unitS2E, start2point)
    dot2 = np.inner(unitS2E, end2point)

    ## �e�m����
    normS2E = np.linalg.norm(start2end)
    normS2P = np.linalg.norm(start2point)
    normE2P = np.linalg.norm(end2point)

    ## �����x�N�g���Ɨ��[�x�N�g���̊p�x
    angle1 = np.arccos(dot1/normS2E/normS2P)
    angle2 = np.arccos(dot2/normS2E/normS2P)

    #�e�p�x�̉s�p����
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


# �{�[�����o�b�g�ɓ��������ꏊ. return �����D
def hitPoint(point: np.ndarray ,vecStart: np.ndarray , vecEnd: np.ndarray):
  # �x�N�g������
  start2end = vecEnd - vecStart #�o�b�g��"�O���b�v"����"��"�ւ̃x�N�g��
  start2point = point - vecStart #"�o�b�g�̃O���b�v"����"���̒��S"�ւ̃x�N�g��

  # ��������
  start2end = np.delete(start2end, 2)
  start2point = np.delete(start2point, 2)

  # s2e����Ƃ������x�N�g���̐���
  baseVect = np.concatenate([np.matrix(start2end).T, rotate(90) @ np.matrix(start2end).T], 1) #2x2dim

  # s2p��,s2e�Ƃ����90�x��]�������x�N�g���̕����ɂ킯��
  solve = np.linalg.solve(baseVect, start2point.T)
  
  return solve[0], solve[1]

  
def hitAngle(ballCenterPoint: np.ndarray, vecStart: np.ndarray, vecEnd: np.ndarray):
  start2end = vecEnd - vecStart #�o�b�g��"�O���b�v"����"��"�ւ̃x�N�g��
  start2point = ballCenterPoint - vecStart #"�o�b�g�̃O���b�v"����"���̒��S"�ւ̃x�N�g��

  # x,y�x�N�g���݂̂ɂ���
  S2E_xy = np.delete(start2end, 2)
  S2P_xy = np.delete(start2point, 2)

  # angle = arccos(S2E_xy �E S2P_xy / |S2E_xy| / |S2P_xy|)
  angle_xy = np.arccos( np.dot(S2E_xy, S2P_xy) / np.linalg.norm(S2E_xy) / np.linalg.norm(S2P_xy))

  return angle_xy
