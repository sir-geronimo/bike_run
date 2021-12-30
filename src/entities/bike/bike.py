import pygame.image
from pygame.rect import Rect
from pygame.surface import Surface

from src.core.window import box, WIDTH, HEIGHT
from src.entities.entity import Entity
from src.utils.utils import get_file_path


class Bike(Entity):
    rect: Rect
    image: Surface
    speed: int = 100
    life: int = 0

    def __init__(self):
        super().__init__()
        self._load_image()
        self.rect = self.image.get_rect()
        self._reset_position()
        self.life = 3

    def _load_image(self):
        sprite = get_file_path(__file__, 'sprite.png')
        image = pygame.image.load(sprite).convert_alpha()
        width, height = image.get_size()

        self.image = pygame.transform.scale(image, (width // 6, height // 6))

    def process_input(self, delta_time) -> None:
        keys = pygame.key.get_pressed()

        movement_x = keys[pygame.K_d] - keys[pygame.K_a]
        movement_y = keys[pygame.K_s] - keys[pygame.K_w]

        self.rect.x += round(self.speed * movement_x * delta_time)
        self.rect.y += round(self.speed * movement_y * delta_time)
        box(self.rect)

    def update(self, delta_time, **kwargs) -> None:
        pass

    def render(self, delta_time) -> None:
        pass

    def die(self) -> None:
        self.life = 0

    def _reset_position(self):
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
