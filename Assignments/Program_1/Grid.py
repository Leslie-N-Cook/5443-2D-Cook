#############################################################
# Leslie Cook
# Sudoku Pygame
# 5443 - 2D gaming
# Griffin - Spring 23
# This Grid class contains all of the logic to set up
# the sudoku game board with values 1-9 exactly once
# in each row, column and 3x3 block 
# it build a randomly generated sudoku solution
# then randomly deletes a set number of values from the solution
#############################################################
from random import randint
import copy
from rich import print
"""
class Grid 
     builds a 9x9 game board layout in the pygame window
     fills the grid with randomly generated values 1-9 for the sudoku game
     
Methods :
     def __init__():
        init method lets the the Grid class initialize its objects attributes
    
     def build_grid() : 
        fills each tile with 1-9 values
        leaves 32 squares blank to play the game
        
     def get_sol() :
     	gets a copy of the sudoku solution
     
     def fill_tiles() :
        tags the tiles with their respective randomly generated values
        checks that column and rows are okay to fill such values 
    
     def delete_items() : 
        indexes all rows and columns with each 1-9 value
        determines which tiles to to leave blank 
        
    def solve() : 
        solves the sudoku grid before choosing which tiles to leave blank
        
    def row_OK() :
        checks that all  rows don't have the same value twice
        
    def col_OK() : 
        checks that all columns don't have the same value twice
        
    def mid_tiles_OK() :
        checks that all 3x3 inner grids don't have the same value twice 
        in each row and column
    
    def OK_to_fill() : 
        after checking that all rows and columns don't have the same values 
        more than once this function gives the OK to fill the tiles with 1-9 values
        
    def find_blank() : 
        finds which tiles to leave blank 
     
"""
class Grid:
    def __init__(self):
        self.grid = [[0] * 9 for _ in range(9)]
        self.build_grid()


    def build_grid(self):
        self.fill_tiles()
        self.solution = copy.deepcopy(self.grid)
        #print(self.solution)
        # sets the number of tiles to leave blank
        self.delete_items(32)
        
    def get_sol(self):
        return self.solution
        
    def fill_tiles(self):
        #set the tag to false for _ from 0-8
        tag = [False for _ in range(9)]
        #set blank = to the find_blank() function
        blank = self.find_blank()
        # if blank is none return true
        if blank is None:
            return True
        #row and col is equal to blank[0] and blank[1]
        row, col = blank[0], blank[1]
        #while this is true
        while True:
            #num is given random integer bewteen 1-9
            num = randint(1,9)
            #tag[num-1] is set to True
            tag[num - 1] = True
            #if its OK_to fill, the row and column with that number
            if self.OK_to_fill(row, col, num):
                #set the number equal to the row and column on the grid
                self.grid[row][col] = num
                #if youn can fill the tile
                if self.fill_tiles():
                    #return true
                    return True
                #otherwise the row and column on the grid is 0
                self.grid[row][col] = 0
            #if the tag count is true, its equal to 9 
            if tag.count(True) == 9:
                #otherwise its false
                return False

    def delete_items(self, count):
        # while the count is not equal to zero
        while count != 0:
            # set the index to a random int between 0-80 
            index = randint(0, 80)
            # set the row and column to the index/9 
            row, col  = int(index / 9), index % 9
            while self.grid[row][col - 1 if col != 0 else col] == 0:
                index = randint(0, 80)
                row, col = int(index / 9), index % 9 - 1
            self.grid[row][col - 1 if col != 0 else col] = 0
            #decrement the count
            count -= 1

    def solve(self):
        #set blank = to the find_blank() function
        blank = self.find_blank()
        if blank is None:
            #print("solve blank T")
            return True
        row, col = blank[0], blank[1]
        for num in range(1,10):
            #check if the row, col, number from OK_to_fill function
            if self.OK_to_fill(row, col, num):
                #set the grid's row and column to the number 
                self.grid[row][col] = num
                #recursive call to solve again
                if self.solve():
                    #print("solve T")
                    return True
                self.grid[row][col] = 0
        #print("solve F")        
        return False

    def row_OK(self, row, num):
        #for the 9 rows
        for i in range(9):
            #if the grids coloumns are equal to the number
            if self.grid[row][i] == num:
                #print("row_OK F")
                return False
        #print("row_OK T")
        return True

    def col_OK(self, col, num):
        #for the 9 columns
        for i in range(9):
            #if the grids coloumns are equal to the number 
            if self.grid[i][col] == num:
                #print("col_OK F")
                return False
        #print("col_OK T")    
        return True

    def mid_tiles_OK(self, row, col, num):
        # for the 3 rows
        for i in range(3):
            # for the 3 colummns
            for j in range(3):
                #if the grid's row + (0,1,2) and col + (0,1,2) is equal to the value
                if self.grid[row + i][col + j] == num:
                    #print("mid_tiles_OK F")
                    return False 
        #print("mid_tiles_OK T")
        return True

    def OK_to_fill(self, row, col, num):
        #return the value in the row and the value in the col 
        #and the values in the row and col of the 3x3 section
        return self.row_OK(row, num) and                                                                self.col_OK(col, num) and                                                                   self.mid_tiles_OK(row - row % 3, col - col % 3, num)      
            
    def find_blank(self):
        #for the 9 rows
        for i in range(9):
            #for the 9 columns
            for j in range(9):
                #if the row and col = 0
                if self.grid[i][j] == 0:
                    #return the row and col
                    return [i, j]
        #otherwise return none        
        return None