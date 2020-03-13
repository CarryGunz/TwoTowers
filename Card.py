import Sprite
import Player
import pygame


class Card:
    taken_card_num = None
    cards_count = 0

    def __init__(self, sprite_, owner_, opponent_):
        self.price = 0
        self.sprite = sprite_
        self.card_num = Card.cards_count
        self.attributes = []
        self.owner = owner_
        self.opponent = opponent_
        self.getNewCardNum()

    def useCard(self):
        for func in self.attributes:
            func()


    def movableImg(self, screen):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if click[0] == 1 and self.sprite.x + self.sprite.width > mouse[
            0] > self.sprite.x and self.sprite.y + self.sprite.height > mouse[
            1] > self.sprite.y and Card.taken_card_num is None:
            Card.taken_card_num = self.card_num

        elif click[0] == 0 and 200 < mouse[1] < 600 and Card.taken_card_num is not None:
            self.useCard()
        elif click[0] == 0:
            Card.taken_card_num = None
        if Card.taken_card_num == self.card_num:
            self.sprite.x = mouse[0] - (self.sprite.width / 2)
            self.sprite.y = mouse[1] - (self.sprite.height / 2)
    def getNewCardNum(self):
        Card.cards_count = Card.cards_count + 1
        return Card.cards_count



# --------

def addAttackAttribute(tower, damage):
    tower.height = tower.height - damage


def addRepairAttribute(tower, repair_number):
    tower.height = tower.height + repair_number


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


# --------
# Functions for special cards:

def nullFunction():  # Delete this after adding normal functions
    pass


class SpecialCard(Card):
    def __init__(self):
        self.using_ref = nullFunction

    def useCard(self):
        self.using_ref()
