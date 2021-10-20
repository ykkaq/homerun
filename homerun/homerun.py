import pygame
from pygame.locals import *
import sys
import os

imgGround = pygame.image.load("pct/ground.png")
imgPitcher = pygame.image.load("pct/baseball_pitcher_woman.png")
imgPitcher = pygame.transform.smoothscale(imgPitcher, (122, 150)) #orgn = 732*800


def main():
    pygame.init()
    pygame.display.set_caption("テスト")
    screen = pygame.display.set_mode((1200,900))
    clock = pygame.time.Clock()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.blit(imgGround,[0,0])
        screen.blit(imgPitcher,[550,10])
        pygame.display.update()
        clock.tick(30)
        
if __name__ == "__main__":
    main()

