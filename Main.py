import pygame
import random
import sys
import math
import Player
import Tower
gameBoard = pygame.image.load('images/gameBoard.png')
menuImage = pygame.image.load('images/menuImage.png')
playButton = pygame.image.load('images/playButton.png')
settingsButton = pygame.image.load('images/settingsButton.png')
quitButton = pygame.image.load('images/quitButton.png')

class Menu:
    def __init__(self):
        pass
    def showMenu(self):
        win.blit(menuImage, (0,0))
        win.blit(playButton, (456,200))
        win.blit(settingsButton, (456, 350))
        win.blit(quitButton, (456, 500))
        pygame.display.update()
player = Player
main_menu = Menu
pygame.init()
win = pygame.display.set_mode((1280,720))

def drawGame():
    win.blit(gameBoard, (0,0))
    pygame.display.update()
def main():
    game_started = True
    while game_started:
        main_menu.showMenu(main_menu)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_started = False
main()
pygame.quit()