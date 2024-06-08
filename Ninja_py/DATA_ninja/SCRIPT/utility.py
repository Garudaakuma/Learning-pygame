# imports
import pygame
import os

BASE_IMG_PATH = 'Ninja_py/DATA_ninja/IMAGES/' # Ninja_py is built because is executed from folder "learning-pygame"


def load_image(path:str):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey('#000000')
    return img


def load_images(path:str):
    images = []
    print(BASE_IMG_PATH + path)
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(f'{path}/{img_name}'))
    return images
