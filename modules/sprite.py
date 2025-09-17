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
		self.rect.x = self.coordinates[0]
		self.rect.y = self.coordinates[1]
		if (self.rect.left < 220):
			self.coordinates[0] += 5
		if (self.rect.right > 1060):
			self.coordinates[0] -= 5
		if (self.rect.top < 0):
			self.coordinates[1] += 5
		if (self.rect.bottom > 580):
			self.coordinates[1] -= 5
	def draw(self,screen,rotation=0):
		if (self.frame_number == 1):
			frame = pg.transform.scale(self.spritesheet, (self.width,self.height))
			screen.blit(pg.transform.rotate(frame,rotation),self.rect)
		else:
			frame = pg.transform.scale(self.spritesheet.load_frame(self.current_frame), (self.width,self.height))
			screen.blit(pg.transform.rotate(frame,rotation),self.rect)

class Projectile(Sprite):
	"""Sprite child class that handles constanly moving objects"""
	def __init__(self,spritesheet,width,height,frame_number=1,coordinates=[0,0],speed=[1,0]):
		super().__init__(spritesheet,width,height,frame_number,coordinates,speed)
	def update(self):
		self.coordinates[0] += self.speed[0]
		self.coordinates[1] += self.speed[1]
		self.rect.x = self.coordinates[0]
		self.rect.y = self.coordinates[1]
		if (self.rect.top < 0):
			return True
		return False
		