import pygame
import my_math

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
    ping_pong_individual_total_time = 2 #time for each ping to pong and vice versa
    container = pygame.sprite.Group()
    def __init__(self,x:int,y:int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/blocks/trap.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.ping_pong_curr_time = 0
        self.ping_pong_amount = 3

    def play_ping_pong_animation(self,deltatime:float):
        if self.ping_pong_amount%2==0:
            self.image.set_alpha(my_math.lerp(255,0,self.ping_pong_curr_time))
        else:
            self.image.set_alpha(my_math.lerp(0,255,self.ping_pong_curr_time))

        self.ping_pong_curr_time += deltatime/self.ping_pong_individual_total_time

    def update(self,deltatime:float):
        if(self.ping_pong_curr_time < 1 and self.ping_pong_amount >= 0):
            self.play_ping_pong_animation(deltatime)
        else:
            self.ping_pong_amount -= 1
            self.ping_pong_curr_time = 0
        if self.ping_pong_amount < 0:
            self.image.set_alpha(0)


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
                
    def draw_and_update_sprites(self,win:pygame.surface.Surface,deltatime)->None:
        for bc in Blocks.block_classes:
            bc.container.update(deltatime)
            bc.container.draw(win)
