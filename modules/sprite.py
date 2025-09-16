import pygame as pg

class Sprite:
	"""Container for properties of sprite"""
	def __init__(self,spritesheet,width,height,frame_number=1,coordinates=[0,0],speed=0.5):
		self.spritesheet = spritesheet
		self.width = width
		self.height = height
		self.frame_number = frame_number
		self.current_frame = 0
		self.speed = speed
		self.rect = pg.Rect((0,0),(self.width,self.height))
		self.rect.x = coordinates[0]
		self.rect.y = coordinates[1]
		self.coordinates = coordinates
	def update(self):
		if (self.rect.left < 220):
			self.coordinates[0] += 5
		if (self.rect.right > 1060):
			self.coordinates[0] -= 5
		if (self.rect.top < 0):
			self.coordinates[1] += 5
		if (self.rect.bottom > 580):
			self.coordinates[1] -= 5
		self.rect.x = self.coordinates[0]
		self.rect.y = self.coordinates[1]
	def draw(self,screen):
		if (self.frame_number == 1):
			screen.blit(self.spritesheet,self.rect)
		else:
			frame = pg.transform.scale(self.spritesheet.load_frame(self.current_frame), (self.width,self.height))
			screen.blit(frame,self.rect)