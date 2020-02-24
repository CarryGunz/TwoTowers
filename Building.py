# Класс Здание (Building) назначение - управление и изображение ресурсов
# Атрибуты: Назначение здания (Typ_building), Стоимость и сила здания (Price_building),
# Мана здания (Health_building), Изображение здания
# Методы: Добавить здание, Разрушить здание, Выполнить действие здания, Продать здание
# Наследуемые классы:
#   Атакующее здание
#   Ремонтирующее здание
#   Специальное здание

import pygame
import random
import sys
import math

class Building:
    price = 0
    sprite = 0
    owner = 0
    def __init__(self):
        self.price = 0
        self.sprite = 0
        self.owner = 0
    def useBuilding(self):
        pass

class AttackBuilding(Building):
    def __init__(self):
        self.price = price
        self.sprite = sprite
        self.owner = owner
    def useBuilding(self):
        pass

class RepairBuilding(Building):
    def __init__(self):
        self.price = price
        self.sprite = sprite
        self.owner = owner
    def useBuilding(self):
        pass

class SpecialBuilding(Building):
    using_ref = 0
    def __init__(self):
        self.price = price
        self.sprite = sprite
        self.owner = owner
        self.using_ref = using_ref
    def useBuilding(self):
        pass