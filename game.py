import pygame as pg
import sys
import modules
pg.init()
screen = pg.display.set_mode((1280,720))
clock = pg.time.Clock()
TITLESCENE = 0
GAMESCENE = 1
current_scene = GAMESCENE

def Game():
	PlayerAsset = pg.image.load("assets/images/PNG FILES/hypership.png")
	PlayerAsset = modules.sheet.Spritesheet(PlayerAsset,24,24)
	Bullet = pg.image.load("assets/images/PNG FILES/bullet.png")
	Player = modules.sprite.Sprite(PlayerAsset,24*2.5,24*2.5,11,[1280/2,580])
	running = True
	while running:
		screen.fill("black")
		for event in pg.event.get():
			if (event.type == pg.QUIT):
				pg.quit()
				sys.exit()
		keys = pg.key.get_pressed()
		if (keys[pg.K_LEFT]):
			Player.current_frame = 2
			Player.coordinates[0] -= Player.speed
			Player.draw(screen,rotation=15)
		if (keys[pg.K_RIGHT]):
			Player.current_frame = 1
			Player.coordinates[0] += Player.speed
			Player.draw(screen,rotation=-15)
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
		pg.display.flip()
		clock.tick()
def init():
	Game()

init()