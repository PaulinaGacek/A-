from tkinter import N
import pygame
from grid import Grid
from algorithm import Algorithm
from utils import loadParameters
from button import Button, ButtonHandler

WIDTH, ALGORITHM, HEURISTICS = loadParameters()
WIN = pygame.display.set_mode((WIDTH, WIDTH + 50))

def main(win, width):
	ROWS = 50
	grid = Grid.make_grid(ROWS, width)
	ButtonHandler.initialise_list()

	start = None
	end = None

	run = True
	while run:
		Grid.draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = Grid.get_clicked_pos(pos, ROWS, width)
				print(row, col)
				if row < ROWS and col < ROWS:
					spot = grid[row][col]
					if not start and spot != end:
						start = spot
						start.make_start()

					elif not end and spot != start:
						end = spot
						end.make_end()

					elif spot != end and spot != start:
						spot.make_barrier()

				else: #button check
					b = Button("pierwszy") 

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = Grid.get_clicked_pos(pos, ROWS, width)
				if row < WIDTH and col < WIDTH:
					spot = grid[row][col]
					spot.reset()
					if spot == start:
						start = None
					elif spot == end:
						end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbours(grid)

					Algorithm.a_star(lambda: Grid.draw_path(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = Grid.make_grid(ROWS, width)
		ButtonHandler.draw_all_buttons(win,width)
		pygame.display.update()
	pygame.quit()

main(WIN, WIDTH)