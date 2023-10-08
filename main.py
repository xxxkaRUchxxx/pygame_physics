import pygame as pg
from sys import exit
from pygame.locals import *
import settings
import person

steve = person.Men()
krovosos = person.Men('fireman', [100, 100], 1)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    keys = pg.key.get_pressed()
    if keys[K_LEFT]:
        steve.walk(x = -0.5)
    if keys[K_RIGHT]:
        steve.walk(x = 0.5)
    if keys[K_UP]:
        steve.walk(y = -0.5)
    if keys[K_DOWN]:
        steve.walk(y = 0.5)


    settings.scr.fill(settings.bg_color)
    steve.draw()
    pg.display.flip()

