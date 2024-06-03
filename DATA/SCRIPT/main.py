# imports
import pygame
import sys

# imports self library:
import DATA.SCRIPT.utility as _ut
import DATA.SCRIPT.entities as _en
import DATA.SCRIPT.tile_map as _ti


class Game:
    def __init__(self) -> None:
        pygame.init()
        
        self.screen_resolution = [640, 480] # width, height
        self.background_color = "#4287f5" # background
        
        pygame.display.set_caption("...")
        self.screen = pygame.display.set_mode((self.screen_resolution[0], self.screen_resolution[1]))
        self.display = pygame.Surface((self.screen_resolution[0]/2, self.screen_resolution[1]/2))
        
        self.clock = pygame.time.Clock()
        self.FPS = 60
        
        self.movement = [False, False]
        
        self.assets = {
            'decor': _ut.load_images('tiles/decor'),
            'grass': _ut.load_images('tiles/grass'),
            'large_decor': _ut.load_images('tiles/large_decor'),
            'stone': _ut.load_images('tiles/stone'),
            'player': _ut.load_image('entities/player.png')
        }
        
        self.player = _en.PhysicsEntity(self, 'player', (50, 50), (8, 15))
        
        self.tile_map = _ti.tile_map(self, tile_size=16)
        
        ...
        
    def run(self):
        print("main.py - inicializado!")
        while True:
            self.display.fill(self.background_color)
            
            self.tile_map.render(self.display)
            
            self.player.update(self.tile_map, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Programa finalizado!")
                    pygame.quit()
                    sys.exit()
                # PRESSED KEY
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[1] = True
                # RELEASED KEY
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.movement[1] = False
                        
            # update clock
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(self.FPS)

