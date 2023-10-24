import pygame


class Earth:
    def __init__(self):
        self.window_name = 'Planeta Terra'

    def display(self):
        pygame.display.set_caption(self.window_name)

