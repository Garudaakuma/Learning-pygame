# imports labrary
import pygame as pyg, sys, time

# imports self library
...

class Game():
    def __init__(self) -> None:
        pyg.init()
        
        self.RESOLUTION = (1270, 720)
        self.BACKGROUND_COLOR = '#000000'
        self.FPS = 60
        
        pyg.display.set_caption('Stay alive!')
        self.screen = pyg.display.set_mode(self.RESOLUTION, )
        self.display = pyg.Surface((self.screen.get_width()/2, self.screen.get_height()/2))
        
        
        self.clock = pyg.time.Clock()
        self.last_time = time.time()
        
    def run(self):
        while True:
            dt = time.time() - self.last_time   # delta time
            dt *= self.FPS                      # remain time/movement constant
            self.last_time = time.time()        # updates last time
            
            self.display.fill(self.BACKGROUND_COLOR)
            
            ...
            
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    sys.exit()
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        pyg.quit()
                        sys.exit()
                    
            self.screen.blit(pyg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.clock.tick(self.FPS)
            pyg.display.update()