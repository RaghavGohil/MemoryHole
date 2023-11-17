import pygame

class Block:
    def __init__(self):
        self.__hole_image = pygame.image.load('assets/blocks/hole.png').convert_alpha()
        self.__trap_image = pygame.image.load('assets/blocks/trap.png').convert_alpha()
        self.__wall_image = pygame.image.load('assets/blocks/wall.png').convert_alpha()
        self.blocks = {
            'H':self.__hole_image,
            'T':self.__trap_image,
            'W':self.__wall_image,
        }
    def draw_blocks(self,win:pygame.Surface):
        for block in self.blocks:
            