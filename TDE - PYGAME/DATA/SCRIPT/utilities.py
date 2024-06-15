
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
        return surface.get_rect(midbottom = (vector2))

    def font_rect(self, surface: pyg.Surface, pos: float):
        return surface.get_rect(center = pos)



class transition_image():
    def __init__(self, display: pyg.Surface) -> None:
        self.display = display
        self.fade_alpha = 0
        self.fade_surface = pyg.Surface((display.get_width(), display.get_height())).convert()
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



class text_fonts():
    def __init__(self, display: pyg.Surface, font_ttf: str, size: int, pos: tuple, text: str, antialias: bool, color: str):
        self.display = display

        self.font_obj = pyg.font.Font(utility(display).PATH['FONTS']+font_ttf, size)
        self.font_surface = self.font_obj.render(text, antialias, color).convert()
        self.font_pos = pos
        self.font_rect = self.font_surface.get_rect(center = self.font_pos)

    def draw_rect(self, color: str, size:int):
        return pyg.draw.rect(self.display, color, self.font_rect, border_radius=size)



class Mouse():
    def __init__(self, display: pyg.Surface) -> None:
        self.display = display
        self.pos = pyg.mouse.get_pos()
        self.surface = utility(display).image_load('IMAGE','cursor.png')
        self.rect = self.surface.get_rect(center=(self.pos[0], self.pos[1]))
        self.mask = pyg.mask.from_surface(self.surface)
        self.clicked = False

    def update(self):
        self.pos = pyg.mouse.get_pos()
        self.pos = (self.pos[0]/2, self.pos[1]/2)
        self.rect.center = (self.pos[0], self.pos[1])

    def render(self):
        return self.display.blit(self.surface, self.rect)



class button_rect():
    def __init__(self, display: pyg.Surface, size: tuple, pos: tuple, color:str, text_obj: text_fonts):
        self.display = display
        self.text_obj = text_obj
        self.surface = pyg.Surface(size).convert()
        self.color = color
        self.fill = self.surface.fill(color)
        self.rect = self.surface.get_rect(center=pos)
        self.mask = pyg.mask.from_surface(self.surface)

    def render(self):
        self.display.blit(self.surface, self.rect)
        self.display.blit(self.text_obj.font_surface, self.text_obj.font_rect)

    def check_collision(self, m_obj: Mouse, color:str):
        self.surface.fill(self.color)
        if self.mask.overlap(m_obj.mask, (m_obj.pos[0] - self.rect.x, m_obj.pos[1] - self.rect.y)):
            self.surface.fill(color)
            self.render()

print("utilities.py loaded!")
