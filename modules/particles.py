import pygame as pg
import random as rand
class Particle:
	"""Handles an individual particle"""
	def __init__(self,color,group,coordinates,lifetime,coordinates):
		self.color = color
		self.group = group
		self.lifetime = lifetime
		self.coordinates = coordinates
		self.speed = 1
class ParticleGroup:
	"""Handles creation and behavior of individual particles
	   Create a particlegroup by making a child of this class so the properties of the "update" function can be edited independently
	"""
	def __init__(self,color,coordinates,lifetime,lifeloss):
		self.color = color
		self.lifetime = lifetime
		self.lifeloss = lifeloss
		self.particlelist = []
	def GroupParticle(self,starting_coordinates=[0,0],group=ParticleGroup):
		return Particle(self.color,group,self.lifetime,starting_coordinates)
	def particlebehavior(self,particle):
		self.lifetime -= lifeloss
	def updateall(self):
		for particle in self.particlelist:
			dead = particlebehavior(particle)
			if (dead == 0):
				self.particlelist.remove(particle)
	def createGroupParticle(self,starting_coordinates=[0,0]):
		particle = GroupParticle(starting_coordinates)
		#edit particle attributes below
		return particle

class StarGroup(ParticleGroup):
	"""docstring for StarGroup"""
	def __init__(self,color=(255,255,255),coordinates=[0,0],lifetime,lifeloss):
		super().__init__(color,coordinates,lifetime,lifeloss)
	def createGroupParticle(self,starting_coordinates=[0,0]):
		particle = GroupParticle(starting_coordinates)
		particle.coordinates = [rand.randint(250,1030),0]
		particle.speed = rand.randint(0.5,2)
		self.particlelist.append(particle)
	def particlebehavior(self,particle):
		particle.lifetime -= lifeloss
		particle.coordinates[1] += particle.speed
		if (particle.lifetime <= 0):
			return 0
		return 1
