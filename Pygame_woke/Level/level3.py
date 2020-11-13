import pygame, sys, role.god.baseGod, bullet.baseBullet, role.enemy.boss, role.enemy.npc, time, pygame.freetype
from global_parameter import *

#关卡等级1，包括30个小怪，1个boss，boss血量80左右
def Level_3(god = role.god.baseGod.God()):
    pygame.init()
    size = (windows_width, windows_height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('第3关')
    fclock = pygame.time.Clock()
    fps = 60

    pause = 0
    over_bul = False

    combat_background = pygame.image.load('Image/background/combat_background3.jpg')
    combat_background_rect = combat_background.get_rect()

    combat_information = pygame.image.load('Image/background/combat_information.jpg')
    combat_information_rect = combat_information.get_rect()
    combat_information_rect = combat_information_rect.move(960, 0)

    back1 = pygame.image.load('Image/font/back1.png')
    back2 = pygame.image.load('Image/font/back2.png')
    back_rect = back1.get_rect()
    back_rect = back_rect.move(1050, 600)

    enemy_bullet_list = []
    god_bullet_list = []
    enemy_list = []
    boss_list = []
    old_time = time.time()
    boss_come_judge = False           #指示位，指使boss是否该出现
    boss_attack_judge = 0
    enemy_come = [True, True, True, True, True, True, True, True, True, True, True]

    def intersection(rect1, rect2):
        return pygame.Rect.colliderect(rect1, rect2)

    def bullet_update(screen):
        for v in god_bullet_list:
            if v.outOfBounder():
                v.exist = 0
                continue
            for k in enemy_list:
                if k.life > 0 and intersection(v.jrange, k.jrange):
                    v.exist = 0
                    k.life = k.life - 1
                    break
            for k in boss_list:
                if k.life > 0 and intersection(v.jrange, k.jrange):
                    v.exist = 0
                    k.life = k.life - 1
                    break
        ti = 0
        tl = len(god_bullet_list)
        while ti < tl:
            if god_bullet_list[ti].exist == 0:
                del god_bullet_list[ti]
                tl = tl - 1
                continue
            screen.blit(god_bullet_list[ti].rep, god_bullet_list[ti].repr)
            god_bullet_list[ti].move()
            ti = ti + 1

        for v in enemy_bullet_list:
            if v.outOfBounder():
                v.exist = 0
                continue
            if god.life > 0 and intersection(god.jrange, v.jrange):
                v.exist = 0
                if god.defendnum > 0:
                    god.defendnum = god.defendnum - 1
                else:
                    god.life = god.life - 1
                break
        ti = 0
        tl = len(enemy_bullet_list)
        while ti < tl:
            if enemy_bullet_list[ti].exist == 0:
                del enemy_bullet_list[ti]
                tl = tl - 1
                continue
            screen.blit(enemy_bullet_list[ti].rep, enemy_bullet_list[ti].repr)
            enemy_bullet_list[ti].move()
            ti = ti + 1

    def enemy_update(screen):
        ti = 0
        tl = len(enemy_list)
        while ti < tl:
            if enemy_list[ti].life <= 0:
                del enemy_list[ti]
                tl = tl - 1
                continue
            screen.blit(enemy_list[ti].rep, enemy_list[ti].repr)
            enemy_list[ti].move()
            ti = ti + 1

    def enemy_attack():
        # global judge
        b = time.time()
        for a in enemy_list:
            if b - a.ntime >= a.attackInterval:
                for i in a.attack(16):
                    enemy_bullet_list.append(
                        bullet.baseBullet.BaseBullet(speed=[i.speed[0], i.speed[1]], pos=i.repr.center, camp=i.camp))
                # print(len(blt))
                # judge = judge + 1
                a.ntime = b

    def boss_attack():
        nonlocal boss_attack_judge
        b = time.time()
        for a in boss_list:
            if b - a.ntime >= 1:
                for i in a.attack(boss_attack_judge % 3):
                    enemy_bullet_list.append(
                        bullet.baseBullet.BaseBullet(speed=[i.speed[0], i.speed[1]], pos=i.repr.center, camp=i.camp))
                a.ntime = b
                boss_attack_judge = boss_attack_judge + 1

    def god_update(screen):
        if god.life <= 0:
            nonlocal over_bul
            over_bul = True
        else:
            god.move()
            img = pygame.image.load('Image/defend/skill.png')
            liumangxing_rect = img.get_rect()
            liumangxing_rect.center = god.repr.center
            if god.defendnum > 0:
                screen.blit(img, liumangxing_rect)
            screen.blit(god.rep, god.repr)

    def combat_information_update(screen):
        screen.blit(combat_information, combat_information_rect)
        if back_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(back2, back_rect)
        else:
            screen.blit(back1, back_rect)
        ft = pygame.freetype.Font('Font/SIMLI.TTF', 36)
        ft.render_to(screen, (1015, 50), '作战信息', fgcolor=BLACK, size=50)
        ft.render_to(screen, (1000, 150), '人物生命:' + str(god.life), fgcolor=BLACK, size=30)
        ft.render_to(screen, (1000, 250), '人物护盾:' + str(god.defendnum), fgcolor=BLACK, size=30)
        ft.render_to(screen, (1000, 350), '小怪数量:' + str(len(enemy_list)), fgcolor=BLACK, size=30)
        ft.render_to(screen, (1000, 450), '可用技能:' + str(god.skill_time), fgcolor=BLACK, size=30)
        if len(boss_list) != 0:
            ft.render_to(screen, (1000, 550), 'BOSS生命:' + str(boss_list[0].life), fgcolor=BLACK, size=30)

    #npd何时出场
    def npc_come(time):
        if time >= 5 and time <= 5.1 and enemy_come[0] == True:
            enemy_list.append(role.enemy.npc.Npc(pos = 1))
            enemy_list.append(role.enemy.npc.Npc(pos = 2))
            enemy_come[0] = False
        elif  enemy_come[1] == True:
            enemy_list.append(role.enemy.npc.Npc(pos = 2))
            enemy_list.append(role.enemy.npc.Npc(pos = 6))
            enemy_list.append(role.enemy.npc.Npc(pos = 7))
            enemy_come[1] = False
        elif enemy_come[2] == True:
            enemy_list.append(role.enemy.npc.Npc(pos = 6))
            enemy_list.append(role.enemy.npc.Npc(pos = 7))
            enemy_list.append(role.enemy.npc.Npc(pos = 1))
            enemy_list.append(role.enemy.npc.Npc(pos = 2))
            enemy_list.append(role.enemy.npc.Npc(pos = 3))
            enemy_come[2] = False
        elif enemy_come[3] == True:
            enemy_list.append(role.enemy.npc.Npc(pos = 1))
            enemy_list.append(role.enemy.npc.Npc(pos = 2))
            enemy_list.append(role.enemy.npc.Npc(pos = 3))
            enemy_list.append(role.enemy.npc.Npc(pos = 4))
            enemy_list.append(role.enemy.npc.Npc(pos = 5))
            enemy_come[3] = False
        elif enemy_come[4] == True:
            enemy_list.append(role.enemy.npc.Npc(pos = 1))
            enemy_list.append(role.enemy.npc.Npc(pos = 2))
            enemy_list.append(role.enemy.npc.Npc(pos = 3))
            enemy_list.append(role.enemy.npc.Npc(pos = 6))
            enemy_list.append(role.enemy.npc.Npc(pos = 7))
            enemy_come[4] = False
        elif enemy_come[5] == True:
            enemy_list.append(role.enemy.npc.Npc(pos = 1))
            enemy_list.append(role.enemy.npc.Npc(pos = 4))
            enemy_list.append(role.enemy.npc.Npc(pos = 5))
            enemy_come[5] = False
        elif enemy_come[6] == True:
            enemy_list.append(role.enemy.npc.Npc(pos = 1))
            enemy_list.append(role.enemy.npc.Npc(pos = 2))
            enemy_list.append(role.enemy.npc.Npc(pos = 3))
            enemy_list.append(role.enemy.npc.Npc(pos = 4))
            enemy_list.append(role.enemy.npc.Npc(pos = 5))
            enemy_come[6] = False
        elif enemy_come[7] == True:
            enemy_list.append(role.enemy.npc.Npc(pos=1))
            enemy_list.append(role.enemy.npc.Npc(pos=2))
            enemy_list.append(role.enemy.npc.Npc(pos=3))
            enemy_list.append(role.enemy.npc.Npc(pos=4))
            enemy_list.append(role.enemy.npc.Npc(pos=5))
            enemy_list.append(role.enemy.npc.Npc(pos=6))
            enemy_list.append(role.enemy.npc.Npc(pos=7))
            enemy_list.append(role.enemy.npc.Npc(pos = 1))
            enemy_come[7] = False
        elif enemy_come[8] == True:
            enemy_list.append(role.enemy.npc.Npc(pos=1))
            enemy_list.append(role.enemy.npc.Npc(pos=2))
            enemy_list.append(role.enemy.npc.Npc(pos=3))
            enemy_list.append(role.enemy.npc.Npc(pos=4))
            enemy_list.append(role.enemy.npc.Npc(pos=5))
            enemy_list.append(role.enemy.npc.Npc(pos=1))
            enemy_list.append(role.enemy.npc.Npc(pos=2))
            enemy_list.append(role.enemy.npc.Npc(pos=3))
            enemy_list.append(role.enemy.npc.Npc(pos=4))
            enemy_list.append(role.enemy.npc.Npc(pos=5))
            enemy_come[8] = False
        elif enemy_come[9] == True:
            enemy_list.append(role.enemy.npc.Npc(pos=1))
            enemy_list.append(role.enemy.npc.Npc(pos=2))
            enemy_list.append(role.enemy.npc.Npc(pos=3))
            enemy_list.append(role.enemy.npc.Npc(pos=6))
            enemy_list.append(role.enemy.npc.Npc(pos=7))
            enemy_list.append(role.enemy.npc.Npc(pos=1))
            enemy_list.append(role.enemy.npc.Npc(pos=2))
            enemy_list.append(role.enemy.npc.Npc(pos=3))
            enemy_list.append(role.enemy.npc.Npc(pos=6))
            enemy_list.append(role.enemy.npc.Npc(pos=7))
            enemy_come[9] = False
        elif enemy_come[10] == True:
            enemy_list.append(role.enemy.npc.Npc(pos=2))
            enemy_list.append(role.enemy.npc.Npc(pos=4))
            enemy_list.append(role.enemy.npc.Npc(pos=6))
            enemy_list.append(role.enemy.npc.Npc(pos=7))
            enemy_list.append(role.enemy.npc.Npc(pos=1))
            enemy_list.append(role.enemy.npc.Npc(pos=3))
            enemy_list.append(role.enemy.npc.Npc(pos=2))
            enemy_list.append(role.enemy.npc.Npc(pos=6))
            enemy_list.append(role.enemy.npc.Npc(pos=6))
            enemy_list.append(role.enemy.npc.Npc(pos=4))
            enemy_list.append(role.enemy.npc.Npc(pos=2))
            enemy_come[10] = False
            nonlocal boss_come_judge
            boss_come_judge = True

    #boss何时出现
    def boss_come():
        #global boss_come_judge
        nonlocal boss_come_judge
        if boss_come_judge == True and len(enemy_list) == 0:
            boss_list.append(role.enemy.boss.Boss(name = "level3", life = 200, speed = [-5,0]))  #boss出现
            boss_come_judge = False

    def boss_update(screen):
        ti = 0
        tl = len(boss_list)
        while ti < tl:
            if boss_list[ti].life <= 0:
                del boss_list[ti]
                tl = tl-1
                if tl == 0:
                    nonlocal over_bul
                    over_bul = True
                continue
            screen.blit(boss_list[ti].rep, boss_list[ti].repr)
            boss_list[ti].move(2)
            ti = ti+1


    def clean():
        l = len(enemy_bullet_list)
        while l != 0:
            del enemy_bullet_list[l-1]
            l = l-1
        l = len(god_bullet_list)
        while l != 0:
            del god_bullet_list[l-1]
            l = l-1
        l = len(enemy_list)
        while l != 0:
            del enemy_list[l-1]
            l = l-1
        l = len(boss_list)
        while l != 0:
            del boss_list[l-1]
            l = l-1
        return

    def game_over():
        clean()
        if god.life > 0:
            return 1
        else:
            return 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                clean()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_rect.collidepoint(pygame.mouse.get_pos()):
                    clean()
                    return 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = pause^1
                if event.key == pygame.K_RIGHT:
                    god.speed[0] += god.move_speed
                elif event.key == pygame.K_LEFT:
                    god.speed[0] -= god.move_speed
                elif event.key == pygame.K_UP:
                    god.speed[1] -= god.move_speed
                elif event.key == pygame.K_DOWN:
                    god.speed[1] += god.move_speed
                elif event.key == pygame.K_x and god.skill_time > 0:
                    god.skill_time -= 1
                    if god.skill_type == 2:
                        god.defendskill(screen)
                    elif god.skill_type == 1:
                        god.shootskill(screen)
                        for i in god.specialattack(24):
                            god_bullet_list.append(
                                bullet.baseBullet.BaseBullet(speed=[i.speed[0], i.speed[1]], pict=god.blt.pict, pos=i.repr.center, camp=i.camp))
                elif event.key == pygame.K_z:
                    god_bullet_list.append(god.attack())
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    god.speed[0] -= god.move_speed
                elif event.key == pygame.K_LEFT:
                    god.speed[0] += god.move_speed
                elif event.key == pygame.K_UP:
                    god.speed[1] += god.move_speed
                elif event.key == pygame.K_DOWN:
                    god.speed[1] -= god.move_speed

        #print(len(enemy_bullet_list), len(god_bullet_list), len(enemy_list))
        screen.fill(BLACK)
        screen.blit(combat_background, combat_background_rect)
        now_time = time.time()
        if len(enemy_list) == 0:
            npc_come(now_time - old_time)
            boss_come()
        if pause == 0:
            enemy_attack()
            boss_attack()
            bullet_update(screen=screen)
            enemy_update(screen=screen)
            boss_update(screen = screen)
            god_update(screen=screen)
        if over_bul == True:
            # print(over_bul)
            return game_over()
        combat_information_update(screen=screen)
        pygame.display.update()
        #gc.collect()
        fclock.tick(fps)

