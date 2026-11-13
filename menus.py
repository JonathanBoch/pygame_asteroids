import pygame, sys
from constants import *

class Menu:
    def __init__(self, name: str, selectable_boxes: list[str]) -> None:
        self.name = name
        self.selectable_boxes = selectable_boxes
        self.num_boxes = len(selectable_boxes) + 1

    def get_boxes(self, offset_list: list[int]) -> list[tuple[tuple[float]]]:
        box_coords_list = []
        offset_num = 0
        for box_loop in self.selectable_boxes:
            box_loop_width = BOX_DIMENSIONS[box_loop][0]
            box_loop_height = BOX_DIMENSIONS[box_loop][1]
            offset_loop = offset_list[offset_num]
            box_coords = self.get_box_coords(box_loop_width, box_loop_height, offset_loop)

            box_coords_list.append(box_coords)
            offset_num += 1
        return box_coords_list

    def get_box_coords(box_width, box_height, vert_offset=0) -> tuple[tuple[float]]:
        top_left = ((SCREEN_WIDTH/ 2) - (box_width / 2), (SCREEN_HEIGHT / 2) - (box_height / 2) - vert_offset)
        top_right = ((SCREEN_WIDTH / 2) + (box_width / 2), (SCREEN_HEIGHT / 2) - (box_height / 2) - vert_offset)
        bottom_left = ((SCREEN_WIDTH / 2) - (box_width / 2), (SCREEN_HEIGHT / 2) + (box_height / 2) - vert_offset)
        bottom_right = ((SCREEN_WIDTH / 2) + (box_width / 2), (SCREEN_HEIGHT / 2) + (box_height / 2) - vert_offset)
        return (bottom_left, bottom_right, top_right, top_left)

    def get_text_coords(self, offset_list: list[tuple[int]]):


def start(screen) -> None:
    start_screen = Menu("Start", START_BOXES)

    move_down_count = 0
    max_move_down = 1
    can_move_down = True
    can_move_up = False
    selectable_boxes = ["Start", "Options"]

    arrow_coords = (((SCREEN_WIDTH/ 2) - 200, (SCREEN_HEIGHT / 2) - 50),\
                    ((SCREEN_WIDTH/ 2) - 130, (SCREEN_HEIGHT / 2) - 50),\
                    ((SCREEN_WIDTH/ 2) - 150, (SCREEN_HEIGHT / 2) - 70),\
                    ((SCREEN_WIDTH/ 2) - 150, (SCREEN_HEIGHT / 2) - 30),\
                    ((SCREEN_WIDTH/ 2) - 130, (SCREEN_HEIGHT / 2) - 50))

    while on_static_screen(pygame.K_RETURN):
        screen.fill("black")

        large_font = pygame.font.Font(None, 2*FONT_SIZE)
        medium_font = pygame.font.Font(None, round(1.5*FONT_SIZE))

        font_surface_start = large_font.render("Start", None, FONT_COLOR)
        screen.blit(font_surface_start, START_TEXT_COORDS)
        pygame.draw.polygon(screen, "white", START_BOX_COORDS, LINE_WIDTH)

        font_surface_options = medium_font.render("Options", None, FONT_COLOR)
        screen.blit(font_surface_options, OPTIONS_TEXT_COORDS)
        pygame.draw.polygon(screen, "white", OPTIONS_BOX_COORDS, LINE_WIDTH)

        small_font = pygame.font.Font(None, FONT_SIZE)
        font_surface_help = small_font.render("Press ""ENTER/RETURN"" to confirm", None, FONT_COLOR)
        screen.blit(font_surface_help, START_HELP_TEXT_COORDS)
        font_surface_help2 = small_font.render("Press ""W/S"" to navigate", None, FONT_COLOR)
        screen.blit(font_surface_help2, START_HELP2_TEXT_COORDS)

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

        currently_selected = selectable_boxes[move_down_count]

        pygame.draw.polygon(screen, "white", arrow_coords, LINE_WIDTH)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    # return currently_selected here (on this line)
    # So it changes the behavior if "Start" or "Options" is selected

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
    screen.blit(font_surface_start, PAUSE_TEXT_COORDS)

    small_font = pygame.font.Font(None, FONT_SIZE)
    font_surface_help = small_font.render("Press ""ENTER/RETURN"" to unpause", None, FONT_COLOR)
    screen.blit(font_surface_help, PAUSE_HELP_TEXT_COORDS)

    pygame.draw.polygon(screen, "white", PAUSE_BOX_COORDS, LINE_WIDTH)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return