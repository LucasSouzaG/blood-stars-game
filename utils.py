import pygame


# Fazer um carrosel com a imagem de fundo
    # rel_x = X % menu.menu_background().get_rect().width
    # menu_display.blit(menu.menu_background(), (rel_x - menu.menu_background().get_rect().width,0))
    # if rel_x < 1280:
    #     menu_display.blit(menu.menu_background(), (rel_x,0))

    # X -= 4

def calculate_screen_center(screen_resolution, image):
    tela_largura, tela_altura = screen_resolution
    
    x = (tela_largura - image.get_width()) // 2
    y = (tela_altura - image.get_height()) // 2
    
    return (x,y)

def button_learning_game():
        image_learning_game = pygame.image.load('screens\images\learning_game.png').convert_alpha()
        image_learning_game = pygame.transform.scale(image_learning_game, (35,35))
        return image_learning_game

# Desenvolver funcao para criar botão, ref: https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
def button():
    
    # initializing the constructor 
    pygame.init() 
    
    # screen resolution 
    res = (720,720) 
    
    # opens up a window 
    screen = pygame.display.set_mode(res) 
    
    # white color 
    color = (255,255,255) 
    
    # # light shade of the button 
    color_light = (170,170,170) 
    
    # # dark shade of the button 
    color_dark = (100,100,100) 
    
    # stores the width of the 
    # screen into a variable 
    width = screen.get_width() 
    
    # stores the height of the 
    # screen into a variable 
    height = screen.get_height() 
    
    # defining a font 
    smallfont = pygame.font.SysFont('Corbel',35) 
    
    # rendering a text written in 
    # this font 
    text = smallfont.render('quit' , True , color) 
    
    while True: 
        
        for ev in pygame.event.get(): 
            
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 

                #if the mouse is clicked on the 
                # button the game is terminated 
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                    pygame.quit() 
                    
        # fills the screen with a color 
        screen.fill((60,25,60)) 
        
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
        
        # if mouse is hovered on a button it 
        # changes to lighter shade  
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
            pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
            
        else: 
            pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
        
        # superimposing the text onto our button 
        screen.blit(text , (width/2+50,height/2)) 
        
        # updates the frames of the game 
        pygame.display.update() 