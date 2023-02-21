import pygame
from Grid import Grid
from Tile import Tile

"""  
class Play :
    sets up the game for the user to play sudoku
    
functions within the Play class : 

    def location(): 
        gets the coordinates of a selected tile in order to set a value
    
    def temp_location():
        gets the coordinates of the selected tile to store a temporarty value until the user chooses to set the value into the tile
        
    def draw():
        uses pygame.draw.line to make horizontal and vertical lines that create the 9x9 gird layout
        draws a thicker line every 3rd line thats drawn
        
    def select():
        sets a selected tile to True for game play
        
    def clear():
        allows user to clear the tile of input
        
    def click(): 
        gets the position when the player click a button
        
    def check_blank_tile():
        check for blank tiles in the game to know if game has been completed
        
    def check_solution():
        checks the if the players solution is correct or not
"""

class Play:
    def __init__(self, width, height, display):
        
        self.grid = Grid() #call Grid class 
        self.row = 9
        self.col = 9
        self.display = display
        #list comprehension # call Tile class to 
        self.tiles = [[Tile(self.grid.grid[i][j], i, j, width, height, self.display) for j in range(9)] for i in range(9)]
        self.width = width
        self.height = height
        self.selected = None
        self.highlighted = None
 
    def location(self, value):
        row, col = self.selected
        self.tiles[row][col].set(value)
        
    def temp_location(self, value):
        row, col = self.selected
        self.tiles[row][col].set_temp(value)
        
    def draw(self, box):
        #gets the amount of space needed for a 9x9 grid to line up correctly 
        space = self.width / 9 
        for i in range(self.row + 1):
            # tells the game to draw a thickerline every 3rd row/col
            if i % 3 == 0 and i != 0:
                thick = 3
            else:
            #otherwise thickness is set to 1
                thick = 1
            pygame.draw.line(box, (255, 255, 255), (0, i * space), (self.width, i * space), thick)
            pygame.draw.line(box, (255, 255, 255), (i * space, 0), (i * space, self.height), thick)
            
        for i in range(9):
            for j in range(9):
                self.tiles[i][j].draw(box)
    
    def check_correct(self, row, col, num):
        print(len(self.grid.get_sol()))
        return self.grid.solution[row][col] == num
    
    def select(self, row, col):
        #make sure the board is clear before selecting anything
        self.clear_board()
        #cast row and col as integers
        row, col = int(row), int(col)
        #set selected to True
        self.tiles[row][col].selected = True
        # set the value of selected the same as (row, col)
        self.selected = (row, col)
        # highlihgt the entire row 
        self.highlightRow(row)
        # highlight the entire col
        self.highlightCol(col)
        
    def clear_board(self):
        for i in range(9):
            for j in range(9):
                #set selected and highlighted to False
                self.tiles[i][j].selected = False
                self.tiles[i][j].highlighted = False
        
    def highlightRow(self, row):
        for j in range(9):
            #print(int(row))
            self.tiles[int(row)][j].highlighted = True
        
    def highlightCol(self, col):
        for i in range(9):
            #print(int(col))
            self.tiles[i][int(col)].highlighted = True
        
    # def debug(self):
    #     for i in range(9):
    #         for j in range(9):
    #             s = self.tiles[i][j].selected
    #             h = self.tiles[i][j].highlighted
    #             print(f"{s},{h}",end = " ")
    #         print()
                
    def clear(self):
        row, col = self.selected
        # clear the values to set and set_temp to 0
        self.tiles[row][col].set(0)
        self.tiles[row][col].set_temp(0)
        
    def click(self, position):
        # get the position when clicked
        if position[0] < self.width and position[1] < self.height:
            space = self.width / 9
            x = position[0] // space
            y = position[1] // space
            #print(x,y)
            return (y, x)
        else:
            return None
    
    def check_blank_tile(self):
        #self.grid.find_blank()
        for i in range(9):
            for j in range(9):
                #print(self.tiles[i][j])
                if self.tiles[i][j] == 0:
                    print("blank T")
                    return True 
        print("blank F")               
        return False
    
    def check_solution(self):
        self.grid.solve()
        for i in range(9):
            for j in range(9):
                if self.grid.grid[i][j] != self.tiles[i][j].value:
                    print("solution T")
                    return True 
        print("solution F")               
        return False        
    