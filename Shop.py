# Класс Shop назначение - покупка карт и изображение карт с вопросительным знаком (для показания рандомности карт)
# Атрибуты:
#   Покупка - bye_card
#   Стоимость - cost_card
#   Изображение магазина с картами
#   Продажа карт - sell_card
import pygame
import random
import sys
import math
import Sprite
import AllCards

WOODEN = 1
BRONZE = 2
SILVER = 3
GOLDEN = 4


class ShopButton:
    def __init__(self, sprite, button_type, shop, button_x, button_y):
        self.sprite = sprite
        self.button_type = button_type
        self.shop_ref = shop
        self.sprite.x = button_x
        self.sprite.y = button_y

    def isClick(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(mouse[0], mouse[1])
        if click[0] == 1 and self.sprite.x + self.sprite.width > mouse[0] > \
                self.sprite.x and self.sprite.y + self.sprite.height > \
                mouse[1] > self.sprite.y:
            self.shop_ref.buyCard(self.button_type)

        else:
            return False


class Shop:
    def __init__(self):
        self.player = None
        self.computer = None
        self.wooden_button = ShopButton(Sprite.Sprite(pygame.image.load('images/WoodenButton.png')),
                                        WOODEN, self, 250, 40)

    def buyCard(self, card_type):
        # 1,2,4,8 - Цены за карты

        if card_type == WOODEN and self.player.player_gold >= 1:
            self.player.cards.append(AllCards.wooden_cards[random.randint(0, 1)].cloneCard())
            self.player.player_gold -= 1
        elif card_type == BRONZE and self.player.player_gold >= 2:
            pass
        elif card_type == SILVER and self.player.player_gold >= 4:
            pass
        elif card_type == GOLDEN and self.player.player_gold >= 8:
            pass
        self.player.setPlayerCardsOwner()

    def sellWeakCard(self, x, y):
        pass
