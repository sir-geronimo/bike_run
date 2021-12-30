from typing import List

from pygame.sprite import Group, Sprite
from pygame.surface import Surface


class Entity(Sprite):
    def process_input(self, delta_time):
        pass

    def update(self, delta_time):
        pass

    def render(self, surface: Surface):
        pass


class EntityGroup(Group):
    entities: List[Entity] = []  # TODO: Remove this to avoid duplicity

    def __init__(self, entity: Entity = None):
        if entity is None:
            super().__init__()
            return

        super().__init__(entity)
        self.entities.append(entity)

    def process_input(self, delta_time):
        for entity in self.entities:
            entity.process_input(delta_time)

    def update(self, delta_time):
        super().update(delta_time)

    def render(self, surface: Surface):
        for entity in self.entities:
            entity.render(surface)
        super().draw(surface)
