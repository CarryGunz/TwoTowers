import pygame
import random
import sys
import math
import Player
import Tower
import Shop
import Card
import time

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
        # win.blit(text_timer, (620, 35)) # отображение таймера
        pygame.display.update()
    def timerGame(self): # таймер на десятки минут и секунды
        frame_count = 0
        start_timer = "1 5. 0" # стартовое время

        while True:
            pygame.time.Clock().tick(60)
            frame_count += 1

            hour = int(start_timer[0])
            minute = int(start_timer[2])
            second = int(start_timer[5])

            if second > 0 and frame_count == 20:
                frame_count = 0
                second -= 1
            if second == 0 and minute > 0 and frame_count == 20:
                frame_count = 0
                second = 9
                minute -= 1
            if minute == 0 and hour > 0 and frame_count == 20:
                frame_count = 0
                minute = 9
                second = 9
                hour -= 1

            start_timer = str(hour) + " " + str(minute) + ". " + str(second)
            red = (255, 0, 0)
            font = pygame.font.SysFont('DS-Digital', 50, False, False)
            text_timer = font.render(start_timer, True, red)
            win.blit(text_timer, (620, 35))  # отображение таймера

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