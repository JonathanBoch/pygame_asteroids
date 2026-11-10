import pygame

from wrap import where_off_screen, adjust_pos
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.which_side = where_off_screen(self)
        self.lives = PLAYER_LIVES
        self.invincibility_timer = 0
        self.speed = 0
        self.prev_move_key = None

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED_MAX * dt

    def update(self, dt: float) -> None:
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            if self.prev_move_key == "s":
                self.speed = 0
            self.prev_move_key = "w"
            self.move(dt, True)

        if keys[pygame.K_s]:
            if self.prev_move_key == "w":
                self.speed = 0
            self.prev_move_key = "s"
            self.move(-dt, True)

        if keys[pygame.K_SPACE]:
            self.shoot()

        if where_off_screen(self) != self.which_side:
            self.which_side = where_off_screen(self)
            adjust_pos(self, self.which_side)

        if self.invincibility_timer > 0:
            self.invincibility_timer -= dt

        if (not keys[pygame.K_w]) and (not keys[pygame.K_s]) and (self.speed > 0):
            if self.prev_move_key == "w":
                self.move(dt, False)
            else:
                self.move(-dt, False)

    def move(self, dt: float, speeding_up: bool) -> None:
        if speeding_up:
            self.speed += PLAYER_ACCEL_MOVE * abs(dt)
        else:
            self.speed -= PLAYER_ACCEL_MOVE * abs(dt)

        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)

        if self.speed >= PLAYER_SPEED_MAX:
            self.speed = PLAYER_SPEED_MAX
        if self.speed < 0:
            self.speed = 0

        rotated_with_speed_vector = rotated_vector * self.speed * dt
        self.position += rotated_with_speed_vector

    def shoot(self) -> None:
        if self.shoot_timer > 0:
            return
        else:
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN_SECONDS

            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1)
            shot.velocity = shot.velocity.rotate(self.rotation)
            shot.velocity *= PLAYER_SHOOT_SPEED

    def respawn(self) -> None:
        self.lives -= 1
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.rotation = 0
        self.invincibility_timer = PLAYER_INVINCIBILITY_TIMER_SEC