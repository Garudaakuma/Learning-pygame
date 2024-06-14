# imports
import pygame as pyg

# import self library
import DATA.SCRIPT.utilities as util_

class scary():
    def __init__(self, display: pyg.Surface, image: str, pos: list):
        self.display = display
        self.surface = util_.utility(display).image_load('IMAGE', image)

print("scenario.py loaded!")