import pygame
import random
import sys
import math
import Player
import Tower
import Shop
import Card

#Consts
WindowHeight = 1280
WindowWidth = 720

#Menu
menuImage = pygame.image.load('images/menuImage.png')
playButton = pygame.image.load('images/playButton.png')
settingsButton = pygame.image.load('images/settingsButton.png')
quitButton = pygame.image.load('images/quitButton.png')

#Game
towerSprite = None     #...
shopSprite = None     #...
gameBoard = pygame.image.load('images/gameBoard.png')
#Cards makes their own sprites by their own

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
        #background
        win.blit(gameBoard, (0, 0))
        #some intervals
        card_interval = 8 - len(player.cards)
        top_offset = 568 #568 px to card panel from top on  gameBoard.png
        left_offset = 206 + 870/2 #206 px from left to card panel on picture, 870 px is width of card panel on picture (picture: gameBoard.png)
        #make intervals beautiful
        if (len(player.cards) > 0):
            left_offset -= player.cards[0].sprite.image.get_width()/2 * (len(player.cards))
        #cycle to place and show cards
        x = 0
        for card in player.cards:
            card.sprite.x = left_offset + x*(card_interval + card.sprite.image.get_width())
            card.sprite.y = top_offset
            win.blit(card.sprite.image, (left_offset + x*(card_interval + card.sprite.image.get_width()), top_offset))
            x += 1
        pygame.display.flip()
        pygame.display.update()


current_state = Menu()
shop = Shop.Shop(shopSprite)

player = Player.Player("abc", shop)
tower = Tower.Tower(player, towerSprite)
player.getTower(tower)

player.cards = [Card.Card(player)]*5

pygame.init()
win = pygame.display.set_mode((WindowHeight, WindowWidth))

def main():
    game_started = True
    while game_started:
        current_state.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_started = False
main()
pygame.quit()