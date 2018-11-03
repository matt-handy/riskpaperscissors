from constants import *
import pygame
from Location import Location

class Risk():
	def __init__(self, screen):
		self.screen = screen
		self.surface = pygame.Surface((WIDTH, HEIGHT))
		self.img = pygame.transform.scale(
			pygame.image.load('2000px-Risk_board.svg.png').convert(),
			(1000,692)
		)
		self.locations = []
		self.locations.append(Location(self,80,112,"Alaska"))
		self.locations.append(Location(self,168,112,"NW Territory"))
		self.locations.append(Location(self,158,161,"Alberta"))
		self.locations.append(Location(self,222,160,"Ontario"))
		self.locations.append(Location(self,294,165,"Quebec"))
		self.locations.append(Location(self,345,71,"Greenland"))
		self.locations.append(Location(self,161,233,"Western US"))
		self.locations.append(Location(self,237,247,"Eastern US"))
		self.locations.append(Location(self,170,321,"Central America"))

	def process_keydown(self, key):
		pass

	def draw(self):
		self.surface.fill(SHADOW)
		self.surface.blit(self.img,(0,0))
		for location in self.locations:
			location.draw()
		self.screen.blit(self.surface, (0, 0))
