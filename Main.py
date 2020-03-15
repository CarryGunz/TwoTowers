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

#Константы
WindowHeight = 1280
WindowWidth = 720
TableX = 211
TableY = 124
TableWidth = 858
TableHeight = 397


class State:

    def __init__(self):
        self.current_state = 0

    def show(self):
        pass

game_state = State()

class Menu(State):
    def __init__(self):
        self.current_state = 1
        self.menuImage = pygame.image.load('images/menuImage.png')
        self.playButton = pygame.image.load('images/playButton.png')
        self.settingsButton = pygame.image.load('images/settingsButton.png')
        self.quitButton = pygame.image.load('images/quitButton.png')

    def show(self):
        win.blit( self.menuImage, (0, 0))
        win.blit( self.playButton, (456, 200))
        win.blit( self.settingsButton, (456, 350))
        win.blit( self.quitButton, (456, 500))

        pygame.display.update()

    def checkButtonClick(self):
        global game_state
        m_x, m_y = pygame.mouse.get_pos()

        if 200 < m_y < 330 and 456 < m_x < 700:
            game_state = Game()


class Game(State):
    def __init__(self):
        self.current_state = 2
        self.card_on_hand = None

        # <Sprites> Спрайты
        self.towerSprite = None
        self.shopSprite = None
        self.gameBoard = pygame.image.load('images/gameBoard.png')
        # </Sprites>

        # <GameThings> Разное
        self.shop = Shop.Shop(self.shopSprite)
        self.computer = AI.AI(self.shop)
        self.computer.tower = Tower.Tower(self.computer, self.towerSprite)

        self.player = Player.Player("abc", self.shop, self.computer)
        self.player.tower = Tower.Tower(self.player, self.towerSprite)
        # </GameThings>

        # <Cards> Карты

        self.all_cards = []
        self.player.cards = []

        #Предлагаю складывать карты не по номерам, а по ссылкам
        #Ссылки в python есть!

        #Сделать!
        #for i in range(0, 5):
        #    card_ = Card.Card(...)
        #    player.cards.append(card_)


        # </Cards>

        #<Временное>

        card_effect1 = Card.CardEffect(self.player, 4, Card.addAttackEffect)
        card1 = Card.Card(Sprite.Sprite(pygame.image.load('images/BallistaShot.png')), self.player)
        card1.addCardEffect(card_effect1)
        self.all_cards.append(card1)
        self.player.cards.append(card1)

        card_effect2 = Card.CardEffect(self.player, 3, Card.addRepairEffect)
        card1 = Card.Card(Sprite.Sprite(pygame.image.load('images/WoodenBarricades.png')), self.player)
        card1.addCardEffect(card_effect2)
        self.all_cards.append(card1)
        self.player.cards.append(card1)

        card_effect3 = Card.CardEffect(self.player, 7, Card.addAttackEffect)
        card1 = Card.Card(Sprite.Sprite(pygame.image.load('images/CatapultShot.png')), self.player)
        card1.addCardEffect(card_effect3)
        self.all_cards.append(card1)
        self.player.cards.append(card1)

        card_effect4 = Card.CardEffect(self.player, 5, Card.addRepairEffect)
        card1 = Card.Card(Sprite.Sprite(pygame.image.load('images/LightFortification.png')), self.player)
        card1.addCardEffect(card_effect4)
        self.all_cards.append(card1)
        self.player.cards.append(card1)
        #</Временное>


    def timerGame(self):  # таймер на десятки минут и секунды
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


    def showCards(self):
        for card in self.player.cards:
            win.blit(card.sprite.image, (card.sprite.x, card.sprite.y))


    def placeCards(self):
        card_interval = 8 - len(self.player.cards)
        top_offset = 568
        left_offset = 206 + 870 / 2

        if (len(self.player.cards) > 0):
            left_offset -= self.player.cards[0].sprite.image.get_width() / 2 * (len(self.player.cards))

        x = 0
        for card in self.player.cards:
            if card != self.card_on_hand:
                #print(card.sprite.x, card.sprite.y)
                card.sprite.x = left_offset + x * (card_interval + card.sprite.image.get_width())
                card.sprite.y = top_offset
                x += 1

    #Проверяет, взята ли карта
    def checkCardsOnClick(self):
        for card in self.player.cards:
            if card.isClick() and (self.card_on_hand == None):
                self.card_on_hand = card

    #Убирает карту из руки
    def dropCard(self):
        if self.card_on_hand != None:
            if TableX + TableWidth > self.card_on_hand.sprite.x > TableX and TableY + TableHeight > self.card_on_hand.sprite.y > TableY:
                self.card_on_hand.useCard()
            self.card_on_hand = None

    #Двигает карту на руке
    def moveCardOnHand(self):
        if self.card_on_hand != None:
            self.card_on_hand.move()

    def show(self):
        win.blit(self.gameBoard, (0, 0))

        self.placeCards()
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
        player1_hp = font2.render('Прочность: ' + str(self.player.tower.height), True, white)
        win.blit(player1_name, (35, 580))
        win.blit(player1_hp, (36, 620))

        # Вывод информации о компьютере
        AI_name = font.render('Компьютер', True, white)
        AI_hp = font2.render('Прочность: ' + str(self.computer.tower.height), True, white)
        win.blit(AI_name, (1110, 580))
        win.blit(AI_hp, (1111, 620))

game_state = Menu()

pygame.init()
win = pygame.display.set_mode((WindowHeight, WindowWidth))


def main():
    global game_state
    game_started = True

    while game_started:
        game_state.show()

        pressed = pygame.mouse.get_pressed()
        if not pressed[0]:
            if game_state.current_state == 2:  # Game
                game_state.dropCard()


        for event in pygame.event.get():
            #for card in player.cards:
            #   if card.movableImg():
            #       player.cards.remove(card)
            if event.type == pygame.QUIT:
                game_started = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state.current_state == 1: #Menu
                    game_state.checkButtonClick()
                elif game_state.current_state == 2: #Game
                    game_state.checkCardsOnClick()

            if event.type == pygame.MOUSEMOTION:
                if game_state.current_state == 2:  # Game
                    game_state.moveCardOnHand()

                #if event.button == 1:
                #    if game_state.current_state == 0:
                #        game_state.checkButtonClick()
                #       if game_state.current_state == 1:
                #            game_state = Game()
                #            game_state.placeCards()


main()
pygame.quit()
