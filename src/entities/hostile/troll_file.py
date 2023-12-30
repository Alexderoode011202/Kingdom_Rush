from entity_base import Entitiy
import pygame
from pygame import Rect, Surface

class Goblin(Entitiy):
    def __init__(self, image_link: str, start_x: int, start_y: int) -> None:
        super().__init__(image_link,start_x, start_y,hp=50, damage_range=(2,4), attack_speed=1, armor_level=0, magical_protection=0)