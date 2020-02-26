import pygame
import random
import sys
import math
import Player
import Tower
gameBoard = pygame.image.load('images/gameBoard.png')

player = Player
pygame.init()
win = pygame.display.set_mode((1280,720))

def drawGame():
    win.blit(gameBoard, (0,0))
    pygame.display.update()
def main():
    game_started = True
    while game_started:
        drawGame()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_started = False
main()
pygame.quit()