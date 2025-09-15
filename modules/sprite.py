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
	def update(self):
		pass
	def draw(self,screen):
		if (self.frame_number == 1):
			screen.blit(self.spritesheet,self.rect)
		else:
			frame = pg.transform.scale(self.spritesheet.load_frame(self.current_frame), (self.width,self.height))
			screen.blit(frame,self.rect)