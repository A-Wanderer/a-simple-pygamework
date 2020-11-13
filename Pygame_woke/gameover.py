import pygame, sys
from global_parameter import *

def gameover1():
    pygame.init()
    size = (windows_width, windows_height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('游戏结束')

    game_over1_background = pygame.image.load('Image/background/game_over1_background.jpg')
    game_over1_background_rect = game_over1_background.get_rect()

    back1 = pygame.image.load('Image/font/back1.png')
    back2 = pygame.image.load('Image/font/back2.png')
    back_rect = back1.get_rect()
    back_rect = back_rect.move(580, 350)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_rect.collidepoint(pygame.mouse.get_pos()):
                    return
        screen.fill(BLACK)
        screen.blit(game_over1_background, game_over1_background_rect)
        if back_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(back2, back_rect)
        else:
            screen.blit(back1, back_rect)

        pygame.display.update()

def gameover2():
    pygame.init()
    size = (windows_width, windows_height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('游戏结束')

    game_over2_background = pygame.image.load('Image/background/game_over2_background.jpg')
    game_over2_background_rect = game_over2_background.get_rect()

    back1 = pygame.image.load('Image/font/back1.png')
    back2 = pygame.image.load('Image/font/back2.png')
    continue1 = pygame.image.load('Image/font/continue1.png')
    continue2 = pygame.image.load('Image/font/continue2.png')
    back_rect = back1.get_rect()
    back_rect = back_rect.move(580, 350)
    continue_rect = continue1.get_rect()
    continue_rect = continue_rect.move(580, 450)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_rect.collidepoint(pygame.mouse.get_pos()):
                    return 0
                if continue_rect.collidepoint(pygame.mouse.get_pos()):
                    return 1
        screen.fill(BLACK)
        screen.blit(game_over2_background, game_over2_background_rect)
        if back_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(back2, back_rect)
        else:
            screen.blit(back1, back_rect)
        if continue_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(continue2, continue_rect)
        else:
            screen.blit(continue1, continue_rect)
        pygame.display.update()
