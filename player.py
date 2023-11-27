from my_math import *
from blocks import * 
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player/player.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self.move_amt = 5 
        self.move_time = 3
        self.lerp_time = 0
        self.can_collide = True
    
    def set_player(self,pos:tuple)->None:
        self.rect.topleft = pos 
    
    def update(self,framed_delta:float,change_level):
        self.__move_player(framed_delta)
        self.__hole_collision_level_change(change_level)

    def draw(self,win:pygame.surface.Surface)->None:
        win.blit(self.image, self.rect)

    def __move_player(self,framed_delta:float)->None: #framed_delta = framed_delta * framerate
        keys = pygame.key.get_pressed()
        temp_pos = [self.rect.topleft[0],self.rect.topleft[1]]
        if keys[pygame.K_UP] or keys[pygame.K_w]: 
            temp_pos[1] -= self.move_amt * framed_delta
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            temp_pos[1] += self.move_amt * framed_delta
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: 
            temp_pos[0] -= self.move_amt * framed_delta
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: 
            temp_pos[0] += self.move_amt * framed_delta
        
        self.rect.topleft = tuple(temp_pos)
        
    def __hole_collision_level_change(self, change_level)->None: # change level callback actually calls the generate level in game
        collide = False
        for hole in HoleBlock.container:
            collide = self.rect.colliderect(hole.rect)
        if collide:
            Blocks.del_all_blocks()
            change_level()
            can_collide = True
        else:
            can_collide = False

    def draw_and_update_sprite(self,win:pygame.surface.Surface,framed_delta:float,change_level)->None: #for learning about the arguments visit functions above
        self.update(framed_delta,change_level)
        self.draw(win)
