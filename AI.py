import random
import Card
import AllCards
class AI:
    def __init__(self, shop):
        self.tower = None
        self.cards = []
        self.buildings = []
        self.player_gold = 3
        self.shop = shop
        self.turn_income = 1
        self.opponent = None
        self.turn_cards_played = 0

    def setPlayerCardsOwner(self):
        for card in self.cards:
            card.owner = self
            for effect in card.effects:
                effect.setOwner(self)

    def TurnAI(self):

        x = random.randint(0, 100)
        if x < 65:
            return

        #Buy cards

        rest = self.player_gold % 8
        amount = self.player_gold // 8
        self.player_gold = self.player_gold - amount*8

        for i in range(0, amount):
            #self.cards.append() gold
            pass

        rest = self.player_gold % 4
        amount = self.player_gold // 4
        self.player_gold = self.player_gold - amount * 4

        for i in range(0, amount):
            self.cards.append(AllCards.silver_cards[random.randint(0, len(AllCards.silver_cards)-1)].cloneCard())
            pass

        rest = self.player_gold % 2
        amount = self.player_gold // 2
        self.player_gold = self.player_gold - amount * 2

        for i in range(0, amount):
            self.cards.append(AllCards.bronze_cards[random.randint(0, len(AllCards.bronze_cards)-1)].cloneCard())
            pass

        rest = self.player_gold % 1
        amount = self.player_gold // 1
        self.player_gold = self.player_gold - amount * 1

        for i in range(0, amount):
            self.cards.append(AllCards.wooden_cards[random.randint(0, len(AllCards.wooden_cards)-1)].cloneCard())
            pass

        self.setPlayerCardsOwner()

        #Use cards
        for self.turn_cards_played in range(2):
            k = 100 - self.tower.height  # 100 - max height
            max_effect = None
            max_effect_card = None
            if k < random.randint(0, 100):# if ... do heal
                for card in self.cards:
                    for effect in card.effects:
                        if effect.effect == Card.addRepairEffect:
                            if max_effect == None:
                                max_effect = effect
                                max_effect_card = card
                                continue

                            if max_effect.effect_power < effect.effect_power:
                                max_effect = effect
                                max_effect_card = card
                if max_effect_card != None:
                    max_effect_card.useCard()
            else:
                if random.randint(0, 2) > 1:
                    for card in self.cards:
                        for effect in card.effects:
                            if effect.effect == Card.addAttackEffect:
                                if max_effect == None:
                                    max_effect = effect
                                    max_effect_card = card
                                    continue

                                if max_effect.effect_power < effect.effect_power:
                                    max_effect = effect
                                    max_effect_card = card
                    if max_effect_card != None:
                        max_effect_card.useCard()
                else:
                    for card in self.cards:
                        if card.is_building:
                            card.useCard()
                            break
