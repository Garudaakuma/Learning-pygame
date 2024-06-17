# imports
import pygame as pyg

# import self library
import DATA.SCRIPT.utilities as util_

class scenery():
    def __init__(self, display: pyg.Surface, image: str, pos_x: float, pos_y: float):
        self.display = display
        self.surfaces = [util_.utility(display).image_load('IMAGE', image),
                         util_.utility(display).image_load('IMAGE', image)]
        self.rects = [self.surfaces[0].get_rect(midbottom=(pos_x, pos_y)),
                      self.surfaces[1].get_rect(midbottom=(self.display.get_width()+pos_x, pos_y))]
    def render(self, speed, dt):
        for rect in self.rects:
            if rect.x <= -(self.display.get_width()):
                rect.x = self.display.get_width()
            rect.x -= speed * dt
            self.display.blit(self.surfaces[self.rects.index(rect)], (rect.x - (speed - 1), rect.y))

print("scenario.py loaded!")
