class AI:
    def __init__(self, shop):
        self.tower = None
        self.cards = []
        self.buildings = []
        self.player_gold = 3
        self.shop = shop
        self.turnIncome = 1
        self.opponent = None
