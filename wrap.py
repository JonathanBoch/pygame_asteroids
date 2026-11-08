import pygame

from circleshape import CircleShape
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def adjust_pos(self: CircleShape, where_list: list[str]):
        if "l" in where_list:
            self.position.x += SCREEN_WIDTH + 2*self.radius
        if "r" in where_list:
            self.position.x -= SCREEN_WIDTH + 2*self.radius
        if "t" in where_list:
            self.position.y += SCREEN_HEIGHT  + 2*self.radius # top is y=0, positive y is down
        if "b" in where_list:
            self.position.y -= SCREEN_HEIGHT  + 2*self.radius

def where_off_screen(self: CircleShape):
    where_list = []
    if (self.position.x < -self.radius):
        where_list.append("l")
    if (self.position.x > SCREEN_WIDTH + self.radius):
        where_list.append("r")
    if (self.position.y < -self.radius): # top is y=0, positive y is down
        where_list.append("t")
    if (self.position.y > SCREEN_HEIGHT + self.radius):
        where_list.append("b")
    return where_list