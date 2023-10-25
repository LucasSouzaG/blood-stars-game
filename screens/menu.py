import pygame
from settings import WINDOW_RESOLUTION

class Main_menu:
    def __init__(self):
        self.window_name = 'Menu Principal'

    def display(self):
        pygame.init()
        pygame.display.set_mode(WINDOW_RESOLUTION)
        pygame.display.set_caption(self.window_name)

