import Sprite
import Player


class Card:
    def __init__(self):
        self.price = 0
        self.sprite = Sprite()
        self.owner = Player()

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