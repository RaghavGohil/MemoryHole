from utils import *
import config
import font_renderer
import colors
import level_generator
import background
import pygame
import player

RUNNING = True

win = pygame.display.set_mode(config.WIN_SIZE,pygame.SCALED)
pygame.display.set_caption(config.WIN_TITLE)
if config.FULLSCREEN:
    pygame.display.toggle_fullscreen()

clock = pygame.time.Clock()

deltatime = 0.0

def toggle_fullscreen(event:pygame.event.Event)->None:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:
            pygame.display.toggle_fullscreen()

#initailize:
renderer = font_renderer.FontRenderer(win)
text = renderer.createFont(20)
player = player.Player()
background = background.Background()
level_generator = level_generator.LevelGenerator()

try:
    level_generator.load_level(player)
except Exception as e:
    quit_r(f"level could not be generated {e}")

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
        player.draw_and_update_sprite(win,deltatime*config.FPS,lambda:level_generator.load_level(player))
    except Exception as e:
        quit_r(f"level could not be generated {e}")

    renderer.renderFont(text,'why are you working?',colors.WHITE,0,0) 
    #update
    pygame.display.flip()

    #clocking
    clock_tick = clock.tick(config.FPS)
    deltatime = clock_tick/1000 
