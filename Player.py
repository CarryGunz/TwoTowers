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
        self.turnIncome = 1
        self.opponent = _opponent

    def lose(self):
        pass

    def win(self):
        pass



