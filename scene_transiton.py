import pygame
import my_math
import colors
import config
import font_renderer

class SceneTransition:
    def __init__(self,win:pygame.surface.Surface,animation_time:int)->None:
        self.win = win
        self.font_size = 40
        self.renderer = font_renderer.FontRenderer(win)
        self.font = self.renderer.create_font(self.font_size)
        self.current_time = 0
        self.animation_time = animation_time
        self.surface = pygame.Surface((config.WIN_SIZE[0],config.WIN_SIZE[1]))
        self.surface.fill(colors.BLACK)

    def __calculate_animation_frame(self,deltatime:float)->None:
        self.current_time += deltatime/self.animation_time
        self.surface.set_alpha(my_math.lerp(255,0,self.current_time))

    def play_animation(self,deltatime:float)->None:
        if self.current_time < 1:
            self.__calculate_animation_frame(deltatime) 
            self.win.blit(self.surface,(0,0))
        else:
            self.surface.set_alpha(0)

    def __render_font(self,message:str)->None:
        self.renderer.render_font(self.font,message,colors.WHITE,config.WIN_SIZE[0],config.WIN_SIZE[1],align_center=True)