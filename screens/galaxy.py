import pygame
from settings import WINDOW_RESOLUTION
from pygame.sprite import Sprite


class Galaxy(Sprite):
    def __init__(self):
        self.window_name = 'Galáxia'

    def display(self):
        display = pygame.display.set_mode(WINDOW_RESOLUTION)
        pygame.display.set_caption(self.window_name)
        pygame.display.flip() 
        return display

    def background(self):
        image_background = pygame.image.load('screens\images\menu_background.jpeg').convert_alpha()
        image_background = pygame.transform.scale(image_background, WINDOW_RESOLUTION)
        return image_background
    
    def test(self):
        return 'AQ'
