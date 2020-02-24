class Player:
    def __init__(self, _name, _tower, _shop):
        self.name = _name
        self.game_score = 0
        self.tower = _tower
        self.cards = []
        self.buildings = []
        self.player_gold = 0
        self.shop = _shop

    def lose(self):
        pass
    def win(self):
        pass



