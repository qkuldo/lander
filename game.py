import pygame as pg
import sys
import modules
import random as rand
pg.init()
screen = pg.display.set_mode((1280,720))
clock = pg.time.Clock()
TITLESCENE = 0
GAMESCENE = 1
current_scene = GAMESCENE

def Game():
	PlayerAsset = pg.image.load("assets/images/PNG FILES/hypership.png")
	PlayerAsset = modules.sheet.Spritesheet(PlayerAsset,24,24)
	BulletAsset = pg.image.load("assets/images/PNG FILES/bullet.png")
	Player = modules.sprite.Sprite(PlayerAsset,24*2.5,24*2.5,11,[1280/2,580])
	running = True
	stargroup = modules.particle.StarGroup()
	starspawn = rand.randint(1,100)
	player_bulletlist = []
	player_cooldown = 0
	print(stargroup.lifetime)
	while running:
		screen.fill("black")
		for event in pg.event.get():
			if (event.type == pg.QUIT):
				pg.quit()
				sys.exit()
		keys = pg.key.get_pressed()
		if (starspawn <= 0):
			stargroup.createGroupParticle(minspeed=0.01,maxspeed=1)
			starspawn = rand.randint(1,100)
		stargroup.updateall(screen)
		if (keys[pg.K_SPACE] and player_cooldown <= 0):
			if (Player.current_frame == 0):
				player_bulletlist.append(modules.sprite.Projectile(BulletAsset,16,24,1,[Player.rect.midtop[0]-7,Player.rect.midtop[1]],speed=[0,-1]))
			elif (Player.current_frame == 1):
				player_bulletlist.append(modules.sprite.Projectile(BulletAsset,16,24,1,[Player.rect.midtop[0]-7,Player.rect.midtop[1]],speed=[1,-1],rotation=-5))
			elif (Player.current_frame == 2):
				player_bulletlist.append(modules.sprite.Projectile(BulletAsset,16,24,1,[Player.rect.midtop[0]-7,Player.rect.midtop[1]],speed=[-1,-1],rotation=5))
			player_cooldown = 200
		for bullet in player_bulletlist:
			dead = bullet.update()
			if (dead):
				player_bulletlist.remove(bullet)
			else:
				bullet.draw(screen)
		if (keys[pg.K_LEFT]):
			Player.current_frame = 2
			Player.coordinates[0] -= Player.speed
			Player.draw(screen,rotation=5)
		if (keys[pg.K_RIGHT]):
			Player.current_frame = 1
			Player.coordinates[0] += Player.speed
			Player.draw(screen,rotation=-5)
		if (not (keys[pg.K_RIGHT] or keys[pg.K_LEFT])):
			Player.current_frame = 0
			Player.draw(screen)
		if (keys[pg.K_UP]):
			Player.coordinates[1] -= Player.speed
		elif (keys[pg.K_DOWN]):
			Player.coordinates[1] += Player.speed
		Player.update()
		pg.draw.line(screen,(255,255,255),(220,580),(220,0))
		pg.draw.line(screen,(255,255,255),(1060,580),(1060,0))
		pg.draw.line(screen,(255,255,255),(220,580),(1060,580))
		starspawn -= 1
		player_cooldown -= 1
		pg.display.flip()
		clock.tick()
def init():
	Game()

init()