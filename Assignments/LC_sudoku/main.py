import pygame
import sys
import time
import utilities
from Play import Play


def end_game(gameTime):
    content = [
        {"text":" ",'font_size':20,'align':'left','color':'white'},
        {"text":" ",'font_size':20,'align':'center','color':'white'},
        {"text":" SUDOKU SOLVED! ",'font_size':60,'align':'left','color':'red'},
        {"text":"  ",'font_size':20,'align':'center','color':'white'},
        {"text":f"       You Finished in: {gameTime}",'font_size':20,'align':'left','color':'red'},
    ]
    image = utilities.makePopUp(content,border_size=20,border_color='white',fill_color='black',width=600,height=275)
    image.show()
    image.save(f"popup.png")

def draw_screen(window, grid, time):
    window.fill((0, 0, 0))
    font = pygame.font.Font("fonts/Futura.ttf", 32)
    text = font.render("Clock " + utilities.set_time(time), 1,(0,255,255))
    window.blit(text, (680, 400))
    # text = font.render("Quit", 1, (128, 128, 128))
    # window.blit(text, (900, 445))
    font = pygame.font.Font("fonts/Futura.ttf", 28)
    text = font.render("SUDOKU RULES", 1, (255, 255, 0))
    window.blit(text, (540+130,100))
    font = pygame.font.Font("fonts/Futura.ttf", 16)
    text = font.render("1. Each row must contain the numbers 1-9 exactly once each",1, (255, 128, 0))                
    window.blit(text, (540+10 ,140))
    text = font.render("2. Each column must contain the numbers 1-9 exactly once each", 1, (255, 0, 0))
    window.blit(text, (540+10 ,160))
    text = font.render("3. Each 3x3 grid must contain the numbers 1-9 exactly once each",1, (255, 0, 127))
    window.blit(text, (540+10 ,180))
    font = pygame.font.Font("fonts/Futura.ttf", 28)
    text = font.render("GAME PLAY", 1, (255, 0, 255))
    window.blit(text, (540+150,245))
    font = pygame.font.Font("fonts/Futura.ttf", 18)
    text = font.render("Select the box to play a value", 1, (127, 0, 255))
    window.blit(text, (540+30,280))
    text = font.render("Press ENTER to set the value in the box", 1, (0, 0, 255))
    window.blit(text, (540+30,300))
    text = font.render("Press BACKSPACE to remove the value and try again", 1, (0, 127,255))
    window.blit(text, (540+30,320))
                       
    grid.draw(window)

pygame.init()

box = pygame.display.set_mode((1050, 545))
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
                    gameTime = utilities.set_time(current_time) 
                    end_game(gameTime)
                    start = time.time()
                    grid = Play(540, 540)
                    pressed = None
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #print(pos)
            clicked = grid.click(pos)
            #print(clicked)
            if clicked:
                grid.select(clicked[0], clicked[1])
                pressed = None
                
    if grid.selected and pressed is not None:
            grid.temp_location(pressed)
        
    draw_screen(box, grid, current_time)
    pygame.display.update()


pygame.quit()
            
                    