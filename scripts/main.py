import pygame
from grid import Grid

WIDTH = 400
WIN = pygame.display.set_mode((WIDTH, WIDTH))

def main(win, width):
    pygame.display.set_caption("A*")
    
    ROWS = 50
    grid = Grid.make_grid(ROWS, width)

    start = None
    run = True
    end = None
    started = False

    while run:
        Grid.draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if started: # when algorithm started user cannot click
                continue
            if pygame.mouse.get_pressed()[0]: # left mouse button
                pos = pygame.mouse.get_pos()
                row, col = Grid.get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]

                if start is None:
                    start = spot
                    start.make_start()
                elif end is None:
                    if spot.get_pos() != start.get_pos():
                        end = spot
                        end.make_end()
                elif spot.get_pos() != end.get_pos() and spot.get_pos() != start.get_pos():
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]: # rigth mouse button
                pass
    pygame.quit()


main(WIN, WIDTH)