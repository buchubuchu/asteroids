from circleshape import CircleShape
import pygame
import random
from logger import log_event
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        split_angle_1 = random.uniform(20, 50)
        split_velocity_1 = self.velocity.rotate(split_angle_1)
        split_angle_2 = random.uniform(20, 50)
        split_velocity_2 = self.velocity.rotate(split_angle_2)

        split_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid_1 = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, split_radius)
        split_asteroid_1.velocity = split_velocity_1 * 1.2
        split_asteroid_2.velocity = split_velocity_2 * 1.2
