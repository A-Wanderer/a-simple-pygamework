import pygame, sys, god_select, global_parameter
import moviepy.editor

pygame.init()

size = (global_parameter.windows_width, global_parameter.windows_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('幻想纪元')

icon = pygame.image.load('Image/icon/icon.jpg')
pygame.display.set_icon(icon)

clip = moviepy.editor.VideoFileClip('Videos/beginning.mp4')
clip.preview()
#clip.reader.close()
#clip.audio.reader.close_proc()

homepage_background = pygame.image.load('Image/background/homepage_background.jpg')
homepage_background_rect = homepage_background.get_rect()


homepage_title = pygame.image.load('Image/font/homepage_title.png')

start_game1 = pygame.image.load('Image/font/start_game1.png')
start_game2 = pygame.image.load('Image/font/start_game2.png')
exit_game1 = pygame.image.load('Image/font/exit_game1.png')
exit_game2 = pygame.image.load('Image/font/exit_game2.png')
start_game_rect = start_game1.get_rect()
exit_game_rect = exit_game1.get_rect()
homepage_title_rect = homepage_title.get_rect()

homepage_title_rect = homepage_title_rect.move(200, 100)
start_game_rect = start_game_rect.move(300, 360)
exit_game_rect = exit_game_rect.move(300, 460)

pygame.mixer.init()
pygame.mixer.music.load('Music/bgm.wav')
pygame.mixer.music.play(-1, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_game_rect.collidepoint(pygame.mouse.get_pos()):
                god_select.select_god()
            elif exit_game_rect.collidepoint(pygame.mouse.get_pos()):
                sys.exit()

    screen.fill(global_parameter.BLACK)

    screen.blit(homepage_background, homepage_background_rect)
    screen.blit(homepage_title, homepage_title_rect)
    if start_game_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(start_game2, start_game_rect)
    else:
        screen.blit(start_game1, start_game_rect)
    if exit_game_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(exit_game2, exit_game_rect)
    else:
        screen.blit(exit_game1, exit_game_rect)

    pygame.display.update()