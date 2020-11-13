import role.baseRole, pygame
import bullet.baseBullet
import time
from global_parameter import *


class BaseEnemy(role.baseRole.Role):
    ntime = 0.0
    attackInterval = 0.0
    def __init__(self, name, life, speed, blt, ntime=time.time(), attackInterval=1.0):
        super().__init__()
        if speed is None:
            self.speed = [0, 0]
        self.name = name
        self.life = life
        self.speed = speed
        self.blt = blt
        self.ntime = ntime
        self.attackInterval = attackInterval

    def updateBullet(self):
        self.blt.repr.center = self.repr.center
        self.blt.jrange = self.blt.repr

    def move(self):
        width = combat_width
        height = combat_height*2/3
        if self.repr.left < 0 or self.repr.right > width:
            self.speed[0] *= -1
            if width < self.repr.right < self.repr.right + self.speed[0]:
                self.speed[0] *= -1
            if self.repr.left + self.speed[0] < self.repr.left < 0:
                self.speed[0] *= -1
        if self.repr.bottom > height or self.repr.top < 0:
            self.speed[1] *= -1
            if height < self.repr.bottom < self.repr.bottom + self.speed[1]:
                self.speed[1] *= -1
            if self.repr.top + self.speed[1] < self.repr.top < 0:
                self.speed[1] *= -1
        self.jrange = self.repr = self.repr.move(self.speed[0], self.speed[1])
        self.updateBullet()





