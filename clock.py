import pygame, time

pygame.font.init()

class Clock:
	def __init__(self):
		self.start_time = None
		self.elapsed_time = 120
		self.font = pygame.font.SysFont("monospace", 35)

	def start_timer(self):
		self.start_time = time.time()

	def update_timer(self):
		if self.start_time is not None:
			current_time = time.time()
			elapsed = current_time - self.start_time
			self.elapsed_time = max(0, 120 - elapsed)

	def display_timer(self):
		secs = int(self.elapsed_time % 60)
		mins = int(self.elapsed_time / 60)
		my_time = self.font.render(f"{mins:02}:{secs:02}", True, pygame.Color("white"))
		return my_time

	def stop_timer(self):
		self.start_time = None
	
	def get_elapsed_time(self):
		return self.elapsed_time
	
	def reset_timer(self):
		self.elapsed_time = 120