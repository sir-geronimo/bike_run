import pygame.display
from pygame import Surface, Rect
from pygame.time import Clock

WIDTH, HEIGHT = 480, 720
CENTER_WIDTH, CENTER_HEIGHT = WIDTH/2, HEIGHT/2


class Window(object):
    screen: Surface
    clock: Clock

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = Clock()

    def update(self, fps) -> float:
        ticks = self.clock.tick(fps)
        pygame.display.flip()
        self.screen.fill(pygame.Color('black'))

        return ticks * 0.001


def box(rect: Rect, vertical: bool = True, horizontal: bool = True):
    if horizontal:
        if rect.right >= WIDTH:
            rect.right = WIDTH
        if rect.left <= 0:
            rect.left = 0

    if vertical:
        if rect.bottom >= HEIGHT:
            rect.bottom = HEIGHT
        if rect.top <= 0:
            rect.top = 0
