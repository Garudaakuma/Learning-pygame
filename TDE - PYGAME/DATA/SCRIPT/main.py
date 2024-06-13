
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
        self.sky_rect = self.sky_surface.get_rect(midbottom=(self.display.get_width()/2,self.display.get_height()+65))
        self.sky_surface2 = self.util.image_load('IMAGE','sky_background.png')
        self.sky_rect2 = self.sky_surface.get_rect(midbottom=(self.display.get_width() + self.display.get_width()/2,self.display.get_height()+65))

        self.ground_surface = self.util.image_load('IMAGE','floor_grass.png')

        self.fade_obj = util_.transition_image(self.display)

        self.score = 0
        self.speed = 1

        self.snail_obj = enti_.Enemy(self.display, 'snail')

        self.player_obj = play_.Player(self.display)

        self.mouse_obj = util_.Mouse(self.display)
        pyg.mouse.set_visible(False)


    def run(self):
        while True:
            dt = time.time() - self.last_time   # delta time
            dt *= self.FPS                      # remain time/movement constant
            self.last_time = time.time()        # updates last time

            self.mouse_obj.update()

            if self.game_state['Game']:
                self.display.fill(self.BACKGROUND_COLOR)

                # render
                if self.sky_rect2.x <= -(self.display.get_width()): 
                    self.sky_rect2.x = self.display.get_width()
                self.sky_rect2.x -= self.speed * dt
                self.display.blit(self.sky_surface2, self.sky_rect2)
                
                if self.sky_rect.x <= -(self.display.get_width()): 
                    self.sky_rect.x = self.display.get_width()
                self.sky_rect.x -= self.speed * dt
                self.display.blit(self.sky_surface, self.sky_rect)

                self.display.blit(self.ground_surface, (0,self.display.get_height()-32))

                # text
                fps_text = util_.text_fonts(self.display, 'ConsolaMono-book.ttf', 10, (0,0), f'fps: {self.clock.get_fps()*dt:.0f}', False, '#1b1d1e')
                self.display.blit(fps_text.font_surface, fps_text.font_pos)

                score_text = util_.text_fonts(self.display, 'Daydream.ttf', 20, (self.display.get_width()/2, self.display.get_height()/4), f'score: {self.score:.0F}', False, '#1b1d1e')
                score_text.draw_rect('#f8f8f2', 5)
                self.display.blit(score_text.font_surface, score_text.font_rect)

                self.score += 0.1

                # snail walking
                self.snail_obj.walk_cicle(self.speed,dt)

                # player
                self.display.blit(self.player_obj.surface, self.player_obj.rect)
                self.player_obj.physics_update(dt)

                KEYS = pyg.key.get_pressed()
                if KEYS[pyg.K_d] or KEYS[pyg.K_RIGHT]:
                    self.player_obj.rect.x += 3 * dt
                if KEYS[pyg.K_a] or KEYS[pyg.K_LEFT]:
                    self.player_obj.rect.x -= 3 * dt

                if self.fade_obj.fade_alpha >= 0: self.fade_obj.fade_out(10, dt)

                if self.snail_obj.colligion_check(self.player_obj.rect):
                    self.fade_obj.fade_in(45, dt)
                    self.player_obj.gravity = 0
                    if self.fade_obj.fade_alpha >= 255:
                        self.game_state['Game_over'] = True
                        self.game_state['Game'] = False

            if self.game_state['Game_over']:
                self.display.fill('#3e3d32')

                gameOver_text = util_.text_fonts(self.display, 'Daydream.ttf', 30, (self.display.get_width()/2, self.display.get_height()/2), 'Game Over!', False, '#f92672')
                gameOver_text.draw_rect('#1b1d1e', 5)
                self.display.blit(gameOver_text.font_surface, gameOver_text.font_rect)

                text_option = util_.text_fonts(self.display, 'Daydream.ttf', 20, (self.display.get_width()/2, self.display.get_height()/2+40), 'RETRY', False, '#1b1d1e')
                reset_button = util_.button_rect(self.display, (128, 32), (self.display.get_width()/2, self.display.get_height()/2+40), '#f92672', text_option)
                reset_button.render()

                text_exit = util_.text_fonts(self.display, 'Daydream.ttf', 20, (self.display.get_width()/2, self.display.get_height()/2+80), 'EXIT', False, '#1b1d1e')
                exit_button = util_.button_rect(self.display, (128, 32), (self.display.get_width()/2, self.display.get_height()/2+80), '#f92672', text_exit)
                exit_button.render()

                if exit_button.mask.overlap(self.mouse_obj.mask, (self.mouse_obj.pos[0] - exit_button.rect.x, self.mouse_obj.pos[1] - exit_button.rect.y)):
                    exit_button.check_collision(self.mouse_obj, '#f8f8f2')
                    if self.mouse_obj.clicked: self.end()

                if reset_button.mask.overlap(self.mouse_obj.mask, (self.mouse_obj.pos[0] - reset_button.rect.x, self.mouse_obj.pos[1] - reset_button.rect.y)):
                    reset_button.check_collision(self.mouse_obj, '#f8f8f2')
                    if self.mouse_obj.clicked:
                        self.game_state['Game'] = True
                        self.game_state['Game_over'] = False
                        self.score = 0
                        self.speed = 1
                        self.snail_obj.reset()
                        self.player_obj.reset()
                        self.mouse_obj.clicked = False
                        continue
                self.mouse_obj.render()
                if self.fade_obj.fade_alpha >= 0: self.fade_obj.fade_out(10, dt)

            # check events in pygame
            for event in pyg.event.get():
                if event.type == pyg.QUIT: self.end()
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE: self.end()
                    if self.game_state['Game']:
                        if event.key == pyg.K_SPACE and self.player_obj.ground or event.key == pyg.K_w and self.player_obj.ground or event.key == pyg.K_UP and self.player_obj.ground:
                            self.player_obj.gravity = -14
                            self.player_obj.ground = False
                if event.type == pyg.MOUSEBUTTONDOWN and self.player_obj.ground and self.game_state['Game']:
                    if self.player_obj.rect.collidepoint((event.pos[0]/2, event.pos[1]/2)):
                        self.player_obj.gravity = -14
                        self.player_obj.ground = False
                if event.type == pyg.MOUSEBUTTONDOWN:
                    self.mouse_obj.clicked = True

            # screen / clock / display || updates
            self.screen.blit(pyg.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.clock.tick(self.FPS)
            pyg.display.update()


    def end(self):
        print("Game over!")
        pyg.quit()
        sys.exit()

print("main.py loaded!")
