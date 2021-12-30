import random

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from src.core.road import LANES
from src.core.window import HEIGHT, WIDTH
from src.entities.entity import Entity
from src.utils.utils import get_file_path


class Obstacle(Entity):
    rect: Rect
    image: Surface
    speed: int = 200
    is_alive: bool = False

    def __init__(self, lane: int = None):
        super().__init__()
        self._load_image()
        self.rect = self.image.get_rect()

        self.spawn(lane)

    def _load_image(self):
        sprite = get_file_path(__file__, 'sprite.png')
        image = pygame.image.load(sprite).convert()
        image.set_colorkey((255, 255, 255))
        width, height = image.get_size()

        self.image = pygame.transform.scale(image, (width // 2, height // 2))

    def update(self, dt, **kwargs) -> None:
        self.move(dt)

    def render(self, surface: Surface):
        pass

    def move(self, dt):
        self.rect.y += self.speed * dt

        if self.rect.top >= HEIGHT:
            self.die()

    def spawn(self, lane: int = None):
        if self.is_alive:
            return

        self.is_alive = True

        lane_position = WIDTH / LANES
        if lane is None:
            lane = random.choice([0.5, 1.5, 2.5]) * lane_position
        self.rect.center = (lane, 0)

    def die(self):
        if not self.is_alive:
            return

        self.is_alive = False
        super().kill()
