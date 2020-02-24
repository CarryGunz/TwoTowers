# Класс Здание (Building) назначение - управление и изображение ресурсов
# Атрибуты: Назначение здания (Typ_building), Стоимость и сила здания (Price_building),
# Мана здания (Health_building), Изображение здания
# Методы: Добавить здание, Разрушить здание, Выполнить действие здания, Продать здание
# Наследуемые классы:
#   Атакующее здание
#   Ремонтирующее здание
#   Снижающее урон здание
#   Приносящее золото здание
import pygame
import random
import sys
import math

class Building:
    def __init__(self):