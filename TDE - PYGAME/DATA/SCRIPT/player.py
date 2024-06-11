# import
import pygame as pyg

# self import
import DATA.SCRIPT.utilities as util_

class Player():
    def __init__(self, display: pyg.Surface):
        self.display = display
        self.util = util_.utility(display)
        
        self.surface = self.util.image_load('IMAGE','PLAYER/player_standing.png')
        self.pos = pyg.Vector2(32, self.display.get_height()-32)
        self.rect = self.util.get_rect(self.surface, self.pos)
        
        self.ground = True
        self.gravity = 0
    
    def reset(self):
        self.pos = pyg.Vector2(32, self.display.get_height()-32)
        self.rect = self.util.get_rect(self.surface, self.pos)
        self.ground = True
        self.gravity = 0
    
    def physics_update(self, dt):
        self.gravity += 1 * dt
        self.rect.y += min(10, self.gravity + 0.1) * dt
        if self.rect.bottom >= self.display.get_height()-32:
            self.ground = True
            self.rect.bottom = self.display.get_height()-32