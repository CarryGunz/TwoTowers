import Sprite
import Player
import pygame
import copy
class CardEffect:
    def __init__(self, owner, effect_power, effect):
        self.owner = owner
        self.effect_power = effect_power
        self.effect = effect

    def activateEffect(self):
        self.effect(self.owner, self.effect_power)
    def setOwner(self, owner):
        self.owner = owner
        self.owner.opponent = owner.opponent



class Card:
    taken_card_num = None
    cards_count = 0

    def __init__(self, sprite, owner):
        self.price = 0
        self.sprite = sprite
        self.effects = []
        self.owner = owner


    def useCard(self):
        for effect in self.effects:
            effect.activateEffect()

    def addCardEffect(self, card_effect):
        self.effects.append(card_effect)

    def isClick(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if click[0] == 1 and self.sprite.x + self.sprite.width > mouse[0] >\
                self.sprite.x and self.sprite.y + self.sprite.height >\
                mouse[1] > self.sprite.y:
            return True
        else:
            return False

    def move(self):
        mouse = pygame.mouse.get_pos()
        x_center = self.sprite.width/2
        y_center = self.sprite.height/2

        self.sprite.x = mouse[0] - x_center
        self.sprite.y = mouse[1] - y_center

    def cloneCard(self):
        new_card = Card(copy.copy(self.sprite), self.owner)
        new_card.effects = self.effects
        new_card.price = self.price
        return new_card






# --------


def addAttackEffect(owner, damage):
    owner.opponent.tower.height = owner.opponent.tower.height - damage


def addRepairEffect(owner, repair_effect):
    owner.tower.height = owner.tower.height + repair_effect
    if owner.tower.height > 100:
        owner.tower.height = 100

#Сделать...
def addCreateBuildingEffect(owner, building_type):
    pass


class SupportCard(Card):
    def useCard(self):
        pass


# --------
# Functions for special cards:

def nullFunction():  # Delete this after adding normal functions
    pass


class SpecialCard(Card):
    def __init__(self):
        self.using_ref = nullFunction

    def useCard(self):
        self.using_ref()
