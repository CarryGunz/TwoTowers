import Tower
class Player:
    def __init__(self, _name, _shop, _opponent):
        self.name = _name
        self.game_score = 0
        self.tower = None
        self.cards = []
        self.buildings = []
        self.player_gold = 3
        self.shop = _shop
        self.turn_income = 1
        self.opponent = _opponent
        self.turn_cards_played = 0

    def setPlayerCardsOwner(self):
        for card in self.cards:
            card.owner = self
            for effect in card.effects:
                effect.setOwner(self)


    def showPlayerBuildings(self, screen):
        for building in self.buildings:
            screen.blit(building.sprite.image, (building.sprite.x, building.sprite.y))
    def usePlayerBuildings(self):
        for building in self.buildings:
            building.useBuilding()
    def lose(self):
        pass

    def win(self):
        pass



