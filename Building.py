import pygame
import random
import sys
import math
import copy

class Building:

    def __init__(self, sprite, effect, id):
        self.sprite = sprite
        self.owner = None
        self.building_effect = effect
        self.id = id

    def placeBuilding(self):
        if self.owner.tower.is_human:

            if len(self.owner.buildings) == 1:
                self.sprite.x = 240
                self.sprite.y = 140
            if len(self.owner.buildings) == 2:
                self.sprite.x = 240
                self.sprite.y = 320
            if len(self.owner.buildings) == 3:
                self.sprite.x = 400
                self.sprite.y = 140
            if len(self.owner.buildings) == 4:
                self.sprite.x = 400
                self.sprite.y = 320
            else:
                return False



    def useBuilding(self):
        self.building_effect(self.owner)

    def cloneBuilding(self):
        new_build = Building(copy.copy(self.sprite), self.building_effect, self.id)
        return new_build

def archerTowerEffect(owner):
    owner.opponent.tower.height -= 1


def goldMineEffect(owner):
    owner.player_gold += 1
