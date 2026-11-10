import pygame, sys

from constants import *

def start(screen) -> str:
    pygame.init()
    action = None

    while on_start_screen():
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
                action = "quit"
                return action

def on_start_screen() -> bool:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        return False
    return True