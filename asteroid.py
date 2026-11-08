import pygame, random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, \
                ASTEROID_MAX_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float, velocity=0) -> None:
        super().__init__(x, y, radius)
        self.score = self.radius / ASTEROID_MIN_RADIUS
        self.velocity = velocity
        self.can_wrap = False
        self.which_side = self.where_off_screen()

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

        if self.where_off_screen() != self.which_side:
            self.which_side = self.where_off_screen()
            self.adjust_pos(self.which_side)

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

    def adjust_pos(self, where_list):
        if "l" in where_list:
            self.position.x += SCREEN_WIDTH + 2*self.radius
        if "r" in where_list:
            self.position.x -= SCREEN_WIDTH + 2*self.radius
        if "t" in where_list:
            self.position.y += SCREEN_HEIGHT  + 2*self.radius # top is y=0, positive y is down
        if "b" in where_list:
            self.position.y -= SCREEN_HEIGHT  + 2*self.radius

    def where_off_screen(self):
        where_list = []
        if (self.position.x < -self.radius):
            where_list.append("l")
        if (self.position.x > SCREEN_WIDTH + self.radius):
            where_list.append("r")
        if (self.position.y < -self.radius): # top is y=0, positive y is down
            where_list.append("t")
        if (self.position.y > SCREEN_HEIGHT + self.radius):
            where_list.append("b")
        return where_list