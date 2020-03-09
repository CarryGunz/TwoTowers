import Sprite
import Player
import pygame


class Card:
    takenCardNum = None
    def __init__(self, owner, card_num_):
        self.price = 0
        self.sprite = Sprite.Sprite(pygame.image.load('images/damageCard1.png'))
        self.owner = owner
        self.card_num = card_num_

    def useCard(self):
        pass

    def movableImg(self, screen):

        is_dragging = False
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()


        if click[0] == 1 and self.sprite.x + self.sprite.width > mouse[0] > self.sprite.x and self.sprite.y + self.sprite.height > mouse[
            1] > self.sprite.y and Card.takenCardNum is None:
            is_dragging = True
            Card.takenCardNum = self.card_num

        elif click[0] == 0:
            is_dragging = False
            Card.takenCardNum = None

        if Card.takenCardNum == self.card_num:
            self.sprite.x = mouse[0] - (self.sprite.width / 2)
            self.sprite.y = mouse[1] - (self.sprite.height / 2)
        

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