import levels
from player import Player
import blocks 
import config
import pygame

class LevelGenerator: # levels can only be generated if the player has spawned in.
    is_transitioning = False
    current_level = -1 

    def __init__(self):
        self.__block_script= blocks.Blocks() 
        self.num_blocks_xandy = int(config.WIN_SIZE[0]/blocks.Blocks.block_size)
    
    def __check_level_integrity(self,level_index:int)->None:
        has_found_player = False
        has_found_hole = False
        players_in_level = 0

        for y in range(self.num_blocks_xandy):
            for x in range(self.num_blocks_xandy):
                c = levels.maps[level_index][y][x]
                self.__block_script.add_blocks_to_groups(c,x*blocks.Blocks.block_size,y*blocks.Blocks.block_size) 
                if c == 'P': # only spawn in the player once
                    has_found_player = True
                    players_in_level += 1
                elif c == 'H':
                    has_found_hole = True
                if players_in_level > 1:
                    raise Exception(f'Too many players in one level! Index: {level_index}')

        if not has_found_player or not has_found_hole:
            raise Exception(f'Invalid level! Please add P or H to maintain integrity. Index: {level_index}')

    def load_level(self,player:Player)->None: #LevelGenerator.current_level starts with 0
        LevelGenerator.current_level += 1 # start with level 0
        if (LevelGenerator.current_level) > len(levels.maps)-1:
                raise Exception('Level number cannot be greater than number of maps.')

        self.__check_level_integrity(LevelGenerator.current_level)

        for y in range(self.num_blocks_xandy):
            for x in range(self.num_blocks_xandy):
                c = levels.maps[LevelGenerator.current_level][y][x]
                self.__block_script.add_blocks_to_groups(c,x*blocks.Blocks.block_size,y*blocks.Blocks.block_size) 
                if c == 'P': # only spawn in the player once
                    player.set_player((x*blocks.Blocks.block_size,y*blocks.Blocks.block_size))
    
    def draw_level(self,win:pygame.surface.Surface,deltatime:float)->None:
        self.__block_script.draw_and_update_sprites(win,deltatime)
