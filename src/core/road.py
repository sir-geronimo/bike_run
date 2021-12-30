from typing import Tuple, List

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from src.core.window import WIDTH, HEIGHT

LANES = 3
STRIPE_WIDTH = 10
STRIPE_HEIGHT = 50
BORDER_WIDTH = 15
STRIPE_COLOR = (200, 200, 0, 0.7)
BORDER_COLOR = (255, 255, 255, 1)


class Road(object):
    # (left, right) borders
    borders: Tuple[Rect, Rect]
    stripes: List[Rect]
    speed = 250

    def __init__(self):
        left = Rect(
            (BORDER_WIDTH, 0),
            (BORDER_WIDTH, HEIGHT)
        )
        right = Rect(
            ((WIDTH - (BORDER_WIDTH * 2)), 0),
            (BORDER_WIDTH, HEIGHT)
        )
        self.borders = (left, right)
        self.stripes = self._init_stripes()

    def _init_stripes(self) -> List[Rect]:
        stripe_distance = self.get_road_size() / LANES
        stripes = []

        for lane in range(1, LANES):
            stripe = Rect(
                abs((STRIPE_WIDTH * 2) + (stripe_distance * lane)),
                0,
                STRIPE_WIDTH,
                STRIPE_HEIGHT,
            )

            for n in range(1, 10):
                copied = stripe.copy()
                copied.y += n * (STRIPE_HEIGHT + 50)

                stripes.append(copied)

            stripes.append(stripe)

        return stripes

    def loop(self, delta_time: float, surface: Surface):
        self.draw_boundaries(surface)
        self.draw_stripes(delta_time, surface)

    def draw_boundaries(self, surface: Surface):
        for border in self.borders:
            pygame.draw.rect(surface, BORDER_COLOR, border)

    def draw_stripes(self, delta_time: float, surface: Surface):
        for stripe in self.stripes:
            stripe.y += self.get_speed() * delta_time
            if stripe.y >= HEIGHT:
                stripe.y = 0

            pygame.draw.rect(surface, STRIPE_COLOR, stripe)

    def get_speed(self) -> float:
        return self.speed

    def get_road_size(self) -> int:
        (left, right) = self.borders
        return right.left - left.right
