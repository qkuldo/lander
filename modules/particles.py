import pygame as pg
import random as rand
class Particle:
	"""Handles an individual particle"""
	def __init__(self,color,group,coordinates,lifetime):
		self.color = color
		self.group = group
		self.lifetime = lifetime
		self.coordinates = coordinates
		self.speed = 1
		self.radius = 1
class ParticleGroup:
	"""Handles creation and behavior of individual particles
	   Create a particlegroup by making a child of this class so the properties of the "update" function can be edited independently
	"""
	def __init__(self,color,coordinates,lifetime,lifeloss):
		self.color = color
		self.lifetime = lifetime
		self.lifeloss = lifeloss
		self.particlelist = []
		self.radius = 1
	def GroupParticle(self,g:"ParticleGroup",starting_coordinates=[0,0]):
		return Particle(self.color,g,starting_coordinates,self.lifetime)
	def particlebehavior(self,particle):
		self.lifetime -= lifeloss
	def updateall(self,screen):
		for particle in self.particlelist:
			dead = self.particlebehavior(particle,screen)
			if (dead == 0):
				self.particlelist.remove(particle)
	def createGroupParticle(self,starting_coordinates=[0,0]):
		particle = GroupParticle(starting_coordinates)
		#edit particle attributes below
		return particle

class StarGroup(ParticleGroup):
	"""docstring for StarGroup"""
	def __init__(self,color=(255,255,255),coordinates=[0,0],lifetime=5000,lifeloss=2):
		super().__init__(color,coordinates,lifetime,lifeloss)
	def createGroupParticle(self,starting_coordinates=[0,0],minspeed=1,maxspeed=2):
		particle = self.GroupParticle(starting_coordinates)
		particle.coordinates = [rand.randint(250,1030),0]
		particle.speed = rand.uniform(minspeed,maxspeed)
		particle.radius = self.radius
		self.particlelist.append(particle)
	def particlebehavior(self,particle,screen):
		particle.lifetime -= self.lifeloss
		particle.coordinates[1] += particle.speed
		pg.draw.circle(screen,particle.color,particle.coordinates,particle.radius)
		if (particle.lifetime <= 0 or particle.coordinates[1] > 580):
			return 0
		return 1
