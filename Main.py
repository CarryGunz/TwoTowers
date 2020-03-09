import pygame
import random
import sys
import math
import Player
import Tower
import Shop
import Card
import time

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


def timerGame(): # таймер на десятки минут и секунды
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

        if 200 < m_y < 330 and 456 < m_x < 700:
            self.current_state = 1

game_state = Menu()
shop = Shop.Shop(shopSprite)
player = Player.Player("abc", shop)
tower = Tower.Tower(player, towerSprite)
player.getTower(tower)

player.cards.append(Card.Card(player, 1))
player.cards.append(Card.Card(player, 2))
player.cards.append(Card.Card(player, 3))
player.cards.append(Card.Card(player, 4))
player.cards.append(Card.Card(player, 5))
class Game(State):
    def __init__(self):
        self.current_state = 1
        pass

    def showCards(self):
        for card in player.cards:

            win.blit(card.sprite.image, (card.sprite.x, card.sprite.y))



    def placeCards(self):
        global player
        card_interval = 8 - len(player.cards)
        top_offset = 568
        left_offset = 206 + 870 / 2

        if (len(player.cards) > 0):
            left_offset -= player.cards[0].sprite.image.get_width() / 2 * (len(player.cards))

        x = 0
        for card in player.cards:
            card.sprite.x = left_offset + x * (card_interval + card.sprite.image.get_width())
            card.sprite.y = top_offset
            x += 1



    def show(self):
        win.blit(gameBoard, (0, 0))

        self.showCards()
        pygame.display.flip()
        pygame.display.update()





pygame.init()
win = pygame.display.set_mode((WindowHeight, WindowWidth))

def main():
    global game_state
    game_started = True

    while game_started:
        game_state.show()

        for event in pygame.event.get():
            for card in player.cards:
                card.movableImg(win)
            if event.type == pygame.QUIT:
                game_started = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    if game_state.current_state == 0:
                        game_state.checkButtonClick()
                        if game_state.current_state == 1:
                            game_state = Game()
                            game_state.placeCards()






main()
pygame.quit()