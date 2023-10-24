import pygame


class Galaxy:
    def __init__(self):
        self.window_name = 'Galáxia'

    def display(self):
        pygame.init()
        pygame.display.set_caption(self.window_name)

