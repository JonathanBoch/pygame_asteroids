import pygame, random
from logger import log_event
from wrap import where_off_screen, adjust_pos
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, \
                ASTEROID_MAX_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float, velocity=0) -> None:
        super().__init__(x, y, radius)
        self.score = self.radius / ASTEROID_MIN_RADIUS
        self.velocity = velocity
        self.which_side = where_off_screen(self)

    def draw(self, screen, font_color="white") -> None:
        pygame.draw.circle(screen, font_color, self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

        if where_off_screen(self) != self.which_side:
            self.which_side = where_off_screen(self)
            adjust_pos(self, self.which_side)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        rand_rotate = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(rand_rotate)
        new_velocity2 = self.velocity.rotate(-rand_rotate)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2 * 1.2