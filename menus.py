import pygame, sys
from constants import *
from boxes import Box

class Menu:
    def __init__(self, name: str) -> None:
        self.name = name
        self.selectable_boxes = self.get_box_names()

    def get_box_names(self) -> list[str]:
        box_names = []
        for box_loop in SCREEN_INFO[self.name]:
            if "Help" not in box_loop:
                box_names.append(box_loop)
        return box_names

    def init_arrow(self, box: Box) -> tuple[tuple[float]]:
        return ((box.position_TL[0] - ARROW_OFFSET - ARROW_LENGTH, box.position_TL[1] + (box.height / 2)),\
                (box.position_TL[0] - ARROW_OFFSET, box.position_TL[1] + (box.height / 2)),\
                (box.position_TL[0] - ARROW_OFFSET - ARROW_POINT_LENGTH, box.position_TL[1] + ARROW_POINT_HEIGHT + (box.height / 2)),\
                (box.position_TL[0] - ARROW_OFFSET - ARROW_POINT_LENGTH, box.position_TL[1] - ARROW_POINT_HEIGHT + (box.height / 2)),\
                (box.position_TL[0] - ARROW_OFFSET, box.position_TL[1] + (box.height / 2)))

    def move_arrow(self):
        pass

    def draw_boxes(self):
        pass

    def draw_text(self):
        pass


def start(screen) -> str:
    start_screen = Menu("Start")
    start_box = Box(SCREEN_INFO["Start"]["Start"])
    controls_box = Box(SCREEN_INFO["Start"]["Controls"])
    help_text = Box(SCREEN_INFO["Start"]["Help"])
    help2_text = Box(SCREEN_INFO["Start"]["Help2"])

    move_down_count = 0
    max_move_down = 1
    can_move_down = True
    can_move_up = False
    currently_selected = start_screen.selectable_boxes[move_down_count]

    arrow_coords = start_screen.init_arrow(start_box)

    while on_static_screen(pygame.K_RETURN):
        screen.fill("black")

        large_font = pygame.font.Font(None, 2*FONT_SIZE)
        medium_font = pygame.font.Font(None, round(1.5*FONT_SIZE))

        font_surface_start = large_font.render(start_box.name, None, FONT_COLOR)
        screen.blit(font_surface_start, start_box.text_pos)
        pygame.draw.polygon(screen, FONT_COLOR, start_box.corner_coords, LINE_WIDTH)

        font_surface_controls = medium_font.render(controls_box.name, None, FONT_COLOR)
        screen.blit(font_surface_controls, controls_box.text_pos)
        pygame.draw.polygon(screen, FONT_COLOR, controls_box.corner_coords, LINE_WIDTH)

        small_font = pygame.font.Font(None, FONT_SIZE)
        font_surface_help = small_font.render(help_text.name, None, FONT_COLOR)
        screen.blit(font_surface_help, help_text.text_pos)
        font_surface_help2 = small_font.render(help2_text.name, None, FONT_COLOR)
        screen.blit(font_surface_help2, help2_text.text_pos)

        if pygame.key.get_pressed()[pygame.K_s] and can_move_down:
            can_move_up = True
            move_down_count += 1
            if move_down_count >= max_move_down:
                can_move_down = False
            arrow_coords = move_arrow(arrow_coords, -100)
        if pygame.key.get_pressed()[pygame.K_w] and can_move_up:
            can_move_down = True
            move_down_count -= 1
            if move_down_count <= 0:
                can_move_up = False
            arrow_coords = move_arrow(arrow_coords, 100)

        currently_selected = start_screen.selectable_boxes[move_down_count]

        pygame.draw.polygon(screen, "white", arrow_coords, LINE_WIDTH)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    return currently_selected

def on_static_screen(key_pressed) -> bool:
    keys = pygame.key.get_pressed()
    if keys[key_pressed]:
        return False
    if keys[pygame.K_ESCAPE]:
        sys.exit()
    return True

def move_arrow(coords, y_amount) -> tuple[tuple[float]]:
    new_coords = []
    for coord_loop in coords:
        new_coords.append((coord_loop[0], coord_loop[1] - y_amount))
    new_coords = tuple(new_coords)
    return new_coords

def pause(screen) -> None:    
    large_font = pygame.font.Font(None, 2*FONT_SIZE)
    font_surface_start = large_font.render("PAUSED", None, FONT_COLOR)
    #screen.blit(font_surface_start, PAUSE_TEXT_COORDS)

    small_font = pygame.font.Font(None, FONT_SIZE)
    font_surface_help = small_font.render("Press ""ENTER/RETURN"" to unpause", None, FONT_COLOR)
    #screen.blit(font_surface_help, PAUSE_HELP_TEXT_COORDS)

    #pygame.draw.polygon(screen, "white", PAUSE_BOX_COORDS, LINE_WIDTH)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return