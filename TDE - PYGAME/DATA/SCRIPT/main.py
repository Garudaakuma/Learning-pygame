# imports labrary
import pygame as pyg, sys, time

# imports self library
...

class Game():
    def __init__(self) -> None:
        self.PATH = 'TDE - PYGAME/DATA/IMAGE/'
        self.RESOLUTION = (1600, 800) # in display = (x: 800, y: 400)
        self.BACKGROUND_COLOR = '#fd971f'
        self.FPS = 60

        pyg.init()
        pyg.display.set_caption('RUN! RUN! RUN!')
        self.screen = pyg.display.set_mode(self.RESOLUTION, )
        self.display = pyg.Surface((self.screen.get_width()/2, self.screen.get_height()/2))

        self.clock = pyg.time.Clock()   # create clock
        self.last_time = time.time()    # gets time

        self.sky_surface = pyg.image.load(self.PATH+'sky_background.png').convert()
        self.ground_surface = pyg.image.load(self.PATH+'floor_grass.png').convert()

        self.score = 0

        self.snail_enmy = pyg.image.load(self.PATH+'ENEMYS/snail.png').convert()
        self.snail_pos = pyg.Vector2(self.display.get_width()+32,self.display.get_height()-32)
        self.snail_rect = self.snail_enmy.get_rect(midbottom = (self.snail_pos))

        self.player_surface = pyg.image.load(self.PATH+'PLAYER/player_standing.png').convert()
        self.player_pos = pyg.Vector2(32, self.display.get_height()-32)
        self.player_rect = self.player_surface.get_rect(midbottom = (self.player_pos))
        self.player_ground = True
        self.player_gravity = 0

    def run(self):
        while True:
            dt = time.time() - self.last_time   # delta time
            dt *= self.FPS                      # remain time/movement constant
            self.last_time = time.time()        # updates last time

            self.display.fill(self.BACKGROUND_COLOR)

            # render
            self.display.blit(self.sky_surface, (0,65))
            self.display.blit(self.ground_surface, (0,self.display.get_height()-32))

            # text
            PATH_FONT = 'TDE - PYGAME/DATA/FONTS/'
            fps_surface = pyg.font.Font(f'{PATH_FONT}ConsolaMono-Book.ttf', 10).render(f'fps: {self.clock.get_fps()*dt:.0f}', False, '#1b1d1e').convert()
            self.display.blit(fps_surface, (0, 0))

            score_surface = pyg.font.Font(f'{PATH_FONT}Daydream.ttf', 20).render(f'Score: {self.score}', False, '#1b1d1e').convert()
            score_rect = score_surface.get_rect(center=(self.display.get_width()/2, self.display.get_height()/4))
            pyg.draw.rect(self.display, '#f8f8f2', score_rect, border_radius=5)
            self.display.blit(score_surface, score_rect)
            
            # snail walking
            self.display.blit(self.snail_enmy, self.snail_rect)
            self.snail_rect.x -= 1 * dt # calling snail x position and subtracting
            if self.snail_rect.right < -32: self.snail_rect.x = self.display.get_width()+32
            
            # player
            self.display.blit(self.player_surface, self.player_rect)
            self.player_gravity += 1 * dt
            self.player_rect.y += min(10, self.player_gravity + 0.1) * dt # gravity working in player
            if self.player_rect.bottom >= self.display.get_height()-32: 
                self.player_ground = True
                self.player_rect.bottom = self.display.get_height()-32
            
            KEYS = pyg.key.get_pressed()
            if KEYS[pyg.K_d] or KEYS[pyg.K_RIGHT]:
                self.player_rect.x += 3 * dt
            if KEYS[pyg.K_a] or KEYS[pyg.K_LEFT]:
                self.player_rect.x -= 3 * dt
            
            for event in pyg.event.get():
                if event.type == pyg.QUIT: self.end()
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE: self.end()
                    if event.key == pyg.K_SPACE and self.player_ground or event.key == pyg.K_w and self.player_ground or event.key == pyg.K_UP and self.player_ground:
                        self.player_gravity = -12
                        self.player_ground = False
                if event.type == pyg.MOUSEBUTTONDOWN and self.player_ground:
                    if self.player_rect.collidepoint((event.pos[0]/2, event.pos[1]/2)):
                        self.player_gravity = -12
                        self.player_ground = False
            
            self.screen.blit(pyg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.clock.tick(self.FPS)
            pyg.display.update()
    def end(self):
        print("Game over!")
        pyg.quit()
        sys.exit()
