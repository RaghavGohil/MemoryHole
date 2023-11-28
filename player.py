from my_math import *
from blocks import * 
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player/player.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self.move_speed= 5 
        self.move_time = 3
        self.lerp_time = 0
    
    def set_player(self,pos:tuple)->None:
        self.rect.topleft = pos 
    
    def update(self,framed_delta:float,change_level):
        self.__move_player(framed_delta)
        self.__hole_collision_level_change(change_level)

    def draw(self,win:pygame.surface.Surface)->None:
        win.blit(self.image, self.rect)

    def __move_player(self,framed_delta:float)->None: #framed_delta = framed_delta * framerate
        keys = pygame.key.get_pressed()
        direction = [0,0]
        if keys[pygame.K_UP] or keys[pygame.K_w]: 
            direction[1] -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            direction[1] += 1
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: 
            direction[0] -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: 
            direction[0] += 1
        
        if not vec_is_zero(direction):
            normalized_pos = vec_mul(vec_normalize(direction),self.move_speed*framed_delta)
            self.rect.topleft = tuple(vec_add(list(self.rect.topleft),normalized_pos))
        
    def __hole_collision_level_change(self, change_level)->None: # change level callback actually calls the generate level in game
        collide = False

        for hole in HoleBlock.container:
            collide = self.rect.colliderect(hole.rect)
            if collide == True:
                break 

        if collide:
            Blocks.del_all_blocks()
            change_level() # changes the level itself so there is no need to put checks for collision

    def __wall_collision(self)->None:
        pass


    def draw_and_update_sprite(self,win:pygame.surface.Surface,framed_delta:float,change_level)->None: #for learning about the arguments visit functions above
        self.update(framed_delta,change_level)
        self.draw(win)
