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
	def __init__(self,spritesheet,width,height,frame_number=1,coordinates=[0,0],speed=[1,0],rotation=0,attack=1):
		super().__init__(spritesheet,width,height,frame_number,coordinates,speed)
		self.rotation = rotation
		self.attack = attack
	def update(self):
		self.coordinates[0] += self.speed[0]
		self.coordinates[1] += self.speed[1]
		self.rect.x = self.coordinates[0]
		self.rect.y = self.coordinates[1]
		if (self.rect.top < 0 or self.rect.left < 220 or self.rect.right > 1060):
			return True
		return False
	def draw(self,screen):
		if (self.frame_number == 1):
			frame = pg.transform.scale(self.spritesheet, (self.width,self.height))
			screen.blit(pg.transform.rotate(frame,self.rotation),self.rect)
		else:
			frame = pg.transform.scale(self.spritesheet.load_frame(self.current_frame), (self.width,self.height))
			screen.blit(pg.transform.rotate(frame,self.rotation),self.rect)
class SpecialSprite(Sprite):
	"""Sprite child class that has more attributes attached"""
	def __init__(self,spritesheet,width,height,frame_number=1,coordinates=[0,0],speed=0.5,hp=1,attack=1):
		super().__init__(spritesheet,width,height,frame_number,coordinates,speed)
		self.hp = hp
		self.attack = attack

		