import pygame, sys
from constants import *
from boxes import Box

class Menu:
    def __init__(self, name: str) -> None:
        self.name = name
        self.selectable_boxes = self.get_box_names()
        self.currently_selected = self.selectable_boxes[0]

    def get_box_names(self) -> list[Box]:
        box_list = []
        for box_loop in SCREEN_INFO[self.name]:
            if "Help" not in box_loop:
                box_init_loop = Box(SCREEN_INFO[self.name][box_loop])
                box_list.append(box_init_loop)
        return box_list

    def init_arrow(self, box: Box) -> tuple[tuple[float]]:
        box_pos_x = box.position_TL[0]
        box_pos_y = box.position_TL[1]
        return ((box_pos_x - ARROW_OFFSET - ARROW_LENGTH, box_pos_y + (box.height / 2)),\
                (box_pos_x - ARROW_OFFSET, box_pos_y + (box.height / 2)),\
                (box_pos_x - ARROW_OFFSET - ARROW_POINT_LENGTH, box_pos_y + ARROW_POINT_HEIGHT + (box.height / 2)),\
                (box_pos_x - ARROW_OFFSET - ARROW_POINT_LENGTH, box_pos_y - ARROW_POINT_HEIGHT + (box.height / 2)),\
                (box_pos_x - ARROW_OFFSET, box_pos_y + (box.height / 2)))

    def check_move_arrow(self, current_coords) -> tuple[tuple[float]]:
        new_coords = current_coords

        current_selection_index = self.selectable_boxes.index(self.currently_selected)
        max_index = len(self.selectable_boxes) - 1
        can_move_down = False
        can_move_up = False
        if current_selection_index < max_index:
            can_move_down = True
        elif current_selection_index > 0:
            can_move_up = True

        y_move = 0
        x_move = 0

        if pygame.key.get_pressed()[pygame.K_s] and can_move_down:
            y_move = self.selectable_boxes[current_selection_index + 1].position_TL[1] - self.currently_selected.position_TL[1]
            x_move = self.selectable_boxes[current_selection_index + 1].position_TL[0] - self.currently_selected.position_TL[0]

            can_move_up = True
            self.currently_selected = self.selectable_boxes[current_selection_index + 1]
            if current_selection_index >= max_index:
                can_move_down = False
            new_coords = self.move_arrow(current_coords, y_move, x_move)
        elif pygame.key.get_pressed()[pygame.K_w] and can_move_up:
            y_move = self.selectable_boxes[current_selection_index - 1].position_TL[1] - self.currently_selected.position_TL[1]
            x_move = self.selectable_boxes[current_selection_index - 1].position_TL[0] - self.currently_selected.position_TL[0]

            can_move_down = True
            self.currently_selected = self.selectable_boxes[current_selection_index - 1]
            if current_selection_index <= 0:
                can_move_up = False
            new_coords = self.move_arrow(current_coords, y_move, x_move)
        return new_coords

    def move_arrow(self, coords, y_amount, x_amount) -> tuple[tuple[float]]:
        new_coords = []
        for coord_loop in coords:
            new_coords.append((coord_loop[0] + x_amount, coord_loop[1] + y_amount))
        new_coords = tuple(new_coords)
        return new_coords

    def draw(self, box_to_draw: Box, font_size=REG_FONT_SIZE, screen=None, line_width=0) -> None:
        font_surface = font_size.render(box_to_draw.name, None, FONT_COLOR)
        screen.blit(font_surface, box_to_draw.text_pos)
        pygame.draw.polygon(screen, FONT_COLOR, box_to_draw.corner_coords, line_width)

    def on_static_screen(self, key_pressed=pygame.K_RETURN) -> bool:
        keys = pygame.key.get_pressed()
        if keys[key_pressed]:
            return False
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        return True