import pymunk.pygame_util
import pygame as pg
from random import randrange
from pygame.locals import *

pymunk.pygame_util.positive_y_is_up = False
SCREEN = WIDTH, HEIGHT = (1600, 900)
FPS = 60

pg.init()
scr = pg.display.set_mode(SCREEN)
clock = pg.time.Clock()

C_FONT = pg.font.SysFont('Arial', 30)
count = 0
def counter():
    count_text = C_FONT.render(str(count), True, (0, 0, 200))
    count_area = count_text.get_rect()
    count_area.topleft = (45, 28)
    return [count_text, count_area]

draw_options = pymunk.pygame_util.DrawOptions(scr)


space = pymunk.Space()
space.gravity = 0, 2000
floor_shape = pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20)
space.add(floor_shape)


# создание объекта
counter_img = pg.image.load('counter.png')
counter_rect = counter_img.get_rect()
counter_rect.topleft = (20, 20)


def create_ball(space, pos, ball_mass:int = 1, ball_radius:int = 50, color:tuple = (0, 191, 255, 1)):
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.8
    ball_shape.friction = 0.5
    ball_shape.color = color
    space.add(ball_body, ball_shape)

def create_rect(space, pos):
    rect_mass, rect_size = 1, (75, 50)
    rect_moment = pymunk.moment_for_box(rect_mass, rect_size)
    rect_body = pymunk.Body(rect_mass, rect_moment)
    rect_body.position = pos
    rect_shape = pymunk.Poly.create_box(rect_body, rect_size)
    rect_shape.elasticity = 0.2
    rect_shape.friction = 0.1
    rect_shape.color = [randrange(256) for i in range(4)]
    space.add(rect_body, rect_shape)

while True:
    count_text = counter()
    scr.fill(pg.Color('grey'))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                space = pymunk.Space()
                space.gravity = 0, 2000
                floor_shape = pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20)
                space.add(floor_shape)
    mouse = pg.mouse.get_pressed()
    try:
        if mouse[0]:
            create_ball(space, event.pos)
            count += 1
        if mouse[1]:
            create_ball(space, event.pos, 50, 75, (255, 0, 0, 0.8))
            count += 5
        if mouse[2]:
            create_rect(space, event.pos)
    except Exception as e:
        print('Eror 404')

    space.step(1/FPS)
    space.debug_draw(draw_options)
    scr.blit(counter_img, counter_rect)
    scr.blit(count_text[0], count_text[1])
    pg.display.flip()
    clock.tick(FPS)