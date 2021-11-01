import pygame
from pygame.locals import *
import sys
import os

imgGround = pygame.image.load("pct/ground.png")
imgPitcher = pygame.image.load("pct/baseball_pitcher_woman_fix.png")
imgPitcher = pygame.transform.smoothscale(imgPitcher, (122, 150)) #orgn = 732*800
imgBall = pygame.image.load("pct/baseball_ball.png")
imgBall = pygame.transform.smoothscale(imgBall, (20, 20))
imgBat = pygame.image.load("pct/sport_baseball_bat.png")
imgBat = pygame.transform.rotozoom(imgBat, -50 ,0.22) #orgn_size = 479*610

def main():
    pygame.init()

    pygame.display.set_caption("テスト")
    screen = pygame.display.set_mode((1200,900))
    clock = pygame.time.Clock()
    
    ball_y = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

  
        screen.blit(imgGround,[0,0])
        screen.blit(imgPitcher,[550,10])
        screen.blit(imgBall,[600,ball_y])
        screen.blit(imgBat,[500,650])
        pygame.display.update()
        clock.tick(30)
        ball_y = (ball_y + 10) % 900


        
if __name__ == "__main__":
    main()

