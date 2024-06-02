# imports
import pygame

BASE_IMG_PATH = 'DATA/IMAGES/'
def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey('#000000')
    return img