import Card
import Sprite
import pygame
import AllBuildings


card_effect1 = Card.CardEffect(4, Card.addAttackEffect)
card1 = Card.Card(Sprite.Sprite(pygame.image.load('images/BallistaShot.png')))
card1.addCardEffect(card_effect1)

card_effect2 = Card.CardEffect(3, Card.addRepairEffect)
card2 = Card.Card(Sprite.Sprite(pygame.image.load('images/WoodenBarricades.png')))
card2.addCardEffect(card_effect2)

card_effect3 = Card.CardEffect(7, Card.addAttackEffect)
card3 = Card.Card(Sprite.Sprite(pygame.image.load('images/CatapultShot.png')))
card3.addCardEffect(card_effect3)

card_effect4 = Card.CardEffect(5, Card.addRepairEffect)
card4 = Card.Card(Sprite.Sprite(pygame.image.load('images/LightFortification.png')))
card4.addCardEffect(card_effect4)

card_effect5 = Card.CardEffect(12, Card.addAttackEffect)
card5 = Card.Card(Sprite.Sprite(pygame.image.load('images/SiegeRam.png')))
card5.addCardEffect(card_effect5)

card_effect6 = Card.CardEffect(9, Card.addRepairEffect)
card6 = Card.Card(Sprite.Sprite(pygame.image.load('images/SteelGates.png')))
card6.addCardEffect(card_effect6)

card_effect7 = Card.CardEffect(2, Card.addAttackEffect)
card_effect8 = Card.CardEffect(2, Card.addRepairEffect)
card7 = Card.Card(Sprite.Sprite(pygame.image.load('images/MilitaSquad.png')))
card7.addCardEffect(card_effect7)
card7.addCardEffect(card_effect8)

card_effect9 = Card.CardEffect(4, Card.addAttackEffect)
card_effect10 = Card.CardEffect(4, Card.addRepairEffect)
card8 = Card.Card(Sprite.Sprite(pygame.image.load('images/FootmenSquad.png')))
card8.addCardEffect(card_effect9)
card8.addCardEffect(card_effect10)

card_effect11 = Card.CardEffect(7, Card.addAttackEffect)
card_effect12 = Card.CardEffect(7, Card.addRepairEffect)
card9 = Card.Card(Sprite.Sprite(pygame.image.load('images/KnightsSquad.png')))
card9.addCardEffect(card_effect11)
card9.addCardEffect(card_effect12)

card10 = Card.Card(Sprite.Sprite(pygame.image.load('images/ArcherTower.png')))
card10.is_building = True
card10.card_building = AllBuildings.building1.cloneBuilding()

card11 = Card.Card(Sprite.Sprite(pygame.image.load('images/GoldMine.png')))
card11.is_building = True



wooden_cards = [card1, card2, card7, card10]
bronze_cards = [card3, card4, card8]
silver_cards = [card5, card6, card9]
