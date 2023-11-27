from my_math import *
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
    
    def set_player(self,pos:tuple)->None:
        self.rect.topleft = pos 
    
    def update(self,framed_delta:float):
        self.__move_player(framed_delta)

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
        #if(self.lerp_time < self.move_time):
        #    self.rect.topleft = tuple(lerp(list(self.rect.topleft),temp_pos,self.lerp_time))
        #self.lerp_time += framed_delta
        #self.rect.topleft = tuple(pos)

    def draw_and_update_sprite(self,win:pygame.surface.Surface,framed_delta:float)->None:
        self.update(framed_delta)
        self.draw(win)
