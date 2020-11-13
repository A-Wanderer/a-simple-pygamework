import pygame, bullet.baseBullet, role.baseRole, math
from global_parameter import *


class God(role.baseRole.Role):
    skill = ''
    move_speed = 0
    defendnum = 0
    skill_type = 0
    skill_time = 0
    def __init__(self, name='', life=100, speed=None, pict='god1.png', blt=bullet.baseBullet.BaseBullet(speed=[0, -4], camp=0, pict='bullet2.png'), skill='spot2', move_speed=5, skill_type=1, skill_time=3):
        super().__init__()
        if speed is None:
            speed = [0, 0]
        self.move_speed = move_speed
        self.speed = speed
        self.name = name
        self.skill_time = skill_time
        self.skill_type = skill_type
        self.life = life
        self.pict = pict
        self.rep = pygame.image.load('Image/god/'+pict)
        self.repr = self.rep.get_rect()
        self.repr.center = (combat_width/2, combat_height/4*3)
        self.jrange = self.repr
        self.skill = skill
        self.blt = blt

    def attack(self):
        return bullet.baseBullet.BaseBullet(speed=[0, -4], pict=self.blt.pict, pos=self.repr.center, camp=1)

    def shootskill(self, screen):
        Max = 355
        '''
        for num in range(0, Max):
            screen.blit(pygame.image.load('Video/' + 'spot' + '/tmpPic' + str(num) + '.jpg'), [-160, -80])
            pygame.display.flip()
        '''
        return

    def defendskill(self, screen):
        self.defendnum += 20
        Max = 489
        '''
        for num in range(0, Max):
            screen.blit(pygame.image.load('Video/' + 'spot2' + '/tmpPic' + str(num) + '.jpg'), [-160, -80])
            pygame.display.flip()
        '''
        return

    def specialattack(self, n=16):
        ar = []
        sp = [self.blt.speed[0], self.blt.speed[1]]
        for i in range(0, n):
            t1 = int(sp[0] * math.cos(2 * math.pi * i / n) - sp[1] * math.sin(2 * math.pi * i / n))
            t2 = int(sp[0] * math.sin(2 * math.pi * i / n) + sp[1] * math.cos(2 * math.pi * i / n))
            ar.append(bullet.baseBullet.BaseBullet(speed=[t1, t2], pos=self.repr.center, camp=1))
        return ar

    def updateBullet(self):
        self.blt.repr.center = self.repr.center
        self.blt.jrange = self.blt.repr

    def move(self):
        self.jrange = self.repr = self.repr.move(self.speed[0], self.speed[1])
        self.updateBullet()