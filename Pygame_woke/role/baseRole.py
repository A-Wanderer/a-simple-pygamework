import pygame
import bullet.baseBullet


class Role:
    name = ''
    life = 0
    speed = [0, 0]
    pict = ''
    rep = pygame.Surface((0, 0))
    repr = pygame.Rect((0, 0), (0, 0))
    jrange = pygame.Rect((0, 0), (0, 0))
    blt = bullet.baseBullet.BaseBullet()

    def __init__(self):
        return

    def move(self):
        return

    def attack(self):
        return

    def die(self):
        if self.life <= 0:
            return True
        else:
            return False