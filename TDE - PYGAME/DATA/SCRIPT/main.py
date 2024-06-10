
# imports labrary
import pygame as pyg, sys, time

# imports self library
import DATA.SCRIPT.utilities as util_
import DATA.SCRIPT.entitys as enti_

class Game():
    def __init__(self) -> None:
        self.RESOLUTION = (1600, 800) # in display = (x: 800, y: 400)
        self.BACKGROUND_COLOR = '#fd971f'
        self.FPS = 60

        self.game_state = {
            'Game': True,
            'Game_over': False
        }

        pyg.init()
        pyg.display.set_caption('CapyRun')
        self.screen = pyg.display.set_mode(self.RESOLUTION, )
        self.display = pyg.Surface((self.screen.get_width()/2, self.screen.get_height()/2)).convert()

        self.clock = pyg.time.Clock()   # create clock
        self.last_time = time.time()    # gets time
        
        self.util = util_.utility(self.display)
        
        self.sky_surface = self.util.image_load('IMAGE','sky_background.png')
        self.ground_surface = self.util.image_load('IMAGE','floor_grass.png')

        self.fade_alpha = 255
        self.fade_surface = pyg.Surface((self.display.get_width(),self.display.get_height())).convert()
        self.fade_surface.fill('#1b1d1e')
        self.fade_surface.set_alpha(self.fade_alpha)

        self.score = 0

        self.snail_obj = enti_.enemy(self.display, 'snail')
        
        self.player_surface = pyg.image.load(self.PATH['IMAGE']+'PLAYER/player_standing.png').convert()
        self.player_pos = pyg.Vector2(32, self.display.get_height()-32)
        self.player_rect = self.player_surface.get_rect(midbottom = (self.player_pos))
        self.player_ground = True
        self.player_gravity = 0

    def run(self):
        while True:
            dt = time.time() - self.last_time   # delta time
            dt *= self.FPS                      # remain time/movement constant
            self.last_time = time.time()        # updates last time

            if self.game_state['Game']:
                self.display.fill(self.BACKGROUND_COLOR)

                # render
                self.display.blit(self.sky_surface, (0,65))
                self.display.blit(self.ground_surface, (0,self.display.get_height()-32))

                # text
                fps_surface = pyg.font.Font(f'{self.PATH['FONTS']}ConsolaMono-Book.ttf', 10).render(f'fps: {self.clock.get_fps()*dt:.0f}', False, '#1b1d1e').convert()
                self.display.blit(fps_surface, (0, 0))

                score_surface = pyg.font.Font(f'{self.PATH['FONTS']}Daydream.ttf', 20).render(f'Score: {self.score}', False, '#1b1d1e').convert()
                score_rect = score_surface.get_rect(center=(self.display.get_width()/2, self.display.get_height()/4))
                pyg.draw.rect(self.display, '#f8f8f2', score_rect, border_radius=5)
                self.display.blit(score_surface, score_rect)
                
                # snail walking
                self.snail_obj.enemy_walk(1,dt)
                
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
                
                if self.fade_alpha >= 0:
                    self.fade_alpha -= 10
                    self.fade_surface.set_alpha(self.fade_alpha)
                    self.display.blit(self.fade_surface, (0,0))
                
                if self.snail_obj.colligion_check(self.player_rect):
                    self.fade_alpha += 45
                    self.fade_surface.set_alpha(self.fade_alpha)
                    self.display.blit(self.fade_surface, (0,0))
                    
                    if self.fade_alpha >= 255:
                        self.game_state['Game_over'] = True
                        self.game_state['Game'] = False
                    
            if self.game_state['Game_over']:
                self.display.fill('#3e3d32')
                
                gameOver_surface = pyg.font.Font(self.PATH['FONTS']+'Daydream.ttf', 30).render('Game Over!', False, '#f92672')
                gameOver_rect = gameOver_surface.get_rect(center=(self.display.get_width()/2,self.display.get_height()/2))
                pyg.draw.rect(self.display, '#1b1d1e', gameOver_rect,border_radius=5)
                self.display.blit(gameOver_surface, gameOver_rect)
                
                if self.fade_alpha >= 0:
                    self.fade_alpha -= 10
                    self.fade_surface.set_alpha(self.fade_alpha)
                    self.display.blit(self.fade_surface, (0,0))
            
            for event in pyg.event.get():
                if event.type == pyg.QUIT: self.end()
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE: self.end()
                    if self.game_state['Game']:
                        if event.key == pyg.K_SPACE and self.player_ground or event.key == pyg.K_w and self.player_ground or event.key == pyg.K_UP and self.player_ground:
                            self.player_gravity = -12
                            self.player_ground = False
                if event.type == pyg.MOUSEBUTTONDOWN and self.player_ground and self.game_state['Game']:
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
