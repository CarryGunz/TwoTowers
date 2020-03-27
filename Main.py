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
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
TABLE_X = 211
TABLE_Y = 124
TABLE_WIDTH = 858
TABLE_HEIGHT = 397


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
        win.blit(self.menuImage, (0, 0))
        win.blit(self.playButton, (456, 200))
        win.blit(self.settingsButton, (456, 350))
        win.blit(self.quitButton, (456, 500))

        pygame.display.update()

    def checkButtonClick(self):
        global game_state
        m_x, m_y = pygame.mouse.get_pos()

        if 200 < m_y < 330 and 456 < m_x < 700:
            game_state = Game()



class GameButton:
    def __init__(self, sprite, button_x, button_y):
        self.sprite = sprite
        self.sprite.x = button_x
        self.sprite.y = button_y

    def isMouseOn(self):
        m_x, m_y = pygame.mouse.get_pos()
        return self.sprite.checkMouseOn(m_x, m_y)

class Timer:
    def __init__(self, max_value):
        self.start_time = pygame.time.get_ticks()
        self.max_value = max_value

    def getSeconds(self):
        return int(self.max_value - (pygame.time.get_ticks() - self.start_time)/1000)

    def restart(self):
        self.start_time = pygame.time.get_ticks()

class Game(State):
    def __init__(self):
        self.current_state = 2
        self.card_on_hand = None

        # <Sprites> Спрайты

        self.gameBoard = pygame.image.load('images/gameBoard.png')

        # </Sprites>

        # <GameThings> Разное
        self.shop = Shop.Shop()
        self.computer = AI.AI(self.shop)
        self.computer.tower = Tower.Tower(self.computer, False)

        self.player = Player.Player("abc", self.shop, self.computer)
        self.player.tower = Tower.Tower(self.player, True)

        self.computer.opponent = self.player
        self.shop.player = self.player
        self.shop.computer = self.computer

        self.timer = Timer(20)
        self.end_turn = False
        # </GameThings>
        # <GameButtons>
        self.end_turn_button = GameButton(Sprite.Sprite(pygame.image.load('images/EndTurnButton.png')), 750, 12)
        self.delete_card_button = GameButton(Sprite.Sprite(pygame.image.load('images/DeleteButton.png')), 960, 569)

        # </GameButtons>
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
        self.getStartCards()
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

    def showBuildings(self):
        for build in self.player.buildings:
            win.blit(build.sprite.image, (build.sprite.x, build.sprite.y))

        for build in self.computer.buildings:
            win.blit(build.sprite.image, (build.sprite.x, build.sprite.y))

    def placeCards(self):
        card_interval = 8 - len(self.player.cards)
        top_offset = 568
        left_offset = 206 + 760 / 2 #206 + 870 / 2

        if (len(self.player.cards) > 0):
            left_offset -= self.player.cards[0].sprite.image.get_width() / 2 * (len(self.player.cards))

        x = 0
        for card in self.player.cards:
            if card != self.card_on_hand:

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
            if TABLE_X + TABLE_WIDTH > self.card_on_hand.sprite.x > TABLE_X and TABLE_Y + TABLE_HEIGHT > self.card_on_hand.sprite.y > TABLE_Y:
                self.card_on_hand.useCard()

                #self.all_cards.remove(self.card_on_hand)
                self.card_on_hand.owner.cards.remove(self.card_on_hand)
            self.card_on_hand = None

    #Двигает карту на руке
    def moveCardOnHand(self):
        if self.card_on_hand != None:
            self.card_on_hand.move()

    def show(self):
        win.blit(self.gameBoard, (0, 0))
        win.blit(self.shop.wooden_button.sprite.image, (233, 32))
        win.blit(self.shop.bronze_button.sprite.image, (305, 32))
        win.blit(self.shop.silver_button.sprite.image, (377, 32))
        win.blit(self.end_turn_button.sprite.image, (750, 12))
        win.blit(self.delete_card_button.sprite.image, (self.delete_card_button.sprite.x,
                                                        self.delete_card_button.sprite.y))

        self.player.tower.showTower(win)
        self.computer.tower.showTower(win)
        self.placeCards()
        self.showCards()
        self.showPlayersStats()
        self.showBuildings()
        pygame.display.flip()
        pygame.display.update()


    def showPlayersStats(self):
        # Создание шрифтов для вывода текста
        white = (255, 255, 255)
        yellow = (255, 215, 0)
        font = pygame.font.Font('freesansbold.ttf', 18)

        # Вывод информации о игроке
        player1_name = font.render('Ваша башня', True, white)
        player1_hp = font.render('Прочность: ' + str(self.player.tower.height), True, white)
        player1_gold = font.render('Золото: ' + str(self.player.player_gold), True, yellow)
        player1_cards_amount = font.render(f'Карты: {len(self.player.cards)}/7', True, white)
        player1_amount_of_used_cards1 = font.render('Использовано', True, white)
        player1_amount_of_used_cards2 = font.render(f'карт: {self.player.turn_cards_played}/2', True, white)
        win.blit(player1_name, (35, 580))
        win.blit(player1_hp, (36, 600))
        win.blit(player1_gold, (36, 620))
        win.blit(player1_amount_of_used_cards1, (36, 640))
        win.blit(player1_amount_of_used_cards2, (36, 660))
        win.blit(player1_cards_amount, (36, 680))

        player1_timer_info = font.render(f'{self.timer.getSeconds()}', True, white)
        win.blit(player1_timer_info, (625, 33))

        # Вывод информации о компьютере
        AI_name = font.render('Ваш противник', True, white)
        AI_hp = font.render('Прочность: ' + str(self.computer.tower.height), True, white)
        AI_gold = font.render('Золото: ' + str(self.computer.player_gold), True, yellow)
        win.blit(AI_name, (1107, 580))
        win.blit(AI_hp, (1111, 620))
        win.blit(AI_gold, (1111, 660))
    def getStartCards(self):
        self.player.cards.append(AllCards.wooden_cards[random.randint(0, len(AllCards.wooden_cards)-1)].cloneCard())
        self.player.cards.append(AllCards.wooden_cards[random.randint(0, len(AllCards.wooden_cards)-1)].cloneCard())
        self.player.cards.append(AllCards.wooden_cards[random.randint(0, len(AllCards.wooden_cards)-1)].cloneCard())
        self.player.setPlayerCardsOwner()

        self.computer.cards.append(AllCards.wooden_cards[random.randint(0, len(AllCards.wooden_cards) - 1)].cloneCard())
        self.computer.cards.append(AllCards.wooden_cards[random.randint(0, len(AllCards.wooden_cards) - 1)].cloneCard())
        self.computer.cards.append(AllCards.wooden_cards[random.randint(0, len(AllCards.wooden_cards) - 1)].cloneCard())
        self.computer.setPlayerCardsOwner()

    def usePlayersBuildings(self):
        for build in self.player.buildings:
            build.useBuilding()
        for build in self.computer.buildings:
            build.useBuilding()

game_state = Menu()

pygame.init()
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

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
            if event.type == pygame.QUIT:
                game_started = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state.current_state == 1: #Menu
                    game_state.checkButtonClick()
                elif game_state.current_state == 2: #Game
                    game_state.checkCardsOnClick()
                    if len(game_state.player.cards) < 7:
                        game_state.shop.wooden_button.isClick()
                        game_state.shop.bronze_button.isClick()
                        game_state.shop.silver_button.isClick()
                    if game_state.end_turn_button.isMouseOn():
                        game_state.end_turn = True

            if event.type == pygame.MOUSEMOTION:
                if game_state.current_state == 2:  # Game
                    game_state.moveCardOnHand()

            if event.type == pygame.MOUSEBUTTONUP:
                if game_state.current_state == 2:  # Game
                    if game_state.card_on_hand != None:
                        if game_state.delete_card_button.isMouseOn():
                            game_state.player.player_gold += 1
                            game_state.card_on_hand.owner.cards.remove(game_state.card_on_hand)
                            game_state.card_on_hand = None

        if game_state.current_state == 2:  # Game
            if game_state.timer.getSeconds() <= 0:
                game_state.end_turn = True

            if game_state.end_turn:
                game_state.usePlayersBuildings()

                game_state.player.turn_cards_played = 0
                game_state.computer.turn_cards_played = 0
                game_state.computer.TurnAI()
                game_state.player.player_gold += game_state.player.turn_income
                game_state.computer.player_gold += game_state.computer.turn_income
                game_state.timer.restart()
                game_state.end_turn = False



main()
pygame.quit()
