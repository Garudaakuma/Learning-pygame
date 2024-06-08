# imports
import pygame as pyg_, sys

# imports self library
...

class Game():
    def __init__(self):
        pyg_.init()
        
        self.screen_size = [1270, 720]
        self.background_color = '#aaaaaa'
        
        self.display = pyg_.display.set_mode((self.screen_size[0], self.screen_size[1]))
        self.surface = pyg_.Surface((self.screen_size[0]/2, self.screen_size[1]/2))
        
        self.clock = pyg_.time.Clock()
        self.FPS = 120
        
        self.pos_circle = pyg_.Vector2(self.surface.get_width() / 2, self.surface.get_height() / 2)
        self.pos_y = [True, False]
        self.pos_x = [True, False]
        self.speed = 1
        
    def up_down(self):
        
        # y
        if self.pos_y[0]:
            self.pos_circle.y += self.speed
            if self.pos_circle.y >= self.surface.get_height() - 15:
                self.pos_y[0] = False
                self.pos_y[1] = True
                self.speed += 1
        if self.pos_y[1]:
            self.pos_circle.y -= self.speed
            if self.pos_circle.y <= 15:
                self.pos_y[0] = True
                self.pos_y[1] = False
                self.speed += 1
        
        # x
        if self.pos_x[0]:
            self.pos_circle.x += self.speed
            if self.pos_circle.x >= self.surface.get_width() - 15:
                self.pos_x[0] = False
                self.pos_x[1] = True
                self.speed += 1
        if self.pos_x[1]:
            self.pos_circle.x -= self.speed
            if self.pos_circle.x <= 15:
                self.pos_x[0] = True
                self.pos_x[1] = False
                self.speed += 1
        
        print(f'x:{self.pos_circle.x:>7}, y:{self.pos_circle.y:>7} || speed:{self.speed:>4}')
        
    def run(self):
        print("Game running!")
        while True:
            self.surface.fill(self.background_color)
            
            pyg_.draw.circle(self.surface, '#0000d5', self.pos_circle, 15)
            
            self.up_down()
            
            for event in pyg_.event.get():
                if event.type == pyg_.QUIT:
                    print("Game quit!")
                    pyg_.quit()
                    sys.exit()
                if event.type == pyg_.KEYDOWN:
                    if event.key == pyg_.K_ESCAPE:
                        print("Game quit!")
                        pyg_.quit()
                        sys.exit()
            
            self.display.blit(pyg_.transform.scale(self.surface, self.display.get_size()), (0,0))
            pyg_.display.update()
            self.clock.tick(self.FPS)
            