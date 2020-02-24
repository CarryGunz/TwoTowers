import pygame
import random
import sys
import math

pygame.init()
win = pygame.display.set_mode((1280,720))
game_started = True
while game_started:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_started = False

pygame.quit()