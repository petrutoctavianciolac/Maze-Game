import pygame
import time

pygame.font.init()

class Game:
	def __init__(self, goal_cell, tile):
		self.font = pygame.font.SysFont("impact", 35)
		self.message_color = pygame.Color("darkorange")
		self.goal_cell = goal_cell
		self.tile = tile

	def add_goal_point(self, screen):

		img = pygame.image.load('assets/door.png')
		img = pygame.transform.scale(img, (self.tile, self.tile))
		screen.blit(img, (self.goal_cell.x * self.tile, self.goal_cell.y * self.tile))

	def message(self, mes):

		if mes == False:
			msg = self.font.render('You Win!!', True, self.message_color)
		else:
			msg = self.font.render('You Lose!!', True, self.message_color)
		return msg

	def is_win(self, player):
		goal_cell_abs_x, goal_cell_abs_y = self.goal_cell.x * self.tile, self.goal_cell.y * self.tile
		if player.x >= goal_cell_abs_x and player.y >= goal_cell_abs_y:
			return True
		else:
			return False