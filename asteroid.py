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
        self.life_clock = 0
        self.can_wrap = False
        self.which_side = self.where_off_screen()

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

        if self.life_clock != 0 and self.is_fully_off_screen():
                print("Fully off screen")
                self.kill()

        if self.is_part_off_screen() and self.can_wrap:
            print("Partially off screen, wrapping")
            new_asteroid = Asteroid(self.position.x, self.position.y, self.radius, self.velocity)
            new_asteroid.adjust_pos()
            self.can_wrap = False

        old_which_side = self.which_side
        self.which_side = self.where_off_screen()
        if self.which_side != old_which_side:
            self.can_wrap = True

        self.life_clock += dt

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

    def is_part_off_screen(self):
        return (self.position.x < self.radius) | \
            (self.position.x > SCREEN_WIDTH - self.radius) | \
            (self.position.y < self.radius) | \
            (self.position.y > SCREEN_HEIGHT - self.radius)

    def where_off_screen(self):
        where_list = []
        if (self.position.x < self.radius):
            where_list.append("l")
        if (self.position.x > SCREEN_WIDTH - self.radius):
            where_list.append("r")
        if (self.position.y < self.radius):
            where_list.append("t")
        if (self.position.y > SCREEN_HEIGHT - self.radius):
            where_list.append("b")
        return where_list

    def adjust_pos(self):
        if (self.position.x < self.radius):
            self.position.x += SCREEN_WIDTH

        if (self.position.x > SCREEN_WIDTH - self.radius):
            self.position.x -= SCREEN_WIDTH

        if (self.position.y < self.radius):
            self.position.y += SCREEN_HEIGHT

        if (self.position.y > SCREEN_HEIGHT - self.radius):
            self.position.y -= SCREEN_HEIGHT

    def is_fully_off_screen(self):
        return (self.position.x < -self.radius) | \
            (self.position.x > SCREEN_WIDTH + self.radius) | \
            (self.position.y < -self.radius) | \
            (self.position.y > SCREEN_HEIGHT + self.radius)