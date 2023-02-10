import pygame
import sys
import time
import utilities
from threading import Thread
from Play import Play


def redraw_box(window, grid, time):
    window.fill((0, 0, 0))
    font = pygame.font.Font("fonts/Futura.ttf", 26)
    text = font.render("Clock: " + utilities.set_time(time), 1, (255, 255, 255))
    window.blit(text, (540 - 160, 555))
    text = font.render("Help", 1, (255, 255, 255))
    window.blit(text, (20, 555))
    
    
    grid.draw(window)
    

pygame.init()

box = pygame.display.set_mode((540, 600))
pygame.display.set_caption("SUDOKU 4 U")

grid = Play(540, 540)
running = True
pressed = None
start = time.time()



while running:
       
    current_time = round(time.time() - start)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if utilities.get_key(e.key) is not None:
                pressed = utilities.get_key(e.key)
            elif e.key == pygame.K_BACKSPACE:
                grid.clear()
                pressed = None
            elif e.key == pygame.K_RETURN:
                x, y = grid.selected
                grid.location(pressed)
                if grid.check_blank_tile() is False and grid.check_solution() is True:
                    end_str = "\nCongratulations! You finished in " + utilities.set_time(current_time) 
                    utilities.display_messageBox(end_str, "SUDOKU SOLVED!")
                    start = time.time()
                    grid = Play(540, 540)
                    pressed = None
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            # thread = Thread(target=utilities.display_messageBox, args=(1.5, 'New message from another thread'))
            # thread.start(daemon=True)
        
            pos = pygame.mouse.get_pos()
            print(pos)
            clicked = grid.click(pos)
            print(clicked)
            if clicked:
                grid.select(clicked[0], clicked[1])
                pressed = None
                
    if grid.selected and pressed is not None:
            grid.temp_location(pressed)
        
    redraw_box(box, grid, current_time)
    pygame.display.update()


pygame.quit()
            
                    