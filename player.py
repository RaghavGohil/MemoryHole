import math
import animator
from my_math import *
from blocks import * 
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # loading animations
        self.animator = animator.Animator()
        self.animation_fps = 10 #frames to play in a sec(not made this dymnamic enough because it is a simple game duh)

        self.idle_animation = [pygame.image.load('assets/player/player1.png')]
        self.walking_animation = [pygame.image.load('assets/player/player1.png'),pygame.image.load('assets/player/player2.png')]
        
        self.animator.add_animation('idle',self.idle_animation)
        self.animator.add_animation('walking',self.walking_animation)

        self.image = self.animator.image 

        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)

        self.move_speed = 2 
        self.collision_move_amt = 2

        self.is_facing_right = True
    
    def set_player(self,pos:tuple)->None:
        self.rect.topleft = pos 
    
    def update(self,framed_delta:float,change_level):
        self.__hole_collision_level_change(change_level)
        self.__wall_collision()
        self.__move_player(framed_delta)
        self.__animate_player(framed_delta)
        self.__flip_sprite()

    def draw(self,win:pygame.surface.Surface)->None:
        win.blit(self.image, self.rect)

    def __flip_sprite(self)->None:
        self.image = pygame.transform.flip(self.image,not self.is_facing_right,False)

    def __animate_player(self,framed_delta:float)->None:
        self.animator.play_animation(self.animation_fps,framed_delta) 
        self.image = self.animator.image

    def __move_player(self,framed_delta:float)->None: #framed_delta = framed_delta * framerate
        self.keys = pygame.key.get_pressed()
        direction = [0,0]
        if (self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]): 
            direction[0] -= 1
            self.is_facing_right = False
        if (self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]): 
            direction[0] += 1
            self.is_facing_right = True 
        if (self.keys[pygame.K_UP] or self.keys[pygame.K_w]): 
            direction[1] -= 1
        if (self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]):
            direction[1] += 1
        
        if not vec_is_zero(direction):
            direction_speed_vec = vec_mul(vec_normalize(direction),self.move_speed*framed_delta)
            self.rect.topleft = vec_add(self.rect.topleft,direction_speed_vec)
            self.animator.change_state('walking')
        else:
            self.animator.change_state('idle')
        
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
        walls = pygame.sprite.spritecollide(self, WallBlock.container,False)
        for wall in walls:
            if self.rect.right > wall.rect.left:
                self.rect.right -= self.collision_move_amt
            if self.rect.left > wall.rect.right:
                self.rect.right += self.collision_move_amt
            if self.rect.bottom > wall.rect.top:
                self.rect.bottom -= self.collision_move_amt
            if self.rect.top > wall.rect.bottom:
                self.rect.top += self.collision_move_amt

    def draw_and_update_sprite(self,win:pygame.surface.Surface,framed_delta:float,change_level)->None: #for learning about the arguments visit functions above
        self.update(framed_delta,change_level)
        self.draw(win)
