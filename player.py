import config
import animator
from global_data import GlobalData
from debug_screen import DebugScreen
from my_math import *
from blocks import * 
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self,win):
        pygame.sprite.Sprite.__init__(self)
        # loading animations
        self.win = win
        self.animator = animator.Animator()
        self.animation_fps = 10#frames to play in a sec(not made this dymnamic enough because it is a simple game duh)

        self.idle_animation = [pygame.image.load('assets/player/player1.png')]
        self.walking_animation = [pygame.image.load('assets/player/player2.png'),pygame.image.load('assets/player/player1.png')]
        
        self.animator.add_animation('idle',self.idle_animation)
        self.animator.add_animation('walking',self.walking_animation)

        self.image = self.animator.image 

        self.rect = self.image.get_rect()
        self.sidelen = self.rect.right/2
        self.rect.topleft = (0,0)
        self.hitbox = self.rect.inflate(-15,-9)
        self.hitbox_offset = (5,5)

        self.move_speed = 150 

        self.collision_move_amt = 1
        self.collision_move_amt_boundary = 3

        self.is_facing_right = True
    
    @staticmethod
    def collided(sprite,other):
        return sprite.hitbox.colliderect(other)

    def set_player(self,pos:tuple)->None:
        self.rect.topleft = pos 
    
    def update(self,change_level,restart_level):
        self.__hole_collision(change_level)
        self.__trap_collision(restart_level)
        self.__wall_collision()
        self.__boundary_collision()
        self.__move_player()
        self.__animate_player()
        self.__flip_sprite()

    def draw(self)->None:
        self.win.blit(self.image, self.rect)
        self.__draw_debug()
    
    def __draw_debug(self):
        DebugScreen.instance.draw_rect(self.rect)
        DebugScreen.instance.draw_rect(self.hitbox)
    def __flip_sprite(self)->None:
        self.image = pygame.transform.flip(self.image,not self.is_facing_right,False)

    def __animate_player(self)->None:
        self.animator.play_animation(self.animation_fps,GlobalData.deltatime) 
        self.image = self.animator.image

    def __move_player(self)->None:

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
            direction_speed_vec = vec_mul(vec_normalize(direction),self.move_speed*GlobalData.deltatime)
            self.rect.topleft = vec_add(self.rect.topleft,direction_speed_vec)
            self.animator.change_state('walking')
        else:
            self.animator.change_state('idle')

        #update the hitbox
        self.hitbox.topleft = vec_add(self.rect.topleft,self.hitbox_offset)
        
    def __hole_collision(self, change_level)->None: # change level callback actually calls the generate level in game
        if pygame.sprite.spritecollide(self,HoleBlock.container,False,Player.collided):
            Blocks.del_all_blocks()
            change_level() # changes the level itself so there is no need to put checks for collision

    def __trap_collision(self,restart_level)->None:#restart level callback restarts the level
        if pygame.sprite.spritecollide(self,TrapBlock.container,False,Player.collided):
            Blocks.del_all_blocks()
            restart_level() # changes the level itself so there is no need to put checks for collision

    def __boundary_collision(self)->None:
        if self.hitbox.left < 0:
            self.rect.x += self.collision_move_amt_boundary
        if self.hitbox.right > config.WIN_SIZE[0]:
            self.rect.x -= self.collision_move_amt_boundary
        if self.hitbox.top < 0:
            self.rect.y += self.collision_move_amt_boundary
        if self.hitbox.bottom > config.WIN_SIZE[1]:
            self.rect.y -= self.collision_move_amt_boundary

    def __wall_collision(self)->None:
        walls = pygame.sprite.spritecollide(self, WallBlock.container,False,Player.collided)
        for wall in walls:
            if wall.rect.collidepoint((self.rect.right,self.rect.top+self.sidelen)):
                self.rect.x -= self.collision_move_amt
            if wall.rect.collidepoint((self.rect.left ,self.rect.top+self.sidelen)):
                self.rect.x += self.collision_move_amt
            if wall.rect.collidepoint((self.rect.left+self.sidelen,self.rect.top)):
                self.rect.y += self.collision_move_amt
            if wall.rect.collidepoint((self.rect.left+self.sidelen,self.rect.bottom)):
                self.rect.y -= self.collision_move_amt
            
    def draw_and_update_sprite(self,change_level,restart_level)->None: #for learning about the arguments visit functions above
        self.update(change_level,restart_level)
        self.draw()
