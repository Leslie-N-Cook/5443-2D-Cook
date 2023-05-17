#############################################################
# Leslie Cook
# Sudoku Pygame
# 5443 - 2D gaming
# Griffin - Spring 23
# This Tile class contains functions for user interactive 
# graphics while playing the sudoku game
#############################################################
import pygame
""" 
def draw_rect_alpha() : 
    makes a transparent color filled rectangle 
"""


def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)
    

class Tile:
    """
    The Tile class sets up the user interactive graphics for the game
    
    Attributes
    ----------
    
        row : 9
            number of rows in the game board
        col : 9
            number of columns in the game board
       
        GRAY : (128, 128, 128)
            color of the temporary value in the tile
            
        BLACK : (0, 0, 0)
            color of the background of the tile
            
        GREEN : (10, 246, 165)
            color of the selected tile
            
        WHITE : (255, 255, 255)
            color of the value in the tile
            
        HIGHLIGHT : pygame.Color(0, 255, 140, 75)
            color of the highlighted row and column of the selected tile using alpha values to make it transparent
            
        self.value : value
            The value entered by the user

        self.temp : 0
            a temporary place holder value

        self.row : row
            the row of the tile

        self.col : col
            the column if the tile

        self.width : width
            width of the grid

        self.height : height
            the height of the grid

        self.selected : False
            boolean initially sets a selected tile to false 

        self.highlighted : False
            boolean initially sets a highlighted tile to false

        self.display : display
            pygame display

    Methods
    ------- 
        def __init__():
            init method lets the the Tile class initialize its objects attributes

        def draw() :
            allows the user to input values in each individual tile
            sets a temporary value in gray at the top left of the tile box
            user presses enter to peramanately place that value in the box and the color of the number changes to white
            also draws a green rectangle when the user clicks on a single tile
        
        def set() :
            sets the value into the chosen tile
            
        def set_temp() :
            allows the user to set a temporary value in the selected tile
    
    """
    # set the row and column to 9 x 9
    row = 9
    col = 9
    # set up some colors 
    GRAY = (128, 128, 128)
    BLACK = (0, 0, 0)
    GREEN = (10, 246, 165)
    WHITE = (255, 255, 255)
    HIGHLIGHT = pygame.Color(0,255, 140, 75)

    def __init__(self, value, row, col, width, height, display):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        self.highlighted = False
        self.display = display

    def draw(self, box):
        font = pygame.font.Font("fonts/Futura.ttf", 26)
        # space is equal to the width o the game board / 9
        # this is to evenly space everything in a 9x9 grid
        space = self.width / 9
        
        x = self.col * space
        y = self.row * space
        
        if self.temp != 0 and self.value == 0:
            # temporarily puts the value in the top left corner
            text = font.render(str(self.temp), 1, self.GRAY)
            box.blit(text, (x + 3, y + 3))
        elif self.value != 0:
            # sets the value in the center of the tile 
            text = font.render(str(self.value), 1, self.WHITE)
            box.blit(text, (x + (space / 2 - text.get_width() / 2), y + (space / 2 - text.get_height() / 2)))
            
        if self.highlighted:
            # highlights the row and col of the selected item 
            draw_rect_alpha(self.display, self.HIGHLIGHT, (x, y, space, space))
            
        if self.selected:
            # draws a rectangle around the selected tile
            pygame.draw.rect(box, self.GREEN, (x, y, space, space), 3)
            
    def set(self, value):
        # permanately set the user input value 
        self.value = value
        
    def set_temp(self, value):
        #temporarily set the user input value
        self.temp = value