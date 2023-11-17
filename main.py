from utils import *
import config
import colors
import level_generator
import pygame

win = pygame.display.set_mode(config.WIN_SIZE)

pygame.display.set_caption(config.WIN_TITLE)

RUNNING = True

while RUNNING:
    #events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            quit_r("X pressed.")
    #refresh
    win.fill(colors.WHITE)

    #draw

    try:
        level_generator.draw_level(win,0)
    except e:
        quit_r('Unable to generate level.'+e)

    #update
    pygame.display.flip()