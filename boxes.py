import pygame
from constants import *

class Box:
    def __init__(self, information: list[tuple[int] | str]):
        self.name = information[0]
        self.width = information[1][0]
        self.height = information[1][1]

        self.corner_coords = self.get_corner_coords(information[2][1])
        self.position_TL = self.corner_coords[3]
        self.text_pos = (self.position_TL[0] + information[3][0], self.position_TL[1] - information[3][1])
    
    def get_corner_coords(self, vert_offset=0) -> tuple[tuple[float]]:
        top_left = ((SCREEN_WIDTH/ 2) - (self.width / 2), (SCREEN_HEIGHT / 2) - (self.height / 2) + vert_offset)
        top_right = ((SCREEN_WIDTH / 2) + (self.width / 2), (SCREEN_HEIGHT / 2) - (self.height / 2) + vert_offset)
        bottom_left = ((SCREEN_WIDTH / 2) - (self.width / 2), (SCREEN_HEIGHT / 2) + (self.height / 2) + vert_offset)
        bottom_right = ((SCREEN_WIDTH / 2) + (self.width / 2), (SCREEN_HEIGHT / 2) + (self.height / 2) + vert_offset)
        return (bottom_left, bottom_right, top_right, top_left)