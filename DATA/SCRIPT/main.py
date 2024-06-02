# imports
import pygame
import sys

# imports self library:
import DATA.SCRIPT.utility as _ut
import DATA.SCRIPT.entities as _en

class Game:
    def __init__(self) -> None:
        pygame.init()
        
        self.screen_resolution = (640, 480) # width, height
        self.background_color = "#4287f5" # background
        
        pygame.display.set_caption("...")
        self.screen = pygame.display.set_mode(self.screen_resolution)
        
        self.clock = pygame.time.Clock()
        self.FPS = 60
        
        self.movement = [False, False]
        
        self.assets = {
            'player': _ut.load_image('entities/player.png')
        }
        
        self.player = _en.PhysicsEntity(self, 'player', (50, 50), (8, 15))
        
    def run(self):
        print("main.py - inicializado!")
        while True:
            self.screen.fill(self.background_color)
            
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # PRESSED KEY
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_d:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_a:
                        self.movement[1] = True
                # RELEASED KEY
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_d:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_a:
                        self.movement[1] = False
                        
            # update clock
            pygame.display.update()
            self.clock.tick(self.FPS)

