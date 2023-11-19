from my_math import *
import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player/player.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self.move_amt = 30
        self.move_time = 3
        self.lerp_time = 0
    
    def set_player(self,pos:tuple)->None:
        self.rect.topleft = pos 
    
    def update(self,events:pygame.event.Event,deltatime:float):
        self.__move_player(events,deltatime)

    def draw(self,win:pygame.surface.Surface)->None:
        win.blit(self.image, self.rect)

    def __move_player(self,events:pygame.event.Event,deltatime:float)->None:
        temp_pos = [self.rect.topleft[0],self.rect.topleft[1]]
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w or e.key == pygame.K_UP:
                    temp_pos[1] -= self.move_amt
                elif e.key == pygame.K_s or e.key == pygame.K_DOWN:
                    temp_pos[1] += self.move_amt
                elif e.key == pygame.K_a or e.key == pygame.K_LEFT:
                    temp_pos[0] -= self.move_amt
                elif e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                    temp_pos[0] += self.move_amt
        
        if(self.lerp_time < self.move_time):
            self.rect.topleft = tuple(lerp(list(self.rect.topleft),temp_pos,self.lerp_time))
        self.lerp_time += deltatime
        #self.rect.topleft = tuple(pos)

    def draw_and_update_sprite(self,win:pygame.surface.Surface,events:pygame.event.Event,deltatime:float)->None:
        self.update(events,deltatime)
        self.draw(win)