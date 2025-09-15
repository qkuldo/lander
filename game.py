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
	Player = modules.sprite.Sprite(PlayerAsset,24*2.5,24*2.5,11,[1280/2,580])
	running = True
	SCREEN_RECT = pg.Rect(0,0,1200,720)
	SCREEN_RECT.x = 0
	SCREEN_RECT.y = 0
	while running:
		screen.fill("black")
		for event in pg.event.get():
			if (event.type == pg.QUIT):
				pg.quit()
				sys.exit()
		keys = pg.key.get_pressed()
		if (keys[pg.K_LEFT]):
			Player.current_frame = 2
			Player.rect.x -= Player.speed
		if (keys[pg.K_RIGHT]):
			Player.current_frame = 1
			Player.rect.x += Player.speed
		if (not (keys[pg.K_RIGHT] or keys[pg.K_LEFT])):
			Player.current_frame = 0
		if (keys[pg.K_UP]):
			Player.rect.y -= Player.speed
		elif (keys[pg.K_DOWN]):
			Player.rect.y += Player.speed
		Player.rect.clamp_ip(SCREEN_RECT)
		Player.update()
		Player.draw(screen)
		pg.display.flip()
		clock.tick()
def init():
	Game()

init()