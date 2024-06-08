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
        self.pos_y_c, self.pos_x_c = [True, False], [True, False]
        
        self.pos_poly1 = pyg_.Vector2(self.surface.get_width() / 2, self.surface.get_height() / 2)
        self.pos_x_1, self.pos_y_1 = [True, False], [True, False]
        self.pos_poly2 = pyg_.Vector2(self.surface.get_width() / 2, (self.surface.get_height() / 2) + 25)
        self.pos_x_2, self.pos_y_2 = [True, False], [True, False]
        
    def up_down(self, vector, pos_x, pos_y, speed=1):
        # y
        if pos_y[0]:
            vector.y += speed
            if vector.y >= self.surface.get_height():
                pos_y[0] = False
                pos_y[1] = True
                #speed += 1
        if pos_y[1]:
            vector.y -= speed
            if vector.y <= 0:
                pos_y[0] = True
                pos_y[1] = False
                #speed += 1
        
        # x
        if pos_x[0]:
            vector.x += speed
            if vector.x >= self.surface.get_width():
                pos_x[0] = False
                pos_x[1] = True
                #speed += 1
        if pos_x[1]:
            vector.x -= speed
            if vector.x <= 0:
                pos_x[0] = True
                pos_x[1] = False
                #speed += 1
                
        
    def run(self):
        print("Game running!")
        while True:
            self.surface.fill(self.background_color)
            
            pyg_.draw.polygon(self.surface, '#0000d5', [(self.pos_poly1.x, self.pos_poly1.y), (self.pos_poly2.x, self.pos_poly2.y)], 25)
            self.up_down(self.pos_poly1, self.pos_x_1, self.pos_y_1)
            self.up_down(self.pos_poly2, self.pos_x_2, self.pos_y_2)
            
            pyg_.draw.circle(self.surface, '#00d500', self.pos_circle, 15)
            self.up_down(self.pos_circle, self.pos_x_c, self.pos_y_c)
            
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
            