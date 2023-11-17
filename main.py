from utils import *
import config
import colors
import level_generator
import pygame

win = pygame.display.set_mode(config.WIN_SIZE)

pygame.display.set_caption(config.WIN_TITLE)

RUNNING = True

#initailize:
level_generator = level_generator.LevelGenerator()

while RUNNING:
    #events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit_r("X pressed.")
    #refresh
    win.fill(colors.WHITE)

    #draw
    level_generator.draw_level(win,0)

    #update
    pygame.display.flip()