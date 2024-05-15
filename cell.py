import pygame
from random import choice

class Cell:
	def __init__(self, x, y, thickness):
		self.x, self.y = x, y
		self.thickness = thickness
		self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
		self.visited = False

	def draw(self, sc, tile):
		x = self.x * tile
		y = self.y * tile
		if self.walls['top']:
			pygame.draw.line(sc, pygame.Color('black'), (x, y), (x + tile, y), self.thickness)
		if self.walls['right']:
			pygame.draw.line(sc, pygame.Color('black'), (x + tile, y), (x + tile, y + tile), self.thickness)
		if self.walls['bottom']:
			pygame.draw.line(sc, pygame.Color('black'), (x, y + tile), (x + tile, y + tile), self.thickness)
		if self.walls['left']:
			pygame.draw.line(sc, pygame.Color('black'), (x, y), (x, y + tile), self.thickness)

	def check_cell(self, x, y, cols, rows, grid_cells):
		if x < 0 or x >= cols or y < 0 or y >= rows:
			return False
		return grid_cells[x + y * cols]

	def check_neighbors(self, cols, rows, grid_cells):
		neighbors = []
		top = self.check_cell(self.x, self.y - 1, cols, rows, grid_cells)
		right = self.check_cell(self.x + 1, self.y, cols, rows, grid_cells)
		bottom = self.check_cell(self.x, self.y + 1, cols, rows, grid_cells)
		left = self.check_cell(self.x - 1, self.y, cols, rows, grid_cells)
		if top and not top.visited:
			neighbors.append(top)
		if right and not right.visited:
			neighbors.append(right)
		if bottom and not bottom.visited:
			neighbors.append(bottom)
		if left and not left.visited:
			neighbors.append(left)
		return choice(neighbors) if neighbors else False