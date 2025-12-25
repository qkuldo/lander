import pygame as pg
import sys
import modules
import random as rand
import math
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((1280,720))
clock = pg.time.Clock()
TITLESCENE = 0
GAMESCENE = 1
current_scene = GAMESCENE
def loadSpritesheetFile(filepath,width,height):
	asset = pg.image.load(filepath)
	return modules.sheet.Spritesheet(asset,width,height)
def Game():
	slowdown_timer = 500
	playerAsset = loadSpritesheetFile("assets/images/PNG FILES/hypership.png",17,16)
	bulletAsset = pg.image.load("assets/images/PNG FILES/bullet.png")
	enemyAssets = {"Warden Ship":loadSpritesheetFile("assets/images/PNG FILES/warden-enemy.png",17,18),"bullet":pg.image.load("assets/images/PNG FILES/enemyFlying-bullet.png")}
	Player = modules.sprite.SpecialSprite(playerAsset,24*2.5,24*2.5,11,[1280/2,580],hp=20)
	testSprite = modules.sprite.SpecialSprite(enemyAssets["Warden Ship"],24*2.5,24*2.5,0,[1280/2,0],hp=20)
	enemyTestSprite = modules.sprite.SpecialSprite(enemyAssets["Warden Ship"],24*2.5,24*2.5,0,[0,0],speed=20,hp=20,optional_params={"deadCenter":[1280/2,90],"movementAngle":0,"radius":100})
	running = True
	stargroup = modules.particle.StarGroup()
	starspawn = rand.randint(1,30)
	player_bulletlist = []
	enemy_bulletlist = []
	player_cooldown = 0
	scroll_speed = 0
	speed_up_timer = 30
	game_bg = pg.Rect((220,0),(840,580))
	SFX = {"playerShoot":pg.mixer.Sound("assets/sfx/playerShoot.wav")}
	typeLegend = {"basicBullet":0}
	debug_mode = False
	while running:
		player_hp_rect = pg.Rect((200,580-Player.hp*10),(15,Player.hp*10))
		moved_ltor = False
		screen.fill("black")
		for event in pg.event.get():
			if (event.type == pg.QUIT):
				pg.quit()
				sys.exit()
		keys = pg.key.get_pressed()
		left_to_right_list = [keys[pg.K_LEFT],keys[pg.K_a],keys[pg.K_RIGHT],keys[pg.K_d]]
		if (starspawn <= 0):
			if (scroll_speed == 0):
				stargroup.createGroupParticle(minspeed=0.1,maxspeed=5)
			elif (scroll_speed == 1):
				stargroup.createGroupParticle(minspeed=0.5,maxspeed=7)
			elif (scroll_speed == 2):
				stargroup.createGroupParticle(minspeed=1,maxspeed=10)
			elif (scroll_speed == 3):
				stargroup.createGroupParticle(minspeed=5,maxspeed=12)
			starspawn = rand.randint(1,30)
		pg.draw.rect(screen,(16,4,17),game_bg)
		if (keys[pg.K_SPACE] and player_cooldown <= 0):
			player_bulletlist.append(modules.sprite.Projectile(bulletAsset,16,24,1,[Player.rect.midtop[0]-7,Player.rect.midtop[1]],speed=[0,-10],attack=Player.attack))
			player_cooldown = 30
			SFX["playerShoot"].play()
		for bullet in player_bulletlist:
			dead = bullet.update()
			if (dead):
				player_bulletlist.remove(bullet)
			else:
				bullet.draw(screen)
		for bullet in enemy_bulletlist:
			if (typeLegend["basicBullet"] == bullet.optional_params["type"]):
				dead = bullet.update()
			if (pg.Rect.colliderect(bullet.rect,Player.rect)):
				Player.hp -= bullet.attack
				enemy_bulletlist.remove(bullet)
			else:
				if (dead):
					enemy_bulletlist.remove(bullet)
				else:
					bullet.draw(screen)
		if (True in left_to_right_list):
			if (not moved_ltor and (keys[pg.K_RIGHT] or keys[pg.K_d])):
				moved_ltor = True
				if (scroll_speed == 0):
					Player.coordinates[0] += Player.speed
				elif (scroll_speed == 1):
					Player.coordinates[0] += Player.speed*1.2
				elif (scroll_speed == 2):
					Player.coordinates[0] += Player.speed*1.4
				elif (scroll_speed == 3):
					Player.coordinates[0] += Player.speed*1.6
				testSprite.current_frame = 2
				if (scroll_speed == 0):
					Player.current_frame = 2
				elif (scroll_speed == 1):
					Player.current_frame = 5
				elif (scroll_speed == 2):
					Player.current_frame = 8
				elif (scroll_speed == 3):
					Player.current_frame = 11
				Player.draw(screen,rotation=0)
			if (not moved_ltor and (keys[pg.K_LEFT] or keys[pg.K_a])):
				moved_ltor = True
				testSprite.current_frame = 1
				if (scroll_speed == 0):
					Player.current_frame = 1
					Player.coordinates[0] -= Player.speed
				elif (scroll_speed == 1):
					Player.current_frame = 4
					Player.coordinates[0] -= Player.speed*1.2
				elif (scroll_speed == 2):
					Player.current_frame = 7
					Player.coordinates[0] -= Player.speed*1.4
				elif (scroll_speed == 3):
					Player.current_frame = 10
					Player.coordinates[0] -= Player.speed*1.6
				Player.draw(screen,rotation=0)
		else:
			testSprite.current_frame = 0
			if (scroll_speed == 0):
				Player.current_frame = 0
			elif (scroll_speed == 1):
				Player.current_frame = 3
			elif (scroll_speed == 2):
				Player.current_frame = 6
			elif (scroll_speed == 3):
				Player.current_frame = 9
			Player.draw(screen)
		#testSprite.draw(screen)
		if (keys[pg.K_UP] or keys[pg.K_w]):
			if (scroll_speed == 0):
				Player.coordinates[1] -= Player.speed
			elif (scroll_speed == 1):
				Player.coordinates[1] -= Player.speed*1.2
			elif (scroll_speed == 2):
				Player.coordinates[1] -= Player.speed*1.4
			elif (scroll_speed == 3):
				Player.coordinates[1] -= Player.speed*1.6
		if (keys[pg.K_DOWN] or keys[pg.K_s]):
			if (scroll_speed == 0):
				Player.coordinates[1] += Player.speed
			elif (scroll_speed == 1):
				Player.coordinates[1] += Player.speed*1.2
			elif (scroll_speed == 2):
				Player.coordinates[1] += Player.speed*1.4
			elif (scroll_speed == 3):
				Player.coordinates[1] += Player.speed*1.6

		if ((keys[pg.K_RSHIFT] or keys[pg.K_LSHIFT]) and scroll_speed < 3):
			speed_up_timer -= 0.1
			if (slowdown_timer < 500):
				slowdown_timer += 1
		else:
			slowdown_timer -= 1
		if (speed_up_timer <= 0):
			if (scroll_speed == 0):
				speed_up_timer = 60
			elif (scroll_speed == 1):
				speed_up_timer = 70
			elif (scroll_speed == 2):
				speed_up_timer = 80
			scroll_speed += 1
		if (slowdown_timer <= 0 and scroll_speed > 0):
			scroll_speed -= 1
		Player.update()
		enemy_wardenBehavior(enemyTestSprite,screen,enemy_bulletlist,enemyAssets)
		stargroup.updateall(screen)
		pg.draw.line(screen,(255,255,255),(220,580),(220,0))
		pg.draw.line(screen,(255,255,255),(1060,580),(1060,0))
		pg.draw.line(screen,(255,255,255),(220,580),(1060,580))
		pg.draw.rect(screen,(230,104,78),player_hp_rect)
		if (debug_mode):
			pg.draw.rect(screen,(255,255,255),Player.rect)
		starspawn -= 1
		player_cooldown -= 1
		pg.display.flip()
		clock.tick(60)
		if (Player.hp <= 0):
			gameOver()
def init():
	Game()

def gameOver():
	pg.quit()
	sys.exit()

def enemy_wardenBehavior(enemy,screen,bulletlist,assets):
	enemy.optional_params["movementAngle"] += enemy.speed
	bullet = modules.sprite.Projectile(assets["bullet"],16,24,1,[enemy.rect.midbottom[0]-7,enemy.rect.midbottom[1]],speed=[0,10],attack=enemy.attack,optional_params={"type":0})
	end_angle = 2250
	if (enemy.optional_params["movementAngle"] == 180 or enemy.optional_params["movementAngle"] == 1500 or enemy.optional_params["movementAngle"] == 800 or enemy.optional_params["movementAngle"] == 1900):
		bulletlist.append(bullet)
	if (enemy.optional_params["movementAngle"] >= end_angle):
		enemy.optional_params["movementAngle"] = 0
	enemy.coordinates[0] = enemy.optional_params["deadCenter"][0] + enemy.optional_params["radius"] * math.cos(enemy.optional_params["movementAngle"]/360)
	enemy.coordinates[1] = enemy.optional_params["deadCenter"][1] + enemy.optional_params["radius"] * math.sin(enemy.optional_params["movementAngle"]/360)
	enemy.update()
	enemy.draw(screen)

init()