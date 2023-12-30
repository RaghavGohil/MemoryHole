from utils import *
import config
import font_renderer
import colors
import level_generator
import background
import debug_screen
import pygame
import player

RUNNING = True

win = pygame.display.set_mode(config.WIN_SIZE,pygame.SCALED)
pygame.display.set_caption(config.WIN_TITLE)
if config.START_WITH_FULLSCREEN:
    pygame.display.toggle_fullscreen()

clock = pygame.time.Clock()

curr_fps = 0.0
deltatime = 0.0

def toggle_fullscreen(event:pygame.event.Event)->None:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:
            pygame.display.toggle_fullscreen()

#initailize:
player = player.Player()
background = background.Background()
debug_screen = debug_screen.DebugScreen(win)
level_generator = level_generator.LevelGenerator(player)

while RUNNING:
    #events
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            quit_r("X pressed.")
        toggle_fullscreen(e)
    #refresh
    win.fill(colors.WHITE)

    #draw

    background.draw_bg(win,0)
    level_generator.draw_level(win,deltatime)
    
    try:
        player.draw_and_update_sprite(win,deltatime,deltatime*curr_fps,lambda:level_generator.change_level(player),lambda:level_generator.restart_level(player))
    except Exception as e:
        quit_r(f"level could not be generated {e}")

    debug_screen.draw_debug_info(curr_fps)
    #update
    pygame.display.flip()

    #clocking
    curr_fps = clock.get_fps()
    clock_tick = clock.tick(config.FPS)
    deltatime = clock_tick/1000 
