import pygame
from constants import *
from menus import Menu
from boxes import Box

def start(start_screen: Menu, screen) -> Box:
    start_box = Box(SCREEN_INFO["Start"]["Start"])
    controls_box = Box(SCREEN_INFO["Start"]["Controls"])
    help_text = Box(SCREEN_INFO["Start"]["Help"])
    help2_text = Box(SCREEN_INFO["Start"]["Help2"])

    start_screen.currently_selected = start_screen.selectable_boxes[0]

    arrow_coords = start_screen.init_arrow(start_box)

    selected_smth = False

    while not selected_smth:
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
            if event.type == pygame.KEYDOWN:
                selected_smth = start_screen.on_static_screen()

    return start_screen.currently_selected

def pause(pause_screen: Menu, screen) -> bool:
    empty_box = Box(SCREEN_INFO["Pause"]["HelpNone"])
    resume_box = Box(SCREEN_INFO["Pause"]["Resume"])
    controls_box = Box(SCREEN_INFO["Pause"]["Controls"])

    regular_font = pygame.font.Font(None, REG_FONT_SIZE)
    medium_font = pygame.font.Font(None, MED_FONT_SIZE)
    large_font = pygame.font.Font(None, LARGE_FONT_SIZE)

    pause_screen.draw(resume_box, large_font, screen, LINE_WIDTH)
    pause_screen.draw(controls_box, medium_font, screen, LINE_WIDTH)

    arrow_coords = pause_screen.init_arrow(pause_screen.currently_selected)
    arrow_coords = pause_screen.check_move_arrow(arrow_coords)
    pygame.draw.polygon(screen, LINE_COLOR, arrow_coords, LINE_WIDTH)

    selected_smth = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
        if event.type == pygame.KEYDOWN:
            selected_smth = pause_screen.on_static_screen()

    if selected_smth:
        selected_box = pause_screen.currently_selected
    selected_box = empty_box
    return selected_box, not pause_screen.on_static_screen()

def controls(control_screen: Menu, screen) -> Box:
    empty_box = Box(SCREEN_INFO["Controls"]["HelpNone"])
    back_box = Box(SCREEN_INFO["Controls"]["Back"])
    help_text = Box(SCREEN_INFO["Controls"]["Back"])

    regular_font = pygame.font.Font(None, REG_FONT_SIZE)
    medium_font = pygame.font.Font(None, MED_FONT_SIZE)
    large_font = pygame.font.Font(None, LARGE_FONT_SIZE)

    control_screen.draw(back_box, large_font, screen, LINE_WIDTH)
    control_screen.draw(help_text, medium_font, screen, LINE_WIDTH)

    arrow_coords = control_screen.init_arrow(control_screen.currently_selected)
    arrow_coords = control_screen.check_move_arrow(arrow_coords)
    pygame.draw.polygon(screen, LINE_COLOR, arrow_coords, LINE_WIDTH)

    selected_smth = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
        if event.type == pygame.KEYDOWN:
            selected_smth = control_screen.on_static_screen()

    if selected_smth:
        return control_screen.currently_selected
    return empty_box