import pygame
from pygame import Rect, Surface
from sys import exit
from typing import Tuple

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



while True:
    # Event handler:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    print(pygame.mouse.get_pos())
    # blitting handler:
    
    display.blit(background, background_rect)
    pygame.display.update()
    clock.tick(60)


