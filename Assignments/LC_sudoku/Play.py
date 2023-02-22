###############################################################
# Leslie Cook
# Sudoku Pygame
# 5443 - 2D gaming
# Griffin - Spring 23
# This Play class draws the actual 9x9 sudoku grid on the screen
# It inherits the Grid class and the Tile class to input the 
# logic for the game board from Grid and 
# user interactive graphics from Tile
################################################################
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
    
    def check_correct() : 
        returns true if the number in the grid is correct with the solution of the game
        
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
        self.row = 9 #number of rows
        self.col = 9 #numer of columns
        self.display = display
        #list comprehension # call Tile class in a list with parameters of the called from Grid, i(row),j(column), width,height (of each individual tile), dislpaly for j(columns) from 0 - 8, for i(rows) from 0-8
        self.tiles = [[Tile(self.grid.grid[i][j], i, j, width, height, self.display) for j in range(9)] for i in range(9)]
        self.width = width # width of the game board
        self.height = height # height of the game board
        self.selected = None # set selected to None
        self.highlighted = None # set highlighted to none
 
    def location(self, value):
        # get the location of the row and col selected
        row, col = self.selected
        # set the uer input value in that location
        self.tiles[row][col].set(value)
        
    def temp_location(self, value):
        # get the location of the row and col selected
        row, col = self.selected
        # set a temporary uer input value in that location
        self.tiles[row][col].set_temp(value)
        
    def draw(self, display):
        # gets the amount of space needed for a 9x9 grid to line up correctly 
        space = self.width / 9 
        # for the 10 lines of rows and 10 lines of columns 
        for i in range(self.row + 1):
            # draw a thickerline every 3rd row/col
            if i % 3 == 0 and i != 0:
                thick = 3
            else:
                #otherwise thickness is set to 1
                thick = 1
                # draw the white lines on the display as evenly spaced columns
            pygame.draw.line(display, (255, 255, 255), (0, i * space), (self.width, i * space), thick)
                # draw the white lines on the display as evenly spaced rows
            pygame.draw.line(display, (255, 255, 255), (i * space, 0), (i * space, self.height), thick)
            
        for i in range(9):
            for j in range(9):
                #draw on the tiles on the display
                self.tiles[i][j].draw(display)
    
    def check_correct(self, row, col, num):
        #print(len(self.grid.get_sol()))
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
        # clear the board from user interactive graphics
        for i in range(9):
            for j in range(9):
                #set selected and highlighted to False
                self.tiles[i][j].selected = False
                self.tiles[i][j].highlighted = False
        
    def highlightRow(self, row):
        #highlights the entire row in a different color when 
        #a single tile is selected 
        for j in range(9):
            #print(int(row))
            self.tiles[int(row)][j].highlighted = True
        
    def highlightCol(self, col):
        #highlights the entire column in a different color when 
        #a single tile is selected 
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
        # clears the uer input value 
        row, col = self.selected
        # clear the values to set and set_temp to 0
        self.tiles[row][col].set(0)
        self.tiles[row][col].set_temp(0)
        
    def click(self, position):
        # get the position when mouse click is detected
        if position[0] < self.width and position[1] < self.height:
            space = self.width / 9
            x = position[0] // space
            y = position[1] // space
            #print(x,y)
            #return the postion of the selected tile
            return (y, x)
        else:
            return None
    
    def check_blank_tile(self):
        #checks if there are blank tiles on the grid
        for i in range(9):
            for j in range(9):
                #print(self.tiles[i][j])
                #if rows and column of the tiles is blank
                if self.tiles[i][j] == 0:
                    #print("blank T")
                    return True 
        #print("blank F")               
        return False
    
    def check_solution(self):
        #checks if the solution is correct or not 
        # call the solve function in Grid class
        self.grid.solve()
        for i in range(9):
            for j in range(9):
                #if Grid row, columns are not equal to the Tile values 
                if self.grid.grid[i][j] != self.tiles[i][j].value:
                    # return true (game is not complete) 
                    #print("solution T")
                    return True 
        # return false only when the whole grid is filled with correct values
        #print("solution F")               
        return False        
    