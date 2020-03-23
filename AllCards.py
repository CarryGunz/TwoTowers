import Card
import Sprite
import pygame


card_effect1 = Card.CardEffect(None, 4, Card.addAttackEffect)
card1 = Card.Card(Sprite.Sprite(pygame.image.load('images/BallistaShot.png')), None)
card1.addCardEffect(card_effect1)

card_effect2 = Card.CardEffect(None, 3, Card.addRepairEffect)
card2 = Card.Card(Sprite.Sprite(pygame.image.load('images/WoodenBarricades.png')), None)
card2.addCardEffect(card_effect2)

card_effect3 = Card.CardEffect(None, 7, Card.addAttackEffect)
card3 = Card.Card(Sprite.Sprite(pygame.image.load('images/CatapultShot.png')), None)
card3.addCardEffect(card_effect3)

card_effect4 = Card.CardEffect(None, 5, Card.addRepairEffect)
card4 = Card.Card(Sprite.Sprite(pygame.image.load('images/LightFortification.png')), None)
card4.addCardEffect(card_effect4)

card_effect5 = Card.CardEffect(None, 12, Card.addAttackEffect)
card5 = Card.Card(Sprite.Sprite(pygame.image.load('images/SiegeRam.png')), None)
card5.addCardEffect(card_effect5)

card_effect6 = Card.CardEffect(None, 9, Card.addRepairEffect)
card6 = Card.Card(Sprite.Sprite(pygame.image.load('images/SteelGates.png')), None)
card6.addCardEffect(card_effect6)

wooden_cards = [card1, card2]
bronze_cards = [card3, card4]
silver_cards = [card5, card6]
