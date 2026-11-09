import pygame, sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0.0

    pygame.font.init()
    score = 0
    font = pygame.font.Font(None, FONT_SIZE)
    font_coord_score = (FONT_X, FONT_Y_TOP)
    font_coord_lives = (FONT_X, FONT_Y_TOP + FONT_SPACING)
    font_coord_invincibility = (FONT_X, FONT_Y_TOP + 2*FONT_SPACING)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        log_state()
        for event in pygame.event.get():
            pass
        
        screen.fill("black")
        
        updatable.update(dt)
        for drawable_item in drawable:
            drawable_item.draw(screen)

        asteroid_loop: Asteroid
        for asteroid_loop in asteroids:
            if asteroid_loop.collides_with(player):

                if player.invincibility_timer > 0:
                    pass
                elif (player.lives - 1 <= 0):
                    log_event("player_died")
                    print(f"Game over!\nScore: {score}")
                    sys.exit()
                else:
                    player.respawn()
                    log_event("player_hit_respawned")

            shot_loop: Shot
            for shot_loop in shots:
                if shot_loop.collides_with(asteroid_loop):
                   log_event("asteroid_shot")
                   shot_loop.kill()
                   asteroid_loop.split()
                   score = int(score + asteroid_loop.score)

        font_surface_score = font.render(f"Score: {score}", None, FONT_COLOR)
        font_surface_lives = font.render(f"Lives left: {player.lives}", None, FONT_COLOR)
        screen.blits([(font_surface_score, font_coord_score), \
                      (font_surface_lives, font_coord_lives)])

        if player.invincibility_timer > 0:
            font_surface_invincibility = \
                font.render(f"Invincibility: {round(player.invincibility_timer, 1)}", None, FONT_COLOR)
            screen.blit(font_surface_invincibility, font_coord_invincibility)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()
