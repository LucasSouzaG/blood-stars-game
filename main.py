from screens.menu import Menu
from screens.learning_game import Learning_Game
from screens.select_ship import Select_ship
from utils import calculate_screen_center, button_learning_game, button_return
from settings import WINDOW_RESOLUTION
import pygame

run = True

menu = Menu()
menu_display = menu.display()
menu_open = True

learning_game = Learning_Game()
learning_game_open = True

select_ship = Select_ship()
select_ship_open = True

while run:
    # if menu_open:
    #     menu_display = menu.display()
    #     menu_display.blit(menu.background(), (0,0))
    #     menu_display.blit(menu.title(), calculate_screen_center(WINDOW_RESOLUTION, menu.title()))
    #     menu_display.blit(button_learning_game(), (10,10))
    #     learning_game_open = True
    #     menu_open = False

    for event in pygame.event.get():

        if menu_open:
            menu_display = menu.display_refresh()
            menu_display.blit(menu.background(), (0,0))
            menu_display.blit(menu.title(), calculate_screen_center(WINDOW_RESOLUTION, menu.title()))
            menu_display.blit(button_learning_game(), (10,10))
            learning_game_open = True
            menu_open = False
            
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
            if event.key == pygame.K_ESCAPE:  # Verifica se a tecla pressionada foi o "ESC"
                run = False
            elif learning_game_open == True:
                select_ship_display = select_ship.display()
                select_ship_display.blit(select_ship.background(), (0,0)) 

                select_ship_display.blit(button_return(), (10,10)) # Imagem/botão de retorno
                print('AQ')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clique do botão esquerdo do mouse
                        if x > 9 and x < 46 and y > 9 and y < 46:  # Defina as coordenadas do botão de transição
                            menu_open = True
        
        elif event.type == pygame.MOUSEBUTTONDOWN: # Verifica o clique do mouse
            if event.button == 1:  # Clique do botão esquerdo do mouse
                x, y = event.pos
                print(f'Posicao do clique {x},{y}')  # Posição do clique

                if x > 9 and x < 46 and y > 9 and y < 46:  # Defina as coordenadas do botão de transição
                    if learning_game_open:
                        learning_game_display = learning_game.display()
                        learning_game_display.blit(learning_game.background(), (0,0)) # Imagem de fundo

                        learning_game_display.blit(button_return(), (10,10)) # Imagem/botão de retorno

                        learning_game_display.blit(learning_game.ship(360), (260,300)) # Imagem nave
                        learning_game_display.blit(learning_game.arrow(90), (306,305)) # Imagem seta
                        learning_game_display.blit(learning_game.arrow(90), (350,305)) # Imagem seta
                        learning_game_display.blit(learning_game.button(90), (300,350)) # imagem botão

                        learning_game_display.blit(learning_game.ship(360), (500,215)) # Imagem nave
                        learning_game_display.blit(learning_game.arrow(360), (505,305)) # Imagem seta
                        learning_game_display.blit(learning_game.arrow(360), (505,270)) # Imagem seta
                        learning_game_display.blit(learning_game.button(360), (500,350)) # imagem botão

                        learning_game_display.blit(learning_game.ship(360), (700,300)) # Imagem nave
                        learning_game_display.blit(learning_game.arrow(180), (705,215)) # Imagem seta
                        learning_game_display.blit(learning_game.arrow(180), (705,260)) # Imagem seta
                        learning_game_display.blit(learning_game.button(180), (700,350)) # imagem botão

                        learning_game_display.blit(learning_game.ship(360), (940,300)) # Imagem nave
                        learning_game_display.blit(learning_game.arrow(270), (905,305)) # Imagem seta
                        learning_game_display.blit(learning_game.arrow(270), (860,305)) # Imagem seta
                        learning_game_display.blit(learning_game.button(270), (900,350))

                        learning_game_open = False
                    else:
                        menu_open = True

    pygame.display.update()
    pygame.time.Clock().tick(60)
  