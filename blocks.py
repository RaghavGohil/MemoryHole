import pygame

class Block:

    def __init__(self):
        self.__hole_image = pygame.image.load('assets/blocks/hole.png').convert_alpha()
        self.__trap_image = pygame.image.load('assets/blocks/trap.png').convert_alpha()
        self.__wall_image = pygame.image.load('assets/blocks/wall.png').convert_alpha()
        self.block_size = 30
        self.blocks = {
            'H':self.__hole_image,
            'T':self.__trap_image,
            'W':self.__wall_image,
        }

    def draw_blocks(self,win:pygame.Surface,block_id:str,x:int,y:int)->None:
        try:
            block_img = self.blocks.get(block_id)
            if block_id != None:
                win.blit(block_img,(x*self.block_size,y*self.block_size))
            else:
                raise Exception(f"Unable to get block id {block_id}")
        except Exception as e:
            print(e)