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

class Shop:
    def __init__(self):
        self.image=font.render(str(random.randint(100,1000)), 1, [255, 0, 0])
        self.width=self.image.get_width()
    def sellWeakCard(self, x, y, ):
        pass