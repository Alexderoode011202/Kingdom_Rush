"""This is just a demo where I test and get used to core features of what the game will approximately look like.
The things that will have to be accounted for when making the real deal:
1. finding the paths of all media
2. making sure the game works on all screen sizes
"""

import pygame
from pygame import Rect, Surface
from sys import exit
from typing import Tuple
import pandas as pd
from pandas import DataFrame


pygame.init()
window_size: Tuple[int, int] = (800, 800)
display = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

#metadata
pygame.display.set_caption("Kingdom Rush Clone")
pygame.display.set_icon(pygame.image.load("media/icon/icon.png"))

# background:
background: Surface = pygame.image.load("media/maps/first_stage/Level2-Stage1.jpg")
background = pygame.transform.scale(background, window_size)
background_rect: Rect = background.get_rect(bottomright = window_size)

#troll
enemy: Surface = pygame.image.load("media/globlin1.png")
enemy = pygame.transform.scale_by(enemy, factor= 0.175)
enemy_rect: Rect = enemy.get_rect(midbottom = (window_size[0]/2, window_size[1]/2))

# path declaration:
path_df = pd.read_csv("test_environment/expanded_dataset_map1_phase1.csv")


while True:
    # Event handler:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    print(pygame.mouse.get_pos())
    # blitting handler:
    
    display.blit(background, background_rect)
    display.blit(enemy, enemy_rect)
    pygame.display.update()
    clock.tick(60)


