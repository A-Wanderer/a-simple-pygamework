import pygame, role.enemy.baseEnemy, bullet.baseBullet, math, time
from global_parameter import *


class Boss(role.enemy.baseEnemy.BaseEnemy):
    firstAppear = 1
    x_speed = 0
    y_speed = 0
    attackStyle = 0
    def __init__(self, name='', life=100, speed=None, pict='boss2.png',blt=bullet.baseBullet.BaseBullet(speed=[0, 4], camp=1), firstAppear=1, attackStyle=0, attackInterval=0.5):
        super(Boss, self).__init__(name, life, speed, blt, attackInterval=attackInterval)
        if speed is None:
            speed = [5, 2]
        self.speed = [speed[0], speed[1]]
        self.x_speed = speed[0]
        self.y_speed = speed[1]
        self.pict = pict
        self.firstAppear = firstAppear
        self.attackStyle = attackStyle
        self.rep = pygame.image.load('Image/enemy/boss/' + pict)
        self.jrange = self.repr = self.rep.get_rect()
        self.ntime = time.time()
        self.repr.center = (combat_width / 2, -20)

    def moveStyle1(self):
        # 向斜下飞，碰到右边界停止右飞，开始竖直向上
        if self.repr.right >= combat_width - 10:
            self.speed[0] = 0
            self.speed[1] = -self.y_speed
        # 向上到达上边界后，开始向左下飞
        if self.repr.top <= 10 and self.repr.right >= combat_width - 10:
            self.speed[0] = -self.x_speed
            self.speed[1] = self.y_speed
        # 飞到左边界后，停止左飞，开始向竖直向上飞
        if self.repr.left <= 10:
            self.speed[0] = 0
            self.speed[1] = -self.y_speed
        # 向上到达上边界后，开始向右下飞
        if self.repr.top <= 10 and self.repr.left <= 10:
            self.speed[0] = self.x_speed
            self.speed[1] = self.y_speed

    def moveStyle2(self):
        # boss横着走的时候判定
        if self.speed[0] != 0 and self.speed[1] == 0:
            if self.repr.centery <= combat_height / 4 and self.repr.right >= combat_width - 10:
                self.speed[0] = 0
                self.speed[1] = -self.x_speed
            if self.repr.centery >= combat_height / 4 and self.repr.left <= 10:
                self.speed[0] = 0
                self.speed[1] = -self.x_speed
            if self.repr.centery >= combat_height / 2 - 5 and self.repr.right >= combat_width - 10:
                self.repr.center = self.repr.width / 2 + 10, self.repr.height / 2 + 10
                self.jrange = self.repr
                # self.speed = [-self.x_speed,0]
                # 闪现
        # boss竖着走的时候的判定
        elif self.speed[0] == 0 and self.speed[1] != 0:
            if self.repr.centery >= combat_height / 4 and self.repr.right >= combat_width - 10:
                self.speed[0] = self.x_speed
                self.speed[1] = 0
            if self.repr.centery >= combat_height / 2 and self.repr.left <= 10:
                self.speed[0] = -self.x_speed
                self.speed[1] = 0
        # boss斜着走时候的判定

    def moveStyle3(self):
        # boss横着走时候的判定
        if self.speed[0] != 0 and self.speed[1] == 0:
            if self.repr.centerx >= combat_width / 2 and self.repr.centery >= combat_height / 2 - 5:
                self.speed[0] = 0
                self.speed[1] = self.y_speed
            if self.repr.centerx >= combat_width / 2 and self.repr.right >= combat_width - 10:
                self.speed[0] = 0
                self.speed[1] = -self.y_speed
        # boss竖着走的时候判定
        elif self.speed[0] == 0 and self.speed[1] != 0 and self.speed != [0, 2]:
            if self.repr.left <= 10 and self.repr.centery >= combat_height / 2 - 5:
                self.speed[0] = -self.y_speed
                self.speed[1] = 0
            if self.repr.top <= 10 and self.repr.centerx >= combat_width / 2 - 5:
                self.speed[0] = -self.y_speed
                self.speed[1] = 0
            if self.repr.centery >= combat_height / 2 - 5 and self.repr.right >= combat_width - 10:
                self.repr.center = self.repr.width / 2 + 10, self.repr.height / 2 + 10
                self.jrange = self.repr
                # 闪现，要改

    def attackStyle1(self, n=6):
        ar1 = []
        sp = [self.blt.speed[0], self.blt.speed[1]]
        for i in range(0, n):
            t1 = float(sp[0])
            t2 = float(sp[1])
            sp[0] = int(t1 * math.cos(2 * math.pi / n) - t2 * math.sin(2 * math.pi / n))
            sp[1] = int(t1 * math.sin(2 * math.pi / n) + t2 * math.cos(2 * math.pi / n))
            ar1.append(bullet.baseBullet.BaseBullet(speed=[sp[0], sp[1]], pos=self.blt.repr.center, camp=1))
        return ar1

    # 环形子弹
    def attackStyle2(self, n=24):
        ar2 = []
        sp = [self.blt.speed[0], self.blt.speed[1]]
        for i in range(0, n):
            t1 = int(sp[0] * math.cos(2 * math.pi * i / n) - sp[1] * math.sin(2 * math.pi * i / n))
            t2 = int(sp[0] * math.sin(2 * math.pi * i / n) + sp[1] * math.cos(2 * math.pi * i / n))
            ar2.append(bullet.baseBullet.BaseBullet(speed=[t1, t2], pos=self.blt.repr.center, camp=1))
        return ar2

    # 前方三向直线子弹
    def attackStyle3(self):
        ar3 = []
        sp = [self.blt.speed[0], self.blt.speed[1]]
        ar3.append(bullet.baseBullet.BaseBullet(speed=[sp[0], sp[1]], pos=self.blt.repr.center, camp=1))
        t1 = int(sp[0] * math.cos(-math.pi / 6) - sp[1] * math.sin(-math.pi / 6))
        t2 = int(sp[0] * math.sin(-math.pi / 6) + sp[1] * math.cos(-math.pi / 6))
        ar3.append(bullet.baseBullet.BaseBullet(speed=[t1, t2], pos=self.blt.repr.center, camp=1))
        t3 = int(sp[0] * math.cos(math.pi / 6) - sp[1] * math.sin(math.pi / 6))
        t4 = int(sp[0] * math.sin(math.pi / 6) + sp[1] * math.cos(math.pi / 6))
        ar3.append(bullet.baseBullet.BaseBullet(speed=[t3, t4], pos=self.blt.repr.center, camp=1))
        return ar3

    #通过改变参数来控制攻击方式
    def attack(self, n=1):
        if n%3 == 0:
            return self.attackStyle1()
        elif n%3 == 1:
            return self.attackStyle2()
        elif n%3 == 2:
            return self.attackStyle3()

    def appear(self):
        if self.firstAppear == 1:
            self.speed = [0, 2]
            if self.repr.bottom >= 150:
                self.speed = [5, 2]
                self.firstAppear = 0

    def move(self, n):
        self.appear()
        if n == 1:
            self.moveStyle1()
        elif n == 2:
            self.moveStyle2()
        else:
            self.moveStyle3()
        super().move()
        # self.repr.center = (combat_width / 2, -self.repr.center[1])

