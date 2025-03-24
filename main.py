import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import os

pygame.init()

clock = pygame.time.Clock()

print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
ast = pygame.sprite.Group()

Player.containers = (updateable, drawable)
Asteroid.containers = (ast, updateable, drawable)
AsteroidField.containers = (updateable,)
Shot.containers = (updateable, drawable)

def main():
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    # Game loop
    running = True
    dt = 0
    
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update game state
        updateable.update(dt)
        # Check for collisions
        for asteroid in ast:
            if player.collide(asteroid):
                print("Game Over!")
                import sys
                sys.exit() 
        
        # Update screen
        screen.fill(color="black")
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        
        # Control frame rate and get dt
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()