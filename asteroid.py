from constants import *
from circleshape import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    # @Override
    def draw(self, screen):

        color = "white"
        line_width = 2
        pygame.draw.circle(screen, color, self.position, self.radius, line_width)

    # @Override
    def update(self, dt):
        self.position += self.velocity * dt