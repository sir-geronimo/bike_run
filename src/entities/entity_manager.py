from pygame import display
from pygame.surface import Surface

from src.entities.bike.bike import Bike
from src.entities.entity import EntityGroup
from src.entities.obstacle.obstacle import Obstacle


class EntityManager(object):
    player: EntityGroup
    obstacles: EntityGroup
    all_entities: EntityGroup

    def __init__(self) -> None:
        player = Bike()

        self.player = EntityGroup(player)
        self.obstacles = EntityGroup()
        self.all_entities = EntityGroup(player)

    def process_input(self, delta_time) -> None:
        self.all_entities.process_input(delta_time)

    def update(self, delta_time) -> None:
        self.all_entities.update(delta_time)

    def render(self, surface: Surface = None) -> None:
        if surface is None:
            surface = display.get_surface()

        self.all_entities.render(surface)

    def add_obstacle(self) -> None:
        obstacle = Obstacle()

        self.obstacles.add(obstacle)
        self.all_entities.add(obstacle)
