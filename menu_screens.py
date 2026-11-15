import pygame
from constants import *
from menus import Menu
from boxes import Box

def start(screen) -> str:
    start_screen = Menu("Start")
    start_box = Box(SCREEN_INFO["Start"]["Start"])
    controls_box = Box(SCREEN_INFO["Start"]["Controls"])
    help_text = Box(SCREEN_INFO["Start"]["Help"])
    help2_text = Box(SCREEN_INFO["Start"]["Help2"])

    arrow_coords = start_screen.init_arrow(start_box)

    while start_screen.on_static_screen(pygame.K_RETURN):
        screen.fill("black")

        regular_font = pygame.font.Font(None, REG_FONT_SIZE)
        medium_font = pygame.font.Font(None, MED_FONT_SIZE)
        large_font = pygame.font.Font(None, LARGE_FONT_SIZE)

        start_screen.draw(start_box, large_font, screen, LINE_WIDTH)
        start_screen.draw(controls_box, medium_font, screen, LINE_WIDTH)
        start_screen.draw(help_text, regular_font, screen)
        start_screen.draw(help2_text, regular_font, screen)

        arrow_coords = start_screen.check_move_arrow(arrow_coords, 100)
        pygame.draw.polygon(screen, LINE_COLOR, arrow_coords, LINE_WIDTH)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    return start_screen.currently_selected

def pause(screen) -> None:    
    large_font = pygame.font.Font(None, LARGE_FONT_SIZE)
    font_surface_start = large_font.render("PAUSED", None, FONT_COLOR)
    #screen.blit(font_surface_start, PAUSE_TEXT_COORDS)

    small_font = pygame.font.Font(None, REG_FONT_SIZE)
    font_surface_help = small_font.render("Press ""ENTER/RETURN"" to unpause", None, FONT_COLOR)
    #screen.blit(font_surface_help, PAUSE_HELP_TEXT_COORDS)

    #pygame.draw.polygon(screen, "white", PAUSE_BOX_COORDS, LINE_WIDTH)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return