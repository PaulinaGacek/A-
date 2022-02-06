from colors import Color
import pygame

class Spot:
    def __init__(self, row, col, width, total_rows) -> None:
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.color = Color.white
        self.neighbours = []
    
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == Color.tea_green
    
    def is_open(self):
        return self.color == Color.violet
    
    def is_barrier(self):
        return self.color == Color.black
    
    def is_start(self):
        return self.color == Color.auburn
    
    def is_end(self):
        return self.color == Color.dark_green
    
    def reset(self):
        self.color = Color.white
    
    def make_closed(self):
        self.color = Color.tea_green
    
    def make_open(self):
        self.color = Color.violet
    
    def make_barrier(self):
        self.color = Color.black
    
    def make_start(self):
        self.color = Color.auburn
    
    def make_end(self):
        self.color = Color.dark_green
    
    def make_path(self):
        self.color = Color.orange
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbours(self, grid):
        self.neighbours = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # down
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # up
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # left
            self.neighbours.append(grid[self.row][self.col+1])

        if self.col > 0 and not grid[self.row][self.col-1].is_barrier(): # right
            self.neighbours.append(grid[self.row][self.col-1])

    def __lt__(self, other):
        return False
    
    def __gt__(self, other):
        return True