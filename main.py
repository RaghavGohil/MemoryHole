from utils import *
import config
import colors
import level_generator
import background
import pygame
from player import Player

RUNNING = True

win = pygame.display.set_mode(config.WIN_SIZE)
pygame.display.set_caption(config.WIN_TITLE)

clock = pygame.time.Clock()

deltatime = 0.0

#initailize:

player = Player()

background = background.Background()
level_generator = level_generator.LevelGenerator()
level_generator.generate_level(player,0)

while RUNNING:
    #events
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            quit_r("X pressed.")
    #refresh
    win.fill(colors.WHITE)

    #draw
    background.draw_bg(win,0)
    level_generator.draw_level(win)
    player.draw_and_update_sprite(win,events,deltatime)
    #update
    pygame.display.flip()

    #clocking
    clock_tick = clock.tick(config.GAME_FPS)
    deltatime = clock_tick/1000 