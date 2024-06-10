
# imports labrary
import pygame as pyg, sys, time

# imports self library
import DATA.SCRIPT.utilities    as util_
import DATA.SCRIPT.entitys      as enti_
import DATA.SCRIPT.player       as play_

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
        self.screen = pyg.display.set_mode(self.RESOLUTION)
        self.display = pyg.Surface((self.screen.get_width()/2, self.screen.get_height()/2)).convert()

        self.clock = pyg.time.Clock()   # create clock
        self.last_time = time.time()    # gets time
        
        self.util = util_.utility(self.display)
        
        self.sky_surface = self.util.image_load('IMAGE','sky_background.png')
        self.ground_surface = self.util.image_load('IMAGE','floor_grass.png')

        self.fade_obj = util_.transition_image(self.display)

        self.score = 0

        self.snail_obj = enti_.Enemy(self.display, 'snail')
        
        self.player_obj = play_.Player(self.display)

    def run(self):
        while True:
            dt = time.time() - self.last_time   # delta time
            dt *= self.FPS                      # remain time/movement constant
            self.last_time = time.time()        # updates last time

            pos_mouse = pyg.mouse.get_pos()
            pyg.mouse.get_visible(False)
            mouse_img - pyg.image.load(self.util.PATH['IMAGE']+'cursor.png').convert()
            
            if self.game_state['Game']:
                self.display.fill(self.BACKGROUND_COLOR)

                # render
                self.display.blit(self.sky_surface, (0,65))
                self.display.blit(self.ground_surface, (0,self.display.get_height()-32))

                # text
                fps_text = util_.text_fonts(self.display, 'ConsolaMono-book.ttf', 10, (0,0), f'fps: {self.clock.get_fps()*dt:.0f}', False, '#1b1d1e')
                self.display.blit(fps_text.font_surface, fps_text.font_pos)

                score_text = util_.text_fonts(self.display, 'Daydream.ttf', 20, (self.display.get_width()/2, self.display.get_height()/4), f'score: {self.score}', False, '#1b1d1e')
                score_text.draw_rect('#f8f8f2', 5)
                self.display.blit(score_text.font_surface, score_text.font_rect)
                
                # snail walking
                self.snail_obj.enemy_walk(1,dt)
                
                # player
                self.display.blit(self.player_obj.surface, self.player_obj.rect)
                self.player_obj.physics_update(dt)
                
                KEYS = pyg.key.get_pressed()
                if KEYS[pyg.K_d] or KEYS[pyg.K_RIGHT]:
                    self.player_obj.rect.x += 3 * dt
                if KEYS[pyg.K_a] or KEYS[pyg.K_LEFT]:
                    self.player_obj.rect.x -= 3 * dt
                
                if self.fade_obj.fade_alpha >= 0:
                    self.fade_obj.fade_out(10, dt)
                
                if self.snail_obj.colligion_check(self.player_obj.rect):
                    self.fade_obj.fade_in(45, dt)
                    
                    if self.fade_obj.fade_alpha >= 255:
                        self.game_state['Game_over'] = True
                        self.game_state['Game'] = False
                    
            if self.game_state['Game_over']:
                self.display.fill('#3e3d32')
                
                gameOver_text = util_.text_fonts(self.display, 'Daydream.ttf', 30, (self.display.get_width()/2, self.display.get_height()/2), 'Game Over!', False, '#f92672')
                gameOver_text.draw_rect('#1b1d1e', 5)
                self.display.blit(gameOver_text.font_surface, gameOver_text.font_rect)
                
                if self.fade_obj.fade_alpha >= 0:
                    self.fade_obj.fade_out(10, dt)
            
            for event in pyg.event.get():
                if event.type == pyg.QUIT: self.end()
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE: self.end()
                    if self.game_state['Game']:
                        if event.key == pyg.K_SPACE and self.player_obj.ground or event.key == pyg.K_w and self.player_obj.ground or event.key == pyg.K_UP and self.player_obj.ground:
                            self.player_obj.gravity = -12
                            self.player_obj.ground = False
                if event.type == pyg.MOUSEBUTTONDOWN and self.player_obj.ground and self.game_state['Game']:
                    if self.player_obj.rect.collidepoint((event.pos[0]/2, event.pos[1]/2)):
                        self.player_obj.gravity = -12
                        self.player_obj.ground = False
            
            self.screen.blit(pyg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.clock.tick(self.FPS)
            pyg.display.update()
            
    
    def end(self):
        print("Game over!")
        pyg.quit()
        sys.exit()
