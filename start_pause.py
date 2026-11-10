import pygame, sys

from constants import *

def start(screen) -> None:
    while on_static_screen(pygame.K_RETURN):
        screen.fill("black")

        pygame.font.init()
        large_font = pygame.font.Font(None, 2*FONT_SIZE)
        font_surface_start = large_font.render("Start", None, FONT_COLOR)
        screen.blit(font_surface_start, START_TEXT_COORDS)

        small_font = pygame.font.Font(None, FONT_SIZE)
        font_surface_help = small_font.render("Press ""ENTER/RETURN"" to start", None, FONT_COLOR)
        screen.blit(font_surface_help, HELP_TEXT_COORDS)

        pygame.draw.polygon(screen, "white", START_BOX_COORDS, LINE_WIDTH)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

def on_static_screen(key_pressed) -> bool:
    keys = pygame.key.get_pressed()
    if keys[key_pressed]:
        return False
    if keys[pygame.K_ESCAPE]:
        sys.exit()
    return True

def pause(screen) -> None:
    while on_static_screen(pygame.K_RETURN):
        screen.fill("black")
        
        pygame.font.init()
        large_font = pygame.font.Font(None, 2*FONT_SIZE)
        font_surface_start = large_font.render("PAUSED", None, FONT_COLOR)
        screen.blit(font_surface_start, START_TEXT_COORDS)

        small_font = pygame.font.Font(None, FONT_SIZE)
        font_surface_help = small_font.render("Press ""ENTER/RETURN"" to unpause", None, FONT_COLOR)
        screen.blit(font_surface_help, HELP_TEXT_COORDS)

        pygame.draw.polygon(screen, "white", START_BOX_COORDS, LINE_WIDTH)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return