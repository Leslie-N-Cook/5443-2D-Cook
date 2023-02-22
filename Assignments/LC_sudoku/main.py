##########################################################
                    # Leslie Cook
                    # Sudoku Pygame
                    # 5443 - 2D gaming
                    # Griffin - Spring 23
###########################################################

import pygame
import time
import utilities
from Play import Play


"""
funtions in main.py :

    def end_game() : 
        draws a popup called from utilities that generates a message
        and tells the player how long it took to solve the game
        
    def draw_screen() : 
        fills the background black and writes the game rules to the screen
        and calls utiliites to begin the clock timer

"""

def end_game(gameTime):
    content = [
        {"text":" ",'font_size':20,'align':'left','color':'white'},
        {"text":" ",'font_size':20,'align':'center','color':'white'},
        {"text":" SUDOKU SOLVED! ",'font_size':60,'align':'left','color':'red'},
        {"text":"  ",'font_size':20,'align':'center','color':'white'},
        {"text":f"       You Finished in: {gameTime}",'font_size':20,'align':'left','color':'white'},
    ]
    image = utilities.makePopUp(content,border_size=10,border_color='white',fill_color='black',width=600,height=300)
    image.show()
    image.save(f"popup.png")

def draw_screen(window, play, time):
    # this fill the background of the game in black
    # overlays texts that explains how to play the game 
    # and shows a game clock for the user
    window.fill((0, 0, 0))
    font = pygame.font.Font("fonts/Futura.ttf", 32)
    # call utilities.set_time to set the clock in the game  
    text = font.render("Clock " + utilities.set_time(time), 1,(0,255,255))
    window.blit(text, (680, 400))
    font = pygame.font.Font("fonts/Futura.ttf", 28)
    text = font.render("SUDOKU RULES", 1, (255, 255, 0))
    window.blit(text, (540+130,100))
    font = pygame.font.Font("fonts/Futura.ttf", 16)
    text = font.render("1. Each row must contain the numbers 1-9 exactly once each",1, (255, 128, 0))                
    window.blit(text, (540+10 ,140))
    text = font.render("2. Each column must contain the numbers 1-9 exactly once each", 1, (255, 0, 0))
    window.blit(text, (540+10 ,160))
    text = font.render("3. Each 3x3 play must contain the numbers 1-9 exactly once each",1, (255, 0, 127))
    window.blit(text, (540+10 ,180))
    font = pygame.font.Font("fonts/Futura.ttf", 28)
    text = font.render("GAME PLAY", 1, (255, 0, 255))
    window.blit(text, (540+150,245))
    font = pygame.font.Font("fonts/Futura.ttf", 18)
    text = font.render("Select a blank tile to play a value", 1, (127, 0, 255))
    window.blit(text, (540+30,280))
    text = font.render("Press ENTER to set the value in the display", 1, (0, 0, 255))
    window.blit(text, (540+30,300))
    text = font.render("Press BACKSPACE to remove the value and try again", 1, (0, 127,255))
    window.blit(text, (540+30,320))       
    play.draw(window)
    
    
#initialize pygame module
pygame.init()

#add background music to game
pygame.mixer.init()
pygame.mixer.music.load('music/lofi_falling.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

#sets the size of the whole background module
display = pygame.display.set_mode((1050, 545))
pygame.display.set_caption("SUDOKU 4 U")

# calls the Play class to set the game play display
play = Play(540, 540, display)
running = True
pressed = None
start = time.time()

# while the game is running
while running:
    
    #get the current time to be used later   
    current_time = round(time.time() - start)
    # sets running to false if game is quit
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        # KEYDOWN event gets the keys from funtion in utilities
        if e.type == pygame.KEYDOWN:
            if utilities.get_key(e.key) is not None:
                # sets the event of a key 1-9 to pressed 
                pressed = utilities.get_key(e.key)
            
            elif e.key == pygame.K_BACKSPACE:
                # clears the indivual tile when backspace event happens
                play.clear()
                #sets pressed to none
                pressed = None
                
            elif e.key == pygame.K_RETURN:
                #selects the x,y cooridinate when you enter RETURN to set the value
                x, y = play.selected
                # sets the location of the value you played and passes in pressed key
                play.location(pressed)
                # plays a chime when a correct input value is played on the board
                if play.check_blank_tile() is False and play.check_solution() is True:
                    pygame.mixer.Channel(0).set_volume(0.15)
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('music/success-chime.mp3'))
                    #print(x,y,pressed)
                    if not play.check_correct(x,y,pressed):
                        pygame.mixer.Channel(0).set_volume(0.3)
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('music/f-cked-up_.mp3'))
                    
                # when you've solved the game correctly
                if play.check_blank_tile() is False and play.check_solution() is False:
                    # get the current time and store it in gameTime
                    gameTime = utilities.set_time(current_time) 
                    #call end_game function to create the popup
                    end_game(gameTime)
                    #pause the background music
                    pygame.mixer.music.pause()
                    #play the winning soung called from utilites
                    utilities.win_sound()
                    
                    # tell game to wait 10 seconds before reset
                    pygame.time.wait(10000)
     ###### this will automatically setup a new game ######
                    #restart background music called from utillites
                    utilities.background_music()
                    #reset the current time to 0
                    current_time = 0
                    #create a new starting time
                    start = time.time()
                    # tell Play class to draw a new board
                    play = Play(540, 540, display)
                    #reset pressed to none
                    pressed = None
        # this gets the postion of a mouse click event 
        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #print(pos)
            # sets clicked to click funtion in Play class
            clicked = play.click(pos)
            
            # if a mouse button click is detected
            if clicked:
                # call the Play class to hightlight the individual tile
                play.select(clicked[0], clicked[1])
                # call the Play class to highlight the row and column where the mouse click is detected 
                play.highlightRow(clicked[0])
                play.highlightCol(clicked[1])
                pressed = None
    #if somewhere is seleced and an even button is pressed          
    if play.selected and pressed is not None:
            #set a temporary location calling the Play class
            play.temp_location(pressed)
    #call the draw_screen function and pass in the necessary params    
    draw_screen(display, play, current_time)
    # update the pygame display
    pygame.display.update()


pygame.quit()
            
                    