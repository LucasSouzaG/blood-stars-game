from screens.menu import Main_menu
import pygame

run = True
menu_display = Main_menu().display()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

  