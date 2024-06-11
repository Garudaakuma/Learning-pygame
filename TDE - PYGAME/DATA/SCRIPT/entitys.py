
# import
import pygame as pyg

# self import
import DATA.SCRIPT.utilities as util_

class Enemy():
    def __init__(self, display: pyg.Surface, name:str) -> None:
        self.display = display
        self.util = util_.utility(display)
        self.name = name
        self.enemy_img = self.util.image_load('IMAGE',f'ENEMYS/{self.name}.png')
        self.enemy_vec = pyg.Vector2(self.display.get_width()+32, self.display.get_height()-32)
        self.enemy_rect = self.util.get_rect(self.enemy_img, self.enemy_vec)
    
    def reset(self):
        self.enemy_vec = pyg.Vector2(self.display.get_width()+32, self.display.get_height()-32)
        self.enemy_rect = self.util.get_rect(self.enemy_img, self.enemy_vec)
    
    def enemy_walk(self, speed:int, dt:float):
        self.display.blit(self.enemy_img, self.enemy_rect)
        self.enemy_rect.x -= speed * dt
        if self.enemy_rect.x <= -32: self.enemy_rect.x = self.display.get_width()+32
        
    def colligion_check(self, player_rect) -> bool:
        return self.enemy_rect.colliderect(player_rect)