import pygame
import scene
import tween
import colors
import config
import font_renderer

class SplashScreen(scene.Scene):

    def __init__(self,win:pygame.surface.Surface,message_time:int)->None:
        super().__init__()
        self.win = win
        self.font_size = 12 
        self.renderer = font_renderer.FontRenderer(win)
        self.font = self.renderer.create_font(self.font_size)
        self.surface = pygame.Surface((config.WIN_SIZE[0],config.WIN_SIZE[1]))
        self.surface.fill(colors.STUDIO_COLOR)
        self.logo_scale = 0.8
        self.logo_surface = pygame.image.load('assets/logos/the_low_end_studio_title_transparent.png').convert_alpha()
        self.logo_surface = pygame.transform.smoothscale(self.logo_surface,(self.logo_surface.get_width()*self.logo_scale,self.logo_surface.get_height()*self.logo_scale)) 
        self.logo_surface_rect = self.logo_surface.get_rect(center=(config.WIN_SIZE[0]/2, config.WIN_SIZE[1]/2))
        self.message = '© 2024 The Low End Studio'
        self.message_time = message_time
        self.tween_message= tween.Tween() 

    def draw(self)->bool:
        if self.tween_message.finished == False:
            self.tween_message.count(self.message_time)
        else:
            self.scene_is_finished = True

        self.win.blit(self.surface,(0,0))
        self.__render_font()
        self.__blit_logo()
        return self.scene_is_finished
    

    def __blit_logo(self):
        self.win.blit(self.logo_surface,self.logo_surface_rect)
    
    def __render_font(self)->None:
        self.renderer.render_font(self.font,self.message,colors.WHITE,y=config.WIN_SIZE[1]-50,align_center_x=True,change_alpha=lambda:self.surface.get_alpha())