import levels
from blocks import Blocks
import colors
import config
import pygame

class LevelGenerator:

    def __init__(self):
        self.__block_script= Blocks() 
        self.num_blocks_xandy = 20

    def generate_level(self,num_level:int)->None: #num_level starts with 0
        try:
            if (num_level+1) > len(levels.maps):
                raise Exception('Level number cannot be greater than number of maps.')
        except Exception as e:
            print(e)
        for y in range(self.num_blocks_xandy):
            for x in range(self.num_blocks_xandy):
                c = levels.maps[num_level][y][x]
                self.__block_script.add_blocks_to_groups(c,x,y) 
    
    def draw_level(self,win:pygame.surface.Surface)->None:
        self.__block_script.draw_and_update_sprites(win)