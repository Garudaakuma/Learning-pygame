# imports
import pygame as pyg_

# imports self library
...

class Game():
    def __init__(self) -> None:
        self.display = pyg_.display.set_mode((450,680))
    def run(self):
        print("Game running!")
