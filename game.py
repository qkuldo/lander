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
	Player = modules.sprite.SpecialSprite(PlayerAsset,24*2.5,24*2.5,11,[1280/2,580],hp=20)
	running = True
	stargroup = modules.particle.StarGroup()
	starspawn = rand.randint(1,100)
	player_bulletlist = []
	player_cooldown = 0
	scroll_speed = 0
	speed_up_timer = 2
	player_hp_rect = pg.Rect((200,580-Player.hp*10),(15,Player.hp*10))
	while running:
		screen.fill("black")
		for event in pg.event.get():
			if (event.type == pg.QUIT):
				pg.quit()
				sys.exit()
		keys = pg.key.get_pressed()
		if (starspawn <= 0):
			if (scroll_speed == 0):
				stargroup.createGroupParticle(minspeed=0.01,maxspeed=1)
			elif (scroll_speed == 1):
				stargroup.createGroupParticle(minspeed=0.05,maxspeed=1.5)
			elif (scroll_speed == 2):
				stargroup.createGroupParticle(minspeed=0.1,maxspeed=2)
			elif (scroll_speed == 3):
				stargroup.createGroupParticle(minspeed=0.5,maxspeed=2.5)
			starspawn = rand.randint(1,100)
		stargroup.updateall(screen)
		if (keys[pg.K_SPACE] and player_cooldown <= 0):
			player_bulletlist.append(modules.sprite.Projectile(BulletAsset,16,24,1,[Player.rect.midtop[0]-7,Player.rect.midtop[1]],speed=[0,-1],attack=Player.attack)
			player_cooldown = 200
		for bullet in player_bulletlist:
			dead = bullet.update()
			if (dead):
				player_bulletlist.remove(bullet)
			else:
				bullet.draw(screen)
		if (keys[pg.K_LEFT] or keys[pg.K_a]):
			if (scroll_speed == 0):
				Player.current_frame = 2
			elif (scroll_speed == 1):
				Player.current_frame = 5
			elif (scroll_speed == 2):
				Player.current_frame = 8
			elif (scroll_speed == 3):
				Player.current_frame = 11
			Player.coordinates[0] -= Player.speed
			Player.draw(screen,rotation=5)
		if (keys[pg.K_RIGHT] or keys[pg.K_d]):
			if (scroll_speed == 0):
				Player.current_frame = 1
			elif (scroll_speed == 1):
				Player.current_frame = 4
			elif (scroll_speed == 2):
				Player.current_frame = 7
			elif (scroll_speed == 3):
				Player.current_frame = 10
			Player.coordinates[0] += Player.speed
			Player.draw(screen,rotation=-5)
		if (not ((keys[pg.K_RIGHT] or keys[pg.K_d]) or (keys[pg.K_LEFT] or keys[pg.K_a]))):
			if (scroll_speed == 0):
				Player.current_frame = 0
			elif (scroll_speed == 1):
				Player.current_frame = 3
			elif (scroll_speed == 2):
				Player.current_frame = 6
			elif (scroll_speed == 3):
				Player.current_frame = 9
			Player.draw(screen)
		if (keys[pg.K_UP] or keys[pg.K_w]):
			Player.coordinates[1] -= Player.speed
		elif (keys[pg.K_DOWN] or keys[pg.K_s]):
			Player.coordinates[1] += Player.speed
		if ((keys[pg.K_RSHIFT] or keys[pg.K_LSHIFT]) and scroll_speed < 3):
			speed_up_timer -= 0.001
		if (speed_up_timer <= 0):
			if (scroll_speed == 0):
				speed_up_timer = 3
			elif (scroll_speed == 1):
				speed_up_timer = 4
			elif (scroll_speed == 2):
				speed_up_timer = 6
			scroll_speed += 1
		Player.update()
		pg.draw.line(screen,(255,255,255),(220,580),(220,0))
		pg.draw.line(screen,(255,255,255),(1060,580),(1060,0))
		pg.draw.line(screen,(255,255,255),(220,580),(1060,580))
		pg.draw.rect(screen,(230,104,78),player_hp_rect)
		starspawn -= 1
		player_cooldown -= 1
		pg.display.flip()
		clock.tick()
def init():
	Game()

init()