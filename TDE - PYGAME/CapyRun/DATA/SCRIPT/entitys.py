
# import
import pygame as pyg

# self import
import DATA.SCRIPT.utilities as util_



class Enemy():
    def __init__(self, display: pyg.Surface, name:str) -> None:
        self.display = display
        self.util = util_.utility(display)
        self.name = name
        self.img = self.util.image_load('IMAGE',f'ENEMYS/{self.name}.png')
        self.vec = pyg.Vector2(self.display.get_width()+32, self.display.get_height()-32)
        self.rect = self.util.get_rect(self.img, self.vec)

    def reset(self):
        self.vec = pyg.Vector2(self.display.get_width()+32, self.display.get_height()-32)
        self.rect = self.util.get_rect(self.img, self.vec)

    def walk_cicle(self, speed:int, dt:float):
        self.display.blit(self.img, self.rect)
        self.rect.x -= speed+1 * dt
        if self.rect.x <= -32:
            self.rect.x = self.display.get_width()+32

    def colligion_check(self, player_rect) -> bool:
        return self.rect.colliderect(player_rect)

print("entitys.py loaded!")
