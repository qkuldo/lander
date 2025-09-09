import pygame as pg
import sys
import modules
pg.init()
screen = pg.display.set_mode((1000,1000),pg.FULLSCREEN)
clock = pg.time.Clock()
TITLESCENE = 0
GAMESCENE = 1
current_scene = TITLESCENE