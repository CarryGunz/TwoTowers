import pygame
import random
import sys
import math
import Player
import Tower
import Shop
import Card


WindowHeight = 1280
WindowWidth = 720

menuImage = pygame.image.load('images/menuImage.png')
playButton = pygame.image.load('images/playButton.png')
settingsButton = pygame.image.load('images/settingsButton.png')
quitButton = pygame.image.load('images/quitButton.png')


towerSprite = None
shopSprite = None
gameBoard = pygame.image.load('images/gameBoard.png')


class State:
    current_state = 0
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

    def checkButtonClick(self):
        m_x, m_y = pygame.mouse.get_pos()
        print(m_x, m_y)
        if 200 < m_y < 330 and 456 < m_x < 700:
            self.current_state = 1


class Game(State):
    def __init__(self):
        self.current_state = 1
        pass

    def show(self):

        win.blit(gameBoard, (0, 0))
        #
        card_interval = 8 - len(player.cards)
        top_offset = 568
        left_offset = 206 + 870/2

        if (len(player.cards) > 0):
            left_offset -= player.cards[0].sprite.image.get_width()/2 * (len(player.cards))

        x = 0
        for card in player.cards:
            card.sprite.x = left_offset + x*(card_interval + card.sprite.image.get_width())
            card.sprite.y = top_offset
            win.blit(card.sprite.image, (left_offset + x*(card_interval + card.sprite.image.get_width()), top_offset))
            x += 1
        pygame.display.flip()
        pygame.display.update()



game_state = Menu()
shop = Shop.Shop(shopSprite)

player = Player.Player("abc", shop)
tower = Tower.Tower(player, towerSprite)
player.getTower(tower)

player.cards = [Card.Card(player)]*5

pygame.init()
win = pygame.display.set_mode((WindowHeight, WindowWidth))

def main():
    global game_state
    game_started = True
    while game_started:
        game_state.show()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_started = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if game_state.current_state == 0:
                        print(game_state.current_state)
                        game_state.checkButtonClick()
                        if game_state.current_state == 1:
                            game_state = Game()

main()
pygame.quit()