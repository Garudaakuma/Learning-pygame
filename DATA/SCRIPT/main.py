# imports
import pygame
import sys

# imports biblioteca proprias:
...

def main():
    print("main.py - inicializado!")
    
    pygame.init()
    
    screen_resolution = (640, 480) # width, height
    background_color = "#000000"
    
    pygame.display.set_caption("...")
    screen = pygame.display.set_mode(screen_resolution)
    
    clock = pygame.time.Clock()
    FPS = 60
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick(FPS)