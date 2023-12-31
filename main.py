from utils import *
import config
import font_renderer
import colors
import level_generator
import blocks
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
deltatime = 0.0
framed_delta = 0.0

def toggle_fullscreen(event:pygame.event.Event)->None:
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_x:
            pygame.display.toggle_fullscreen()

#initailize:
_player = player.Player(win)
_blocks = blocks.Blocks(win)
_background = background.Background(win)
_debug_screen = debug_screen.DebugScreen(win)
_level_generator = level_generator.LevelGenerator(_blocks,_player)

while RUNNING:
    
    #events
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            quit_r("X pressed.")
        toggle_fullscreen(e)
    #refresh
    win.fill(colors.WHITE)

    #dynamic data (dynamic data aren't game logic variables but common things like deltatime etc (python doesn't support pass by ref smh))
    player.Player.set_dynamic_data(deltatime,framed_delta)
    blocks.Blocks.set_dynamic_data(deltatime)

    #draw calls
    _background.draw_bg(0)
    _level_generator.draw_level()
    try:
        _player.draw_and_update_sprite(lambda:_level_generator.change_level(_player),lambda:_level_generator.restart_level(_player))
    except Exception as e:
        quit_r(f"level could not be generated {e}")

    #debug

    _debug_screen.draw_debug_info()
    _debug_screen.instance.watch('FPS ',clock.get_fps())
    _debug_screen.instance.watch('DELTATIME ',deltatime)
    _debug_screen.instance.watch('FRAMED DELTA',framed_delta)

    #update
    pygame.display.flip()

    #clocking
    clock_tick = clock.tick(config.FPS)
    deltatime = clock_tick/1000
    framed_delta = deltatime*clock.get_fps()