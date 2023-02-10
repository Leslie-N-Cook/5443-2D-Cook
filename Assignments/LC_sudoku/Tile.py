import pygame

""" 
class Tile:
    sets up each individual with their respective values centered within each box

functions within the Tile class : 

    def draw() :
        allows the user to input values in each individual tile
        sets a temporary value in gray at the top left of the tile box
        user presses enter to peramanately place that value in the box and the color of the number changes to white
        also draws a red rectangle when the user clicks on a single tile
    
    def set():
        sets the value into the chosen tile
        
    def set_temp():
        allows the user to set a temporary value in the selected tile
"""

class Tile:
    row = 9
    col = 9
    GRAY = (128, 128, 128)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, box):
        font = pygame.font.Font("fonts/Futura.ttf", 26)
        space = self.width / 9
        
        x = self.col * space
        y = self.row * space
        
        if self.temp != 0 and self.value == 0:
            # temporarily puts the value in the top left corner
            text = font.render(str(self.temp), 1, self.GRAY)
            box.blit(text, (x + 3, y + 3))
        elif self.value != 0:
            # permanately sets the value in the center of the tile 
            text = font.render(str(self.value), 1, self.WHITE)
            box.blit(text, (x + (space / 2 - text.get_width() / 2), y + (space / 2 - text.get_height() / 2)))
            
        if self.selected:
            # draws a red rectangle around the selected tile
            pygame.draw.rect(box, self.RED, (x, y, space, space), 3)
            
    def set(self, value):
        self.value = value
        
    def set_temp(self, value):
        self.temp = value