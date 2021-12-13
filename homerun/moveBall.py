from sansho import *
import homerun

def sample(p: coordinate):
  p.y = (p.y + 5) % homerun.screenHeight
  return p
