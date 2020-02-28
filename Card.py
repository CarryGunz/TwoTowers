import Sprite
import Player
import pygame


class Card:
    def __init__(self, owner):
        self.price = 0
        self.sprite = Sprite.Sprite(pygame.image.load('images/testCard.png'))
        self.owner = owner

    def useCard(self):
        pass


#--------


class AttackCard(Card):
    def useCard(self):
        pass
class RepairCard(Card):
    def useCard(self):
        pass
class BuildingCard(Card):
    def useCard(self):
        pass
class SupportCard(Card):
    def useCard(self):
        pass


#--------
#Functions for special cards:

def nullFunction(): #Delete this after adding normal functions
    pass


class SpecialCard(Card):
    def __init__(self):
        self.using_ref = nullFunction

    def useCard(self):
        self.using_ref()