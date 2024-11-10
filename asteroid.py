from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
        def __init__(self, x, y, radius):
            super().__init__(x,y, radius)

        def draw(self, screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)

       
        def update(self, dt):
            self.position += self.velocity * dt

        def split(self):
            self.kill()

            if self.radius <= ASTEROID_MIN_RADIUS:
                return
            else:
                random_angle = random.uniform(20, 50)
                direction_1 = self.velocity.rotate(random_angle)
                direction_2 = self.velocity.rotate(-random_angle)

                new_radius_1 = self.radius - ASTEROID_MIN_RADIUS
                new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius_1)
                new_asteroid_1.velocity = direction_1*1.2

                new_radius_2 = self.radius - ASTEROID_MIN_RADIUS
                new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius_2)
                new_asteroid_2.velocity = direction_2*1.2

          
