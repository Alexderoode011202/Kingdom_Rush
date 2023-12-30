import pygame
from pygame import Surface, Rect
from typing import Tuple

class Entitiy:
    def __init__(self, image_link: str, start_x: int, start_y: int, hp: int, speed: int, damage_range: tuple[int, int], attack_speed: int, armor_level: int, magical_protection: int):
        """Still gotta work out the description for this"""
        # combat
        self.damage_range: Tuple[int, int] = damage_range
        self.attack_speed: int = attack_speed
        self.dead: bool = False

        # loading the image and rectangle
        self.own_surface: Surface = pygame.image.load(image_link)
        self.own_rect: Rect = self.own_surface.get_rect(midbottom = (self.x_coord, self.y_coord))

        # health and protection
        self.hp: int = hp
        self.armor_level: int = armor_level
        self.magical_protection: int = magical_protection
        self.fighing: bool = False

        # movement
        self.x_coord: int = start_x
        self.y_coord: int = start_y
        self.start_coord: Tuple[int, int] = (self.x_coord, self.y_coord)
        self.speed: int = speed
        self.goal: Tuple[int, int] = None
        self.last_reached_goal: int = None
        self.n_goals_reached: int = 0

        # diverse:
        self.status_effects: list = []



    def get_health(self) -> int:
        """Returns the amount of HP an entity has in integers"""
        return self.hp
    
    def check_death(self) -> bool:
        """returns whether an entity lives or not"""
        return self.dead
    
    def take_damage(self, n_damage: int) -> None:
        self.hp -= n_damage
        if self.hp <= 0:
            self.dead = True
        return None
    
    def get_coordinates(self) -> Tuple[int, int]:
        """returns the coordinates of an entities feet"""
        return (self.x_coord, self.y_coord)
    
    def set_new_goal(self, goal_coordinates: Tuple[int, int]) -> None:
        """Sets the new goal for the entity to move towards"""
        self.goal


    

