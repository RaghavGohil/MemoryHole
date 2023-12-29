import pygame

class HoleBlock(pygame.sprite.Sprite):
    id = 'H' # static
    container = pygame.sprite.Group()
    def __init__(self,x:int,y:int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/blocks/hole.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

class WallBlock(pygame.sprite.Sprite):
    id = 'W'
    container = pygame.sprite.Group()
    def __init__(self,x:int,y:int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/blocks/wall.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

class TrapBlock(pygame.sprite.Sprite):
    id = 'T'
    container = pygame.sprite.Group()
    def __init__(self,x:int,y:int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/blocks/trap.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)


class Blocks:
    block_classes = [HoleBlock,WallBlock,TrapBlock]
    block_size = 30

    def __init__(self):
        pass

    @staticmethod
    def del_all_blocks():
       for bc in Blocks.block_classes:
            bc.container.empty()

    def add_blocks_to_groups(self,block_id:str,x:int,y:int)->None:
        for bc in Blocks.block_classes:
            if bc.id == block_id:
                bc.container.add(bc(x,y))
                
    def draw_and_update_sprites(self,win:pygame.surface.Surface)->None:
        for bc in Blocks.block_classes:
            bc.container.update()
            bc.container.draw(win)
