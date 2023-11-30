import config
import colors
import pygame

class Animator: # our very own state machine!
    def __init__(self):
        self.image = pygame.Surface([config.GAME_BLOCK_SIZE,config.GAME_BLOCK_SIZE]) 
        self.image.fill(colors.NO_TEXTURE)

        self.current_state = 'default'
        self.__states = {}

        self.index = 0
        self.frame_delay_count = 0

    def change_state(self,state_name:str)->None:
        self.index = 0
        self.current_state = state_name

    def add_animation(self,state_name:str,keyframes:list)->None:
        self.__states.update({state_name:keyframes})

    def play_animation(self,framed_delta:float)->None:
        if self.current_state == 'default':
            self.image = pygame.Surface([config.GAME_BLOCK_SIZE,config.GAME_BLOCK_SIZE])
            self.image.fill(colors.NO_TEXTURE)
        if self.current_state in self.__states:
            keyframes = self.__states.get(self.current_state)
            self.frame_delay_count += framed_delta 
            if self.frame_delay_count > (1/2): # 2 frames in 1 sec
                print(self.index)
                self.image = keyframes[self.index]
                self.index = (self.index + 1) % len(keyframes) 
                self.frame_delay_count = 0
            
        else:
            raise Exception(f'{self.current_state} not in animation states.')
