from spot import Spot
from colors import Color
import pygame

class Grid:

    def make_grid(rows, width):
        grid = []
        gap = width // rows
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                spot = Spot(i, j, gap, rows)
                grid[i].append(spot)
        return grid

    def draw_grid(win, rows, width):
        gap = width // rows
        for i in range(rows):
            pygame.draw.line(win, Color.violet, (0, i*gap), (width, i*gap))
            for j in range(rows):
                pygame.draw.line(win, Color.violet, (j*gap, 0), (j*gap, width))
    
    def draw(win, grid, rows, width):
        win.fill(Color.white)
        for row in grid:
            for spot in row:
                spot.draw(win)
        Grid.draw_grid(win, rows, width)
        # pygame.display.update()
    
    def draw_path(win, grid, rows, width):
        win.fill(Color.white)
        for row in grid:
            for spot in row:
                spot.draw(win)
        Grid.draw_grid(win, rows, width)
        pygame.display.update()
    
    def clear_old_path(win, grid, rows, width):
        #TO DO:
        # clears only spots which are not boundaries, start, end
        win.fill(Color.white)
        for row in grid:
            for spot in row:
                if spot.is_closed() or spot.is_open() or spot.is_path():
                    spot.reset()
                    spot.draw(win)
        Grid.draw_grid(win, rows, width)
        pygame.display.update()
    
    def get_clicked_pos(pos, rows, width):
        gap = width // rows
        y, x = pos

        row = y// gap
        col = x // gap
        return row, col
