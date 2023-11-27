import levels
from player import Player
from blocks import Blocks
import colors
import config
import pygame

class LevelGenerator: # levels can only be generated if the player has spawned in.

    def __init__(self):
        self.__block_script= Blocks() 
        self.num_blocks_xandy = 20
        self.block_size = 30
    
    def generate_level(self,player:Player,num_level:int)->None: #num_level starts with 0
        has_found_player = False
        if (num_level+1) > len(levels.maps):
                raise Exception('Level number cannot be greater than number of maps.')
        for y in range(self.num_blocks_xandy):
            for x in range(self.num_blocks_xandy):
                c = levels.maps[num_level][y][x]
                self.__block_script.add_blocks_to_groups(c,x*self.block_size,y*self.block_size) 
                if c == 'P' and has_found_player == False: # only spawn in the player once
                    player.set_player((x*self.block_size,y*self.block_size))
                    has_found_player = True
        if not has_found_player:
             raise Exception('Player could not be spawned in map! Please add a P in level.')
    
    def draw_level(self,win:pygame.surface.Surface)->None:
        self.__block_script.draw_and_update_sprites(win)
