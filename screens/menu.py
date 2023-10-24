import pygame
from settings import TOTAL_SCREEN_WITH, TOTAL_SCREEN_HEIGHT



class main_menu:
    def __init__(self):
        self.menu_name = 'Menu Principal'

    def display(self):
        pygame.init()
        pygame.display.set_mode((TOTAL_SCREEN_WITH,TOTAL_SCREEN_HEIGHT))
        pygame.display.set_caption(self.menu_name)

