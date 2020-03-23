import pygame
class Tower:
    def __init__(self, _owner, is_human):
        self.height = 50
        self.owner = _owner
        self.is_human = is_human

    def showTower(self, screen):
        if self.is_human:
            floors_number = int(self.height / 10)
            screen.blit(pygame.image.load('images/TowerBottom.png'), (20, 445))
            for num in range(floors_number):
                screen.blit(pygame.image.load('images/TowerFloor.png'), (35, 445 - 27 * (num + 1)))
            screen.blit(pygame.image.load('images/TowerRoof.png'), (20, 435 - 27 * (floors_number + 5)))
        else:
            floors_number = int(self.height / 10)
            screen.blit(pygame.image.load('images/TowerBottom.png'), (1091, 445))
            for num in range(floors_number):
                screen.blit(pygame.image.load('images/TowerFloor.png'), (1106, 445 - 27 * (num + 1)))
            screen.blit(pygame.image.load('images/TowerRoof.png'), (1091, 435 - 27 * (floors_number + 5)))
    def takeDamage(self):
        pass

    def repairTower(self):
        pass
