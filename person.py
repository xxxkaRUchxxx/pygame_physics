import pygame as pg
import settings
from PIL import Image
from random import randint

class Men(pg.sprite.Sprite):
    def __init__(self,name:str = 'steve', pos:list = [400, 400], team:str = 'friend'):
        pg.sprite.Sprite.__init__(self)
        self.__name = name
        self.__pos = pos
        self.__team = team



    def draw(self):
        skin = f'texture/{self.__team}/{self.__name}/Men.png'
        try:
            img = Image.open(skin)
            if img.size[0] > 80 and img.size[1] > 160:
                Exception
            head = img.crop((20, 0, 60, 40))
            body = img.crop((20, 40, 60, 100))
            armL = img.crop((0, 40, 20, 100))
            armR = img.crop((60, 40, 80, 100))
            legL = img.crop((20, 100, 40, 160))
            legR = img.crop((40, 100, 60, 160))
            men_skin = [head, body, armL, armR, legL, legR]
            for i in men_skin:
                settings.scr.blit(pg.image.load(i).convert_alpha(), self.__pos)
        except:
            print('скин не найден | не удалось открыть')


    def walk(self, x:int = 0, y:int = 0):
        if self.__pos[0] < settings.screen[0] and self.__pos[0] >= 0 and self.__pos[1] < settings.screen[1] and self.__pos[1] >= 0:
            self.__pos[0] += x
            self.__pos[1] += y
        else:
            self.__pos[0] = randint(50, settings.screen[1] - 100)
            self.__pos[1] = randint(50, settings.screen[1] - 100)
    # def color(self, walk:int):
    #     if walk == 1:
    #         self.__color_body = 'green'
    #     if walk == 2:
    #         self.__color_body = 'yellow'
    #     if walk == 3:
    #         self.__color_body = 'gold'
    #     if walk == 4:
    #         self.__color_body = 'silver'




