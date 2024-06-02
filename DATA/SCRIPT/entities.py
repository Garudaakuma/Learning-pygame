# imports
import pygame

# imports self library:
import DATA.SCRIPT.main as _ma

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos) # x and y
        self.size = size
        self.velocity = [0, 0]
        
    def update(self, movement=(0, 0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        self.pos[0] += frame_movement[0] # x 
        self.pos[1] += frame_movement[1] # y
        
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
    def render(self, surf):
        surf.blit(self.game.assets[self.type], self.pos)