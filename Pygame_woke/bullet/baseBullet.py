import pygame
from global_parameter import *

class BaseBullet:
    # 弹幕速度,弹幕图片,弹幕所在矩形,弹幕判定矩形,子弹阵营(0我方,1敌方),子弹是否有效
    speed = [0, 0]
    pict = ''
    rep = pygame.Surface((0, 0))
    repr = pygame.Rect((0, 0), (0, 0))
    jrange = pygame.Rect((0, 0), (0, 0))
    camp = 0
    exist = 1

    def __init__(self, speed=None, pict='bullet1.png', pos=(0, 0), camp=0, exist=1):
        if speed is None:
            speed = [0, 0]
        self.speed = speed
        self.pict = pict
        self.camp = camp
        self.exist = exist
        self.rep = pygame.image.load('Image/bullet/' + pict)
        self.repr = self.rep.get_rect()
        self.repr = self.repr.move(pos[0] - self.repr.center[0], pos[1] - self.repr.center[1])
        self.jrange = self.repr

    def move(self):
        self.repr = self.jrange = self.repr.move(self.speed[0], self.speed[1])

    def outOfBounder(self):
        if self.repr.bottom < 0 or self.repr.top > combat_height or self.repr.left > combat_width or self.repr.right < 0:
            return True
        else:
            return False
