import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.circle(screen, white, (self.position), self.radius, 2)

    def update(self, dt):
            self.position += self.velocity * dt
    
    def split(self, position):
        self.kill()
        print(f"killed size {self.radius}")
        if self.radius <= ASTEROID_MIN_RADIUS:
              return
        else:
            angle = random.uniform(20, 50)
            direction_1 = self.velocity.rotate(angle)
            direction_2 = self.velocity.rotate(angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(position[0], position[1], new_radius)
            asteroid.velocity = direction_1 * 1.2
            asteroid = Asteroid(position[0], position[1], new_radius)
            asteroid.velocity = direction_2 * 1.2       