import pygame

from wrap import where_off_screen, adjust_pos
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):

        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = PLAYER_RADIUS

        self.rotation = 0
        self.shoot_timer = 0
        self.which_side = where_off_screen(self)
        self.lives = PLAYER_LIVES
        self.invincibility_timer = 0
        self.move_speed = 0
        self.prev_move_key = None

    # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def get_oriented_radius(self, other: CircleShape) -> float:
        line1_start_end = (self.triangle()[0], self.triangle()[1])
        line2_start_end = (self.triangle()[1], self.triangle()[2])
        line3_start_end = (self.triangle()[2], self.triangle()[0])

        dist_to_line1 = self.get_closest_dist(other.position, line1_start_end)
        dist_to_line2 = self.get_closest_dist(other.position, line2_start_end)
        dist_to_line3 = self.get_closest_dist(other.position, line3_start_end)

        shortest_dist = min(dist_to_line1, dist_to_line2, dist_to_line3)
        
        return abs(other.position.distance_to(self.position)) - shortest_dist

    def get_closest_dist(self, ref_point: pygame.Vector2, start_end: tuple[tuple[int]]) -> float:
        line_start = pygame.Vector2(start_end[0])
        line_end = pygame.Vector2(start_end[1])

        line_segment = line_end - line_start
        point_to_line = ref_point - line_start

        projection_length_ratio = point_to_line.dot(line_segment) / line_segment.length_squared()
        projection_length_ratio = max(0.0, min(1.0, projection_length_ratio))
        closest_point = line_start + line_segment * projection_length_ratio

        closest_dist = ref_point.distance_to(closest_point)
        if closest_dist <= 0:
            return 0
        return closest_dist


    def draw(self, screen, font_color="white") -> None:
        pygame.draw.polygon(screen, font_color, self.triangle(), LINE_WIDTH)

    def rotate(self, dt: float,) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float) -> None:
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            if self.prev_move_key == "s":
                self.move_speed = 0
            self.prev_move_key = "w"
            self.move(dt, True)

        if keys[pygame.K_s]:
            if self.prev_move_key == "w":
                self.move_speed = 0
            self.prev_move_key = "s"
            self.move(-dt, True)

        if keys[pygame.K_SPACE]:
            self.shoot()

        if where_off_screen(self) != self.which_side:
            self.which_side = where_off_screen(self)
            adjust_pos(self, self.which_side)

        if self.invincibility_timer > 0:
            self.invincibility_timer -= dt

        if (not keys[pygame.K_w]) and (not keys[pygame.K_s]) and (self.move_speed > 0):
            if self.prev_move_key == "w":
                self.move(dt, False)
            else:
                self.move(-dt, False)

    def move(self, dt: float, speeding_up: bool) -> None:
        if speeding_up:
            self.move_speed += PLAYER_ACCEL_MOVE * abs(dt)
        else:
            self.move_speed -= PLAYER_ACCEL_MOVE * abs(dt)

        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)

        if self.move_speed >= PLAYER_SPEED_MAX:
            self.move_speed = PLAYER_SPEED_MAX
        if self.move_speed < 0:
            self.move_speed = 0

        rotated_with_speed_vector = rotated_vector * self.move_speed * dt
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
        self.move_speed = 0
        self.rot_speed = 0