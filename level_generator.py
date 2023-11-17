import levels
from blocks import Block
import colors
import config
import pygame

class LevelGenerator:

    def __init__(self):
        self.__block_script= Block() 
        self.num_blocks_xandy = 20

    def draw_level(self,win:pygame.Surface,num_level:int)->None: #num_level starts with 0
        try:
            if (num_level+1) > len(levels.maps):
                raise Exception('Level number cannot be greater than number of maps.')
        except Exception as e:
            print(e)
        for y in range(self.num_blocks_xandy):
            for x in range(self.num_blocks_xandy):
                c = levels.maps[num_level][y][x]
                self.__block_script.draw_blocks(win,c,x,y) 