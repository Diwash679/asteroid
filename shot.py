from circleshape import *
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", (int(self.position.x), int(self.position.y)), SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
