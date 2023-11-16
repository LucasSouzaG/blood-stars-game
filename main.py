from screens.menu import Menu
from utils import calculate_screen_center, button_learning_game
from settings import WINDOW_RESOLUTION
import pygame

run = True
menu = Menu()
menu_display = menu.display()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #Carregar a imagem de fundo do menu
    menu_display.blit(menu.background(), (0,0))
    menu_display.blit(menu.title(), calculate_screen_center(WINDOW_RESOLUTION, menu.title()))
    menu_display.blit(button_learning_game(), (10,10))

    pygame.display.update()
    pygame.time.Clock().tick(60)
  