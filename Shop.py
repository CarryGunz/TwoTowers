#Класс Shop назначение - покупка карт и изображение карт с вопросительным знаком (для показания рандомности карт)
#Атрибуты:
#   Покупка - bye_card
#   Стоимость - cost_card
#   Изображение магазина с картами
#   Продажа карт - sell_card
import pygame
import random
import sys
import math
WOODEN = 1
BRONZE = 2
SILVER = 3
GOLDEN = 4
class ShopButton:
    def __init__(self, sprite, type):
        self.sprite = sprite
        self.type = type
    def isClick(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if click[0] == 1 and self.sprite.x + self.sprite.width > mouse[0] >\
                self.sprite.x and self.sprite.y + self.sprite.height >\
                mouse[1] > self.sprite.y:
            return True
        else:
            return False
class Shop:
    def __init__(self, image):
        self.image = None

    def buyCard(self, card_type):
        if card_type == WOODEN:

            pass
        elif card_type == BRONZE:
            pass
        elif card_type == SILVER:
            pass
        elif card_type == GOLDEN:
            pass

    def sellWeakCard(self, x,y):
        pass
