import pygame


class Mars:
    def __init__(self):
        self.window_name = 'Planeta Marte'

    def display(self):
        pygame.init()
        pygame.display.set_caption(self.window_name)

