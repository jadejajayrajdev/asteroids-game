import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.move(dt)

    def move(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        asteroid_one_velocity = self.velocity.rotate(new_angle)
        asteroid_two_velocity = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one_radius, asteroid_two_radius = new_radius, new_radius

        asteroid_one = Asteroid(self.position.x, self.position.y, asteroid_one_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, asteroid_two_radius)
        asteroid_one.velocity = asteroid_one_velocity * 1.2
        asteroid_two.velocity = asteroid_two_velocity * 1.2
