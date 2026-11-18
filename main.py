import pygame, sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from menus import Menu
from boxes import Box
from menu_screens import *

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.font.init()

    start_screen = Menu("Start")
    control_screen = Menu("Controls")
    chosen_box = start(start_screen, screen)

    started = False
    paused = False
    stop_hold_control = True

    while not started:
        if chosen_box.name == "Start":
            started = True

        elif chosen_box.name == "Controls":
            screen.fill("black")
            chosen_box = controls(control_screen, screen, stop_hold_control)
            if stop_hold_control and (not pygame.key.get_pressed()[pygame.K_RETURN]):
                stop_hold_control = False

        elif chosen_box.name == "Back":
            chosen_box = start(start_screen, screen)
            stop_hold_control = True

        pygame.display.flip()
    
    clock = pygame.time.Clock()
    dt = 0.0

    font = pygame.font.Font(None, REG_FONT_SIZE)
    score = 0

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

    stop_hold_pause = True
    stop_hold_control = True

    while True: # gameloop
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if pygame.key.get_pressed()[pygame.K_p]:
            pause_screen = Menu("Pause")
            paused = True
            init_pause = True
        
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            sys.exit()

        log_state()
        for event in pygame.event.get():
            pass

        screen.fill("black")

        if not paused: # only updates if not paused, still draws (else)
            updatable.update(dt)
            for drawable_item in drawable:
                drawable_item.draw(screen)

            asteroid_loop: Asteroid
            for asteroid_loop in asteroids:
                if asteroid_loop.collides_with(player):

                    if player.invincibility_timer > 0:
                        pass
                    elif (player.lives <= 1):
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
            screen.blits([(font_surface_score, SCORE_DISP_COORDS), \
                        (font_surface_lives, LIVES_DISP_COORDS)])

            if player.invincibility_timer > 0:
                font_surface_invincibility = \
                    font.render(f"Invincibility: {round(player.invincibility_timer, 1)}", None, FONT_COLOR)
                screen.blit(font_surface_invincibility, INVINCIBILITY_DISP_COORDS)
        
        else: # if paused, draws game objects transparently
            for drawable_item in drawable:
                drawable_item.draw(screen, "dark gray")
                
            if (chosen_box.name == "Pause") or init_pause:
                chosen_box = pause(pause_screen, screen, stop_hold_pause)
                if stop_hold_pause and (not pygame.key.get_pressed()[pygame.K_RETURN]):
                    stop_hold_pause = False
                stop_hold_control = True
                init_pause = False

            elif chosen_box.name == "Resume":
                paused = False
                stop_hold_pause = True
                stop_hold_control = True

            elif chosen_box.name == "Controls":
                chosen_box = controls(control_screen, screen, stop_hold_control, paused)
                if stop_hold_control and (not pygame.key.get_pressed()[pygame.K_RETURN]):
                    stop_hold_control = False
                stop_hold_pause = True
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
