import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
             
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
        # Create a rect for efficient collision detection
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        
    def draw(self, screen):
        # Base implementation - can be overridden
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), 
                          self.radius, 1)
    
    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt
        
        # Update collision rect
        self.rect.center = (int(self.position.x), int(self.position.y))
        
    def collides_with(self, other):
        # Circle collision detection
        distance = (self.position - other.position).length()
        return distance < (self.radius + other.radius)