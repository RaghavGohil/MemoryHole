import config
import colors
import pygame
import blocks

class Animator: # our very own state machine!
    def __init__(self):
        self.image = pygame.Surface([blocks.Blocks.block_size,blocks.Blocks.block_size]) 
        self.image.fill(colors.NO_TEXTURE)

        self.current_state = 'default'
        self.__states = {}

        self.index = 0
        self.frame_delay_count = 0

    def change_state(self,state_name:str)->None:
        if self.current_state != state_name: # will not update unnecessarily
            self.index = 0
            self.current_state = state_name

    def add_animation(self,state_name:str,keyframes:list)->None:
        self.__states.update({state_name:keyframes})

    def play_animation(self,fps:int,framed_delta:float)->None: # fps = num of frames to play in a sec
        if self.current_state == 'default':
            self.image = pygame.Surface([config.GAME_BLOCK_SIZE,config.GAME_BLOCK_SIZE])
            self.image.fill(colors.NO_TEXTURE)
        if self.current_state in self.__states:
            keyframes = self.__states.get(self.current_state)
            self.frame_delay_count += framed_delta/config.FPS 
            if self.frame_delay_count > (1/fps):
                self.image = keyframes[self.index]
                self.index = (self.index + 1) % len(keyframes) 
                self.frame_delay_count = 0
            
        else:
            raise Exception(f'{self.current_state} not in animation states.')
