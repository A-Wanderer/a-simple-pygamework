import pygame, sys, global_parameter
import level
import gameover

import role.god.baseGod

def select_god():
    pygame.init()
    size = (global_parameter.windows_width, global_parameter.windows_height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('人物选择')

    god = None
    god_choose = False

    level_list = level.get_level_list()

    god_select_background = pygame.image.load('Image/background/god_select_background.jpg')
    god_select_background_rect = god_select_background.get_rect()


    god1_choose1 = pygame.image.load('Image/font/god1_choose1.png')
    god1_choose2 = pygame.image.load('Image/font/god1_choose2.png')
    god2_choose1 = pygame.image.load('Image/font/god2_choose1.png')
    god2_choose2 = pygame.image.load('Image/font/god2_choose2.png')
    back1 = pygame.image.load('Image/font/back1.png')
    back2 = pygame.image.load('Image/font/back2.png')
    god1_choose_rect = god1_choose1.get_rect()
    god2_choose_rect = god2_choose1.get_rect()
    back_rect = back1.get_rect()

    god1_choose_rect = god1_choose_rect.move(150, 600)
    god2_choose_rect = god2_choose_rect.move(800, 600)
    back_rect = back_rect.move(1100, 650)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if god1_choose_rect.collidepoint(pygame.mouse.get_pos()):
                    god = role.god.baseGod.God(move_speed=4, skill_type=2)
                    god_choose = True
                    #next_op = test_level.Level_1(role.god.baseGod.God(move_speed=4))
                elif god2_choose_rect.collidepoint(pygame.mouse.get_pos()):
                    god = role.god.baseGod.God(move_speed=6, skill_type=1)
                    god_choose = True
                    #next_op = test_level.Level_1(role.god.baseGod.God(move_speed=6))
                elif back_rect.collidepoint(pygame.mouse.get_pos()):
                    return

        if god_choose == True:
            for v in level_list:
                god.speed = [0, 0]
                god.skill_time = 3
                if v(god) == 1:
                    if gameover.gameover2() == 0:
                        break
                    else:
                        continue
                else:
                    break
            gameover.gameover1()
            god_choose = False


        screen.fill(global_parameter.BLACK)
        screen.blit(god_select_background, god_select_background_rect)

        if god1_choose_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(god1_choose2, god1_choose_rect)
        else:
            screen.blit(god1_choose1, god1_choose_rect)
        if god2_choose_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(god2_choose2, god2_choose_rect)
        else:
            screen.blit(god2_choose1, god2_choose_rect)
        if back_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(back2, back_rect)
        else:
            screen.blit(back1, back_rect)


        pygame.display.update()