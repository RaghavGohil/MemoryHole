import levels
import colors
import config
import pygame

def draw_level(win:pygame.Surface,num_level:int,blocks=20)->None: #num_level starts with 0
    if (num_level+1) > len(levels.maps):
        raise Exception('Level number cannot be greater than number of maps')
        return
    block_size = config.WIN_SIZE[0]/blocks;
    for y in range(blocks):
        for x in range(blocks):
            c = levels.maps[num_level][y][x]
            __draw_blocks(win,c,x,y,block_size) 

def __draw_blocks(win:pygame.Surface,block_id:str,x:int,y:int,block_size:int)->None:
    color = ()
    if block_id == 'H':
        color = colors.BRICK
    elif block_id == 'T':
        color = colors.LAND
    elif block_id == 'W':
        color = colors.TREE
    pygame.draw.rect(win,color,(x*block_size,y*block_size,block_size,block_size)) 