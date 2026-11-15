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

    while start_screen.on_static_screen():
        screen.fill("black")

        regular_font = pygame.font.Font(None, REG_FONT_SIZE)
        medium_font = pygame.font.Font(None, MED_FONT_SIZE)
        large_font = pygame.font.Font(None, LARGE_FONT_SIZE)

        start_screen.draw(start_box, large_font, screen, LINE_WIDTH)
        start_screen.draw(controls_box, medium_font, screen, LINE_WIDTH)
        start_screen.draw(help_text, regular_font, screen)
        start_screen.draw(help2_text, regular_font, screen)

        arrow_coords = start_screen.check_move_arrow(arrow_coords)
        pygame.draw.polygon(screen, LINE_COLOR, arrow_coords, LINE_WIDTH)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    return start_screen.currently_selected

def pause(self: Menu, screen) -> None:
    resume_box = Box(SCREEN_INFO["Pause"]["Resume"])
    controls_box = Box(SCREEN_INFO["Pause"]["Controls"])

    regular_font = pygame.font.Font(None, REG_FONT_SIZE)
    medium_font = pygame.font.Font(None, MED_FONT_SIZE)
    large_font = pygame.font.Font(None, LARGE_FONT_SIZE)

    self.draw(resume_box, large_font, screen, LINE_WIDTH)
    self.draw(controls_box, medium_font, screen, LINE_WIDTH)

    arrow_coords = self.init_arrow(self.currently_selected)
    arrow_coords = self.check_move_arrow(arrow_coords)
    pygame.draw.polygon(screen, LINE_COLOR, arrow_coords, LINE_WIDTH)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    return self.on_static_screen()