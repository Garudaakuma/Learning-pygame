# imports
import pygame as pyg

# import self library
import DATA.SCRIPT.utilities as util_

class scary():
    def __init__(self, display: pyg.Surface, image: str, pos: list):
        self.display = display
        self.surface = util_.utility(display).image_load('IMAGE', image)
        self.rect = self.surface.get_rect(midbottom=(pos))
    def render(self, speed, dt):
        self.display.blit(self.surface, (self.rect.x - (speed - 1), self.rect.y))
    def update(self):
        if self.rect.x <= -(self.display.get_width()):
            self.rect.x = self.display.get_width()

print("scenario.py loaded!")