import levels
from player import Player
from blocks import Blocks
import colors
import config
import pygame

class LevelGenerator: # levels can only be generated if the player has spawned in.
    current_level = -1 

    def __init__(self):
        self.__block_script= Blocks() 
        self.num_blocks_xandy = int(config.WIN_SIZE[0]/config.GAME_BLOCK_SIZE)
    
    def generate_level(self,player:Player)->None: #LevelGenerator.current_level starts with 0
        has_found_player = False
        LevelGenerator.current_level += 1 # start with level 0
        if (LevelGenerator.current_level) > len(levels.maps)-1:
                raise Exception('Level number cannot be greater than number of maps.')
        for y in range(self.num_blocks_xandy):
            for x in range(self.num_blocks_xandy):
                c = levels.maps[LevelGenerator.current_level][y][x]
                self.__block_script.add_blocks_to_groups(c,x*config.GAME_BLOCK_SIZE,y*config.GAME_BLOCK_SIZE) 
                if c == 'P' and has_found_player == False: # only spawn in the player once
                    player.set_player((x*config.GAME_BLOCK_SIZE,y*config.GAME_BLOCK_SIZE))
                    has_found_player = True
        if not has_found_player:
             raise Exception('Player could not be spawned in map! Please add a P in level.')
    
    def draw_level(self,win:pygame.surface.Surface)->None:
        self.__block_script.draw_and_update_sprites(win)
