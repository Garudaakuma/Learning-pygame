
# imports
import pygame as pyg

# self import
...

class utility():
    def __init__(self, display: pyg.Surface) -> None:
        self.PATH = {
            'PATH': 'TDE - PYGAME/DATA/',
            'AUDIOS': 'TDE - PYGAME/DATA/AUDIOS/',
            'FONTS': 'TDE - PYGAME/DATA/FONTS/',
            'IMAGE': 'TDE - PYGAME/DATA/IMAGE/',
        }
        self.display = display
    def image_load(self, folder: str, file_name: str) -> pyg.Surface:
        return pyg.image.load(self.PATH[folder]+file_name).convert()
    def get_rect(self, surface: pyg.Surface, vector2: pyg.Vector2) -> pyg.Rect:
        return surface.get_rect(midbottom=(vector2))

 
class transition_image():
    def __init__(self, display) -> None:
        self.fade_alpha = 255
        self.fade_surface = pyg.Surface((self.display.get_width(), self.display.get_height())).convert()
        self.fade_surface.fill('#1b1d1e')
        self.fade_surface.set_alpha(self.fade_alpha)
  
    def fade_in(self, speed, dt):
        self.fade_alpha += speed * dt
        self.fade_surface.set_alpha(self.fade_alpha)
        self.display.blit(self.fade_surface, (0,0))

    def fade_out(self, speed, dt):
        self.fade_alpha -= speed * dt
        self.fade_surface.set_alpha(self.fade_alpha)
        self.display.blit(self.fade_surface, (0,0))

