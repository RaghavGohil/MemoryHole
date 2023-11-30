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
        self.animation_fps = 10 #frames to play in a sec

        self.idle_animation = [pygame.image.load('assets/player/player1.png')]
        self.walking_animation = [pygame.image.load('assets/player/player1.png'),pygame.image.load('assets/player/player2.png')]
        
        self.animator.add_animation('idle',self.idle_animation)
        self.animator.add_animation('walking',self.walking_animation)

        self.image = self.animator.image 

        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)

        self.move_speed = 2 
        self.collision_move_amt = 5

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
        keys = pygame.key.get_pressed()
        direction = [0,0]
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]): 
            direction[0] -= 1
            self.is_facing_right = False
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]): 
            direction[0] += 1
            self.is_facing_right = True 
        if (keys[pygame.K_UP] or keys[pygame.K_w]): 
            direction[1] -= 1
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]):
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
        for wall in WallBlock.container:
            if self.rect.colliderect(wall.rect):
                if wall.rect.right - self.rect.left >= 0: # left 
                    self.rect.left += self.collision_move_amt
                if wall.rect.left - self.rect.right <= 0: # right
                    self.rect.left -= self.collision_move_amt
                if wall.rect.bottom - self.rect.top >= 0: # top 
                    pass
                if wall.rect.top - self.rect.bottom <= 0: # bottom 
                    pass

    def draw_and_update_sprite(self,win:pygame.surface.Surface,framed_delta:float,change_level)->None: #for learning about the arguments visit functions above
        self.update(framed_delta,change_level)
        self.draw(win)
