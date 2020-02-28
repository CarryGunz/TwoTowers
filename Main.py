import pygame
import random
import sys
import math
import Player
import Tower
import Shop

#Consts
WindowHeight = 1280
WindowWidth = 720

#Menu
gameBoard = pygame.image.load('images/gameBoard.png')
menuImage = pygame.image.load('images/menuImage.png')
playButton = pygame.image.load('images/playButton.png')
settingsButton = pygame.image.load('images/settingsButton.png')
quitButton = pygame.image.load('images/quitButton.png')

#Game
towerSprite = None     #...
shopSprite = None     #...

class State:
    def __init__(self):
        pass

    def show(self):
        pass


class Menu(State):
    def __init__(self):
        pass

    def show(self):
        win.blit(menuImage, (0,0))
        win.blit(playButton, (456,200))
        win.blit(settingsButton, (456, 350))
        win.blit(quitButton, (456, 500))
        pygame.display.update()


class Game(State):
    def __init__(self):
        pass

    def show(self):
        win.fill((100, 100, 100))
        card_width = 75
        card_gap = 15 - len(player.cards)
        top_offset = 500
        left_offset = 200
        for x in range(0, len(player.cards)):
            pygame.draw.rect(win, (50, 100, 150), pygame.Rect(left_offset + x*(card_width + card_gap), top_offset, card_width, 150))
            x+=1
        pygame.display.flip()
        pygame.display.update()


current_state = Menu()
shop = Shop.Shop(shopSprite)

player = Player.Player("abc", shop)
tower = Tower.Tower(player, towerSprite)
player.getTower(tower)

player.cards = [None]*10

pygame.init()
win = pygame.display.set_mode((WindowHeight, WindowWidth))


def drawGame():
    win.blit(gameBoard, (0,0))
    pygame.display.update()


def main():
    game_started = True
    while game_started:
        current_state.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_started = False
main()
pygame.quit()