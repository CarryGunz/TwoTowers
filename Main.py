import pygame
import random
import sys
import math
import Player
import Tower
import Shop
import Card
import AI
import AllCards
import time
import copy
import Sprite

WindowHeight = 1280
WindowWidth = 720

menuImage = pygame.image.load('images/menuImage.png')
playButton = pygame.image.load('images/playButton.png')
settingsButton = pygame.image.load('images/settingsButton.png')
quitButton = pygame.image.load('images/quitButton.png')

towerSprite = None
shopSprite = None
gameBoard = pygame.image.load('images/gameBoard.png')


shop = Shop.Shop(shopSprite)
computer = AI.AI(shop)
computer.tower = Tower.Tower(computer, towerSprite)

player = Player.Player("abc", shop, computer)
player.tower = Tower.Tower(player, towerSprite)


# -----------------------Cards

all_cards = []

card_effect1 = Card.CardEffect(player, 4, Card.addAttackEffect)
card1 = Card.Card(Sprite.Sprite(pygame.image.load('images/BallistaShot.png')), player)
card1.addCardEffect(card_effect1)

all_cards.append(card1)
# -------------------

class State:
    current_state = 0

    def __init__(self):
        pass

    def show(self):
        pass


def timerGame():  # таймер на десятки минут и секунды
    frame_count = 0
    start_timer = "1 5. 0"  # стартовое время

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
        win.blit(menuImage, (0, 0))
        win.blit(playButton, (456, 200))
        win.blit(settingsButton, (456, 350))
        win.blit(quitButton, (456, 500))

        pygame.display.update()

    def checkButtonClick(self):
        m_x, m_y = pygame.mouse.get_pos()

        if 200 < m_y < 330 and 456 < m_x < 700:
            self.current_state = 1


game_state = Menu()

player.cards.append(copy.copy(card1))
player.cards[-1].card_num = Card.Card.getNewCardNum(Card.Card)

player.cards.append(copy.copy(card1))
player.cards[-1].card_num = Card.Card.getNewCardNum(Card.Card)

player.cards.append(copy.copy(card1))
player.cards[-1].card_num = Card.Card.getNewCardNum(Card.Card)

player.cards.append(copy.copy(card1))
player.cards[-1].card_num = Card.Card.getNewCardNum(Card.Card)

player.cards.append(copy.copy(card1))
player.cards[-1].card_num = Card.Card.getNewCardNum(Card.Card)


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
            print(card.sprite.x, card.sprite.y)
            card.sprite.x = left_offset + x * (card_interval + card.sprite.image.get_width())
            card.sprite.y = top_offset
            x += 1

    def show(self):
        win.blit(gameBoard, (0, 0))

        self.showCards()
        self.showPlayersStats()
        pygame.display.flip()
        pygame.display.update()

    def showPlayersStats(self):
        # Создание шрифтов для вывода текста
        white = (255, 255, 255)
        font = pygame.font.Font('freesansbold.ttf', 22)
        font2 = pygame.font.Font('freesansbold.ttf', 18)

        # Вывод информации о игроке
        player1_name = font.render('Ваша башня', True, white)
        player1_hp = font2.render('Прочность: ' + str(player.tower.height), True, white)
        win.blit(player1_name, (35, 580))
        win.blit(player1_hp, (36, 620))

        # Вывод информации о компьютере
        AI_name = font.render('Компьютер', True, white)
        AI_hp = font2.render('Прочность: ' + str(computer.tower.height), True, white)
        win.blit(AI_name, (1110, 580))
        win.blit(AI_hp, (1111, 620))


pygame.init()
win = pygame.display.set_mode((WindowHeight, WindowWidth))


def main():
    global game_state
    game_started = True

    while game_started:
        game_state.show()

        for event in pygame.event.get():

            for card in player.cards:
                if card.movableImg():
                    player.cards.remove(card)
            if event.type == pygame.QUIT:
                game_started = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(len(player.cards))
                if event.button == 1:
                    if game_state.current_state == 0:
                        game_state.checkButtonClick()
                        if game_state.current_state == 1:
                            game_state = Game()
                            game_state.placeCards()


main()
pygame.quit()
