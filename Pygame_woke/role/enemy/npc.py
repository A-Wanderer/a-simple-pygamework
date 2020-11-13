import pygame, role.enemy.baseEnemy, bullet.baseBullet, math
from global_parameter import *


class Npc(role.enemy.baseEnemy.BaseEnemy):

    #pos:1上左,2上中,3上右,4左上,5右上,6左中,7右中表示7种不同的出生位置及对应的速度
    def __init__(self, name='', life=1, speed=None, pict='npc1.png', blt=bullet.baseBullet.BaseBullet(speed=[0, 4], camp=1), pos=2, attackInterval=1.0):
        super().__init__(name, life, speed, blt, attackInterval=attackInterval)
        self.pict = pict
        self.rep = pygame.image.load('Image/enemy/npc/' + pict)
        self.repr = self.rep.get_rect()
        if pos == 1:
            self.repr.center = (combat_width / 4, -self.repr.center[1])
            self.speed = [-8, 5]
        elif pos == 2:
            self.repr.center = (combat_width / 2, -self.repr.center[1])
            self.speed = [0, 5]
        elif pos == 3:
            self.repr.center = (combat_width * 3 / 4, -self.repr.center[1])
            self.speed = [8, 5]
        elif pos == 4:
            self.repr.center = (-self.repr.center[0], combat_height/7)
            self.speed = [5, 1]
        elif pos == 5:
            self.repr.center = (combat_width+self.repr.center[0], combat_height/7)
            self.speed = [-5, 1]
        elif pos == 6:
            self.repr.center = (-self.repr.center[0], combat_height *2/ 7)
            self.speed = [5, 0]
        elif pos == 7:
            self.repr.center = (combat_width+self.repr.center[0], combat_height*2/7)
            self.speed = [-5, 0]
        self.jrange = self.repr
        super(Npc, self).updateBullet()
        #print(blt.repr.center)

    def attack(self, n = 4):
        ar = []
        sp = [self.blt.speed[0], self.blt.speed[1]]
        for i in range(0, n):
            t1 = int(sp[0] * math.cos(2 * math.pi * i / n) - sp[1] * math.sin(2 * math.pi * i / n))
            t2 = int(sp[0] * math.sin(2 * math.pi * i / n) + sp[1] * math.cos(2 * math.pi * i / n))
            ar.append(bullet.baseBullet.BaseBullet(speed=[t1, t2], pos=self.repr.center, camp=1))
        return ar





