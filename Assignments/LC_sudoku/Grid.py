from random import randint
import copy
from rich import print
"""
class Grid 
     builds a 9x9 game board layout in the pygame window
     fills the grid with randomly generated values 1-9 for the sudoku game
     
functions within in the Grid class:
    
     def build_grid() : 
        fills each tile with 1-9 values
        leaves 32 squares blank to play the game
     
     def fill_tiles() :
        tags the tiles with their respective randomly generated values
        checks that column and rows are okay to fill such values 
    
     def delete_items() : 
        indexes all rows and columns with each 1-9 value
        determines which tiles to to leave blank 
        
    def solve() : 
        solves the sudoku grid before choosing which tiles to leave blank
        
    def row_OK() :
        checks that all outter rows don't have the same value twice
        
    def col_OK() : 
        checks that all outter columns don't have the same value twice
        
    def mid_tiles_OK() :
        checks that all inner tiles don't have the same value twice 
        in each row adn column
    
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
        print(self.solution)
        # sets the number of tiles to leave blank
        self.delete_items(32)
        
    def get_sol(self):
        return self.solution
        
    def fill_tiles(self):
        tag = [False for _ in range(9)]
        blank = self.find_blank()
        if blank is None:
            return True
        row, col = blank[0], blank[1]
        while True:
            num = randint(1,9)
            tag[num - 1] = True
            
            if self.OK_to_fill(row, col, num):
                self.grid[row][col] = num
                if self.fill_tiles():
                    return True
                
                self.grid[row][col] = 0
            
            if tag.count(True) == 9:
                return False

    def delete_items(self, count):
        while count != 0:
            index = randint(0, 80)
            row, col  = int(index / 9), index % 9
            while self.grid[row][col - 1 if col != 0 else col] == 0:
                index = randint(0, 80)
                row, col = int(index / 9), index % 9 - 1
            self.grid[row][col - 1 if col != 0 else col] = 0
            count -= 1

    def solve(self):
        blank = self.find_blank()
        if blank is None:
            print("solve blank T")
            return True
        row, col = blank[0], blank[1]
        for num in range(1,10):
            if self.OK_to_fill(row, col, num):
                self.grid[row][col] = num
                #recursive call to solve
                if self.solve():
                    print("solve T")
                    return True
                self.grid[row][col] = 0
        print("solve F")        
        return False

    def row_OK(self, row, num):
        for i in range(9):
            if self.grid[row][i] == num:
                #print("row_OK F")
                return False
        #print("row_OK T")
        return True

    def col_OK(self, col, num):
        for i in range(9):
            if self.grid[i][col] == num:
                #print("col_OK F")
                return False
        #print("col_OK T")    
        return True

    def mid_tiles_OK(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if self.grid[row + i][col + j] == num:
                    #print("mid_tiles_OK F")
                    return False 
        #print("mid_tiles_OK T")
        return True

    def OK_to_fill(self, row, col, num):
        return self.row_OK(row, num) and self.col_OK(col, num) and self.mid_tiles_OK(row - row % 3, col - col % 3, num)      
            
    def find_blank(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return [i, j]
        return None